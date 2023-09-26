import unittest
import sys
import io
from tip_calculator import tip_calculator
from unittest import mock, TestCase

class TestTipCalculator(unittest.TestCase):

    def test_tip_calculation_1(self):
        # Test case: Calculate tip for a meal for 1 person.
        expected_output = "Total bill: $125.00\nEach person should pay: $125.00\n"
        input_values = ['100', '1', '15']
        with unittest.mock.patch('builtins.input', side_effect=input_values):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                tip_calculator()
                self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_tip_calculation_large_group(self):
        # Test case: Calculate tip for a meal for 7 people.
        expected_output = "Total bill: $125.00\nEach person should pay: $17.86\n"
        input_values = ['100', '7', '15']
        with unittest.mock.patch('builtins.input', side_effect=input_values):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                tip_calculator()
                self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_tip_calculation_no_tip(self):
        # Test case: Calculate bill with no tip for 5 people.
        expected_output = "Total bill: $110.00\nEach person should pay: $22.00\n"
        input_values = ['100', '5', '0']
        with unittest.mock.patch('builtins.input', side_effect=input_values):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                tip_calculator()
                self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
