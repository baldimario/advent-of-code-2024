"""Steps for the third day of Advent of Code 2024."""

from behave import (  # pylint: disable=no-name-in-module
    given,  # pyright: ignore
    then,  # pyright: ignore
)
from advent_of_code_2024.day_03.main_01 import get_pairs, get_result
from advent_of_code_2024.day_03.main_02 import get_enabled_pairs


@given('the memory "{memory}" initialized with value "{value}"')
def given_a_list(context, memory, value):
    """
    Initialize a list for the given context.
    """
    if not hasattr(context, "memories"):
        context.memories = {}

    context.memories[memory] = value


@then('the extracted pairs from memory "{memory}" are')
def then_memory_pairs_are(context, memory):
    """
    Initialize a list for the given context.
    """
    context.lists = []

    pairs = get_pairs(context.memories[memory])

    for i, row in enumerate(context.table.rows):
        pair = pairs[i]
        expected = tuple(row[0].split())
        assert pair == expected


@then('the extracted enabled pairs from memory "{memory}" are')
def then_memory_enabled_pairs_are(context, memory):
    """
    Initialize a list for the given context.
    """
    context.lists = []

    pairs = get_enabled_pairs(context.memories[memory])

    for i, row in enumerate(context.table.rows):
        pair = pairs[i]
        expected = tuple(row[0].split())
        assert pair == expected


@then('the result of the pairs from memory "{memory}" is "{result}"')
def then_memory_result_is(context, memory, result):
    """
    Initialize a list for the given context.
    """
    pairs = get_pairs(context.memories[memory])
    computed = get_result(pairs)

    assert int(result) == computed


@then('the result of the enabled pairs from memory "{memory}" is "{result}"')
def then_memory_enabled_result_is(context, memory, result):
    """
    Initialize a list for the given context.
    """
    pairs = get_enabled_pairs(context.memories[memory])
    computed = get_result(pairs)

    assert int(result) == computed
