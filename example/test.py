from unittest import TestCase

from example.main import Business
from example.main import Menu


class TestMyExampleClass(TestCase):
    """
    To run all test, use the command

    pytest -vs example/test.py

    """

    def test_business_class(self):
        my_business = Business("Another Software Company", None)
        self.assertEqual(my_business.name, "Another Software Company")

    # def test_something_else(self):
    #     self.assertTrue(False)

    def test_menu_setup(self):
        early_bird_items = {
            'salumeria plate': 8.00,
            'salad and breadsticks (serves 2, no refills)': 14.00,
            'pizza with quattro formaggi': 9.00,
            'duck ragu': 17.50,
            'mushroom ravioli (vegan)': 13.50,
            'coffee': 1.50,
            'espresso': 3.00,
        }

        menu = Menu("menu 1", early_bird_items, "1000", "1400")

        self.assertEqual(menu.name, "menu 1")
        self.assertDictEqual(menu.items, early_bird_items)
        self.assertEqual(menu.start_time, "1000")
        self.assertEqual(menu.end_time, "1400")

        # early_bird_bill = menu.calculate_bill(['sojlrfjodnjksvnk'])
        # self.assertEqual(early_bird_bill, 0)
        #
        # early_bird_bill = menu.calculate_bill(['sojlrfjodnjksvnk'])
        # self.assertEqual(early_bird_bill, 0)
        # early_bird_bill = menu.calculate_bill(['sojlrfjodnjksvnk'])
        # self.assertEqual(early_bird_bill, 0)
        # early_bird_bill = menu.calculate_bill(['sojlrfjodnjksvnk'])
        # self.assertEqual(early_bird_bill, 0)
        # early_bird_bill = menu.calculate_bill(['sojlrfjodnjksvnk'])
        # self.assertEqual(early_bird_bill, 0)
        #
        # early_bird_bill = menu.calculate_bill(['sojlrfjodnjksvnk'])
        # self.assertEqual(early_bird_bill, 0)
