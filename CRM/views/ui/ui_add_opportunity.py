# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_opportunity.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QDialog,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(630, 513)
        Dialog.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #171717;")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.add_btn = QPushButton(Dialog)
        self.add_btn.setObjectName(u"add_btn")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        self.add_btn.setFont(font1)
        self.add_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #E5E5E5;\n"
"    border: 1px solid #737373;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"	padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(204, 204, 204);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(180, 180, 180);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.add_btn)

        self.horizontalSpacer_7 = QSpacerItem(0, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.cancel_btn = QPushButton(Dialog)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setFont(font1)
        self.cancel_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #E5E5E5;\n"
"    border: 1px solid #737373;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"	padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(204, 204, 204);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(180, 180, 180);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.cancel_btn)


        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 10, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 10, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 4, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.title_line = QLineEdit(Dialog)
        self.title_line.setObjectName(u"title_line")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(195)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.title_line.sizePolicy().hasHeightForWidth())
        self.title_line.setSizePolicy(sizePolicy)
        self.title_line.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E5E5E5;\n"
"    border: 1px solid #737373;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font: 10pt \"Segoe UI\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.title_line)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"QDateEdit {\n"
"    background-color: #E5E5E5;\n"
"    border: 1px solid #737373;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* Optional: Style the arrow button */\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #737373;\n"
"    background-color: #D4D4D4;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"/* Optional: Customize the down arrow icon */\n"
"QDateEdit::down-arrow {\n"
"    image: url(:/Resources/arrow_blue.png); /* Replace with your icon */\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.dateEdit.setMinimumDate(QDate(2025, 1, 1))
        self.dateEdit.setCurrentSection(QDateTimeEdit.Section.MonthSection)
        self.dateEdit.setCalendarPopup(False)

        self.horizontalLayout_2.addWidget(self.dateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 10, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.cost_line = QLineEdit(Dialog)
        self.cost_line.setObjectName(u"cost_line")
        sizePolicy.setHeightForWidth(self.cost_line.sizePolicy().hasHeightForWidth())
        self.cost_line.setSizePolicy(sizePolicy)
        self.cost_line.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E5E5E5;\n"
"    border: 1px solid #737373;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font: 10pt \"Segoe UI\";\n"
"}")

        self.horizontalLayout_3.addWidget(self.cost_line)

        self.horizontalSpacer = QSpacerItem(165, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.details_text = QTextEdit(Dialog)
        self.details_text.setObjectName(u"details_text")
        self.details_text.setStyleSheet(u"QTextEdit {\n"
"    background-color: #E5E5E5;\n"
"    border: 1px solid #737373;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font: 10pt \"Segoe UI\";\n"
"}")

        self.verticalLayout_2.addWidget(self.details_text)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 6, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Add Opportunity", None))
        self.add_btn.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Title:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Date:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Cost:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Details:", None))
    # retranslateUi

