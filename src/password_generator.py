from string import ascii_lowercase, ascii_uppercase, punctuation

from PySide6.QtWidgets import QMainWindow

from src.main_window import UiMainWindow
from src.helpers import get_random_symbol, get_random_number


class PasswordGenerator(QMainWindow):
    def __init__(self, parent=None):
        super(PasswordGenerator, self).__init__(parent)
        self.ui = UiMainWindow(self)
        self.password_length = 0

        self.ui.use_lowercase_letters.clicked.connect(self.change_style_on_button_push)
        self.ui.use_uppercase_letters.clicked.connect(self.change_style_on_button_push)
        self.ui.use_special_chars.clicked.connect(self.change_style_on_button_push)
        self.ui.use_numbers.clicked.connect(self.change_style_on_button_push)
        self.ui.generate_password_button.clicked.connect(self.generate_password)
        self.ui.password_length.valueChanged[int].connect(self.change_password_length)

    def change_style_on_button_push(self):
        if self.ui.use_lowercase_letters.isChecked():
            self.ui.use_lowercase_letters.setStyleSheet(
                "background-color: rgb(66, 245, 84);"
                "border: 1px solid rgb(255, 255, 255);"
                "border-radius: 10px;"
            )
        else:
            self.ui.use_lowercase_letters.setStyleSheet(
                "border: 1px solid rgb(255, 255, 255);"
                "border-radius: 10px;"
                "color: rgb(255, 255, 255);"
            )

        if self.ui.use_uppercase_letters.isChecked():
            self.ui.use_uppercase_letters.setStyleSheet(
                "background-color: rgb(66, 245, 84);"
                "border: 1px solid rgb(255, 255, 255);"
                "border-radius: 10px;"
            )
        else:
            self.ui.use_uppercase_letters.setStyleSheet(
                "border: 1px solid rgb(255, 255, 255);"
                "border-radius: 10px;"
                "color: rgb(255, 255, 255);"
            )

        if self.ui.use_special_chars.isChecked():
            self.ui.use_special_chars.setStyleSheet(
                "background-color: rgb(66, 245, 84);"
                "border: 1px solid rgb(255, 255, 255);"
                "border-radius: 10px;"
            )
        else:
            self.ui.use_special_chars.setStyleSheet(
                "border: 1px solid rgb(255, 255, 255);"
                "border-radius: 10px;"
                "color: rgb(255, 255, 255);"
            )

        if self.ui.use_numbers.isChecked():
            self.ui.use_numbers.setStyleSheet(
                "background-color: rgb(66, 245, 84);"
                "border: 1px solid rgb(255, 255, 255);"
                "border-radius: 10px;"
            )
        else:
            self.ui.use_numbers.setStyleSheet(
                "border: 1px solid rgb(255, 255, 255);"
                "border-radius: 10px;"
                "color: rgb(255, 255, 255);"
            )

    def generate_password(self):
        password = ""
        print(f"Debug password length: {self.password_length}")
        print(f"Debug checked a-z status: {self.ui.use_lowercase_letters.isChecked()}")
        print(f"Debug checked special chars status: {self.ui.use_special_chars.isChecked()}")
        for i in range(self.password_length):
            if self.ui.use_lowercase_letters.isChecked():
                password += get_random_symbol(ascii_lowercase)
            if self.ui.use_uppercase_letters.isChecked():
                password += get_random_symbol(ascii_uppercase)
            if self.ui.use_special_chars.isChecked():
                print(f"Debug get punctuation: {get_random_symbol(punctuation)}")
                password += get_random_symbol(punctuation)
            if self.ui.use_numbers.isChecked():
                password += str(get_random_number())

        self.ui.show_password_field.setText(password)

    def change_password_length(self, value):
        self.password_length = value
        self.ui.password_length_view.setText(str(value))
