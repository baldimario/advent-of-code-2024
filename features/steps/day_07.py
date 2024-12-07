"""Steps for the 4th day of Advent of Code 2024."""

from behave import (  # pylint: disable=no-name-in-module
    given,  # pyright: ignore
    then,  # pyright: ignore
)
from advent_of_code_2024.day_07.main_01 import main as main1
from advent_of_code_2024.day_07.main_02 import main as main2


@given("the operations list")
def given_data(context):
    """
    Initialize data
    """
    context.data = []
    for row in context.table.rows:
        value, values = row[0].rstrip().split(": ")
        context.data.append(
            [int(value), [int(v) for v in [int(e) for e in values.split(" ")]]]
        )


@then('the sum of right rquations for * and + operands is "{amount}"')
def then_sum_right_equations_1(context, amount):
    """
    Result
    """
    result = main1(context.data)
    assert result == int(amount)


@then('the sum of right rquations for *, + and || operands is "{amount}"')
def then_sum_right_equations_2(context, amount):
    """
    Result
    """
    result = main2(context.data)
    assert result == int(amount)
