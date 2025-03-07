from fizzbuzz import fizz_buzz

import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_give_1_2_3(self):
        number_list = [1, 2, 3]
        excected_output = [1, 2, "Fizz"]
        self.assertEqual(fizz_buzz(number_list), excected_output)

    def test_give_5_is_Buzz(self):
        number_list = [5]
        excected_output = ["Buzz"]
        self.assertEqual(fizz_buzz(number_list), excected_output)

    def test_give_15_is_FizzBuzz(self):
        number_list = [15]
        excected_output = ["FizzBuzz"]
        self.assertEqual(fizz_buzz(number_list), excected_output)

    def test_give_3_5_15(self):
        number_list = [3, 5, 15]
        expected_output = ["Fizz", "Buzz", "FizzBuzz"]
        self.assertEqual(fizz_buzz(number_list), expected_output)