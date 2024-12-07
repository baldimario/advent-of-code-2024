#!/usr/bin/env python3
"""
Test module for the day_07 module
"""
from advent_of_code_2024.day_07.main_01 import (
    get_operations,
    build_expressions,
    evaluate_expression,
    test_equation as t_equation,
)


class TestDay07:  # pylint: disable=too-few-public-methods
    """
    Test class for the day_07 module
    """

    def test_get_operations(self):
        """Test get_operations"""
        length = 2
        operations = ["+", "*"]
        expected_result = [("+", "+"), ("+", "*"), ("*", "+"), ("*", "*")]
        result = get_operations(length, tuple(operations))
        assert result == expected_result

    def test_build_expressions(self):
        """Test build_expressions"""
        operands = [1, 2, 3]
        operations = ["+", "*"]
        expected_result = [
            [1, "+", 2, "+", 3],
            [1, "+", 2, "*", 3],
            [1, "*", 2, "+", 3],
            [1, "*", 2, "*", 3],
        ]
        result = build_expressions(tuple(operands), tuple(operations))
        assert result == expected_result

    def test_evaluate_expression(self):
        """Test evaluate_expression"""
        expression = [1, "+", 2, "+", 3]
        expected_result = 6
        result = evaluate_expression(expression)
        assert result == expected_result
        expression = [1, "+", 2, "+", 3, "||", 4]
        expected_result = 64
        result = evaluate_expression(expression)
        assert result == expected_result

    def test_test_equation(self):
        """Test test_equation"""
        equation = [6, [1, 2, 3]]
        operations = ["+", "*"]
        expected_result = 6
        result = t_equation(equation, operations)
        assert result == expected_result
