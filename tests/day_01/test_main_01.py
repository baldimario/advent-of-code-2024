#!/usr/bin/env python3
"""
Test module for the main module
"""


class TestMain:  # pylint: disable=too-few-public-methods
    """
    Test class for the main module
    """

    def test_true(self):
        """
        Test dummy
        """
        assert (1 in [1, 2, 3]) == (1 not in [2, 3, 4])
