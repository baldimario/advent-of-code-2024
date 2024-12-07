#!/usr/bin/env python3
"""
2024-12-07
https://adventofcode.com/2024/day/7
"""

import os
import logging
import itertools
from functools import cache

logging.basicConfig(level=logging.DEBUG)


@cache
def get_operations(length, operations):
    """Get operations permutations"""
    return list(itertools.product(operations, repeat=length))


def build_expressions(operands, operations):
    """Build all expressions"""
    operations = get_operations(len(operands) - 1, operations)

    expressions = []
    for ops in operations:
        expression = []
        for i, op in enumerate(ops):
            expression.append(operands[i])
            expression.append(op)
        expression.append(operands[-1])
        expressions.append(expression)

    return expressions


def evaluate_expression(expression):
    """Evaluate single expression"""
    result = expression[0]
    for i in range(1, len(expression), 2):
        op = expression[i]
        num = expression[i + 1]
        if op == "+":
            result += num
        elif op == "*":
            result *= num
        elif op == "||":
            result = int(str(result) + str(num))
    return result


def test_equation(equation, operations):
    """Test single equations"""
    test, operands = equation[0], equation[1]
    expressions = build_expressions(tuple(operands), tuple(operations))

    result = 0
    for expression in expressions:
        if evaluate_expression(tuple(expression)) == int(test):  #!eva
            result += 1

    return int(test) if result > 0 else 0


def main(data):
    """
    Main function
    """

    operations = ["*", "+"]
    result = 0
    for equation in data:
        result += test_equation(equation, operations)

    logging.info("The result is: %s", result)

    logging.info("Done.")
    return result


if __name__ == "__main__":
    inputs = []

    input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")

    with open(input_file, encoding="utf-8") as file:
        for line in file:
            value, values = line.rstrip().split(": ")
            inputs.append([int(value), [int(v) for v in values.split(" ")]])

    main(inputs)
