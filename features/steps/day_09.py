"""Steps for the 9th day of Advent of Code 2024."""

from behave import (  # pylint: disable=no-name-in-module
    given,  # pyright: ignore
    then,  # pyright: ignore
)
from advent_of_code_2024.day_09.main_01 import main as main1


@given('the compressed memory "{memory}"')
def given_compressed_memory(context, memory):
    """
    Initialize data
    """
    context.data = memory


@then('the checksum is "{checksum}"')
def then_checksum_is(context, checksum):
    """
    Result
    """
    result = main1(context.data)
    assert result == int(checksum)
