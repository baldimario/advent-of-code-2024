#!/usr/bin/env python3
"""
2024-12-01
https://adventofcode.com/2024/day/1
"""

import os
import logging

logging.basicConfig(level=logging.DEBUG)


def get_counting_map(list1, list2):
    """
    Get a map where for each element in list1
    counts how many times it appears in list2
    """
    return [{i: list2.count(i)} for i in list1]


def get_similarity_score(counting_map):
    """
    Get the similarity score from a counting map
    multiplying the element by the number of times it appears
    """
    return sum(k * v for i in counting_map for (k, v) in i.items())


def main(data):
    """
    Main function
    """
    list1 = data["list1"]
    list2 = data["list2"]

    logging.info("Getting counting map...")

    counting_map = get_counting_map(list1, list2)

    logging.info("Getting similarity score...")

    result = get_similarity_score(counting_map)

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
