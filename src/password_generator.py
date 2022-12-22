from string import ascii_lowercase, ascii_uppercase, punctuation
from typing import List
from random import randrange

from PySide6.QtWidgets import QMainWindow, QApplication

from src.main_window import UiMainWindow
from src.helpers import get_random_symbol, get_random_number_str
from src.password_complexity import CheckPasswordComplexity
from src.save_password_dialog_window import SavePasswordDialogWindow
from src.styles import CLICKED_BUTTON_STYLE, BUTTON_STYLE


class PasswordGenerator(QMainWindow):
    """
    Generate password logic and interaction with buttons copy and save buttons
    """

    def __init__(self, parent=None):
        """
        Set connection to methods that are called on buttons click.

        :param parent:
        """
        super(PasswordGenerator, self).__init__(parent)
        self.main_window = UiMainWindow(self)
        self.password_length = 0

        self.main_window.use_lowercase_letters.clicked.connect(self.change_style_on_button_press)
        self.main_window.use_uppercase_letters.clicked.connect(self.change_style_on_button_press)
        self.main_window.use_special_chars.clicked.connect(self.change_style_on_button_press)
        self.main_window.use_numbers.clicked.connect(self.change_style_on_button_press)
        self.main_window.generate_password_button.clicked.connect(self.generate_password)
        self.main_window.password_length.valueChanged[int].connect(self.change_password_length)
        self.main_window.copy_password_to_clipboard.clicked.connect(self.copy_password_to_clipboard)
        self.main_window.save_password_to_file.clicked.connect(self.save_password_to_file)

    def change_style_on_button_press(self) -> None:
        """
        Change style of buttons when it clicked.

        :return: None
        """
        if self.main_window.use_lowercase_letters.isChecked():
            self.main_window.use_lowercase_letters.setStyleSheet(CLICKED_BUTTON_STYLE)
        else:
            self.main_window.use_lowercase_letters.setStyleSheet(BUTTON_STYLE)

        if self.main_window.use_uppercase_letters.isChecked():
            self.main_window.use_uppercase_letters.setStyleSheet(CLICKED_BUTTON_STYLE)
        else:
            self.main_window.use_uppercase_letters.setStyleSheet(BUTTON_STYLE)

        if self.main_window.use_special_chars.isChecked():
            self.main_window.use_special_chars.setStyleSheet(CLICKED_BUTTON_STYLE)
        else:
            self.main_window.use_special_chars.setStyleSheet(BUTTON_STYLE)

        if self.main_window.use_numbers.isChecked():
            self.main_window.use_numbers.setStyleSheet(CLICKED_BUTTON_STYLE)
        else:
            self.main_window.use_numbers.setStyleSheet(BUTTON_STYLE)

    def generate_password(self) -> None:
        """
        Generate new password with the specified options: length, what symbols to be used.
        Also check complexity of generate password.

        :return: None
        """

        password = ""
        password_complexity_checker = CheckPasswordComplexity()

        print(f"Debug password length: {self.password_length}")
        print(f"Debug checked a-z status: {self.main_window.use_lowercase_letters.isChecked()}")
        print(f"Debug checked special chars status: {self.main_window.use_special_chars.isChecked()}")
        for _ in range(self.password_length):
            list_for_password_generation = self.get_clicked_buttons()
            password += list_for_password_generation[randrange(len(list_for_password_generation))]

        password_complexity = password_complexity_checker.validate_password(password)
        print(f"Debug password complexity {password_complexity}")
        self.main_window.password_complex_value.setText(password_complexity)
        self.main_window.show_password_field.setText(password)
        password_complexity_checker.reset_password_complexity()

    def change_password_length(self, value) -> None:
        """

        :param value:
        :return: None
        """

        self.password_length = value
        self.main_window.password_length_view.setText(str(value))

    def get_clicked_buttons(self) -> List[str]:
        """
        Get symbols depending on what buttons user click

        :return: list of chars
        """

        result = []

        if self.main_window.use_special_chars.isChecked():
            result.append(get_random_symbol(punctuation))
        if self.main_window.use_lowercase_letters.isChecked():
            result.append(get_random_symbol(ascii_lowercase))
        if self.main_window.use_uppercase_letters.isChecked():
            result.append(get_random_symbol(ascii_uppercase))
        if self.main_window.use_numbers.isChecked():
            result.append(get_random_number_str())

        return result

    def save_password_to_file(self) -> None:
        """
        Save current password value to file.

        :return: None
        """

        print("Save password button clocked")
        current_password_value = self.main_window.show_password_field.text()

        dialog = SavePasswordDialogWindow(self.main_window.main_widget, current_password_value)
        dialog.exec()

    def copy_password_to_clipboard(self) -> None:
        """
        Copy current password value to clipboard.

        :return: None
        """

        clipboard = QApplication.clipboard()
        clipboard.clear(mode=clipboard.Clipboard)
        clipboard.setText(self.main_window.show_password_field.text(), mode=clipboard.Clipboard)
