"""Dependency Injection module."""

from behave import (  # pylint: disable=no-name-in-module
    given,  # pyright: ignore
    then,  # pyright: ignore
)
from advent_of_code_2024.day_02.main_01 import is_safe
from advent_of_code_2024.day_02.main_02 import is_safe_with_tolerance


@given('the signal "{list_name}"')
def given_a_list(context, list_name):
    """
    Initialize a list for the given context.
    """
    if not hasattr(context, "lists"):
        context.lists = {}

    context.lists[list_name] = []

    if context.table:
        for row in context.table.rows:
            context.lists[list_name].append(int(row["value"]))


@then('the signal "{list_name}" should be safe')
def then_list_should_be_safe(context, list_name):
    """
    Asserts that a signal is safe.
    """
    assert is_safe(context.lists[list_name])


@then('the signal "{list_name}" should not be safe')
def then_list_should_not_be_safe(context, list_name):
    """
    Asserts that a signal is not safe.
    """
    assert not is_safe(context.lists[list_name])


@given("these signals")
def given_these_signals(context):
    """
    Initialize a list for the given context.
    """
    context.lists = []

    for row in context.table.rows:
        context.lists.append([int(value) for value in row["values"].split()])


@then("the signals safety should be")
def then_signals_safety_should_be(context):
    """
    Asserts the safety of the signals.
    """
    for index, row in enumerate(context.table.rows):
        assert is_safe(context.lists[index]) == (row["safe"] == "yes")


@then("the number of safe signals should be {count:d}")
def then_number_of_safe_signals_should_be(context, count):
    """
    Asserts the number of safe signals.
    """
    assert sum(1 if is_safe(signal) else 0 for signal in context.lists) == count

@then("the signals safety with tolerance should be")
def then_signals_safety_with_tolerance_should_be(context):
    """
    Asserts the safety of the signals with tolerance.
    """
    for index, row in enumerate(context.table.rows):
        assert is_safe_with_tolerance(context.lists[index]) == (row["safe"] == "yes")

@then("the number of safe signals with tolerance should be {count:d}")
def then_number_of_safe_signals_with_tolerance_should_be(context, count):
    """
    Asserts the number of safe signals with tolerance.
    """
    assert sum(1 if is_safe_with_tolerance(signal) else 0 for signal in context.lists) == count

