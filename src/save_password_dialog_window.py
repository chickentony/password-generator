from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QWidget, QLineEdit


class SavePasswordDialogWindow(QDialog):
    def __init__(self, main_frame: QWidget, password_value: str):
        super().__init__(parent=main_frame)
        self.password = password_value

        self.setWindowTitle("Save password")
        buttons = QDialogButtonBox.Save | QDialogButtonBox.Cancel

        self.button_box = QDialogButtonBox(buttons)
        self.button_box.accepted.connect(self.save_password)
        self.button_box.rejected.connect(self.reject)
        self.button_box.setStyleSheet(
            """
            border: 1px solid rgb(255, 255, 255);
            border-radius: 10px;
            padding: 2px;
            """
        )

        self.layout = QVBoxLayout()
        self.password_label = QLineEdit()
        self.password_label.setStyleSheet(
            """
            border: 1px solid rgb(255, 255, 255);
            border-radius: 10px;
            color: rgb(255, 255, 255);
            font-size: 16px;
            """
        )

        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.button_box)
        self.setStyleSheet(
            """
            color: rgb(255, 255, 255);
            font-size: 20px;
            """
        )
        self.setLayout(self.layout)

    def save_password(self):
        password_label_text = self.password_label.text()
        # ToDo: решить вопрос с блокированием кнопки если поле с названием пароля пустое?

        with open("password.txt", "a") as file:
            file.write(f"{password_label_text} - {self.password}\n")

        self.close()
