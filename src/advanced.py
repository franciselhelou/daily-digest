"""Supplementary ingestion, source diagnostics and semantic clustering for the AI digest."""
import datetime as dt
import hashlib
import logging
import os
import re
import sqlite3
import time
from collections import defaultdict
from urllib.parse import urljoin, urlsplit

import feedparser
import requests
from bs4 import BeautifulSoup

LOG = logging.getLogger('digest.advanced')
UA = 'AI-Intelligence-Digest/2.0 (research metadata aggregation)'


def health_schema(conn):
    conn.executescript('''
    CREATE TABLE IF NOT EXISTS source_health (
      source_id TEXT PRIMARY KEY, source_name TEXT NOT NULL, kind TEXT NOT NULL,
      url TEXT NOT NULL, last_check TEXT, last_success TEXT, last_count INTEGER DEFAULT 0,
      failures INTEGER DEFAULT 0, status TEXT DEFAULT 'new', error TEXT DEFAULT '');
    CREATE TABLE IF NOT EXISTS clusters (
      day TEXT NOT NULL, cluster_id TEXT NOT NULL, canonical_id TEXT NOT NULL,
      finding_id TEXT NOT NULL, similarity REAL NOT NULL,
      PRIMARY KEY(day, finding_id));
    CREATE TABLE IF NOT EXISTS enrichments (
      finding_id TEXT PRIMARY KEY, body TEXT NOT NULL DEFAULT '', word_count INTEGER DEFAULT 0,
      fetched_at TEXT, method TEXT NOT NULL DEFAULT 'excerpt');
    CREATE INDEX IF NOT EXISTS idx_source_health_status ON source_health(status);
    ''')
    conn.commit()


def update_health(conn, name, kind, url, count, error=''):
    sid = hashlib.sha256((kind + ':' + url).encode()).hexdigest()[:28]
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    conn.execute('''INSERT INTO source_health(source_id,source_name,kind,url,last_check,last_success,last_count,failures,status,error)
       VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT(source_id) DO UPDATE SET
       last_check=excluded.last_check,
       last_success=CASE WHEN excluded.status='ok' THEN excluded.last_success ELSE source_health.last_success END,
       last_count=excluded.last_count,
       failures=CASE WHEN excluded.status='ok' THEN 0 ELSE source_health.failures+1 END,
       status=excluded.status,error=excluded.error''',
       (sid,name,kind,url,now,now if not error else None,count,0 if not error else 1,'ok' if not error else 'error',str(error)[:350]))


def source_status(conn):
    return [dict(zip(['source','kind','status','count','failures','last_success','error'], row))
            for row in conn.execute('SELECT source_name,kind,status,last_count,failures,last_success,error FROM source_health ORDER BY status DESC,failures DESC,source_name')]


def fetch_extra(config, conn, timeout=13):
    """Discover sources via feed auto-discovery; ingest public RSS/Atom and optional arXiv search.
    HTML source pages are NEVER treated as evidence of an article merely from nav headings.
    """
    rows=[]
    session=requests.Session()
    session.headers.update({'User-Agent':UA, 'Accept':'application/rss+xml, application/atom+xml, text/html, */*'})
    for src in config.get('extra_feeds', []):
        name, url, category = src['name'], src['url'], src['category']
        try:
            resp=session.get(url,timeout=(5,timeout)); resp.raise_for_status()
            parsed=feedparser.parse(resp.content)
            if not parsed.entries:
                raise ValueError('No RSS/Atom entries found (check source endpoint)')
            valid=0
            for e in parsed.entries[:int(os.getenv('MAX_PER_SOURCE','35'))]:
                stamp=e.get('published_parsed') or e.get('updated_parsed')
                if stamp is None: continue
                from calendar import timegm
                when=dt.datetime.fromtimestamp(timegm(stamp),dt.timezone.utc).isoformat()
                link=e.get('link','')
                if not link.startswith(('http://','https://')): continue
                title=BeautifulSoup(e.get('title',''),'html.parser').get_text(' ',strip=True)[:240]
                if not title: continue
                excerpt=BeautifulSoup(e.get('summary',e.get('description','')),'html.parser').get_text(' ',strip=True)[:1000]
                rows.append(dict(title=title,url=link,source=name,category=category,published=when,summary=excerpt))
                valid+=1
            update_health(conn,name,'feed',url,valid)
        except Exception as exc:
            LOG.warning('Source failed: %s (%s): %s',name,url,exc)
            update_health(conn,name,'feed',url,0,str(exc))
    conn.commit()
    return rows


