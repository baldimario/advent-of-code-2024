#!/usr/bin/env python3
"""
Test module for the day_06 module
"""
from advent_of_code_2024.day_06.main_01 import (
    get_numeric_map_and_player_position,
    evolve,
    count_positions,
)

from advent_of_code_2024.day_06.main_02 import get_loops


class TestDay06:  # pylint: disable=too-few-public-methods
    """
    Test class for the day_06 module
    """

    def test_get_numeric_map_and_player_position(self):
        """Test get_numeric_map_and_player_position"""
        data = [[".", "#", "."], [".", "^", "."], [".", "#", "."]]
        symbol_map = {"#": -1, ".": 0}
        player_symbol = "^"
        expected_numeric_map = [[0, -1, 0], [0, 0, 0], [0, -1, 0]]
        expected_player_position = [1, 1]
        numeric_map, player_position = get_numeric_map_and_player_position(
            data, symbol_map, player_symbol
        )
        assert numeric_map == expected_numeric_map
        assert player_position == expected_player_position

    def test_evolve(self):
        """Test evolve"""
        numeric_map = [[0, -1, 0], [0, 0, 0], [0, -1, 0]]
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # y, x
        player_position = [1, 1]
        player_turns = 0
        expected_numeric_map = [[0, -1, 0], [0, 1, 1], [0, -1, 0]]
        numeric_map = evolve(numeric_map, directions, player_position, player_turns)
        assert numeric_map == expected_numeric_map

    def test_count_positions(self):
        """Test count_positions"""
        numeric_map = [[1, -1, 0], [0, 1, 0], [0, -1, 0]]
        expected_count = 2
        count = count_positions(numeric_map)
        assert count == expected_count

    def test_get_loops(self):
        """Test get_loops"""
        numeric_map = [
            [0, -1, 0, 0],
            [0, 0, 0, 0],
            [-1, 0, 0, 0],
            [0, 0, -1, 0],
        ]
        player_position = [1, 1]
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # y, x
        player_turns = 0
        expected_loops = 1
        loops = get_loops(numeric_map, player_position, directions, player_turns)
        assert loops == expected_loops
