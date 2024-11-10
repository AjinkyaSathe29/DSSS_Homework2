import unittest
from math_quiz import generate_random_integer, generate_random_operator, construct_math_problem


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min = 1
        max = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min, max)
            self.assertTrue(min <= rand_num <= max)

    def generate_random_operator(self):
        # Test that the operator returned is always +, - or *
        for _ in range(1000): 
             operator = generate_random_operator()
             self.assertIn(operator, ['+', '-', '*'])

    def construct_math_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 9, '*', '8 * 9', 72),
                (7, 1, '-', '7 - 1', 6)

            ]

            for n1, n2, operator, expected_problem, expected_answer in test_cases:
                problem, correct_answer = construct_math_problem(n1, n2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(correct_answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
