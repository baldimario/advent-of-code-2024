#!/usr/bin/env python3
"""
2024-12-01
https://adventofcode.com/2024/day/1
"""

import os
import logging

logging.basicConfig(level=logging.DEBUG)


def main(data):
    """
    Main function
    """

    print(data)
    result = 0

    logging.info("Done.")
    return result


if __name__ == "__main__":
    inputs = []

    input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")

    with open(input_file, encoding="utf-8") as file:
        inputs = file.readlines()

    main(inputs)
