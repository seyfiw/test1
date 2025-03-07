import unittest
from number import is_prime_list

def is_prime_list(numbers):
    for num in numbers:
        for n in range(2, num):
            if num % n == 0:
                return False
    return True

class TestPrimeFunctions(unittest.TestCase):

    def test_prime_numbers(self):
        # ทดสอบกรณีที่ส่งเลขจำนวนเฉพาะ
        self.assertTrue(is_prime_list([2, 3, 5, 7, 11]))

    def test_non_prime_numbers(self):
        # ทดสอบกรณีที่ส่งเลขที่ไม่ใช่จำนวนเฉพาะ
        self.assertFalse(is_prime_list([4, 6, 8, 9, 10]))

    def test_mixed_numbers(self):
        # ทดสอบกรณีที่มีทั้งเลขจำนวนเฉพาะและเลขที่ไม่ใช่จำนวนเฉพาะ
        self.assertFalse(is_prime_list([2, 4, 5, 8, 11]))

    def test_empty_list(self):
        # ทดสอบกรณีที่ส่งลิสต์ว่าง
        self.assertTrue(is_prime_list([]))

    def test_single_number(self):
        # ทดสอบกรณีที่มีเพียงเลขเดียว
        self.assertTrue(is_prime_list([7]))
        self.assertFalse(is_prime_list([4]))

if __name__ == "__main__":
    unittest.main()
