from coenumber import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):

    def test_give_2_3_is_prime(self):
        prime_list = [2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_4_6_is_not_prime(self):
        prime_list = [4, 6]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_2_3_5_is_prime(self):
        prime_list = [2, 3, 5]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_8_9_10_is_not_prime(self):
        prime_list = [8, 9, 10]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_empty_list(self):
        prime_list = []
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)  # Empty list is considered valid

if __name__ == "__main__":
    unittest.main()
