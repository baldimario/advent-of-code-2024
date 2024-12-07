#!/usr/bin/env python3
"""
2024-12-06
https://adventofcode.com/2024/day/6
"""

import os
import logging
from advent_of_code_2024.day_06.main_01 import (
    evolve,
    get_numeric_map_and_player_position,
)

logging.basicConfig(level=logging.DEBUG)


def printm(matrix):
    """Prints the input matrix."""
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print("")


def get_loops(numeric_map, player_position, directions, player_turns):
    """Count how many position can generate loops"""
    loops = []
    for j, row in enumerate(numeric_map):
        for i, _ in enumerate(row):
            if player_position == [j, i]:
                continue
            new_map = [[*row] for row in numeric_map]
            new_map[j][i] = -1
            try:
                new_map = evolve(new_map, directions, player_position, player_turns, 10)
            except StopIteration:
                loops.append([j, i])
                continue

    return len(loops)


def main(data):
    """
    Main function
    """

    result = 0

    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # y, x

    player_turns = 0

    symbol_map = {"#": -1, ".": 0}
    player_symbol = "^"

    numeric_map, player_position = get_numeric_map_and_player_position(
        data, symbol_map, player_symbol
    )

    numeric_map = evolve(numeric_map, directions, player_position, player_turns)

    result = get_loops(numeric_map, player_position, directions, player_turns)

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
