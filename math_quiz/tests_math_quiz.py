import unittest
from math_quiz import generate_number, get_random_operator, generate_problem


class TestMathQuiz(unittest.TestCase):
    def test_generate_number(self):
        """
        Test the random number generator function.

        Test cases:
        1. Numbers are within specified range
        2. Boundary values are possible
        3. Works with different ranges
        """
        # Test case 1: Check if numbers are within range
        min_val, max_val = 1, 10
        for _ in range(100):
            num = generate_number(min_val, max_val)
            self.assertTrue(min_val <= num <= max_val,
                            f"Generated number {num} not in range {min_val}-{max_val}")

        # Test case 2: Test different ranges
        test_ranges = [(1, 5), (1, 10), (0, 100)]
        for min_val, max_val in test_ranges:
            num = generate_number(min_val, max_val)
            self.assertTrue(min_val <= num <= max_val,
                            f"Generated number {num} not in range {min_val}-{max_val}")

    def test_get_random_operator(self):
        """
        Test the random operator generator function.

        Test cases:
        1. Only valid operators are returned
        2. All operators can be generated
        3. Operator distribution is reasonable
        """
        valid_operators = {'+', '-', '*'}
        generated_operators = set()
        operator_count = {'+': 0, '-': 0, '*': 0}

        # Generate many operators to test distribution
        for _ in range(300):
            operator = get_random_operator()
            # Test case 1: Verify operator is valid
            self.assertIn(operator, valid_operators,
                          f"Invalid operator {operator} generated")
            generated_operators.add(operator)
            operator_count[operator] += 1

        # Test case 2: Verify all operators can be generated
        self.assertEqual(generated_operators, valid_operators,
                         "Not all operators were generated")

        # Test case 3: Check if distribution is reasonably uniform
        for count in operator_count.values():
            self.assertTrue(50 <= count <= 150,
                            "Operator distribution seems biased")

    def test_generate_problem(self):
        """
        Test the problem generator function.

        Test cases:
        1. Correct problem string format
        2. Correct answer calculation for each operator
        3. Different number combinations
        4. Edge cases
        """
        # Test case 1 & 2: Basic operations
        test_cases = [
            (5, 3, '+', "5 + 3", 8),
            (10, 5, '-', "10 - 5", 5),
            (4, 3, '*', "4 * 3", 12),
            (1, 1, '+', "1 + 1", 2),  # Edge case: minimum numbers
            (10, 5, '*', "10 * 5", 50)  # Larger numbers
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_problem(num1, num2, operator)

            # Test problem string
            self.assertEqual(problem, expected_problem,
                             f"Problem string incorrect for {num1} {operator} {num2}")

            # Test answer calculation
            self.assertEqual(answer, expected_answer,
                             f"Wrong answer for {num1} {operator} {num2}")


if __name__ == '__main__':
    unittest.main()
