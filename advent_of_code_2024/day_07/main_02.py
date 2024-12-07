#!/usr/bin/env python3
"""
2024-12-07
https://adventofcode.com/2024/day/7
"""

import os
import logging
from advent_of_code_2024.day_07.main_01 import (
    test_equation,
)

logging.basicConfig(level=logging.DEBUG)


def main(data):
    """
    Main function
    """

    operations = ["*", "+", "||"]
    result = 0
    for i, equation in enumerate(data):
        print(i)
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
