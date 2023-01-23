from random import randrange

from PySide6.QtWidgets import QPushButton


def get_random_symbol(symbols: str) -> str:
    """
    Return random char from given string.

    :param symbols: not empty char sequence
    :return: random char
    """
    if not isinstance(symbols, str):
        raise ValueError("Argument must be string type")
    if len(symbols) <= 0:
        raise ValueError("String length must be bigger then 0")

    return symbols[randrange(len(symbols))]


def get_random_number_str(start=0, end=10) -> str:
    """
    Return random number in string format from provided or default range.

    :param start: from where range started
    :param end: where range ended
    :return: number in "123" format
    """

    return str(randrange(start, end))


def check_button_is_clicked(button: QPushButton) -> bool:
    return button.isChecked()
