from random import randrange

from PySide6.QtWidgets import QPushButton


def get_random_symbol(symbols: str) -> str:
    return symbols[randrange(len(symbols))]


def get_random_number_str(start=0, end=10) -> str:
    return str(randrange(start, end))


def check_button_is_clicked(button: QPushButton) -> bool:
    return button.isChecked()
