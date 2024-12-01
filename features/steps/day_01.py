"""Dependency Injection module."""

from behave import (  # pylint: disable=no-name-in-module
    given,  # pyright: ignore
    when,  # pyright: ignore
    then,  # pyright: ignore
)


@given('I have a dictionary "{dictionary}"')
def given_a_have_a_dictionary(context, dictionary):
    """
    Initialize a dictionary for the given context.
    """
    if not hasattr(context, "dictionaries"):
        context.dictionaries = {}

    context.dictionaries[dictionary] = {}


@when('the dictionary "{dictionary}" has the "{key}" key with the value "{value}"')
def when_dictionary_has_key(context, dictionary, key, value):
    """
    Sets the value of a key in a dictionary.
    """
    context.dictionaries[dictionary][key] = value


@then('the dictionary "{dictionary}" should not have the "{key}" key inside')
def then_container_should_have_not_service(context, dictionary, key):
    """
    Asserts that a key is not in a dictionary.
    """
    assert key not in context.dictionaries[dictionary]


@then(
    'the dictionary "{dictionary}" should have the "{key}" key inside with the value "{value}"'
)
def then_container_should_have_service(context, dictionary, key, value):
    """
    Asserts that a key is in a dictionary.
    """
    assert context.dictionaries[dictionary][key] == value
