import unittest
from listOperations import find_max, find_min, calc_average

class TestListOpeartions(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max([9, 4, 3, 2, 1]), 9)
        self.assertEqual(find_max([-5, -3, -1]), -1)
        self.assertEqual(find_max([7]), 7)
        self.assertIsNone(find_max([]))

    def test_find_min(self):
        self.assertEqual(find_min([9, 4, 3, 2, 1]), 1)
        self.assertEqual(find_min([-5, -3, -1]), -5)
        self.assertEqual(find_min([7]), 7)
        self.assertIsNone(find_min([]))

    def test_calc_average(self):
        self.assertEqual(calc_average([1,2,3,4]),2.5)
        self.assertEqual(calc_average([1.5, 2.5, 3.5]),2.5)
        self.assertEqual(calc_average([-2,0,2]),0)
        with self.assertRaises(ValueError): # will raise error as the list should not be empty
            calc_average([])

if __name__== "__main__":
    unittest.main()