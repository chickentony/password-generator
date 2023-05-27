import logging
from random import randrange

from PySide6.QtWidgets import QPushButton

from src.constants import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


def get_random_symbol(symbols: str) -> str:
    """
    Return random char from given string.

    :param symbols: not empty char sequence
    :return: random char
    """

    if not isinstance(symbols, str):
        logger.critical("Invalid argument type %s provided", type(symbols))
        raise ValueError("Argument must be string type")
    if len(symbols) <= 0:
        logger.critical("Argument len must be bigger than provided: %s", len(symbols))
        raise ValueError("String length must be bigger then 0")

    return symbols[randrange(len(symbols))]


def get_random_number_str(start=0, end=10) -> str:
    """
    Return random number in string format from provided or default range.

    :param start: from where range started
    :param end: where range ended
    :return: number in "123" format
    """

    if not all(isinstance(value, int) for value in (start, end)):
        logger.critical(
            "One of argument type ins invalid. Start argument type: %s end argument type: %s",
            type(start),
            type(end)
        )
        raise ValueError("All arguments must be int type")
    if start >= end:
        logger.critical("Start argument %s is bigger than end argument %s", start, end)
        raise ValueError("Start must be less than end")

    return str(randrange(start, end))


def check_button_is_clicked(button: QPushButton) -> bool:
    """
    Return true or false depending on the button state.

    :param button: button component
    :return: True or False
    """

    if not isinstance(button, QPushButton):
        logger.critical("Invalid argument type %s provided", type(button))
        raise ValueError("Argument must be type of QPushButton")

    return button.isChecked()
