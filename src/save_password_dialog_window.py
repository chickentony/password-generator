from logging import getLogger

from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QWidget, QLineEdit
from src.styles import (
    SAVE_PASSWORD_DIALOG_WINDOW_BUTTONS_STYLE,
    SAVE_PASSWORD_DIALOG_WINDOW_PASSWORD_LABEL_INPUT_STYLE, SAVE_PASSWORD_DIALOG_WINDOW_COMMON_STYLE
)


class SavePasswordDialogWindow(QDialog):
    """Save password window class."""

    def __init__(self, main_frame: QWidget, password_value: str):
        """
        Generate basic widgets and buttons.

        :param main_frame: layer where window will be placed
        :param password_value: password value from parent layer that will be saved to file
        """

        super().__init__(parent=main_frame)
        self.password = password_value
        self.logger = getLogger("password_generator")

        # Dialog buttons
        self.setWindowTitle("Save password")
        buttons = QDialogButtonBox.Save | QDialogButtonBox.Cancel
        self.button_box = QDialogButtonBox(buttons)
        self.button_box.accepted.connect(self.save_password)
        self.button_box.rejected.connect(self.reject)
        self.button_box.setStyleSheet(SAVE_PASSWORD_DIALOG_WINDOW_BUTTONS_STYLE)

        # Label input widget
        self.layout = QVBoxLayout()
        self.password_label = QLineEdit()
        self.password_label.setStyleSheet(SAVE_PASSWORD_DIALOG_WINDOW_PASSWORD_LABEL_INPUT_STYLE)

        # Adding all widgets to layer
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.button_box)
        self.setStyleSheet(SAVE_PASSWORD_DIALOG_WINDOW_COMMON_STYLE)
        self.setLayout(self.layout)

    def save_password(self) -> None:
        """
        Save password to txt file. If password label doesn't exist,
        save with relevant string "empty password label".

        :return: None
        """

        password_label_text = self.password_label.text()
        if not password_label_text:
            self.logger.warning("Password label to save is empty. Set 'empty password label' text")
            password_label_text = "empty password label"

        with open("password.txt", "a") as file:
            file.write(f"{password_label_text} - {self.password}\n")
        self.logger.debug(
            "Password '%s' with label '%s' will be saved to file",
            self.password,
            password_label_text
        )
        self.logger.info("Password save to file successfully")

        self.close()
