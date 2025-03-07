import unittest
from RP4 import caesarCipher
class TestCaesarCipher(unittest.TestCase):
    def test_basic_shift(self):
        self.assertEqual(caesarCipher("abc", 3), "def")
        self.assertEqual(caesarCipher("xyz", 2), "zab")
    
    def test_uppercase_shift(self):
        self.assertEqual(caesarCipher("ABC", 3), "DEF")
        self.assertEqual(caesarCipher("XYZ", 2), "ZAB")
    
    def test_mixed_case(self):
        self.assertEqual(caesarCipher("HelloWorld", 5), "MjqqtBtwqi")
    
    def test_large_shift(self):
        self.assertEqual(caesarCipher("abc", 29), "def")  # เท่ากับ shift 3
    
    def test_non_alpha_characters(self):
        self.assertEqual(caesarCipher("hello, world!", 4), "lipps, asvph!")
    
    def test_no_shift(self):
        self.assertEqual(caesarCipher("Test123!", 0), "Test123!")
    
    def test_large_text(self):
        self.assertEqual(caesarCipher("A" * 100000, 1), "B" * 100000)

if __name__ == "__main__":
    unittest.main()