import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupclass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setup')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('sue', 'Schafer', 60000)


    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'sue.Schafer@email.com')

        self.emp_1.first = 'john'
        self.emp_2.first = 'jane'

        self.assertEqual(self.emp_1.email, 'john.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'jane.Schafer@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'sue Schafer')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Schafer')

    def test_apply_raise(self):
        print('test_apply_raise')

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.ok = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_1.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Resonse')


if __name__ == '__main__':
    unittest.main()




















