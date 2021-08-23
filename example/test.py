from unittest import TestCase

from example.main import Business


class TestMyExampleClass(TestCase):
    """
    To run all test, use the command

    pytest -vs example/test.py

    """

    def test_business_class(self):
        my_business = Business("Another Software Company", None)
        self.assertEqual(my_business.name, "Another Software Company")

    