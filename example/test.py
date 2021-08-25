import unittest

from unittest import TestCase
import Calc


class TestCalc(TestCase):

    def test_add(self):
        Calc.add(10, 5)
        self.assertEqual(Calc.add(10, 5), 15)


if __name__ == '__main__':
    unittest.main()


