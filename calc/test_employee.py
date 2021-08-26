import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('Corey', 'Schafer', 50000 )
        self.emp_2 = Employee('sue', 'Schafer', 60000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'sue.Schafer@email.com')

        self.emp_1.first = 'john'
        self.emp_2.first = 'jane'

        self.assertEqual(self.emp_1.email, 'john.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'jane.Schafer@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'sue Schafer')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Schafer')

    def test_apply_raise(self):

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()




















