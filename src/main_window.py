# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PasswordGeneratorBase.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QTextLine)
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QStatusBar, QTextBrowser, QWidget, QLabel, QCheckBox
)


class UiMainWindow:
    def __init__(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName("main_window")
        main_window.resize(635, 371)
        main_window.setStyleSheet("background-color: rgb(0, 0, 0)")

        self.main_widget = QWidget(main_window)
        self.main_widget.setObjectName("main_widget")

        self.show_password_field = QLabel(self.main_widget)
        self.show_password_field.setObjectName("show_password_field")
        self.show_password_field.setGeometry(QRect(20, 100, 391, 50))
        self.show_password_field.setStyleSheet(
            "border: 1px solid rgb(255, 255, 255);\n"
            "border-radius: 10px;\n"
            "color: rgb(255, 255, 255)"
        )

        self.generate_password_button = QPushButton(self.main_widget)
        self.generate_password_button.setObjectName("generate_password_button")
        self.generate_password_button.setGeometry(QRect(420, 100, 61, 51))
        self.generate_password_button.setStyleSheet(
            "border: 1px solid rgb(255, 255, 255);\n"
            "border-radius: 10px;"
        )

        self.copy_password_to_clipboard = QPushButton(self.main_widget)
        self.copy_password_to_clipboard.setObjectName("copy_password_to_clipboard")
        self.copy_password_to_clipboard.setGeometry(QRect(490, 100, 61, 51))
        self.copy_password_to_clipboard.setStyleSheet(
            "border: 1px solid rgb(255, 255, 255);"
            "border-radius: 10px;"
        )

        self.password_length = QSlider(self.main_widget)
        self.password_length.setObjectName("password_length")
        self.password_length.setMaximum(40)
        self.password_length.setGeometry(QRect(30, 220, 351, 22))
        self.password_length.setOrientation(Qt.Horizontal)
        self.password_length.setStyleSheet(
            """
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 5px;
                background: gray;
                margin: 2px 0;
            }
            
            QSlider::handle:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
                border: 1px solid #5c5c5c;
                border-radius: 10px;
                width: 18px;
                margin: -8px 0; 
                border-radius: 3px;
            }

            QSlider::sub-page:horizontal {
                background: green;
            }
            """
        )

        self.password_length_view = QLabel(self.main_widget)
        self.password_length_view.setObjectName("password_length_view")
        self.password_length_view.setGeometry(QRect(400, 220, 41, 31))
        self.password_length_view.setStyleSheet(
            "border: 1px solid rgb(255, 255, 255);\n"
            "border-radius: 10px;\n"
            "color: rgb(255, 255, 255);"
        )

        self.use_lowercase_letters = QPushButton(self.main_widget)
        self.use_lowercase_letters.setCheckable(True)
        self.use_lowercase_letters.setObjectName("use_lowercase_letters")
        self.use_lowercase_letters.setGeometry(QRect(10, 280, 91, 51))
        self.use_lowercase_letters.setStyleSheet(
            "border: 1px solid rgb(255, 255, 255);"
            "border-radius: 10px;"
            "color: rgb(255, 255, 255);"
        )

        self.use_uppercase_letters = QPushButton(self.main_widget)
        self.use_uppercase_letters.setCheckable(True)
        self.use_uppercase_letters.setObjectName("use_uppercase_letters")
        self.use_uppercase_letters.setGeometry(QRect(120, 280, 91, 51))
        self.use_uppercase_letters.setStyleSheet(
            "border: 1px solid rgb(255, 255, 255);"
            "border-radius: 10px;"
            "color: rgb(255, 255, 255);"
        )

        self.use_numbers = QPushButton(self.main_widget)
        self.use_numbers.setCheckable(True)
        self.use_numbers.setObjectName("use_numbers")
        self.use_numbers.setGeometry(QRect(230, 280, 91, 51))
        self.use_numbers.setStyleSheet(
            "border: 1px solid rgb(255, 255, 255);"
            "border-radius: 10px;"
            "color: rgb(255, 255, 255);"
        )

        self.use_special_chars = QPushButton(self.main_widget)
        self.use_special_chars.setCheckable(True)
        self.use_special_chars.setObjectName("use_special_chars")
        self.use_special_chars.setGeometry(QRect(340, 280, 91, 51))
        self.use_special_chars.setStyleSheet(
            "border: 1px solid rgb(255, 255, 255);"
            "border-radius: 10px;"
            "color: rgb(255, 255, 255);"
        )

        main_window.setCentralWidget(self.main_widget)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslate_ui(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("MainWindow", "PasswordGenerator", None))
        self.generate_password_button.setText(QCoreApplication.translate("MainWindow", "Generate password", None))
        self.copy_password_to_clipboard.setText(QCoreApplication.translate("MainWindow", "Copy password", None))
        self.use_lowercase_letters.setText(QCoreApplication.translate("MainWindow", "a-z", None))
        self.use_uppercase_letters.setText(QCoreApplication.translate("MainWindow", "A-Z", None))
        self.use_numbers.setText(QCoreApplication.translate("MainWindow", "0-9", None))
        self.use_special_chars.setText(QCoreApplication.translate("MainWindow", "#$*", None))
    # retranslateUi

