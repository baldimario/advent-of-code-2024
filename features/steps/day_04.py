"""Steps for the 4th day of Advent of Code 2024."""

from behave import (  # pylint: disable=no-name-in-module
    given,  # pyright: ignore
    then,  # pyright: ignore
)
from advent_of_code_2024.day_04.main_01 import word_search


@given("the puzzle")
def given_a_puzzle(context):
    """
    Initialize a puzzle
    """
    data = []
    for row in context.table.rows:
        data.append(row[0].rstrip().split(" "))
    context.puzzle = data


@then('the word count for the word "{word}" is "{amount}"')
def then_word_count_is(context, word, amount):
    """
    Word couunt
    """
    assert word_search(context.puzzle, word) == int(amount)
