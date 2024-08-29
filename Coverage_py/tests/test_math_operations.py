"""
Unit tests for the math_operations module.

This module contains tests for the arithmetic functions
provided by the math_operations module, including addition,
subtraction, and division operations.
"""

import unittest
from math_operations import add, subtract, divide

class TestMathOperations(unittest.TestCase):
    """
    Test cases for the functions in the math_operations module.
    """

    def test_add(self):
        """
        Test addition of two positive integers.
        """
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        """
        Test subtraction of two positive integers.
        """
        self.assertEqual(subtract(5, 3), 2)

    def test_divide(self):
        """
        Test division of two positive integers.
        """
        self.assertAlmostEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Test division by zero raises ValueError.
        """
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_add_negative(self):
        """
        Test addition of two negative integers.
        """
        self.assertEqual(add(-1, -2), -3)

    def test_subtract_negative(self):
        """
        Test subtraction of two negative integers.
        """
        self.assertEqual(subtract(-5, -3), -2)

    def test_divide_small_number(self):
        """
        Test division with a very small denominator.
        """
        self.assertAlmostEqual(divide(1, 0.0001), 10000)

    def test_divide_large_numbers(self):
        """
        Test division with very large numbers.
        """
        self.assertEqual(divide(1e+10, 1e+5), 1e+5)

    def test_add_non_numeric(self):
        """
        Test addition with non-numeric inputs raises TypeError.
        """
        with self.assertRaises(TypeError):
            add("string", 2)

    def test_subtract_non_numeric(self):
        """
        Test subtraction with non-numeric inputs raises TypeError.
        """
        with self.assertRaises(TypeError):
            subtract(5, "string")

    def test_divide_non_numeric(self):
        """
        Test division with non-numeric inputs raises TypeError.
        """
        with self.assertRaises(TypeError):
            divide("string", 2)

if __name__ == '__main__':
    unittest.main()
