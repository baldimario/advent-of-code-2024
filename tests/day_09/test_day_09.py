#!/usr/bin/env python3
"""
Test module for the day_09 module
"""
from advent_of_code_2024.day_09.main_01 import (
    get_memory_blocks,
    get_checksum,
    fragment_memory_blocks,
)


class TestDay09:  # pylint: disable=too-few-public-methods
    """
    Test class for the day_09 module
    """

    def test_get_memory_blocks(self):
        """get memory blocks"""
        compressed_memory = "12345"
        memory_blocks = get_memory_blocks(compressed_memory)
        assert len(memory_blocks) == 15

    def test_fragment_memory_blocks(self):
        """fragment block memory"""
        compressed_memory = "12345"
        memory_blocks = get_memory_blocks(compressed_memory)
        memory_blocks = fragment_memory_blocks(memory_blocks)
        assert memory_blocks[0]["free"] is False

    def test_get_checksum(self):
        """get checksum"""
        compressed_memory = "12345"
        memory_blocks = get_memory_blocks(compressed_memory)
        memory_blocks = fragment_memory_blocks(memory_blocks)
        checksum = get_checksum(memory_blocks)
        assert checksum == 60
