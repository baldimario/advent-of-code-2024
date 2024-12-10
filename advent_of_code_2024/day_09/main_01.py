#!/usr/bin/env python3
"""
2024-12-09
https://adventofcode.com/2024/day/9
"""

import os
import logging

logging.basicConfig(level=logging.DEBUG)


def get_memory_blocks(compressed_memory):
    """Get memory block from the compressed representation"""
    memory_blocks = []
    value_count = 0
    for count, block in enumerate(compressed_memory):
        for _ in range(int(block)):
            item = {
                "position": count,
                "original": block,
                "value": str(value_count),
                "free": count % 2 != 0,
            }
            memory_blocks.append(item)
        if count % 2 == 0:
            value_count += 1
    return memory_blocks


def fragment_memory_blocks(memory_blocks):
    """Fragment memory"""
    right = len(memory_blocks) - 1
    left = 0
    while True:
        while not memory_blocks[left]["free"]:
            left += 1

        while memory_blocks[right]["free"]:
            right -= 1

        if right - left == -1:
            break

        memory_blocks[right], memory_blocks[left] = (
            memory_blocks[left],
            memory_blocks[right],
        )
    return memory_blocks


def get_checksum(expanded_memory):
    """Compute memory checksum"""
    checksum = 0
    for count, cell in enumerate(expanded_memory):
        if not cell["free"]:
            checksum += int(cell["value"]) * count
    return checksum


def main(compressed_memory):
    """
    Main function
    """

    memory_blocks = get_memory_blocks(compressed_memory)
    memory_blocks = fragment_memory_blocks(memory_blocks)
    result = get_checksum(memory_blocks)

    logging.info("The result is: %s", result)

    logging.info("Done.")
    return result


if __name__ == "__main__":
    input_data = []

    input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")

    with open(input_file, encoding="utf-8") as file:
        input_data = file.read()

    main(input_data)
