import unittest

from report import remove_none_values
from report import sort_pages
from crawl import get_urls_from_string
from crawl import normalize_url

class Tests(unittest.TestCase):
    def test_remove_none_values(self):
        self.assertEqual({}, remove_none_values({"1": None}))
        self.assertEqual({"1": "1"}, remove_none_values({"1": "1", "2": None}))
        self.assertEqual({}, remove_none_values({}))
        self.assertEqual({"1": "1"}, remove_none_values({"1": "1"}))

    def test_sort_pages(self):
        self.assertEqual([('first', 45)], sort_pages({'first': 45}))
        self.assertEqual([('first', 45), ('second', 62), ('third', 75)], sort_pages({'first': 45, 'second': 62, 'third': 75} ))

    def test_get_urls_from_string(self):
        self.assertEqual(["https://blog.boot.dev"], get_urls_from_string('<html><body><a href="https://blog.boot.dev"><span>Boot.dev></span></a></body></html>', "https://blog.boot.dev",))

    def test_normalize_url(self):
        self.assertEqual('docs.python.org:80/3/library/urllib.parse.html', normalize_url("http://docs.python.org:80/3/library/urllib.parse.html?highlight=params#url-parsing"))
        self.assertEqual('docs.python.org:80/3/library/urllib.parse.html', normalize_url("http://docs.python.org:80/3/library/urllib.parse.html?highlight=params#url-parsing/"))

if __name__ == "__main__":
    unittest.main()
