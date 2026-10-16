import sqlite3
import unittest
from src.advanced import cluster_items, health_schema, source_status, update_health

class AdvancedTests(unittest.TestCase):
    def test_clusters_near_duplicate(self):
        rows=[{'title':'Model Alpha launches with low cost inference','url':'https://a.test/1'},
              {'title':'Model Alpha launches with low cost inference today','url':'https://b.test/2'},
              {'title':'EU publishes AI compliance implementation guidance','url':'https://c.test/3'}]
        result=cluster_items(rows)
        self.assertEqual(len(result),2)
        self.assertEqual(len(result[0]),2)
    def test_source_health_failure_recovery(self):
        conn=sqlite3.connect(':memory:')
        health_schema(conn)
        update_health(conn,'Test','feed','https://e.test/rss',0,'timeout')
        update_health(conn,'Test','feed','https://e.test/rss',0,'timeout')
        self.assertEqual(source_status(conn)[0]['failures'],2)
        update_health(conn,'Test','feed','https://e.test/rss',3)
        self.assertEqual(source_status(conn)[0]['failures'],0)
        self.assertEqual(source_status(conn)[0]['status'],'ok')

if __name__=='__main__': unittest.main()
