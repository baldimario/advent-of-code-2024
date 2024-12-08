"""Steps for the 4th day of Advent of Code 2024."""

from behave import (  # pylint: disable=no-name-in-module
    given,  # pyright: ignore
    then,  # pyright: ignore
)
from advent_of_code_2024.day_08.main_01 import main as main1


@given("the antenna map")
def given_antenna_map(context):
    """
    Initialize data
    """
    context.data = []
    for row in context.table.rows:
        context.data.append(list(row[0].rstrip()))


@then('the number of antinodes is "{amount}"')
def then_sum_right_equations_1(context, amount):
    """
    Result
    """
    result = main1(context.data)
    assert result == int(amount)
