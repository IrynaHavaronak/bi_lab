import test_code
import unittest


class HappyNumbersTest(unittest.TestCase):
    def test_return_length(self):
        self.assertEqual(len(test_code.happy_numbers(10)), 3)
        self.assertEqual(len(test_code.happy_numbers(40)), 9)
        self.assertEqual(len(test_code.happy_numbers(1000)), 143)

    __res1 = [1, 7, 10]
    __res2 = [1, 7, 10, 13, 19, 23, 28, 31, 32]

    def test_result(self):
        self.assertEquals(test_code.happy_numbers(10), self.__res1)
        self.assertEquals(test_code.happy_numbers(40), self.__res2)


if __name__ == '__main__':
    unittest.main()
