#!/usr/bin/env python3
"""
2024-12-05
https://adventofcode.com/2024/day/5
"""

import os
import logging
from advent_of_code_2024.day_05.main_01 import get_pairs, get_middle_sum

logging.basicConfig(level=logging.DEBUG)


def get_bad_updates(pairs, rules, updates):
    """Get good updates"""
    bad_updates = []
    for j, pair_list in enumerate(pairs):
        is_valid = True
        for pair in pair_list:
            if pair not in rules:
                is_valid = False
        if not is_valid:
            bad_updates.append(updates[j])
    return bad_updates


def fix_bad_updates(bad_updates, rules):
    """fix bad updates"""
    not_fixed = True

    while not_fixed:
        not_fixed = False
        for update in bad_updates:
            for j in range(len(update) - 1):
                pair = [update[j], update[j + 1]]
                if pair not in rules:
                    update[j], update[j + 1] = update[j + 1], update[j]
                    not_fixed = True

    return bad_updates


def main(rules, updates):
    """
    Main function
    """

    pairs = get_pairs(updates)
    bad_updates = get_bad_updates(pairs, rules, updates)
    fixed_updates = fix_bad_updates(bad_updates, rules)
    result = get_middle_sum(fixed_updates)

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
