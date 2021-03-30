import sys
import unittest
import warnings

from app.app import get_status_res,parse_city_ngs


class TestSum(unittest.TestCase):
    def test_resp_status_res(self):
        self.assertEqual(get_status_res(),200)
    def test_parse_city_ngs(self):
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")
        self.assertEqual(parse_city_ngs("test"),"ok")
if __name__ == '__main__':
    unittest.main()