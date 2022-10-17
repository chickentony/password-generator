import sys

from PySide6.QtWidgets import QApplication

from src.password_generator import PasswordGenerator


if __name__ == '__main__':
    app = QApplication()
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())
