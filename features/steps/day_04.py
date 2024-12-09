"""Steps for the 4th day of Advent of Code 2024."""

from behave import (  # pylint: disable=no-name-in-module
    given,  # pyright: ignore
    then,  # pyright: ignore
)
from advent_of_code_2024.day_04.main_01 import word_search
from advent_of_code_2024.day_04.main_02 import word_search_x


@given("the puzzle")
def given_a_puzzle(context):
    """
    Initialize a puzzle
    """
    data = []
    for row in context.table.rows:
        data.append(row[0].rstrip().split(" "))
    context.puzzle = data


@given("the filter")
def given_a_filter(context):
    """
    Initialize a puzzle
    """
    data = []
    for row in context.table.rows:
        data.append([c if c != "-" else None for c in row[0].rstrip().split(" ")])
    context.filter = data


@then('the word count for the word "{word}" is "{amount}"')
def then_word_count_is(context, word, amount):
    """
    Word couunt
    """
    assert word_search(context.puzzle, word) == int(amount)


@then('the word count x for the filter is "{amount}"')
def then_word_x_count_is(context, amount):
    """
    Word couunt
    """
    assert word_search_x(context.puzzle, context.filter) == int(amount)
