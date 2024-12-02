#!/usr/bin/env python3
"""
Test module for the day_02 module
"""
from advent_of_code_2024.day_02.main_01 import (
    derive,
    rectify,
    peak,
    is_safe,
    is_monotonic,
)


class TestDay02:  # pylint: disable=too-few-public-methods
    """
    Test class for the day_02 module
    """

    def test_derive(self):
        """
        Test the derive function
        """
        assert derive([1, 2, 3, 4]) == [1, 1, 1]
        assert derive([1, 3, 6, 10]) == [2, 3, 4]
        assert derive([1, 4, 9, 16]) == [3, 5, 7]

    def test_rectify(self):
        """
        Test the rectify function
        """
        assert rectify([1, 1, 1]) == [1, 1, 1]
        assert rectify([-2, 3, -4]) == [2, 3, 4]
        assert rectify([3, 5, 7]) == [3, 5, 7]

    def test_peak(self):
        """
        Test the peak function
        """
        assert peak([1, 1, 1]) == 1
        assert peak([2, 3, 4]) == 4
        assert peak([3, 5, 7]) == 7

    def test_is_safe(self):
        """
        Test the is_safe function
        """
        assert not is_safe([1, 1, 1])
        assert not is_safe([2, 3, 10])
        assert is_safe([3, 5, 7])
        assert not is_safe([3, 5, -7])

    def test_is_monotonic(self):
        """
        Test the is_monotonic function
        """
        assert not is_monotonic([1, 1, 1])
        assert not is_monotonic([2, 1, 1])
        assert is_monotonic([3, 5, 7])
        assert is_monotonic([7, 5, 3])
        assert not is_monotonic([3, 5, -7])
