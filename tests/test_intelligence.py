import datetime as dt
import tempfile
import unittest
from pathlib import Path
from src.intelligence import within_window, group_events, build_report
from src.dashboard import write_dashboard
UTC=dt.timezone.utc
NOW=dt.datetime(2026,10,21,8,0,tzinfo=UTC)
def item(title, age=2, url=None,category='Research'):
 return {'title':title,'url':url or 'https://example.com/'+str(age)+title.replace(' ','-'), 'source':'arXiv AI','category':category,'published':(NOW-dt.timedelta(hours=age)).isoformat(),'summary':'Some research into agent security and evaluation.'}
class IntelligenceTests(unittest.TestCase):
 def test_strict_24h(self):
  self.assertTrue(within_window(item('New',24),NOW))
  self.assertFalse(within_window(item('Old',24.01),NOW))
  self.assertFalse(within_window(item('Future',-1),NOW))
  self.assertFalse(within_window({**item('Undated'), 'published':''},NOW))
 def test_clusters_and_boundaries(self):
  rows=[item('New agent security evaluation',1),item('New agent security evaluation',1,'https://elsewhere.com/story'),item('Old research release',30)]
  events=group_events(rows,NOW)
  self.assertEqual(len(events),1)
  self.assertEqual(len(events[0]['coverage']),1)
 def test_dashboard_artifacts(self):
  events=group_events([item('New agent security evaluation')],NOW)
  report=build_report(events,12,10,NOW)
  with tempfile.TemporaryDirectory() as d:
   write_dashboard(Path(d),report)
   self.assertIn('categories',(Path(d)/'data.json').read_text())
   self.assertIn('Explore categories',(Path(d)/'index.html').read_text())
   self.assertIn('Show remaining',(Path(d)/'app.js').read_text())
if __name__=='__main__':unittest.main()
