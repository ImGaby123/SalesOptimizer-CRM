# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts_email.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QWidget)

class Ui_contacts_email(object):
    def setupUi(self, contacts_email):
        if not contacts_email.objectName():
            contacts_email.setObjectName(u"contacts_email")
        contacts_email.resize(440, 280)
        contacts_email.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.gridLayout_2 = QGridLayout(contacts_email)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.recipient_line = QLineEdit(contacts_email)
        self.recipient_line.setObjectName(u"recipient_line")
        self.recipient_line.setStyleSheet(u"QLineEdit {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"    color: white;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font: 10pt \"Segoe UI\";\n"
"}")

        self.horizontalLayout_23.addWidget(self.recipient_line)


        self.gridLayout.addLayout(self.horizontalLayout_23, 0, 0, 1, 1)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer)

        self.send_btn = QPushButton(contacts_email)
        self.send_btn.setObjectName(u"send_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_btn.sizePolicy().hasHeightForWidth())
        self.send_btn.setSizePolicy(sizePolicy)
        self.send_btn.setMinimumSize(QSize(90, 0))
        self.send_btn.setMaximumSize(QSize(90, 16777215))
        self.send_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font: 10pt \"Segoe UI\";\n"
"    text-align: center;\n"
"	padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200);  /* Darker gray on hover */\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 180, 180);  /* Darker gray on press */\n"
"}\n"
"")

        self.horizontalLayout_35.addWidget(self.send_btn)


        self.gridLayout.addLayout(self.horizontalLayout_35, 7, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.email_txt = QTextEdit(contacts_email)
        self.email_txt.setObjectName(u"email_txt")
        self.email_txt.setStyleSheet(u"QTextEdit {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"    color: white;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font: 10pt \"Segoe UI\";\n"
"}")

        self.horizontalLayout_33.addWidget(self.email_txt)


        self.gridLayout.addLayout(self.horizontalLayout_33, 5, 0, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.subject_line = QLineEdit(contacts_email)
        self.subject_line.setObjectName(u"subject_line")
        self.subject_line.setStyleSheet(u"QLineEdit {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"    color: white;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font: 10pt \"Segoe UI\";\n"
"}")

        self.horizontalLayout_24.addWidget(self.subject_line)


        self.gridLayout.addLayout(self.horizontalLayout_24, 4, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(contacts_email)

        QMetaObject.connectSlotsByName(contacts_email)
    # setupUi

    def retranslateUi(self, contacts_email):
        contacts_email.setWindowTitle(QCoreApplication.translate("contacts_email", u"New Message", None))
        self.recipient_line.setPlaceholderText(QCoreApplication.translate("contacts_email", u"Recipient", None))
        self.send_btn.setText(QCoreApplication.translate("contacts_email", u"Send", None))
        self.email_txt.setHtml(QCoreApplication.translate("contacts_email", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.subject_line.setPlaceholderText(QCoreApplication.translate("contacts_email", u"Subject", None))
    # retranslateUi

