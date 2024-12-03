#!/usr/bin/env python3
"""
Test module for the day_03 module
"""
from advent_of_code_2024.day_03.main_01 import get_pairs, get_result
from advent_of_code_2024.day_03.main_02 import get_enabled_pairs


class TestDay03:  # pylint: disable=too-few-public-methods
    """
    Test class for the day_03 module
    """

    def test_get_pairs(self):
        """
        Test the get_pairs function
        """
        data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        result = get_pairs(data)

        assert result == [("2", "4"), ("5", "5"), ("11", "8"), ("8", "5")]

    def test_get_result(self):
        """
        Test the get_result function
        """
        pairs = [("2", "4"), ("5", "5"), ("11", "8"), ("8", "5")]
        result = get_result(pairs)

        assert result == 161

    def test_get_enabled_pairs(self):
        """
        Test the get_enabled_pairs function
        """
        data = (
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        )
        result = get_enabled_pairs(data)

        assert result == [("2", "4"), ("8", "5")]
