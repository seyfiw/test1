import unittest
from RP6 import gridChallenge

class TestGridChallenge(unittest.TestCase):
    def test_valid_grids(self):
        self.assertEqual(gridChallenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES")
        self.assertEqual(gridChallenge(["abc", "ade", "efg"]), "YES")
    

    def test_single_row(self):
        self.assertEqual(gridChallenge(["abcde"]), "YES")
        self.assertEqual(gridChallenge(["zyxwv"]), "YES")
    
    def test_single_column(self):
        self.assertEqual(gridChallenge(["a", "b", "c", "d"]), "YES")
        self.assertEqual(gridChallenge(["d", "c", "b", "a"]), "NO")
    
    def test_large_grid(self):
        self.assertEqual(gridChallenge(["abcdefghij" for _ in range(100)]), "YES")

if __name__ == "__main__":
    unittest.main()