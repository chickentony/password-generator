from unittest.mock import patch

import pytest

from src.helpers import get_random_symbol, get_random_number_str


@patch("src.helpers.randrange")
def test_func_get_random_symbol_should_return_random_symbol(mock_helpers_randrange):
    symbols = "some string"
    mock_helpers_randrange.return_value = 2
    expected_result = "m"

    result = get_random_symbol(symbols)

    assert result == expected_result, (
        f"Expected result: {expected_result} does not match actual: {result}"
    )


@pytest.mark.parametrize(
    'symbols',
    [
        pytest.param(123, id='int'),
        pytest.param(123.0, id='float'),
        pytest.param([], id='list'),
        pytest.param({}, id='dict'),
        pytest.param((), id='tuple'),
        pytest.param(None, id='none'),
        pytest.param(True, id='bool'),
    ]
)
def test_func_get_random_symbol_should_raise_exception_with_invalid_argument_type(symbols):
    with pytest.raises(ValueError):
        get_random_symbol(symbols)


def test_func_get_random_symbol_should_raise_exception_with_empty_string_argument():
    with pytest.raises(ValueError):
        get_random_symbol("")


@patch("src.helpers.randrange")
def test_func_get_random_number_str_should_return_random_number(mock_helpers_randrange):
    mock_helpers_randrange.return_value = 5
    expected_result = "5"
    start = 0
    end = 10

    result = get_random_number_str(start, end)

    assert result == expected_result, (
        f"Expected result: {expected_result} does not match actual: {result}"
    )
