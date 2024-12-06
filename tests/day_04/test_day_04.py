#!/usr/bin/env python3
"""
Test module for the day_04 module
"""
from advent_of_code_2024.day_04.main_01 import (
    get_rows,
    get_columns,
    get_diagonals,
    count_word,
    word_search,
)

data = [
    ["M", "M", "M", "S", "X", "X", "M", "A", "S", "M"],
    ["M", "S", "A", "M", "X", "M", "S", "M", "S", "A"],
    ["A", "M", "X", "S", "X", "M", "A", "A", "M", "M"],
    ["M", "S", "A", "M", "A", "S", "M", "S", "M", "X"],
    ["X", "M", "A", "S", "A", "M", "X", "A", "M", "M"],
    ["X", "X", "A", "M", "M", "X", "X", "A", "M", "A"],
    ["S", "M", "S", "M", "S", "A", "S", "X", "S", "S"],
    ["S", "A", "X", "A", "M", "A", "S", "A", "A", "A"],
    ["M", "A", "M", "M", "M", "X", "M", "M", "M", "M"],
    ["M", "X", "M", "X", "A", "X", "M", "A", "S", "X"],
]


class TestDay04:  # pylint: disable=too-few-public-methods
    """
    Test class for the day_04 module
    """

    def test_get_rows(self):
        """Test get_rows"""
        expected = data
        assert get_rows(data) == expected

    def test_get_columns(self):
        """Test get_columns"""
        expected = list(map(list, zip(*data)))
        assert get_columns(data) == expected

    def test_get_diagonals(self):
        """Test get_diagonals"""
        diagonals = get_diagonals(data)
        assert len(diagonals) == len(data[0]) + len(data) - 1

    def test_count_word(self):
        """Test count_word"""
        assert count_word(get_rows(data), "XMAS") == 5
        assert count_word(get_columns(data), "XMAS") == 3
        assert count_word(get_diagonals(data), "XMAS") == 5
        assert count_word(get_diagonals(data, True), "XMAS") == 5

    def test_word_search(self):
        """Test word search"""
        assert word_search(data, "XMAS") == 18