def fetch_arxiv_queries(config, conn):
    """Optional targeted arXiv Atom search, rate-limited and bounded."""
    rows=[]
    queries=config.get('arxiv_queries',[])
    for i,q in enumerate(queries):
        name=q['name']; query=q['query']
        try:
            resp=requests.get('https://export.arxiv.org/api/query',params={'search_query':query,'start':0,'max_results':int(q.get('limit',12)),'sortBy':'submittedDate','sortOrder':'descending'},headers={'User-Agent':UA},timeout=25)
            resp.raise_for_status()
            feed=feedparser.parse(resp.content)
            if getattr(feed,'bozo',False) and not feed.entries: raise ValueError('Invalid Atom XML')
            valid=0
            from calendar import timegm
            for e in feed.entries:
                published=e.get('published_parsed')
                if not published: continue
                link=e.get('link','')
                if not link.startswith('https://'): continue
                rows.append({'title':re.sub(r'\s+',' ',e.get('title',''))[:240], 'url':link,'source':'arXiv Search: '+name,'category':q.get('category','Research'),'published':dt.datetime.fromtimestamp(timegm(published),dt.timezone.utc).isoformat(),'summary':re.sub(r'\s+',' ',e.get('summary',''))[:1000]})
                valid+=1
            update_health(conn,name,'arxiv','https://export.arxiv.org/api/query?search_query='+query,valid)
        except Exception as exc:
            update_health(conn,name,'arxiv','https://export.arxiv.org/api/query?search_query='+query,0,str(exc))
        if i < len(queries)-1: time.sleep(3)
    conn.commit()
    return rows


def enrich_recent(conn, items):
    """Fetch allowed short public page text; bounded and disabled by default.
    No paywall bypass, no auth, and no scripts executed.
    """
    if os.getenv('FETCH_FULL_TEXT','0') != '1': return
    session=requests.Session(); session.headers.update({'User-Agent':UA})
    count=0
    for item in items:
        if count>=int(os.getenv('MAX_FULLTEXT','12')): break
        fid=hashlib.sha256(item['url'].encode()).hexdigest()
        if conn.execute('SELECT 1 FROM enrichments WHERE finding_id=?',(fid,)).fetchone(): continue
        try:
            r=session.get(item['url'],timeout=(5,12),headers={'Accept':'text/html'})
            r.raise_for_status()
            if 'text/html' not in r.headers.get('content-type','').lower(): continue
            if len(r.content)>1000000: continue
            soup=BeautifulSoup(r.text,'html.parser')
            for bad in soup(['script','style','nav','footer','header','aside','form']): bad.decompose()
            node=soup.find('article') or soup.find('main') or soup.body
            body=re.sub(r'\s+',' ',node.get_text(' ',strip=True))[:7000] if node else ''
            if len(body)<120: continue
            conn.execute('INSERT OR REPLACE INTO enrichments VALUES(?,?,?,?,?)',(fid,body,len(body.split()),dt.datetime.now(dt.timezone.utc).isoformat(),'public-html'))
            count+=1
        except Exception as exc: LOG.debug('Full text unavailable: %s: %s',item['url'],exc)
    conn.commit()


def cluster_items(items,threshold=0.53):
    """Conservative lexical similarity fallback; no embedding runtime required.
    Compatible with any environment, allows distinct coverage to survive.
    """
    stop={'the','and','for','with','from','into','using','new','ai','a','an','to','of','in','on','is','are','as','at','this','that','how','why','by','your'}
    def tokens(x):
        return set(w for w in re.findall(r'[a-z0-9]{3,}',x.lower()) if w not in stop)
    clusters=[]
    for item in items:
        words=tokens(item['title']); placed=False
        for cluster in clusters:
            other=cluster[0]['_tokens']
            overlap=len(words & other)/max(1,len(words|other))
            if overlap>=threshold:
                item['_similarity']=round(overlap,3)
                cluster.append(item);placed=True;break
        if not placed:
            item['_tokens']=words;item['_similarity']=1.0;clusters.append([item])
    for cluster in clusters:
        for item in cluster: item.pop('_tokens',None)
    return clusters


def save_clusters(conn, clusters, day):
    conn.execute('DELETE FROM clusters WHERE day=?',(day,))
    for group in clusters:
        primary=hashlib.sha256(group[0]['url'].encode()).hexdigest()
        cid=hashlib.sha256((day+primary).encode()).hexdigest()[:20]
        for item in group:
            fid=hashlib.sha256(item['url'].encode()).hexdigest()
            conn.execute('INSERT OR REPLACE INTO clusters VALUES(?,?,?,?,?)',(day,cid,primary,fid,item.get('_similarity',1.0)))
    conn.commit()


def status_markdown(health,top=20):
    failed=[x for x in health if x['status']!='ok']
    lines=['# Source Health','',f'**Tracked:** {len(health)} · **Failed most recently:** {len(failed)}','',
           'Failures are recorded; failing sources do not stop the digest. Check Actions logs for details.','',
           '| Source | Type | Failed runs | Error |','|---|---|---:|---|']
    for x in failed[:top]:
        safe=lambda s: str(s or '').replace('|','\\|').replace('\n',' ')[:120]
        lines.append(f"| {safe(x['source'])} | {safe(x['kind'])} | {x['failures']} | {safe(x['error'])} |")
    if not failed: lines.append('| All checked sources operational | — | 0 | — |')
    return '\n'.join(lines)+'\n'
