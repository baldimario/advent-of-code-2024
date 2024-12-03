#!/usr/bin/env python3
"""
2024-12-03
https://adventofcode.com/2024/day/3
"""

import os
import logging
import re
from advent_of_code_2024.day_03.main_01 import get_result

logging.basicConfig(level=logging.DEBUG)


def get_enabled_pairs(data):
    """
    Preprocess the data
    """

    result = []
    items = re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))", data)
    enabled = True
    for item in items:
        if item[0] == "do()":
            enabled = True

        if item[0] == "don't()":
            enabled = False

        if item[0].startswith("mul") and enabled:
            result.append((item[1], item[2]))

    return result


def main(data):
    """
    Main function
    """

    result = get_result(get_enabled_pairs(data))

    logging.info("The result is: %s", result)

    logging.info("Done.")
    return result


if __name__ == "__main__":
    inputs = []

    input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")

    with open(input_file, encoding="utf-8") as file:
        inputs = file.read()

    main(inputs)
