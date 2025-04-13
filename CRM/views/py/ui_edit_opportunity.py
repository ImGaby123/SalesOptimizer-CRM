# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_opportunity.ui'
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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_edit_opportunity(object):
    def setupUi(self, edit_opportunity):
        if not edit_opportunity.objectName():
            edit_opportunity.setObjectName(u"edit_opportunity")
        edit_opportunity.resize(528, 481)
        edit_opportunity.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #171717;\n"
"color: white;")
        self.gridLayout = QGridLayout(edit_opportunity)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_frame = QFrame(edit_opportunity)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.main_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_8 = QSpacerItem(483, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.main_frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(483, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 267, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.main_frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_11 = QSpacerItem(10, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)

        self.title_line = QLineEdit(self.main_frame)
        self.title_line.setObjectName(u"title_line")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_line.sizePolicy().hasHeightForWidth())
        self.title_line.setSizePolicy(sizePolicy)
        self.title_line.setMinimumSize(QSize(200, 0))
        self.title_line.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setItalic(False)
        self.title_line.setFont(font2)
        self.title_line.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E5E5E5;\n"
"	color: rgb(0, 0, 0);\n"
"    border: 1px solid #737373;\n"
"    border-radius: 5px;\n"
"	padding: 5px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.title_line)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.label_3 = QLabel(self.main_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.date_edit = QDateEdit(self.main_frame)
        self.date_edit.setObjectName(u"date_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.date_edit.sizePolicy().hasHeightForWidth())
        self.date_edit.setSizePolicy(sizePolicy1)
        self.date_edit.setMinimumSize(QSize(110, 0))
        self.date_edit.setMaximumSize(QSize(16777215, 16777215))
        self.date_edit.setFont(font2)
        self.date_edit.setStyleSheet(u"/* QDateEdit main field */\n"
"QDateEdit {\n"
"    color: #171717;\n"
"    background-color: #E5E5E5;\n"
"    border: 1px solid #171717;\n"
"    border-radius: 5px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"/* Drop-down area */\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Calendar icon */\n"
"QDateEdit::down-arrow {\n"
"    image: url(:/Resources/calendar.png);  /* use a dark icon on E5E5E5 background */\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin-right: 14px;\n"
"}\n"
"\n"
"/* Hover */\n"
"QDateEdit:hover {\n"
"    background-color: #E5E5E5;\n"
"    color: #171717;\n"
"    border: 1px solid #171717;\n"
"}\n"
"\n"
"/* Focus */\n"
"QDateEdit:focus {\n"
"    border: 1px solid #171717;\n"
"    background-color: #DADADA;\n"
"    color: #171717;\n"
"}\n"
"\n"
"/* Calendar popup */\n"
"QCalendarWidget {\n"
"    background-color: #E5E5E5;\n"
"    color: #171717;\n"
"    bord"
                        "er: 1px solid #171717;\n"
"    border-radius: 6px;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* Header navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #DADADA;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    background-color: #CCCCCC;\n"
"    color: #171717;\n"
"    border: none;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #BFBFBF;\n"
"}\n"
"\n"
"/* Remove dropdown arrow from tool buttons */\n"
"QCalendarWidget QToolButton::menu-indicator {\n"
"    image: none;\n"
"}\n"
"\n"
"/* Weekday headers */\n"
"QCalendarWidget QHeaderView {\n"
"    background-color: #DADADA;\n"
"}\n"
"\n"
"QCalendarWidget QHeaderView::section {\n"
"    color: #171717;\n"
"    background-color: #DADADA;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Days view */\n"
"QCalendarWidget QAbstractItemView {\n"
"    background-color: #E5E5E5;\n"
"    color: #171717;\n"
"    selection-bac"
                        "kground-color: #171717;  /* Black highlight for selected */\n"
"    selection-color: #E5E5E5;             /* Light text on dark selection */\n"
"    gridline-color: #BFBFBF;\n"
"}\n"
"\n"
"/* Today cell */\n"
"QCalendarWidget QWidget#qt_calendar_today {\n"
"    border: 1px solid #171717;\n"
"    background-color: #DADADA;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Month/year dropdown */\n"
"QCalendarWidget QMenu {\n"
"    background-color: #E5E5E5;\n"
"    color: #171717;\n"
"    border: 1px solid #171717;\n"
"}\n"
"")
        self.date_edit.setMinimumDate(QDate(2025, 1, 1))
        self.date_edit.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.date_edit.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.date_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 10, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.main_frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_13 = QSpacerItem(10, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_13)

        self.cost_line = QLineEdit(self.main_frame)
        self.cost_line.setObjectName(u"cost_line")
        sizePolicy.setHeightForWidth(self.cost_line.sizePolicy().hasHeightForWidth())
        self.cost_line.setSizePolicy(sizePolicy)
        self.cost_line.setMinimumSize(QSize(200, 0))
        self.cost_line.setMaximumSize(QSize(16777215, 16777215))
        self.cost_line.setFont(font2)
        self.cost_line.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E5E5E5;\n"
"	color: rgb(0, 0, 0);\n"
"    border: 1px solid #737373;\n"
"    border-radius: 5px;\n"
"	padding: 5px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.cost_line)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.main_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer_12 = QSpacerItem(40, 5, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_12)

        self.details_text = QTextEdit(self.main_frame)
        self.details_text.setObjectName(u"details_text")
        self.details_text.setFont(font2)
        self.details_text.setStyleSheet(u"QTextEdit {\n"
"	color: rgb(0, 0, 0);\n"
"    background-color: #E5E5E5;\n"
"    border: 1px solid #737373;\n"
"    border-radius: 5px;\n"
"	padding: 5px;\n"
"}")

        self.verticalLayout_2.addWidget(self.details_text)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 267, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(483, 5, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 4, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.save_btn = QPushButton(self.main_frame)
        self.save_btn.setObjectName(u"save_btn")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        self.save_btn.setFont(font3)
        self.save_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #E5E5E5;\n"
"	color: rgb(0, 0, 0);\n"
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

        self.horizontalLayout_4.addWidget(self.save_btn)

        self.horizontalSpacer_7 = QSpacerItem(0, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.cancel_btn = QPushButton(self.main_frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setFont(font3)
        self.cancel_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #E5E5E5;\n"
"	color: rgb(0, 0, 0);\n"
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


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(483, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 6, 1, 1, 1)


        self.gridLayout.addWidget(self.main_frame, 0, 0, 1, 1)


        self.retranslateUi(edit_opportunity)

        QMetaObject.connectSlotsByName(edit_opportunity)
    # setupUi

    def retranslateUi(self, edit_opportunity):
        edit_opportunity.setWindowTitle(QCoreApplication.translate("edit_opportunity", u"edit_opportunity", None))
        self.label.setText(QCoreApplication.translate("edit_opportunity", u"Edit Opportunity", None))
        self.label_2.setText(QCoreApplication.translate("edit_opportunity", u"Title:", None))
        self.label_3.setText(QCoreApplication.translate("edit_opportunity", u"Date:", None))
        self.date_edit.setDisplayFormat(QCoreApplication.translate("edit_opportunity", u"yyyy/MM/dd", None))
        self.label_4.setText(QCoreApplication.translate("edit_opportunity", u"Cost:", None))
        self.label_5.setText(QCoreApplication.translate("edit_opportunity", u"Details:", None))
        self.save_btn.setText(QCoreApplication.translate("edit_opportunity", u"Save", None))
        self.cancel_btn.setText(QCoreApplication.translate("edit_opportunity", u"Cancel", None))
    # retranslateUi

