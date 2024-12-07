#!/usr/bin/env python3
"""
2024-12-05
https://adventofcode.com/2024/day/5
"""

import os
import logging
import math

logging.basicConfig(level=logging.DEBUG)


def get_pairs(updates):
    """Get rule pairs from updates"""
    pairs = []
    for update in updates:
        list_pair = []
        for j in range(len(update) - 1):
            list_pair.append([update[j], update[j + 1]])
        pairs.append(list_pair)
    return pairs


def get_good_updates(pairs, rules, updates):
    """Get good updates"""
    good_updates = []
    for j, pair_list in enumerate(pairs):
        is_valid = True
        for pair in pair_list:
            if pair not in rules:
                is_valid = False
        if is_valid:
            good_updates.append(updates[j])
    return good_updates


def get_middle_sum(good_updates):
    """Sum middle page numbers"""
    result = 0
    for update in good_updates:
        result += update[math.floor(len(update) / 2)]
    return result


def main(rules, updates):
    """
    Main function
    """

    pairs = get_pairs(updates)
    good_updates = get_good_updates(pairs, rules, updates)
    result = get_middle_sum(good_updates)

    logging.info("The result is: %s", result)

    logging.info("Done.")
    return result


if __name__ == "__main__":
    input_rules = []
    input_updates = []

    input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")

    empty_line_found = False  # pylint: disable=invalid-name
    with open(input_file, encoding="utf-8") as file:
        for i, line in enumerate(file):
            if not line.rstrip():
                empty_line_found = True  # pylint: disable=invalid-name
                continue

            if not empty_line_found:
                input_rules.append([int(c) for c in line.rstrip().split("|")])
            else:
                input_updates.append([int(c) for c in line.rstrip().split(",")])

    main(input_rules, input_updates)
