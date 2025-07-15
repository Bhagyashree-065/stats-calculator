import unittest
from mean_var_std import calculate

class TestCalculate(unittest.TestCase):
    def test_valid_input(self):
        result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        expected_mean = [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0]
        self.assertEqual(result['mean'], expected_mean)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate([1, 2, 3])

if __name__ == "__main__":
    unittest.main()