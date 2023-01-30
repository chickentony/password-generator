from unittest.mock import patch

import pytest

from src.helpers import get_random_symbol, get_random_number_str, check_button_is_clicked


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

    result = get_random_number_str()

    assert result == expected_result, (
        f"Expected result: {expected_result} does not match actual: {result}"
    )


def test_func_get_random_number_str_should_return_random_number_of_str_type():
    result = get_random_number_str()

    assert type(result) is str, f"Result type is {type(result)}, must be string type"


@pytest.mark.parametrize(
    'start, end',
    [
        pytest.param("0", "10", id='str'),
        pytest.param(1.1, 10.0, id='float'),
        pytest.param([1], [10], id='list'),
        pytest.param({"1": 1}, {"10": 10}, id='dict'),
        pytest.param((1,), (2,), id='tuple'),
        pytest.param(None, None, id='none'),
        pytest.param(True, False, id='bool'),
    ]
)
def test_func_get_random_number_str_should_raise_exception_with_invalid_arguments_type(start, end):
    with pytest.raises(ValueError):
        get_random_number_str(start, end)


@pytest.mark.parametrize(
    "start, end",
    [
        pytest.param(10, 10, id="equal"),
        pytest.param(11, 10, id="start more than end"),
        pytest.param(1, -10, id="end less than end"),
    ]
)
def test_func_get_random_number_str_should_raise_exception_with_start_argument_more_than_end_argument(
        start, end
):
    with pytest.raises(ValueError):
        get_random_number_str(start, end)


@pytest.mark.parametrize(
    "button",
    [
        pytest.param(123, id='int'),
        pytest.param("123", id='str'),
        pytest.param(123.0, id='float'),
        pytest.param([], id='list'),
        pytest.param({}, id='dict'),
        pytest.param((), id='tuple'),
        pytest.param(None, id='none'),
        pytest.param(True, id='bool'),
    ]
)
def test_func_check_button_is_clicked_should_raise_exception_with_invalid_argument_type(button):
    with pytest.raises(ValueError):
        check_button_is_clicked(button)
