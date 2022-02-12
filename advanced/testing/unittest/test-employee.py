import unittest
from unittest.mock import patch
from employee import Employee

"""
test-class function execute in unorderly.

setUpClass 
  uses: 
      populate from database


tearDownClass
  uses:
      cleanup


If test cases use web data live, if website go down, the test will fails
we don't want test to fail if server is down
-> Mocking

Best Practices:
  test case should be isolated (it should be independent, should not rely on other test cases)

"""


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")
        self.emp_1 = Employee('Prabhu', 'Deva', 30000)
        self.emp_2 = Employee('John', 'Jebadurai', 40000)

    def tearDown(self):
        print("tearDown")

    def test_email(self):
        print("1. test_email")
        self.assertEqual(self.emp_1.email, 'Prabhu.Deva@email.com')
        self.assertEqual(self.emp_2.email, 'John.Jebadurai@email.com')

        self.emp_1.last = "Krishna"
        self.emp_2.last = "Doe"

        self.assertEqual(self.emp_1.email, 'Prabhu.Krishna@email.com')
        self.assertEqual(self.emp_2.email, 'John.Doe@email.com')

    def test_fullname(self):
        print("2. test_fullname")
        self.assertEqual(self.emp_1.fullname, 'Prabhu Deva')
        self.assertEqual(self.emp_2.fullname, 'John Jebadurai')

        self.emp_1.last = "Krishna"
        self.emp_2.last = "Doe"

        self.assertEqual(self.emp_1.fullname, 'Prabhu Krishna')
        self.assertEqual(self.emp_2.fullname, 'John Doe')

    def test_apply_raise(self):
        print("3. test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 31500)
        self.assertEqual(self.emp_2.pay, 42000)

    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Deva/May")
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Jebadurai/June")
            self.assertEqual(schedule, "Bad Response!")

if __name__ == "__main__":
    unittest.main()
