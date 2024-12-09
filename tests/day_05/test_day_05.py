#!/usr/bin/env python3
"""
Test module for the day_05 module
"""
from advent_of_code_2024.day_05.main_01 import (
    get_pairs,
    get_good_updates,
    get_middle_sum,
)
from advent_of_code_2024.day_05.main_02 import get_bad_updates, fix_bad_updates


class TestDay05:  # pylint: disable=too-few-public-methods
    """
    Test class for the day_05 module
    """

    def test_get_pairs(self):
        """Get pairs"""
        updates = [
            [1, 2, 3],
            [4, 5, 6],
        ]
        expected_pairs = [
            [[1, 2], [2, 3]],
            [[4, 5], [5, 6]],
        ]
        assert get_pairs(updates) == expected_pairs

    def test_get_good_updates(self):
        """Get good updates"""
        rules = [
            [1, 2],
            [2, 3],
            [4, 5],
            [5, 6],
        ]
        updates = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        pairs = get_pairs(updates)
        expected_good_updates = [
            [1, 2, 3],
            [4, 5, 6],
        ]
        assert get_good_updates(pairs, rules, updates) == expected_good_updates

    def test_get_middle_sum(self):
        """Get middle sum"""
        rules = [
            [1, 2],
            [2, 3],
            [4, 5],
            [5, 6],
        ]
        updates = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        pairs = get_pairs(updates)
        expected_good_updates = [
            [1, 2, 3],
            [4, 5, 6],
        ]
        good_updates = get_good_updates(pairs, rules, updates)
        expected_middle_sum = sum(
            update[len(update) // 2] for update in expected_good_updates
        )
        assert get_middle_sum(good_updates) == expected_middle_sum

    def test_get_bad_updates(self):
        """Get bad updates"""
        rules = [
            [1, 2],
            [2, 3],
            [4, 5],
            [5, 6],
        ]
        updates = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        pairs = get_pairs(updates)
        expected_bad_updates = [
            [7, 8, 9],
        ]
        assert get_bad_updates(pairs, rules, updates) == expected_bad_updates

    def test_fix_bad_updates(self):
        """Fix bad updates"""
        rules = [
            [1, 2],
            [2, 3],
            [3, 4],
            [4, 5],
            [5, 6],
        ]
        bad_updates = [
            [3, 2, 4],
        ]
        expected_fixed_updates = [
            [2, 3, 4],
        ]
        assert fix_bad_updates(bad_updates, rules) == expected_fixed_updates
