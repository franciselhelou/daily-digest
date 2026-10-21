import tempfile
import unittest
from pathlib import Path
import yaml
from src.add_source import parse_submission, add_source

class AddSourceTests(unittest.TestCase):
    def test_parses_valid(self):
        s=parse_submission('URL: https://example.org/rss.xml\nCategory: Security\nName: Example Alerts')
        self.assertEqual(s['category'], 'Security')
        self.assertEqual(s['url'], 'https://example.org/rss.xml')
    def test_rejects_non_public_urls(self):
        for url in ['http://example.org/feed','https://localhost/x','https://127.0.0.1/x','https://example.com:444/feed','https://foo.internal/rss']:
            with self.subTest(url=url), self.assertRaises(ValueError):
                parse_submission('URL: '+url+'\nCategory: News')
    def test_append_and_deduplicate(self):
        with tempfile.TemporaryDirectory() as d:
            a=Path(d)/'sources.yaml';b=Path(d)/'extra_sources.yaml'
            a.write_text('sources: []\n');b.write_text('extra_feeds: []\n')
            s=parse_submission('URL: https://example.org/feed\nCategory: News')
            self.assertTrue(add_source(s,a,b))
            self.assertFalse(add_source(s,a,b))
            self.assertEqual(len(yaml.safe_load(b.read_text())['extra_feeds']),1)
if __name__=='__main__':unittest.main()
