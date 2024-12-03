#!/usr/bin/env python3
"""
2024-12-02
https://adventofcode.com/2024/day/2
"""

import os
import logging

logging.basicConfig(level=logging.DEBUG)


def derive(signal):
    """
    Derive the finite difference of the signal
    """
    return [b - a for a, b in zip(signal[:-1], signal[1:])]


def is_monotonic(signal):
    """
    Check if the signal is monotonic
    """
    return all(a < b for a, b in zip(signal[:-1], signal[1:])) or all(
        a > b for a, b in zip(signal[:-1], signal[1:])
    )


def rectify(signal):
    """
    Return the absolute value of the value
    """
    return list(map(abs, signal))


def peak(signal):
    """
    Return the maximum value in the signal
    """
    return max(signal)


def is_safe(signal):
    """
    Check if the signal is safe
    """
    return is_monotonic(signal) and peak(rectify(derive(signal))) <= 3


def main(levels):
    """
    Main function
    """

    result = 0
    for signal in levels:
        if is_safe(signal):
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
