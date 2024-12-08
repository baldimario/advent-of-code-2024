#!/usr/bin/env python3
"""
2024-12-07
https://adventofcode.com/2024/day/7
"""

import os
import logging

from advent_of_code_2024.day_08.main_01 import (
    get_antennas,
    get_antinode,
    get_mutual_positions,
)

logging.basicConfig(level=logging.DEBUG)


def get_antinode2(a, b):
    """get position of antinode c from a and b"""
    delta = [b[0] - a[0], b[1] - a[1]]
    return [a[0] - delta[0], a[1] - delta[1]]


def update_map(data, a, b, backward=False):
    """propagate delta forward in direction b-a"""
    height = len(data)
    width = len(data[0])

    while True:
        if not backward:
            c = get_antinode(a, b)
        else:
            c = get_antinode2(a, b)

        if c[0] < 0 or c[0] >= height or c[1] < 0 or c[1] >= width:
            break

        data[c[0]][c[1]] = "#"
        data[a[0]][a[1]] = "#"
        data[b[0]][b[1]] = "#"
        a = b
        b = c

    return data


def compute_t_antinodes(data):
    """Update map setting antinodes"""
    for _, positions in get_antennas(data).items():
        if len(positions) <= 1:
            continue

        for pair in get_mutual_positions(positions):
            if pair[0] == pair[1]:
                continue

            data = update_map(data, pair[0], pair[1])
            data = update_map(data, pair[0], pair[1], backward=True)

    return data


def count_antinodes2(data, single_frequency_antennas=None):
    """count antinodes in map"""
    single_frequency_antennas = single_frequency_antennas or []
    result = 0
    for row in data:
        for element in row:
            if element not in ["."] + single_frequency_antennas:
                result += 1
    return result


def get_single_frequency_antennas(data):
    """get antennas that has no pairs"""
    single_frequency_antennas = []
    for antenna, positions in get_antennas(data).items():
        if len(positions) == 1:
            single_frequency_antennas.append(antenna)
    return single_frequency_antennas


def main(data):
    """
    Main function
    """

    single_frequency_antennas = get_single_frequency_antennas(data)

    data = compute_t_antinodes(data)

    result = count_antinodes2(data, single_frequency_antennas)

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
