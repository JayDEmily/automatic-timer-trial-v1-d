import unittest
from normalizer import normalize


class NormalizeTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(normalize([]), [])

    def test_order_duplicates_and_case(self):
        self.assertEqual(normalize(["North", "west", "North"]), ["North", "west", "North"])

    def test_internal_whitespace(self):
        self.assertEqual(normalize(["a b", "C  d"]), ["a b", "C  d"])

    def test_trims_edges(self):
        self.assertEqual(normalize(["  North  ", "\tWest\n", "\u2003C\u2003"]), ["North", "West", "C"])

    def test_omits_blank_strings(self):
        self.assertEqual(normalize(["", " ", "\t\n", " a ", ""]), ["a"])

    def test_trim_preserves_order_duplicates_case_and_internal_whitespace(self):
        self.assertEqual(normalize(["  A  b ", " c ", "A  b", "\tC d\n"]), ["A  b", "c", "A  b", "C d"])
