# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.resize(308, 331)
        LoginDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.login_label = QLabel(LoginDialog)
        self.login_label.setObjectName(u"login_label")
        font = QFont()
        font.setPointSize(12)
        self.login_label.setFont(font)
        self.login_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.login_label)

        self.username_label = QLabel(LoginDialog)
        self.username_label.setObjectName(u"username_label")

        self.verticalLayout.addWidget(self.username_label)

        self.username_input = QLineEdit(LoginDialog)
        self.username_input.setObjectName(u"username_input")

        self.verticalLayout.addWidget(self.username_input)

        self.uservalidation_label = QLabel(LoginDialog)
        self.uservalidation_label.setObjectName(u"uservalidation_label")
        self.uservalidation_label.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.uservalidation_label)

        self.password_label = QLabel(LoginDialog)
        self.password_label.setObjectName(u"password_label")

        self.verticalLayout.addWidget(self.password_label)

        self.password_input = QLineEdit(LoginDialog)
        self.password_input.setObjectName(u"password_input")

        self.verticalLayout.addWidget(self.password_input)

        self.passvalidation_label = QLabel(LoginDialog)
        self.passvalidation_label.setObjectName(u"passvalidation_label")
        self.passvalidation_label.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.passvalidation_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(LoginDialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.createacc_button = QPushButton(LoginDialog)
        self.createacc_button.setObjectName(u"createacc_button")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setUnderline(True)
        self.createacc_button.setFont(font1)
        self.createacc_button.setMouseTracking(False)
        self.createacc_button.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"    background: transparent;\n"
"")
        self.createacc_button.setAutoDefault(False)
        self.createacc_button.setFlat(True)

        self.horizontalLayout.addWidget(self.createacc_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.login_button = QPushButton(LoginDialog)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setStyleSheet(u" padding: 8px 16px;  /* Padding inside the button */\n"
"    color: white;  /* Font color */\n"
"    background-color: rgb(0, 123, 255);  /* Bootstrap blue */\n"
"    border-radius: 5px;  /* Optional: rounded corners */\n"
"    border: 1px solid rgb(0, 102, 204);  /* Darker border color */")
        self.login_button.setAutoDefault(True)

        self.verticalLayout.addWidget(self.login_button)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(LoginDialog)

        self.login_button.setDefault(True)


        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QCoreApplication.translate("LoginDialog", u"Login", None))
        self.login_label.setText(QCoreApplication.translate("LoginDialog", u"Login", None))
        self.username_label.setText(QCoreApplication.translate("LoginDialog", u"Username: ", None))
        self.uservalidation_label.setText("")
        self.password_label.setText(QCoreApplication.translate("LoginDialog", u"Password:", None))
        self.passvalidation_label.setText("")
        self.label_5.setText(QCoreApplication.translate("LoginDialog", u"Don't have an account?", None))
        self.createacc_button.setText(QCoreApplication.translate("LoginDialog", u"Create Account", None))
        self.login_button.setText(QCoreApplication.translate("LoginDialog", u"Login", None))
    # retranslateUi

