#!/usr/bin/env python3
"""
2024-12-03
https://adventofcode.com/2024/day/3
"""

import os
import logging
import re

logging.basicConfig(level=logging.DEBUG)


def get_pairs(data):
    """
    Get all pairs of numbers
    """

    return re.findall(r"mul\((\d+),(\d+)\)", data)


def get_result(pairs):
    """
    Get the result
    """

    result = 0
    for numbers in pairs:
        result += int(numbers[0]) * int(numbers[1])

    return result


def main(data):
    """
    Main function
    """

    result = get_result(get_pairs(data))

    logging.info("The result is: %s", result)

    logging.info("Done.")
    return result


if __name__ == "__main__":
    inputs = []

    input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")

    with open(input_file, encoding="utf-8") as file:
        inputs = file.read()

    main(inputs)
