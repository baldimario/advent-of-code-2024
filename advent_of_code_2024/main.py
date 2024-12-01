#!/usr/bin/env python3
import questionary
import os

def main():
    questions = [
        {
            'type': 'select',
            'name':  'day',
            'message': 'Select a day',
            'choices': [questionary.Choice(f'{i:0>2}', checked=False) for i in range(1, 32)]
        },
        {
            'type': 'select',
            'name': 'exercise',
            'message': 'Select the exercise',
            'choices': [questionary.Choice(f'{i:0>2}', checked=False) for i in range(1, 3)]
        }
    ]

    answers = questionary.prompt(questions)
    cmd = f'poetry run python -m advent_of_code_2024.{answers["day"]}.{answers["exercise"]}'
    os.system(cmd)


if __name__ == "__main__":
    main()

