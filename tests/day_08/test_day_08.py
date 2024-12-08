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
    compute_antinodes,
)
from advent_of_code_2024.day_08.main_02 import (
    get_antinode2,
    get_single_frequency_antennas,
    update_map,
    count_antinodes2,
)


class TestDay08:  # pylint: disable=too-few-public-methods
    """
    Test class for the day_08 module
    """

    def test_get_antennas(self):
        """Test get_antennas function"""
        data = [[".", "A", "."], [".", "A", "."], [".", ".", "."]]
        expected_result = {"A": [[0, 1], [1, 1]]}
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
            [[1, 0], [1, 0]],
        ]
        assert get_mutual_positions(positions) == expected_result

    def test_get_permutations(self):
        """Test get_permutations function"""
        items = ("A", "B")
        expected_result = [("A", "A"), ("A", "B"), ("B", "A"), ("B", "B")]
        assert get_permutations(items) == expected_result

    def test_get_antinode(self):
        """Test get_antinode function"""
        a = [0, 0]
        b = [1, 1]
        expected_result = [2, 2]
        assert get_antinode(a, b) == expected_result

    def test_count_antinodes(self):
        """Test count_antinodes function"""
        data = [[".", "#", "."], [".", "#", "."], [".", ".", "."]]
        expected_result = 2
        assert count_antinodes(data) == expected_result

    def test_compute_antinodes(self):
        """Test compute_antinodes function"""
        data = [[".", "A", "."], [".", "A", "."], [".", ".", "."]]
        expected_result = [[".", "A", "."], [".", "A", "."], [".", "#", "."]]
        assert compute_antinodes(data) == expected_result

    def test_get_antinode2(self):
        """Test get_antinode2 function"""
        a = [0, 0]
        b = [1, 1]
        expected_result = [-1, -1]
        assert get_antinode2(a, b) == expected_result

        a = [1, 1]
        b = [0, 0]
        expected_result = [2, 2]
        assert get_antinode2(a, b) == expected_result

    def test_get_single_frequency_antennas(self):
        """Test get_single_frequency_antennas function"""
        data = [[".", "A", "."], [".", "A", "."], [".", ".", "."]]
        expected_result = []
        assert get_single_frequency_antennas(data) == expected_result

    def test_update_map(self):
        """Test update_map function"""
        data = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        a = [0, 0]
        b = [1, 1]
        expected_result = [["#", ".", "."], [".", "#", "."], [".", ".", "#"]]
        assert update_map(data, a, b) == expected_result

    def test_count_antinodes2(self):
        """Test count_antinodes2 function"""
        data = [[".", "#", "."], [".", "#", "."], [".", ".", "."]]
        expected_result = 2
        assert count_antinodes2(data) == expected_result
