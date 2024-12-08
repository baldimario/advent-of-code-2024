#!/usr/bin/env python3
"""
2024-12-07
https://adventofcode.com/2024/day/7
"""

import os
import logging
import itertools
from functools import cache

logging.basicConfig(level=logging.DEBUG)


@cache
def get_permutations(items):
    """Get operations permutations"""
    return list(itertools.product(items, repeat=2))


def printm(matrix):
    """Prints the input matrix."""
    for row in matrix:
        for element in row:
            print(element, end="")
        print("")


def get_antennas(data):
    """Get antennas types"""
    antennas = {}
    for j, row in enumerate(data):
        for i, element in enumerate(row):
            if element == ".":
                continue

            if element not in antennas:
                antennas[element] = []

            antennas[element].append([j, i])
    return antennas


def get_mutual_positions(positions):
    """Get pairs of mutual positions"""
    pairs_ids = get_permutations(tuple(range(len(positions))))
    pairs = [[positions[pair_id[0]], positions[pair_id[1]]] for pair_id in pairs_ids]
    return pairs


def get_antinode(a, b):
    """get position of antinode c from a and b"""
    delta = [b[0] - a[0], b[1] - a[1]]
    return [b[0] + delta[0], b[1] + delta[1]]


def compute_antinodes(data):
    """Update map setting antinodes"""
    height = len(data)
    width = len(data[0])
    for _, positions in get_antennas(data).items():
        for pair in get_mutual_positions(positions):
            a, b = pair[0], pair[1]

            if a == b:
                continue

            c = get_antinode(a, b)

            if c[0] < 0 or c[0] >= height or c[1] < 0 or c[1] >= width:
                continue

            data[c[0]][c[1]] = "#"
    return data


def count_antinodes(data):
    """count antinodes in map"""
    result = 0
    for row in data:
        for element in row:
            if element == "#":
                result += 1
    return result


def main(data):
    """
    Main function
    """

    printm(data)
    print(get_antennas(data))

    data = compute_antinodes(data)

    result = count_antinodes(data)

    printm(data)
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
