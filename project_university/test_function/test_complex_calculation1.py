import math
import unittest
from function.complex_calculation import complex_calculation


class TestComplexCalculation(unittest.TestCase):

    def test_normal_calculation(self):
        result = complex_calculation(3, 1, 2)

        expected = ((3**2 + 1**2) / 2) + (
            math.sqrt(3 + 1) * math.factorial(2)
        )

        self.assertEqual(result, expected)

    def test_zero_division(self):
        with self.assertRaises(ValueError):
            complex_calculation(3, 2, 0)

    def test_negative_square_root(self):
        with self.assertRaises(ValueError):
            complex_calculation(-5, 2, 3)

    def test_negative_factorial(self):
        with self.assertRaises(ValueError):
            complex_calculation(3, 2, -1)

    def test_result_type(self):
        result = complex_calculation(3, 1, 2)

        self.assertIsInstance(result, float)


if __name__ == "__main__":
    unittest.main()