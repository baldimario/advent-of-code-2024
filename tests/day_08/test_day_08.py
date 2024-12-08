#!/usr/bin/env python3
"""
Test module for the day_08 module
"""
from advent_of_code_2024.day_08.main_01 import (
    get_antennas,
    get_mutual_positions,
    get_permutations,
    get_antinode,
    count_antinodes,
    compute_antinodes
)

class TestDay08:  # pylint: disable=too-few-public-methods
    """
    Test class for the day_08 module
    """

    def test_get_antennas(self):
        """Test get_antennas function"""
        data = [
            ['.', 'A', '.'],
            ['.', 'A', '.'],
            ['.', '.', '.']
        ]
        expected_result = {'A': [[0, 1], [1, 1]]}
        assert get_antennas(data) == expected_result

    def test_get_mutual_positions(self):
        """Test get_mutual_positions function"""
        positions = [[0, 0], [0, 1], [1, 0]]
        expected_result = [
            [[0, 0], [0, 0]],
            [[0, 0], [0, 1]],
            [[0, 0], [1, 0]],
            [[0, 1], [0, 0]],
            [[0, 1], [0, 1]],
            [[0, 1], [1, 0]],
            [[1, 0], [0, 0]],
            [[1, 0], [0, 1]],
            [[1, 0], [1, 0]]
        ]
        assert get_mutual_positions(positions) == expected_result

    def test_get_permutations(self):
        """Test get_permutations function"""
        items = ('A', 'B')
        expected_result = [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
        assert get_permutations(items) == expected_result

    def test_get_antinode(self):
        """Test get_antinode function"""
        a = [0, 0]
        b = [1, 1]
        expected_result = [2, 2]
        assert get_antinode(a, b) == expected_result

    def test_count_antinodes(self):
        """Test count_antinodes function"""
        data = [
            ['.', '#', '.'],
            ['.', '#', '.'],
            ['.', '.', '.']
        ]
        expected_result = 2
        assert count_antinodes(data) == expected_result

    def test_compute_antinodes(self):
        """Test compute_antinodes function"""
        data = [
            ['.', 'A', '.'],
            ['.', 'A', '.'],
            ['.', '.', '.']
        ]
        expected_result = [
            ['.', 'A', '.'],
            ['.', 'A', '.'],
            ['.', '#', '.']
        ]
        assert compute_antinodes(data) == expected_result
