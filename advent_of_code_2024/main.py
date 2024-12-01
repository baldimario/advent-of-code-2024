#!/usr/bin/env python3
"""
Main module to run the Advent of Code 2024
"""
import os
import questionary


def main():
    """
    Main function to run the Advent of Code 2024
    """
    questions = [
        {
            "type": "select",
            "name": "day",
            "message": "Select a day",
            "choices": [
                questionary.Choice(f"{i:0>2}", checked=False) for i in range(1, 32)
            ],
        },
        {
            "type": "select",
            "name": "exercise",
            "message": "Select the exercise",
            "choices": [
                questionary.Choice(f"{i:0>2}", checked=False) for i in range(1, 3)
            ],
        },
    ]

    answers = questionary.prompt(questions)
    cmd = (
        "poetry run python -m advent_of_code_2024."
        f'day_{answers["day"]}.main_{answers["exercise"]}'
    )
    os.system(cmd)


if __name__ == "__main__":
    main()
