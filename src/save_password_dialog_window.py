from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class SavePasswordDialogWindow(QDialog):
    def __init__(self, main_frame):
        super().__init__(parent=main_frame)

        self.setWindowTitle("Save password")
        buttons = QDialogButtonBox.Save | QDialogButtonBox.Cancel

        self.button_box = QDialogButtonBox(buttons)
        self.button_box.accepted.connect(self.test_fun)
        self.button_box.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        test_message = QLabel("this is test message")
        self.layout.addWidget(test_message)
        self.layout.addWidget(self.button_box)
        self.setStyleSheet(
            """
            color: rgb(255, 255, 255);
            font-size: 20px;
            """
        )
        self.setLayout(self.layout)

    def test_fun(self):
        print("Click save")
        self.close()
