import unittest
from tempConverter import celsius_to_fahrenheit, fahrenheit_to_celsius

class test_tempConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32, places=7)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)
        self.assertAlmostEqual(celsius_to_fahrenheit(-20), -4)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40)  # -40°F = -40°C
        self.assertAlmostEqual(fahrenheit_to_celsius(-4), -20)

    def test_absolute_zero(self):
        with self.assertRaises(ValueError):
            celsius_to_fahrenheit(-300)  # Below -273.15°C

        with self.assertRaises(ValueError):
            fahrenheit_to_celsius(-500)

if __name__ == '__main__':
    unittest.main()