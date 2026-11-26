import unittest
from normalizer import normalize


class NormalizeTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(normalize([]), [])

    def test_order_duplicates_and_case(self):
        self.assertEqual(normalize(["North", "west", "North"]), ["North", "west", "North"])

    def test_internal_whitespace(self):
        self.assertEqual(normalize(["a b", "C  d"]), ["a b", "C  d"])
