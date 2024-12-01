"""Dependency Injection module."""

from behave import (  # pylint: disable=no-name-in-module
    given,  # pyright: ignore
    when,  # pyright: ignore
    then,  # pyright: ignore
)
from advent_of_code_2024.day_01.main_01 import compare_lists, sort_list, sum_list
from advent_of_code_2024.day_01.main_02 import get_counting_map, get_similarity_score


@given('I have a list "{list_name}"')
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


@given('I have two list "{list1}" and "{list2}"')
def given_two_lists(context, list1, list2):
    """
    Initialize two list for the given context.
    """
    if not hasattr(context, "lists"):
        context.lists = {}

    context.lists[list1] = []
    context.lists[list2] = []

    if context.table:
        for row in context.table.rows:
            context.lists[list1].append(int(row["value1"]))
            context.lists[list2].append(int(row["value2"]))


@when('computing the list "{comp_list}" comparing "{list1}" and "{list2}"')
def when_comparing_list(context, comp_list, list1, list2):
    """
    Sets the value of a key in a dictionary.
    """
    context.lists[comp_list] = compare_lists(context.lists[list1], context.lists[list2])


@when('sorting the list "{list_name}"')
def when_sorting_list(context, list_name):
    """
    Sets the value of a key in a dictionary.
    """
    context.lists[list_name] = sort_list(context.lists[list_name])


@then('the list "{list_name}" should be')
def then_list_should_be(context, list_name):
    """
    Asserts that a key is not in a dictionary.
    comparing element by element in the same order.
    """
    expected = [int(row["value"]) for row in context.table.rows]
    print(expected, context.lists[list_name])
    assert context.lists[list_name] == expected


@then('the sum of the list "{list_name}" should be "{value}"')
def then_list_sum_should_be(context, list_name, value):
    """
    Asserts that a key is in a dictionary.
    """
    assert sum_list(context.lists[list_name]) == int(value)


@when('computing the counting map "{count_map}" from the list "{list1}" and "{list2}"')
def when_computing_counting_map(context, count_map, list1, list2):
    """
    Sets the value of a key in a dictionary.
    """
    if not hasattr(context, "dictionaries"):
        context.dictionaries = {}

    context.dictionaries[count_map] = get_counting_map(
        context.lists[list1], context.lists[list2]
    )


@then('the counting map "{count_map}" should be')
def then_counting_map_should_be(context, count_map):
    """
    Asserts that a key is not in a dictionary.
    comparing element by element in the same order.
    """
    expected = [{int(row[0]): int(row[1])} for row in context.table.rows]
    assert context.dictionaries[count_map] == expected


@then(
    'the similarity score computed on the counting map "{count_map}" should be "{value}"'
)
def then_similarity_score_should_be(context, count_map, value):
    """
    Asserts that a key is in a dictionary.
    """
    assert get_similarity_score(context.dictionaries[count_map]) == int(value)
