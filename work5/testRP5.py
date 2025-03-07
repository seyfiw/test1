import unittest
from RP5 import alternate

class TestAlternate(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(alternate("beabeefeab"), 5)
        self.assertEqual(alternate("ababab"), 6)
    
    def test_no_valid_string(self):
        self.assertEqual(alternate("aaaa"), 0)
        self.assertEqual(alternate("abcabcabc"), 0)
    
    def test_single_character(self):
        self.assertEqual(alternate("a"), 0)
        self.assertEqual(alternate("bb"), 0)
    
    def test_alternating_string(self):
        self.assertEqual(alternate("abab"), 4)
        self.assertEqual(alternate("baba"), 4)
    
    def test_large_input(self):
        self.assertEqual(alternate("ab" * 50000), 100000)
    
    def test_edge_cases(self):
        self.assertEqual(alternate("aabbccddeeff"), 2)
        self.assertEqual(alternate("zxyzyx"), 4)

if __name__ == "__main__":
    unittest.main()
