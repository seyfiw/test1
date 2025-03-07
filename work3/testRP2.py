import unittest
from RP2 import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):
    def test_no_deletion_needed(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
    
    def test_all_same_characters(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("BBBBBB"), 5)
    
    def test_some_deletions_needed(self):
        self.assertEqual(alternatingCharacters("AABBAB"), 2)
        self.assertEqual(alternatingCharacters("ABBA"), 1)
    
    def test_single_character(self):
        self.assertEqual(alternatingCharacters("A"), 0)
        self.assertEqual(alternatingCharacters("B"), 0)
    
    def test_alternating_patterns(self):
        self.assertEqual(alternatingCharacters("ABAB"), 0)
        self.assertEqual(alternatingCharacters("AABBAABB"), 4)
    
    def test_large_input(self):
        self.assertEqual(alternatingCharacters("A" * 100000), 99999)
        self.assertEqual(alternatingCharacters("AB" * 50000), 0)

if __name__ == "__main__":
    unittest.main()
