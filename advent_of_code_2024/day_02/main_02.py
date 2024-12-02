#!/usr/bin/env python3
"""
2024-12-01
https://adventofcode.com/2024/day/1
"""

import os
import logging
from advent_of_code_2024.day_02.main_01 import is_safe

logging.basicConfig(level=logging.DEBUG)

def is_safe_with_tolerance(signal):
    """
    Check if the signal is safe
    """
    if is_safe(signal):
        return True

    for i in range(len(signal)):
        if is_safe(signal[:i] + signal[i + 1:]):
            return True

    return False

def main(levels):
    """
    Main function
    """

    result = 0
    for signal in levels:
        if is_safe_with_tolerance(signal):
            result += 1

    logging.info("The result is %s", result)

    logging.info("Done.")
    return result


if __name__ == "__main__":
    inputs = []

    input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")

    with open(input_file, encoding="utf-8") as file:
        for line in file:
            values = [int(value) for value in line.split()]
            inputs.append(values)

    main(inputs)
