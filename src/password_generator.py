from PySide6.QtWidgets import QMainWindow

from src.main_window import UiMainWindow


class PasswordGenerator(QMainWindow):
    def __init__(self, parent=None):
        super(PasswordGenerator, self).__init__(parent)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)
        self.ui.pushButton_3.clicked.connect(self.change_value)
        self.ui.pushButton.clicked.connect(self.generate_password)
        if self.ui.pushButton_3.isChecked():
            print("password is strong")
        else:
            print("not")

    def change_value(self):
        button_style = self.ui.pushButton_3.styleSheet()
        # print(button_style, button_style[0])
        self.ui.pushButton_3.setStyleSheet("background-color: green")
        # print("Some value")

    def generate_password(self):
        self.ui.textBrowser.setText("New password")
        print("Button clicked")
