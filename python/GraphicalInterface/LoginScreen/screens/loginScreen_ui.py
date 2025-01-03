# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginScreen.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.resize(800, 600)
        LoginDialog.setStyleSheet(u"background-color: rgb(51, 83, 57);\n"
"border: none;")
        self.centralwidget = QWidget(LoginDialog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 210, 171, 41))
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid rgb(255, 255, 255);")
        self.lineEdit_3 = QLineEdit(self.frame_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(90, 290, 171, 41))
        self.lineEdit_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-bottom: 2px solid rgb(255, 255, 255);")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 100, 171, 51))
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 360, 121, 31))
        self.pushButton.setStyleSheet(u"border-radius: 4px;\n"
"background-color: rgb(219, 255, 245);")

        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        LoginDialog.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginDialog)

        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QCoreApplication.translate("LoginDialog", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("LoginDialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">LOGIN</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("LoginDialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">SOME IMAGE EXAMPLE</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"Email", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("LoginDialog", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("LoginDialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">SOME IMAGE PERSON ICON</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("LoginDialog", u"Confirm", None))
    # retranslateUi

