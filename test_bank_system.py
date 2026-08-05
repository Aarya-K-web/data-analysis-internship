"""Unit tests for the bank accrued-interest calculation notebook."""

import json
from pathlib import Path
import unittest


def load_calculate_accrued_interest():
    """Load the calculation function from the supplied Jupyter notebook."""
    notebook_path = Path(__file__).with_name("31-07-26 Part A Task 5.ipynb")
    with notebook_path.open(encoding="utf-8") as notebook_file:
        notebook = json.load(notebook_file)

    namespace = {}
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            exec("".join(cell["source"]), namespace)

    return namespace["calculate_accrued_interest"]


calculate_accrued_interest = load_calculate_accrued_interest()


class TestCalculateAccruedInterest(unittest.TestCase):
    def test_standard_positive_interest_calculation(self):
        """Compounds a positive balance at a positive annual rate."""
        result = calculate_accrued_interest(1000, 5, 2)

        self.assertEqual(result, 1102.5)

    def test_zero_interest_rate_returns_effective_balance(self):
        """A zero rate leaves the balance unchanged when there is no fee."""
        result = calculate_accrued_interest(1500, 0, 3)

        self.assertEqual(result, 1500.0)

    def test_transaction_fee_is_deducted_before_compounding(self):
        """Applies interest only to the balance remaining after the fee."""
        result = calculate_accrued_interest(1000, 10, 2, transaction_fee=100)

        self.assertEqual(result, 1089.0)

    def test_boundary_values_allow_zero_balance_and_fee_equal_to_balance(self):
        """Zero balance and a fee equal to the balance are valid edge cases."""
        self.assertEqual(calculate_accrued_interest(0, 5, 1), 0.0)
        self.assertEqual(calculate_accrued_interest(100, 5, 1, transaction_fee=100), 0.0)

    def test_boundary_value_one_year_is_valid(self):
        """The smallest permitted investment term is one year."""
        self.assertEqual(calculate_accrued_interest(1000, 5, 1), 1050.0)

    def test_value_error_for_invalid_numeric_ranges(self):
        """Rejects negative values, a zero-year term, and fees above balance."""
        invalid_arguments = [
            (-1, 5, 1),
            (100, -1, 1),
            (100, 5, 0),
            (100, 5, 1, -1),
            (100, 5, 1, 101),
        ]

        for arguments in invalid_arguments:
            with self.subTest(arguments=arguments):
                with self.assertRaises(ValueError):
                    calculate_accrued_interest(*arguments)

    def test_type_error_for_non_numeric_input(self):
        """Rejects strings and other non-numeric inputs."""
        invalid_arguments = [
            ("1000", 5, 1),
            (1000, None, 1),
            (1000, 5, "1"),
            (1000, 5, 1, []),
        ]

        for arguments in invalid_arguments:
            with self.subTest(arguments=arguments):
                with self.assertRaises(TypeError):
                    calculate_accrued_interest(*arguments)


if __name__ == "__main__":
    unittest.main()
