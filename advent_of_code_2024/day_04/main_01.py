#!/usr/bin/env python3
"""
2024-12-03
https://adventofcode.com/2024/day/3
"""

import os
import logging

logging.basicConfig(level=logging.DEBUG)


def get_rows(data):
    """Returns the input data as is."""
    return data


def get_columns(data):
    """Returns the columns of the input data as rows."""
    return list(map(list, zip(*(data))))


def get_diagonals(data, reverse=False):
    """
    Returns the diagonals of the input data.

    Args:
        data (list): The input data.
        reverse (bool): Whether to reverse the data before getting diagonals. Defaults to False.
    """
    diagonals = []
    data = [list(reversed(row)) for row in data] if reverse else data
    for k in range(len(data[0]) + len(data) - 1):
        diagonal = []
        for i, row in enumerate(data):
            if 0 <= i - (k - len(data[0]) + 1) < len(data):
                diagonal.append(row[i - (k - len(data[0]) + 1)])
        diagonals.append(diagonal)
    return diagonals


def printm(matrix):
    """Prints the input matrix."""
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print("")


def count_word(data, word):
    """
    Counts the occurrences of a word in the input data.

    Args:
        data (list): The input data.
        word (str): The word to count.

    Returns:
        int: The number of occurrences of the word.
    """
    reversed_word = word[::-1]
    counter = 0
    for row in data:
        phrase = "".join(row)
        counter += phrase.count(word)
        counter += phrase.count(reversed_word)
    return counter


def word_search(data, word):
    """Word search counting words for all directions"""
    unfolded = [
        get_rows(data),
        get_columns(data),
        get_diagonals(data),
        get_diagonals(data, True),
    ]

    result = 0
    for unwrapped_data in unfolded:
        result += count_word(unwrapped_data, word)

    return result


def main(data):
    """
    Main function
    """

    result = word_search(data, "XMAS")

    logging.info("The result is: %s", result)

    logging.info("Done.")
    return result


if __name__ == "__main__":
    inputs = []

    input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")

    with open(input_file, encoding="utf-8") as file:
        for line in file:
            inputs.append(list(line.rstrip()))

    main(inputs)
