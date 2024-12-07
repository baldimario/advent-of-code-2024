#!/usr/bin/env python3
"""
2024-12-04
https://adventofcode.com/2024/day/4
"""

import os
import logging

logging.basicConfig(level=logging.DEBUG)


def convolve(data, myfilter):
    """
    Convolve filter over data
    filter is 2d matirx
    data is 2d matrix
    filter can have null value
    all valuies are chars
    rules:
        char * char = 1 if same else 0
        char * null = 0
    """
    result = 0
    filter_height = len(myfilter)
    filter_width = len(myfilter[0])
    data_height = len(data)
    data_width = len(data[0])
    non_null_values_in_filter = sum(
        1 for row in myfilter for value in row if value is not None
    )

    for i in range(data_height - filter_height + 1):
        for j in range(data_width - filter_width + 1):
            convolution_sum = 0
            for k in range(filter_height):
                for z in range(filter_width):
                    if myfilter[k][z] is not None:
                        convolution_sum += (
                            1 if data[i + k][j + z] == myfilter[k][z] else 0
                        )
            result += 1 if convolution_sum == non_null_values_in_filter else 0
    return result


def transpose(matrix):
    """rotate matrix"""
    return [list(reversed(i)) for i in zip(*matrix)]


def word_search_x(data, myfilter):
    """Word search X"""
    result = 0
    for _ in range(4):
        myfilter = transpose(myfilter)

        result += convolve(data, myfilter)

    return result


def main(data):
    """
    Main function
    """
    myfilter = [["M", None, "S"], [None, "A", None], ["M", None, "S"]]

    result = word_search_x(data, myfilter)

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
