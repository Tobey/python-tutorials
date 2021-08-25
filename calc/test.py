import unittest
from calc import calc_func
from unittest import TestCase


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc_func.add(10, 5), 15)
        self.assertEqual(calc_func.add(20, 5), 25)
        self.assertEqual(calc_func.add(35, 5), 40)
        self.assertEqual(calc_func.add(40, 5), 45)
        self.assertEqual(calc_func.add(45, 5), 50)

    def test_multiply(self):
        self.assertEqual(calc_func.multiply(10, 5), 50)
        self.assertEqual(calc_func.multiply(20, 5), 100)
        self.assertEqual(calc_func.multiply(5, 5), 25)
        self.assertEqual(calc_func.multiply(40, 5), 200)
        self.assertEqual(calc_func.multiply(30, 5), 150)

    def test_divide(self):
        self.assertEqual(calc_func.divide(10, 5), 2)
        self.assertEqual(calc_func.divide(20, 5), 4)
        self.assertEqual(calc_func.divide(35, 5), 7)
        self.assertEqual(calc_func.divide(40, 5), 8)
        self.assertEqual(calc_func.divide(45, 5), 9)

        self.assertRaises(ValueError, calc_func.divide, 10, 0)

    def test_subtract(self):
        self.assertEqual(calc_func.subtract(10, 5), 5)
        self.assertEqual(calc_func.subtract(20, 5), 15)
        self.assertEqual(calc_func.subtract(35, 5), 30)
        self.assertEqual(calc_func.subtract(40, 5), 35)
        self.assertEqual(calc_func.subtract(45, 5), 40 )


if __name__ == '__main__':
    unittest.main()
