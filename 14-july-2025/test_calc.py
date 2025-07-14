import unittest
from calc import Calculator

class testCalc(unittest.TestCase):

    # def __init__(self):
    #     pass

    # def test_add(self):
    def setUp(self):
        """Sets up an instance before each test / runs when a test is created"""
        print("Setting up the tests.......")
        self.calc = Calculator() #.calc is a variable that we have made, could be anything

    def test_add(self):
        result = self.calc.add(6,6)
        self.assertEqual(result, 12)

    def test_add_failure(self):
        result = self.calc.add(6,6)
        self.assertEqual(result, 20)

    def test_subtract(self):
        result = self.calc.subtract(50, 10)
        self.assertEqual(result, 40)

    def test_multiply(self):
        result = self.calc.multiply(3, 2)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_zero(self):
        with self.assertRaises(ValueError): # ValueError should be raised
            self.calc.divide(10,0 )

    def tearDown(self):
        """Does any clean up that needs to be done"""
        pass


if __name__ == "calc.py":
    unittest.calc()