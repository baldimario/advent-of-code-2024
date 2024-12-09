#!/usr/bin/env python3
"""
Test module for the day_01 module
"""
from advent_of_code_2024.day_01.main_01 import compare_lists, sort_list, sum_list
from advent_of_code_2024.day_01.main_02 import get_counting_map, get_similarity_score


class TestDay01:  # pylint: disable=too-few-public-methods
    """
    Test class for the day_01 module
    """

    def test_compare_lists(self):
        """
        Test the compare_lists function
        """
        list1 = [1, 2, 3]
        list2 = [1, 1, 1]
        assert compare_lists(list1, list2) == [0, 1, 2]

    def test_sort_list(self):
        """
        Test the sort_list function
        """
        list1 = [3, 2, 1]
        assert sort_list(list1) == [1, 2, 3]

    def test_sum_list(self):
        """
        Test the sum_list function
        """
        list1 = [1, 2, 3]
        assert sum_list(list1) == 6

    def test_get_counting_map(self):
        """
        Test the get_counting_map function
        """
        list1 = [1, 2, 3, 1]
        list2 = [1, 1, 1, 2]
        assert get_counting_map(list1, list2) == [{1: 3}, {2: 1}, {3: 0}, {1: 3}]

    def test_get_similarity_score(self):
        """
        Test the get_similarity_score function
        """
        counting_map = [{1: 3}, {2: 1}, {3: 1}]
        assert get_similarity_score(counting_map) == 8
