from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QSlider, QStatusBar, QWidget, QLabel, QMainWindow

from src.styles import (
    PASSWORD_ACTIONS_BUTTON_STYLE, SHOW_PASSWORD_INPUT_STYLE, PASSWORD_COMPLEXITY_TEXT_STYLE,
    OPTIONS_WINDOW_STYLE, MAIN_WINDOW_STYLE, HORIZONTAL_SCROLLBAR_STYLE
)
from src.constants import (
    PASSWORD_LENGTH_MAX_VALUE, PASSWORD_LENGTH_START_VALUE_TEXT, ICON_FILE_NAMES
)


class UiMainWindow:
    """Class with main layer and all widgets."""

    def __init__(self, main_window: QMainWindow):
        """

        :param main_window: main window with all functional
        """
        if not main_window.objectName():
            main_window.setObjectName("main_window")
        main_window.resize(635, 371)
        main_window.setStyleSheet(MAIN_WINDOW_STYLE)
        main_window.setWindowTitle(
            QCoreApplication.translate("MainWindow", "PasswordGenerator", None)
        )

        self.main_widget = QWidget(main_window)
        self.main_widget.setObjectName("main_widget")

        self.show_password_field = QLabel(self.main_widget)
        self.show_password_field_settings()

        self.generate_password_button = QPushButton(self.main_widget)
        self.generate_password_button_settings()

        self.copy_password_to_clipboard = QPushButton(self.main_widget)
        self.copy_password_to_clipboard_settings()

        self.save_password_to_file = QPushButton(self.main_widget)
        self.save_password_to_file_settings()

        self.password_complex_label = QLabel("Strength:", parent=self.main_widget)
        self.password_complex_label.setGeometry(25, 160, 70, 20)
        self.password_complex_label.setStyleSheet(PASSWORD_COMPLEXITY_TEXT_STYLE)

        self.password_complex_value = QLabel(self.main_widget)
        self.password_complex_value.setGeometry(100, 160, 70, 20)
        self.password_complex_value.setStyleSheet(PASSWORD_COMPLEXITY_TEXT_STYLE)

        self.password_length = QSlider(self.main_widget)
        self.password_length_settings()

        self.password_length_view = QLabel(self.main_widget)
        self.password_length_view_settings()

        self.use_lowercase_letters = QPushButton(self.main_widget)
        self.lowercase_letters_option_button_settings()

        self.use_uppercase_letters = QPushButton(self.main_widget)
        self.uppercase_letters_option_button_settings()

        self.use_numbers = QPushButton(self.main_widget)
        self.numbers_option_button_settings()

        self.use_special_chars = QPushButton(self.main_widget)
        self.special_chars_option_button_settings()

        main_window.setCentralWidget(self.main_widget)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        QMetaObject.connectSlotsByName(main_window)

    def special_chars_option_button_settings(self) -> None:
        """
        Settings for option button.

        :return: None
        """
        self.use_special_chars.setCheckable(True)
        self.use_special_chars.setObjectName("use_special_chars")
        self.use_special_chars.setGeometry(QRect(340, 280, 91, 51))
        self.use_special_chars.setStyleSheet(OPTIONS_WINDOW_STYLE)
        self.use_special_chars.setText(QCoreApplication.translate("MainWindow", "#$*", None))

    def numbers_option_button_settings(self) -> None:
        """
        Settings for option button.

        :return: None
        """
        self.use_numbers.setCheckable(True)
        self.use_numbers.setObjectName("use_numbers")
        self.use_numbers.setGeometry(QRect(230, 280, 91, 51))
        self.use_numbers.setStyleSheet(OPTIONS_WINDOW_STYLE)
        self.use_numbers.setText(QCoreApplication.translate("MainWindow", "0-9", None))

    def uppercase_letters_option_button_settings(self) -> None:
        """
        Settings for option button.

        :return: None
        """

        self.use_uppercase_letters.setCheckable(True)
        self.use_uppercase_letters.setObjectName("use_uppercase_letters")
        self.use_uppercase_letters.setGeometry(QRect(120, 280, 91, 51))
        self.use_uppercase_letters.setStyleSheet(OPTIONS_WINDOW_STYLE)
        self.use_uppercase_letters.setText(QCoreApplication.translate("MainWindow", "A-Z", None))

    def lowercase_letters_option_button_settings(self) -> None:
        """
        Settings for option button.

        :return: None
        """

        self.use_lowercase_letters.setCheckable(True)
        self.use_lowercase_letters.setObjectName("use_lowercase_letters")
        self.use_lowercase_letters.setGeometry(QRect(10, 280, 91, 51))
        self.use_lowercase_letters.setStyleSheet(OPTIONS_WINDOW_STYLE)
        self.use_lowercase_letters.setText(QCoreApplication.translate("MainWindow", "a-z", None))

    def show_password_field_settings(self) -> None:
        """
        Settings for main password field.

        :return: None
        """
        self.show_password_field.setObjectName("show_password_field")
        self.show_password_field.setGeometry(QRect(20, 100, 391, 50))
        self.show_password_field.setStyleSheet(SHOW_PASSWORD_INPUT_STYLE)

    def generate_password_button_settings(self) -> None:
        """
        Settings for generate password button.

        :return: None
        """

        self.generate_password_button.setObjectName("generate_password_button")
        self.generate_password_button.setGeometry(QRect(420, 100, 61, 51))
        self.generate_password_button.setIcon(QIcon(ICON_FILE_NAMES["GENERATE_PASSWORD_ICON"]))
        self.generate_password_button.setIconSize(QSize(30, 30))
        self.generate_password_button.setToolTip("Choose options and click")
        self.generate_password_button.setStyleSheet(PASSWORD_ACTIONS_BUTTON_STYLE)

    def copy_password_to_clipboard_settings(self) -> None:
        """
        Settings for copy password button.

        :return: None
        """

        self.copy_password_to_clipboard.setObjectName("copy_password_to_clipboard")
        self.copy_password_to_clipboard.setGeometry(QRect(490, 100, 61, 51))
        self.copy_password_to_clipboard.setIcon(QIcon(ICON_FILE_NAMES["COPY_PASSWORD_ICON"]))
        self.copy_password_to_clipboard.setIconSize(QSize(30, 30))
        self.copy_password_to_clipboard.setStyleSheet(PASSWORD_ACTIONS_BUTTON_STYLE)

    def save_password_to_file_settings(self) -> None:
        """
        Settings for save password button.

        :return: None
        """

        self.save_password_to_file.setGeometry(QRect(560, 100, 61, 51))
        self.save_password_to_file.setIcon(QIcon(ICON_FILE_NAMES["SAVE_PASSWORD_ICON"]))
        self.save_password_to_file.setIconSize(QSize(30, 30))
        self.save_password_to_file.setStyleSheet(PASSWORD_ACTIONS_BUTTON_STYLE)

    def password_length_settings(self) -> None:
        """
        Settings for password length field.

        :return None
        """

        self.password_length.setObjectName("password_length")
        self.password_length.setMaximum(PASSWORD_LENGTH_MAX_VALUE)
        self.password_length.setGeometry(QRect(30, 220, 351, 22))
        self.password_length.setOrientation(Qt.Horizontal)
        self.password_length.setStyleSheet(HORIZONTAL_SCROLLBAR_STYLE)

    def password_length_view_settings(self) -> None:
        """
        Settings for password length view.

        :return: None
        """

        self.password_length_view.setObjectName("password_length_view")
        self.password_length_view.setGeometry(QRect(400, 210, 51, 41))
        self.password_length_view.setAlignment(Qt.AlignCenter)
        self.password_length_view.setText(PASSWORD_LENGTH_START_VALUE_TEXT)
        self.password_length_view.setStyleSheet(OPTIONS_WINDOW_STYLE)
