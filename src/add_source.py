"""Safely register a source from a GitHub issue, without exposing tokens to Pages.
Usage: python -m src.add_source --issue-file /tmp/issue.json
"""
import argparse
import ipaddress
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import yaml

CATEGORIES = {'Research','Security','Agents','Robotics','Models','Governance','Enterprise',
              'Engineering','Open source','Hardware','News','Regional','Quantum','Community'}
ROOT = Path(__file__).resolve().parent.parent


def parse_submission(body):
    """Treat issue text as untrusted; allow only a short fixed-format entry."""
    if len(body) > 5000:
        raise ValueError('Issue content is too long')
    fields = {}
    for line in body.splitlines():
        match = re.fullmatch(r'(URL|Category|Name):\s*(.*)', line.strip())
        if match:
            fields[match[1]] = match[2].strip()
    raw = fields.get('URL', '')
    if len(raw) > 1500 or any(c.isspace() for c in raw):
        raise ValueError('Invalid URL')
    p = urlsplit(raw)
    host = (p.hostname or '').lower().strip('.')
    if p.scheme != 'https' or not host or p.username or p.password or p.port is not None:
        raise ValueError('Public HTTPS URLs without credentials or custom ports are required')
    if host == 'localhost' or host.endswith(('.local', '.internal', '.localhost', '.test')):
        raise ValueError('Private or test hosts are not allowed')
    try:
        ipaddress.ip_address(host)
    except ValueError:
        if '.' not in host or not re.fullmatch(r'[a-z0-9.-]+', host):
            raise ValueError('Invalid DNS hostname')
    else:
        raise ValueError('IP addresses are not allowed')
    category = fields.get('Category', 'News')
    if category not in CATEGORIES:
        raise ValueError('Invalid category')
    name = fields.get('Name', host)
    if not name or len(name) > 110 or any(c in name for c in '\n\r<>'):
        raise ValueError('Invalid source name')
    # Never pass fragments to the collector.
    url = urlunsplit(('https', p.netloc, p.path or '/', p.query, ''))
    return {'name': name, 'category': category, 'url': url}


def add_source(submission, primary, extra):
    """Return True only if a new source was added. Keep other YAML fields intact."""
    normalized = submission['url'].rstrip('/').casefold()
    for filename, key in ((primary, 'sources'), (extra, 'extra_feeds')):
        doc = yaml.safe_load(Path(filename).read_text(encoding='utf-8')) or {}
        for existing in doc.get(key, []):
            if str(existing.get('url','')).rstrip('/').casefold() == normalized:
                return False
    path = Path(extra)
    doc = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
    doc.setdefault('extra_feeds', []).append(submission)
    path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=110), encoding='utf-8')
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--issue-file', type=Path, required=True)
    args = parser.parse_args()
    payload = json.loads(args.issue_file.read_text(encoding='utf-8'))
    issue = payload.get('issue') or {}
    if not issue.get('title','').startswith('[Add Source]'):
        raise ValueError('Not a source request')
    submission = parse_submission(issue.get('body') or '')
    created = add_source(submission, ROOT/'sources.yaml', ROOT/'extra_sources.yaml')
    print('ADDED' if created else 'EXISTS', submission['url'])

if __name__ == '__main__':
    main()
