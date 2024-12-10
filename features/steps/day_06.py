"""Steps for the 6th day of Advent of Code 2024."""

from behave import (  # pylint: disable=no-name-in-module
    given,  # pyright: ignore
    then,  # pyright: ignore
)
from advent_of_code_2024.day_06.main_01 import main as main1
from advent_of_code_2024.day_06.main_02 import main as main2


@given("the map")
def given_map(context):
    """
    Initialize a table
    """
    data = []
    for row in context.table.rows:
        data.append(list(row[0].rstrip()))
    context.map = data


@then('the position count is "{amount}"')
def then_position_count_is(context, amount):
    """
    Result
    """
    result = main1(context.map)
    assert result == int(amount)


@then('the position that generate loops are "{amount}"')
def then_position_loops_are(context, amount):
    """Result"""
    result = main2(context.map)
    assert result == int(amount)
