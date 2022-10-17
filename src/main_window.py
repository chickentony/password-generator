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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QStatusBar, QTextBrowser, QWidget, QLabel)


class UiMainWindow(object):
    def setup_ui(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.resize(635, 371)
        main_window.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QLabel(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 100, 391, 50))
        self.textBrowser.setStyleSheet(
            u"border: 1px solid rgb(255, 255, 255);\n"
            "border-radius: 10px;\n"
            "color: rgb(255, 255, 255)"
        )
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(420, 100, 61, 51))
        self.pushButton.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(490, 100, 61, 51))
        self.pushButton_2.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 280, 91, 51))
        self.pushButton_3.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(30, 220, 351, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(400, 220, 41, 31))
        self.textBrowser_2.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(120, 280, 91, 51))
        self.pushButton_7.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(230, 280, 91, 51))
        self.pushButton_8.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(340, 280, 91, 51))
        self.pushButton_9.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"")
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PasswordGenerator", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate password", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Copy password", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"a-z", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"A-Z", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"#$*", None))
    # retranslateUi

