import sqlite3
import tempfile
import unittest
from pathlib import Path
from src.pipeline import canonical, clean, init_db, store, create_markdown, NOW

class PipelineTests(unittest.TestCase):
    def test_canonical_utm(self):
        self.assertEqual(canonical('https://example.com/a/?utm_source=x&q=1#frag'), 'https://example.com/a?q=1')
    def test_clean_html(self):
        self.assertEqual(clean('<p>Hello <b>world</b></p>'), 'Hello world')
    def test_storage_deduplication(self):
        with sqlite3.connect(':memory:') as con:
            init_db(con)
            item={'title':'Sample release','url':'https://example.com/release','source':'Test','category':'Models', 'published':NOW.isoformat(),'summary':'An update'}
            self.assertEqual(store(con,[item,item]),1)
            self.assertEqual(con.execute('SELECT count(*) FROM findings').fetchone()[0],1)
    def test_source_links(self):
        item={'title':'Sample','url':'https://example.com/release','source':'Test','category':'Models', 'published':NOW.isoformat(),'summary':'An update'}
        content=create_markdown([item],1,1,'')
        self.assertIn('[Sample](https://example.com/release)', content)
        self.assertIn('## Models',content)

if __name__ == '__main__':
    unittest.main()
