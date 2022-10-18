from string import ascii_lowercase
from random import randrange

from PySide6.QtWidgets import QMainWindow

from src.main_window import UiMainWindow


class PasswordGenerator(QMainWindow):
    def __init__(self, parent=None):
        super(PasswordGenerator, self).__init__(parent)
        self.ui = UiMainWindow(self)
        self.password_length = 0

        self.ui.use_lowercase_letters.clicked.connect(self.change_value)
        self.ui.generate_password_button.clicked.connect(self.generate_password)
        self.ui.password_length.valueChanged[int].connect(self.change_password_length)

        # if self.ui.use_lowercase_letters.isChecked():
        #     print("password is strong")
        # else:
        #     print("not")

    def change_value(self):
        # button_style = self.ui.use_lowercase_letters.styleSheet()
        # print(button_style, button_style[0])
        if not self.ui.use_lowercase_letters.isChecked():
            self.ui.use_lowercase_letters.setStyleSheet("background-color: black")
        else:
            self.ui.use_lowercase_letters.setStyleSheet("background-color: green")
        # print("Some value")

    def generate_password(self):
        password = ""
        print(f"Debug password length: {self.password_length}")
        print(f"Debug checked a-z status: {self.ui.use_lowercase_letters.isChecked()}")
        for i in range(self.password_length):
            if self.ui.use_lowercase_letters.isChecked():
                password += ascii_lowercase[randrange(len(ascii_lowercase))]

        self.ui.show_password_field.setText(password)
        # print("Button clicked")

    def change_password_length(self, value):
        self.password_length = value
        self.ui.password_length_view.setText(str(value))
        # print(f"Change value {value}")

