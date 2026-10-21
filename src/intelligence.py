"""Deterministic, auditable 24-hour prioritization and digest construction."""
import datetime as dt
import hashlib
import re
from collections import Counter, defaultdict

CATEGORIES = ['Top stories','Agents','Security','Research','Robotics','Models','Engineering','Open source','Hardware','Governance','Enterprise','Business','Regional','Quantum','Community','News']
INTERESTS = {
 'Security': ['prompt injection','agent security','vulnerability','exploit','attack','red team','supply chain','mcp','security','privacy','data leak','malware'],
 'Agents': ['agent','agentic','workflow','tool use','orchestration','multi-agent','automation','mcp','computer use'],
 'Governance': ['governance','regulation','policy','compliance','ai act','nist','risk management','safety standard'],
 'Engineering': ['rag','retrieval','inference','fine-tun','training','context window','benchmark','deployment','evaluation','llmops'],
 'Enterprise': ['enterprise','business','insurance','manufacturing','procurement','customer service','operations','supply chain'],
 'Regional': ['lebanon','arabic','middle east','mena','gulf','saudi','uae'],
 'Robotics': ['robot','embodied','humanoid','autonomous','manipulation','spatial'],
 'Research': ['reasoning','transformer','world model','multimodal','benchmark','foundation model'],
 'Models': ['model release','new model','model weights','open weights','api','capability'],
 'Hardware': ['gpu','nvidia','amd','chip','inference','accelerator','memory','compute'],
 'Open source': ['open source','open-source','github','framework','library','sdk'],
 'Quantum': ['quantum machine learning','quantum ai','quantum neural']
}
IMPACT = {
 'critical': ['actively exploited','remote code execution','zero-day','emergency patch','major vulnerability','regulatory deadline'],
 'high': ['released','launch','release','breakthrough','state-of-the-art','new benchmark','open weights','security','attack','policy','standard','framework','agent','reasoning','performance','cost reduction'],
 'medium':['research','training','fine-tuning','method','evaluation','inference','prototype','architecture']
}
LOW_VALUE = ['submitted by /u/', 'weekly roundup', 'discussion thread', 'sponsored']
STOP = set('with from that this their where about model models using across into through which have more ai llm new paper study approach based evaluation results framework method how why what for the and are to in of on by an as at'.split())

def tokens(title):
    return {t for t in re.findall(r'[a-z0-9]{3,}',title.lower()) if t not in STOP}

def classify(row):
    cat=row.get('category','News')
    title=(row.get('title','')+' '+row.get('summary','')[:240]).lower()
    # Route cross-domain AI research into its primary practical domain when clear.
    if cat in ('Research','News','Community','Hardware','Engineering'):
        for label in ('Security','Robotics','Governance','Agents','Regional'):
            hits=sum(bool(re.search(r'\b'+re.escape(w)+r'\b',title)) for w in INTERESTS[label])
            if hits>=2 and (cat!='Hardware' or label=='Security'):
                return label
    return cat if cat in CATEGORIES else 'News'

def score(row):
    title=row['title'].lower(); body=(title+' '+row.get('summary','')[:400].lower())
    category=classify(row)
    relevant=sum(min(2, sum(1 for word in terms if word in body)) for key,terms in INTERESTS.items() if key in ('Security','Agents','Governance','Engineering','Enterprise','Regional','Robotics','Research'))
    matched=[k for k,terms in INTERESTS.items() if any(term in body for term in terms)]
    source=row.get('source','').lower()
    trust=3 if any(v in source for v in ('arxiv','research','github','nist','cisa','owasp','deepmind','openai','anthropic')) else 2 if any(v in source for v in ('techcrunch','aws','microsoft','ieee','hugging face')) else 1
    importance=5 if any(k in body for k in IMPACT['critical']) else 3 if any(k in title for k in IMPACT['high']) else 2 if any(k in body for k in IMPACT['medium']) else 1
    penalty=3 if any(k in body for k in LOW_VALUE) else 0
    if category=='Community': penalty+=2
    value=max(0, round(importance*2+min(relevant,6)+trust-penalty))
    label='High signal' if value>=14 else 'Worth watching' if value>=10 else 'Other developments'
    return value,label,matched

def within_window(item, now, hours=24):
    try:
        date=dt.datetime.fromisoformat(str(item['published']).replace('Z','+00:00'))
        if date.tzinfo is None: return False
        return now-dt.timedelta(hours=hours)<=date.astimezone(dt.timezone.utc)<=now
    except (TypeError, ValueError): return False

def group_events(rows, now, hours=24):
    """Group near-identical titles but keep different technical contributions separate."""
    seen=[]
    for row in rows:
        if not within_window(row,now,hours): continue
        r=dict(row); r['category']=classify(r)
        r['score'],r['priority'],r['interests']=score(r)
        ts=tokens(r['title']); r['event_id']=hashlib.sha256(r['url'].encode()).hexdigest()[:12]
        match=None
        for entry in seen:
            other=tokens(entry['title'])
            sim=len(ts&other)/max(1,len(ts|other))
            if sim>=0.70 and len(ts&other)>=min(3,len(ts),len(other)):
                match=entry;break
        if match is not None:
            match.setdefault('coverage',[]).append({'source':r['source'],'url':r['url']})
            if r['score']>match['score']:
                # Keep canonical event id and merged coverage; prefer higher quality evidence.
                old={'source':match['source'],'url':match['url']}
                history=match['coverage'];ident=match['event_id']
                match.update(r);match['coverage']=history+[old];match['event_id']=ident
        else:
            r['coverage']=[];seen.append(r)
    seen.sort(key=lambda x:(x['score'],x['published']),reverse=True)
    return seen

def build_report(events, fetched, inserted, now, health=None, narratives=None):
    groups=defaultdict(list)
    for item in events: groups[item['category']].append(item)
    top=events[:int(__import__('os').getenv('TOP_STORIES','10'))]
    cats=[]
    for category in CATEGORIES[1:]:
        items=groups.get(category,[])
        if not items: continue
        high=sum(x['priority']=='High signal' for x in items)
        cats.append({'name':category,'count':len(items),'high':high,'top':items[:3],'items':items,
            'narrative':(narratives or {}).get(category) or evidence_summary(category,items)})
    health=health or []
    failed=sum(x.get('status')!='ok' for x in health)
    return {'generated':now.isoformat(),'window_hours':24,'window_start':(now-dt.timedelta(hours=24)).isoformat(),
      'stats':{'events':len(events),'high':sum(x['priority']=='High signal' for x in events),
        'sources_reporting':len({x['source'] for x in events}), 'categories':len(cats), 'records_inserted':inserted,
        'fetched':fetched,'sources_failed':failed,'source_checks':len(health)},
      'top':top,'categories':cats,'health':health,
      'executive':(narratives or {}).get('executive') or executive_summary(top)}

def evidence_summary(category,items):
    if not items: return 'No verified published findings during this window.'
    titles='; '.join(x['title'] for x in items[:3])
    return f"{len(items)} distinct {category.lower()} developments appeared in the last 24 hours. Highest-ranked topics: {titles}. These are relevance signals, not independently verified breakthroughs; consult the linked sources for evidence and actual performance."

def executive_summary(top):
    if not top:return 'No dated findings were collected for the last 24 hours. This may also indicate source failures; see Source health.'
    count=Counter(x['category'] for x in top)
    focus=', '.join(f'{cat} ({n})' for cat,n in count.most_common(4))
    return f'The highest-ranked developments in this 24-hour window concentrate on {focus}. Scores reflect relevance, source type and headline signals, not independently established impact. Read the linked evidence before making decisions.'
