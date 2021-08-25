import unittest
import Calc
from unittest import TestCase
import Calc

class TestCal(unittest.Tastcase):

    def test_add(self):
        result = Calc.add(10, 5)
        self.assertEqual(result, 15)
