"""Steps for the 4th day of Advent of Code 2024."""

from behave import (  # pylint: disable=no-name-in-module
    given,  # pyright: ignore
    then,  # pyright: ignore
)
from advent_of_code_2024.day_05.main_01 import (
    get_pairs,
    get_good_updates,
    get_middle_sum,
)
from advent_of_code_2024.day_05.main_02 import (
    get_bad_updates,
    fix_bad_updates,
)


@given("the rules")
def given_rules(context):
    """
    Initialize a table
    """
    data = []
    for row in context.table.rows:
        data.append([int(c) for c in row[0].rstrip().split(" ")])
    context.rules = data


@given("the updates")
def given_updates(context):
    """
    Initialize a table
    """
    data = []
    for row in context.table.rows:
        data.append([int(c) for c in row[0].rstrip().split(" ")])
    context.updates = data


@then('the middle good pages sum is "{amount}"')
def then_good_sum_is(context, amount):
    """
    Result
    """
    pairs = get_pairs(context.updates)
    good_updates = get_good_updates(pairs, context.rules, context.updates)
    result = get_middle_sum(good_updates)
    assert result == int(amount)


@then('the middle bad pages sum is "{amount}"')
def then_bad_sum_is(context, amount):
    """
    Result
    """
    pairs = get_pairs(context.updates)
    bad_updates = get_bad_updates(pairs, context.rules, context.updates)
    fixed_updates = fix_bad_updates(bad_updates, context.rules)
    result = get_middle_sum(fixed_updates)
    assert result == int(amount)
