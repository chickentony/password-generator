import pytest

from src.password_complexity import CheckPasswordComplexity


def test_init_check_password_complexity_object_with_invalid_arg_type_should_create_new_object():
    password = "12-Jhd"
    expected_result = CheckPasswordComplexity(password)

    result = CheckPasswordComplexity(password)

    assert result == expected_result, (
        f"Result object: {result} doesn't equals expected object: {expected_result}"
    )


def test_init_check_password_complexity_object_with_zero_password_length_should_raise_exception():
    empty_string = ""

    with pytest.raises(ValueError):
        CheckPasswordComplexity(empty_string)


@pytest.mark.parametrize(
    "password",
    [
        pytest.param(12345, id="int"),
        pytest.param(12345.0, id="float"),
        pytest.param([], id="list"),
        pytest.param({}, id="dict"),
        pytest.param((), id="tuple"),
        pytest.param(True, id="bool"),
        pytest.param(None, id="none"),
    ]
)
def test_init_check_password_complexity_object_with_invalid_arg_type_should_raise_exception(
        password
):
    with pytest.raises(ValueError):
        CheckPasswordComplexity(password)


def test_method_set_password_complexity_should_set_password_complexity_property():
    check_password_object = CheckPasswordComplexity("12-Jhd")
    check_password_object.set_password_complexity("normal", True)
    expected_result = "normal"

    result = check_password_object.get_password_complexity()

    assert result == expected_result


@pytest.mark.parametrize(
    "complexity_value_name",
    [
        pytest.param("weak", id="weak value"),
        pytest.param("normal", id="normal value"),
        pytest.param("strength", id="strength value"),
    ]
)
def test_method_set_password_complexity_should_set_password_complexity_with_all_allowed_values_property(
        complexity_value_name
):
    check_password_object = CheckPasswordComplexity("12-Jhd")
    check_password_object.set_password_complexity(complexity_value_name, True)

    result = check_password_object.get_password_complexity()

    assert result == complexity_value_name


@pytest.mark.parametrize(
    "password_complexity_value_name",
    [
        pytest.param(12345, id="int"),
        pytest.param(12345.0, id="float"),
        pytest.param([], id="list"),
        pytest.param({}, id="dict"),
        pytest.param((), id="tuple"),
        pytest.param(True, id="bool"),
        pytest.param(None, id="none"),
    ]
)
def test_method_set_password_complexity_should_raise_exception_with_invalid_first_argument_type(
        password_complexity_value_name
):
    check_password_object = CheckPasswordComplexity("12-Jhd")

    with pytest.raises(ValueError):
        check_password_object.set_password_complexity(password_complexity_value_name, True)


@pytest.mark.parametrize(
    "yes_or_no",
    [
        pytest.param(12345, id="int"),
        pytest.param(12345.0, id="float"),
        pytest.param("12345.0", id="str"),
        pytest.param([], id="list"),
        pytest.param({}, id="dict"),
        pytest.param((), id="tuple"),
        pytest.param(None, id="none"),
    ]
)
def test_method_set_password_complexity_should_raise_exception_with_invalid_second_argument_type(
        yes_or_no
):
    check_password_object = CheckPasswordComplexity("12-Jhd")

    with pytest.raises(ValueError):
        check_password_object.set_password_complexity("normal", yes_or_no)


def test_method_set_password_complexity_should_raise_exception_with_invalid_first_argument_value():
    check_password_object = CheckPasswordComplexity("12-Jhd")
    invalid_value = "some_value"

    with pytest.raises(KeyError):
        check_password_object.set_password_complexity(invalid_value, True)
