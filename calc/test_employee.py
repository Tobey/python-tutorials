import unittest
from calc.employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('sue', 'Smith', 60000)

    def tearDown(self):
        pass

    def test_email(self):

        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('sue','Smith', 60000)

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'sue.smith@email.com')

        emp_1.first = 'john'
        emp_2.first = 'jane'

        self.assertEqual(self.emp_1.email, 'john.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'jane.smith@email.com')

    def test_fullname(self):

        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(self.emp_1.fullname, 'corey schafer')
        self.assertEqual(self.emp_2.fullname, 'sue smith')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'john schafer')
        self.assertEqual(self.emp_2.fullname, 'jane smith')

    def test_apply_raise(self):
        emp_1 = Employee('Corey', 'Schafer', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()




















