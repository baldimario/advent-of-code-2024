#!/usr/bin/env python3
"""
2024-12-06
https://adventofcode.com/2024/day/6
"""

import os
import logging

logging.basicConfig(level=logging.DEBUG)


def printm(matrix):
    """Prints the input matrix."""
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print("")


def get_numeric_map_and_player_position(data, symbol_map, player_symbol):
    """Get numeric map and player position"""
    player_position = None
    numeric_map = []
    for j, row in enumerate(data):
        new_row = []
        for i, element in enumerate(row):
            new_row.append(symbol_map[element] if element in symbol_map else 0)
            if element == player_symbol:
                player_position = [j, i]
        numeric_map.append(new_row)
    return numeric_map, player_position


def evolve(numeric_map, directions, player_position, player_turns):
    """Evolve the algo"""
    map_height = len(numeric_map)
    map_width = len(numeric_map[0])

    exited = False
    while not exited:
        player_direction = directions[player_turns % len(directions)]

        new_position = [
            player_position[0] + player_direction[0],
            player_position[1] + player_direction[1],
        ]

        if (
            new_position[0] < 0
            or new_position[0] >= map_height
            or new_position[1] < 0
            or new_position[1] >= map_width
        ):
            exited = True
            numeric_map[player_position[0]][player_position[1]] += 1
            continue

        next_cell = numeric_map[new_position[0]][new_position[1]]

        if next_cell >= 0:
            numeric_map[player_position[0]][player_position[1]] += 1
            player_position = new_position
            continue

        player_turns += 1
        continue
    return numeric_map


def count_positions(numeric_map):
    """Count result"""
    result = 0
    for row in numeric_map:
        for element in row:
            result += 1 if element > 0 else 0
    return result


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

    result = count_positions(numeric_map)

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
