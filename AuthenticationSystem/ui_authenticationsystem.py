# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authenticationsystem.ui'
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
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_authenticationsystem(object):
    def setupUi(self, authenticationsystem):
        if not authenticationsystem.objectName():
            authenticationsystem.setObjectName(u"authenticationsystem")
        authenticationsystem.resize(313, 331)
        self.verticalLayout_5 = QVBoxLayout(authenticationsystem)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(authenticationsystem)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.verticalLayoutWidget_2 = QWidget(self.login)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 291, 311))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.login_label = QLabel(self.verticalLayoutWidget_2)
        self.login_label.setObjectName(u"login_label")
        font = QFont()
        font.setPointSize(12)
        self.login_label.setFont(font)
        self.login_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.login_label)

        self.username_label = QLabel(self.verticalLayoutWidget_2)
        self.username_label.setObjectName(u"username_label")

        self.verticalLayout_3.addWidget(self.username_label)

        self.username_input = QLineEdit(self.verticalLayoutWidget_2)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.verticalLayout_3.addWidget(self.username_input)

        self.uservalidation_label = QLabel(self.verticalLayoutWidget_2)
        self.uservalidation_label.setObjectName(u"uservalidation_label")
        self.uservalidation_label.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_3.addWidget(self.uservalidation_label)

        self.password_label = QLabel(self.verticalLayoutWidget_2)
        self.password_label.setObjectName(u"password_label")

        self.verticalLayout_3.addWidget(self.password_label)

        self.password_input = QLineEdit(self.verticalLayoutWidget_2)
        self.password_input.setObjectName(u"password_input")

        self.verticalLayout_3.addWidget(self.password_input)

        self.passvalidation_label = QLabel(self.verticalLayoutWidget_2)
        self.passvalidation_label.setObjectName(u"passvalidation_label")
        self.passvalidation_label.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_3.addWidget(self.passvalidation_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.createacc_button = QPushButton(self.verticalLayoutWidget_2)
        self.createacc_button.setObjectName(u"createacc_button")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setUnderline(True)
        self.createacc_button.setFont(font1)
        self.createacc_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.createacc_button.setMouseTracking(False)
        self.createacc_button.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"    background: transparent;\n"
"")
        self.createacc_button.setAutoDefault(False)
        self.createacc_button.setFlat(True)

        self.horizontalLayout_2.addWidget(self.createacc_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.login_button = QPushButton(self.verticalLayoutWidget_2)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setStyleSheet(u" padding: 8px 16px;  /* Padding inside the button */\n"
"    color: white;  /* Font color */\n"
"    background-color: rgb(0, 123, 255);  /* Bootstrap blue */\n"
"    border-radius: 5px;  /* Optional: rounded corners */\n"
"    border: 1px solid rgb(0, 102, 204);  /* Darker border color */")
        self.login_button.setAutoDefault(True)

        self.verticalLayout_3.addWidget(self.login_button)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.login)
        self.signup = QWidget()
        self.signup.setObjectName(u"signup")
        self.verticalLayoutWidget = QWidget(self.signup)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 291, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.signup_label = QLabel(self.verticalLayoutWidget)
        self.signup_label.setObjectName(u"signup_label")
        self.signup_label.setFont(font)
        self.signup_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.signup_label)

        self.username_label_2 = QLabel(self.verticalLayoutWidget)
        self.username_label_2.setObjectName(u"username_label_2")

        self.verticalLayout.addWidget(self.username_label_2)

        self.username_input_2 = QLineEdit(self.verticalLayoutWidget)
        self.username_input_2.setObjectName(u"username_input_2")
        self.username_input_2.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.verticalLayout.addWidget(self.username_input_2)

        self.password_label_2 = QLabel(self.verticalLayoutWidget)
        self.password_label_2.setObjectName(u"password_label_2")

        self.verticalLayout.addWidget(self.password_label_2)

        self.password_input_2 = QLineEdit(self.verticalLayoutWidget)
        self.password_input_2.setObjectName(u"password_input_2")

        self.verticalLayout.addWidget(self.password_input_2)

        self.confirmpass_label = QLabel(self.verticalLayoutWidget)
        self.confirmpass_label.setObjectName(u"confirmpass_label")

        self.verticalLayout.addWidget(self.confirmpass_label)

        self.confirmpass_input = QLineEdit(self.verticalLayoutWidget)
        self.confirmpass_input.setObjectName(u"confirmpass_input")

        self.verticalLayout.addWidget(self.confirmpass_input)

        self.validation_label = QLabel(self.verticalLayoutWidget)
        self.validation_label.setObjectName(u"validation_label")
        self.validation_label.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.validation_label)

        self.signup_button = QPushButton(self.verticalLayoutWidget)
        self.signup_button.setObjectName(u"signup_button")
        self.signup_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.signup_button.setStyleSheet(u" padding: 8px 16px;  /* Padding inside the button */\n"
"    color: white;  /* Font color */\n"
"    background-color: rgb(0, 123, 255);  /* Bootstrap blue */\n"
"    border-radius: 5px;  /* Optional: rounded corners */\n"
"    border: 1px solid rgb(0, 102, 204);  /* Darker border color */")
        self.signup_button.setAutoDefault(True)

        self.verticalLayout.addWidget(self.signup_button)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.stackedWidget.addWidget(self.signup)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.retranslateUi(authenticationsystem)

        self.stackedWidget.setCurrentIndex(1)
        self.login_button.setDefault(True)
        self.signup_button.setDefault(True)


        QMetaObject.connectSlotsByName(authenticationsystem)
    # setupUi

    def retranslateUi(self, authenticationsystem):
        authenticationsystem.setWindowTitle(QCoreApplication.translate("authenticationsystem", u"Dialog", None))
        self.login_label.setText(QCoreApplication.translate("authenticationsystem", u"Login", None))
        self.username_label.setText(QCoreApplication.translate("authenticationsystem", u"Username: ", None))
        self.uservalidation_label.setText("")
        self.password_label.setText(QCoreApplication.translate("authenticationsystem", u"Password:", None))
        self.passvalidation_label.setText("")
        self.label_5.setText(QCoreApplication.translate("authenticationsystem", u"Don't have an account?", None))
        self.createacc_button.setText(QCoreApplication.translate("authenticationsystem", u"Create Account", None))
        self.login_button.setText(QCoreApplication.translate("authenticationsystem", u"Login", None))
        self.signup_label.setText(QCoreApplication.translate("authenticationsystem", u"Signup", None))
        self.username_label_2.setText(QCoreApplication.translate("authenticationsystem", u"Username: ", None))
        self.password_label_2.setText(QCoreApplication.translate("authenticationsystem", u"Password:", None))
        self.confirmpass_label.setText(QCoreApplication.translate("authenticationsystem", u"Confirm Password:", None))
        self.validation_label.setText("")
        self.signup_button.setText(QCoreApplication.translate("authenticationsystem", u"Signup", None))
    # retranslateUi

