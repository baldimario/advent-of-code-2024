#!/usr/bin/env python3
"""
2024-12-01
https://adventofcode.com/2024/day/1
"""

import os
import logging


def compare_lists(list1, list2):
    """
    Compare two lists element by element
    returning a new list with elements
    of list A subtracted by elements of list B
    """
    return [abs(int(i) - int(j)) for i, j in zip(list1, list2)]


def sort_list(list1):
    """
    Sort a list from smallest to largest
    """
    return sorted(list1)


def sum_list(list1):
    """
    Sum a list
    """
    return sum(list1)


def main(data):
    """
    Main function
    """
    list1 = data["list1"]
    list2 = data["list2"]

    logging.info("Sorting lists...")

    list1 = sort_list(list1)
    list2 = sort_list(list2)

    logging.info("Comparing lists...")

    result = compare_lists(list1, list2)

    logging.info("Summing list...")

    result = sum_list(result)

    print(f"The result is: {result}")

    print("Done.")
    return result


if __name__ == "__main__":
    inputs = {
        "list1": [],
        "list2": [],
    }

    input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")

    with open(input_file, encoding="utf-8") as file:
        for line in file:
            value1, value2 = line.split()
            inputs["list1"].append(int(value1))
            inputs["list2"].append(int(value2))

    main(inputs)
