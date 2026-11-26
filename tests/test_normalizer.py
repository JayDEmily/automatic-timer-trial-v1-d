import unittest
from normalizer import normalize


class NormalizeTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(normalize([]), [])

    def test_order_duplicates_and_case(self):
        self.assertEqual(normalize(["North", "west", "North"]), ["North", "west", "North"])

    def test_internal_whitespace(self):
        self.assertEqual(normalize(["a b", "C  d"]), ["a b", "C  d"])

    def test_trim_outer_whitespace(self):
        self.assertEqual(normalize(["  North ", "\twest\n", "South"]), ["North", "west", "South"])

    def test_omit_empty_and_blank_entries(self):
        self.assertEqual(normalize(["", " ", "\t\n", " A ", "", "B"]), ["A", "B"])

    def test_trim_preserves_order_duplicates_case_internal_whitespace(self):
        self.assertEqual(normalize([" A  b ", "west", " A  b", "a B ", "  "]), ["A  b", "west", "A  b", "a B"])
