import unittest
from calc import calc_func
from unittest import TestCase


class TestCalc(unittest.Tastcase):

    def test_add(self):
        result = calc_func.add(10, 5)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
