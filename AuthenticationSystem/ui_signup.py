# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SignupDialog(object):
    def setupUi(self, SignupDialog):
        if not SignupDialog.objectName():
            SignupDialog.setObjectName(u"SignupDialog")
        SignupDialog.resize(308, 345)
        SignupDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(SignupDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.signup_label = QLabel(SignupDialog)
        self.signup_label.setObjectName(u"signup_label")
        font = QFont()
        font.setPointSize(12)
        self.signup_label.setFont(font)
        self.signup_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.signup_label)

        self.username_label = QLabel(SignupDialog)
        self.username_label.setObjectName(u"username_label")

        self.verticalLayout.addWidget(self.username_label)

        self.username_input = QLineEdit(SignupDialog)
        self.username_input.setObjectName(u"username_input")

        self.verticalLayout.addWidget(self.username_input)

        self.password_label = QLabel(SignupDialog)
        self.password_label.setObjectName(u"password_label")

        self.verticalLayout.addWidget(self.password_label)

        self.password_input = QLineEdit(SignupDialog)
        self.password_input.setObjectName(u"password_input")

        self.verticalLayout.addWidget(self.password_input)

        self.confirmpass_label = QLabel(SignupDialog)
        self.confirmpass_label.setObjectName(u"confirmpass_label")

        self.verticalLayout.addWidget(self.confirmpass_label)

        self.confirmpass_input = QLineEdit(SignupDialog)
        self.confirmpass_input.setObjectName(u"confirmpass_input")

        self.verticalLayout.addWidget(self.confirmpass_input)

        self.validation_label = QLabel(SignupDialog)
        self.validation_label.setObjectName(u"validation_label")
        self.validation_label.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.validation_label)

        self.signup_button = QPushButton(SignupDialog)
        self.signup_button.setObjectName(u"signup_button")
        self.signup_button.setStyleSheet(u" padding: 8px 16px;  /* Padding inside the button */\n"
"    color: white;  /* Font color */\n"
"    background-color: rgb(0, 123, 255);  /* Bootstrap blue */\n"
"    border-radius: 5px;  /* Optional: rounded corners */\n"
"    border: 1px solid rgb(0, 102, 204);  /* Darker border color */")
        self.signup_button.setAutoDefault(True)

        self.verticalLayout.addWidget(self.signup_button)


        self.retranslateUi(SignupDialog)

        self.signup_button.setDefault(True)


        QMetaObject.connectSlotsByName(SignupDialog)
    # setupUi

    def retranslateUi(self, SignupDialog):
        SignupDialog.setWindowTitle(QCoreApplication.translate("SignupDialog", u"Signup", None))
        self.signup_label.setText(QCoreApplication.translate("SignupDialog", u"Signup", None))
        self.username_label.setText(QCoreApplication.translate("SignupDialog", u"Username: ", None))
        self.password_label.setText(QCoreApplication.translate("SignupDialog", u"Password:", None))
        self.confirmpass_label.setText(QCoreApplication.translate("SignupDialog", u"Confirm Password:", None))
        self.validation_label.setText("")
        self.signup_button.setText(QCoreApplication.translate("SignupDialog", u"Signup", None))
    # retranslateUi

