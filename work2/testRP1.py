import unittest
from RP1 import is_funny_string 

class TestFunnyString(unittest.TestCase):
    
    def test_funny_string(self):
        self.assertEqual(is_funny_string("acxz"), "Funny")
        self.assertEqual(is_funny_string("aabbb"), "Not Funny")
        self.assertEqual(is_funny_string("abccba"), "Funny")  # แก้จาก "Not Funny" เป็น "Funny"
        self.assertEqual(is_funny_string("abcba"), "Funny")
        self.assertEqual(is_funny_string("a"), "Funny")
        self.assertEqual(is_funny_string("abcd"), "Funny")

    def test_empty_string(self):
        self.assertEqual(is_funny_string(""), "Funny")  # Empty string should be funny

if __name__ == "__main__":
    unittest.main()