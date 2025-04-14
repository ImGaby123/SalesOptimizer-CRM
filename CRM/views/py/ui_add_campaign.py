# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_campaign.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QDialog, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_add_campaign(object):
    def setupUi(self, add_campaign):
        if not add_campaign.objectName():
            add_campaign.setObjectName(u"add_campaign")
        add_campaign.resize(528, 550)
        add_campaign.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #171717;\n"
"color: white;")
        self.gridLayout = QGridLayout(add_campaign)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_frame = QFrame(add_campaign)
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
        self.opportunity_line = QLabel(self.main_frame)
        self.opportunity_line.setObjectName(u"opportunity_line")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.opportunity_line.setFont(font1)
        self.opportunity_line.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.opportunity_line.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.opportunity_line)

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

        self.action_line = QLineEdit(self.main_frame)
        self.action_line.setObjectName(u"action_line")
        sizePolicy.setHeightForWidth(self.action_line.sizePolicy().hasHeightForWidth())
        self.action_line.setSizePolicy(sizePolicy)
        self.action_line.setMinimumSize(QSize(200, 0))
        self.action_line.setMaximumSize(QSize(16777215, 16777215))
        self.action_line.setFont(font2)
        self.action_line.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E5E5E5;\n"
"	color: rgb(0, 0, 0);\n"
"    border: 1px solid #737373;\n"
"    border-radius: 5px;\n"
"	padding: 5px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.action_line)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.main_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.horizontalSpacer_14 = QSpacerItem(10, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_14)

        self.campaign_type_combo = QComboBox(self.main_frame)
        self.campaign_type_combo.addItem("")
        self.campaign_type_combo.addItem("")
        self.campaign_type_combo.addItem("")
        self.campaign_type_combo.addItem("")
        self.campaign_type_combo.addItem("")
        self.campaign_type_combo.addItem("")
        self.campaign_type_combo.addItem("")
        self.campaign_type_combo.addItem("")
        self.campaign_type_combo.setObjectName(u"campaign_type_combo")
        self.campaign_type_combo.setMinimumSize(QSize(200, 0))
        self.campaign_type_combo.setStyleSheet(u"QComboBox {\n"
"    background-color: #E5E5E5;\n"
"    color: #171717;\n"
"    border: 1px solid #737373;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #E5E5E5;\n"
"    color: #171717;\n"
"    border-radius: 10px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.campaign_type_combo)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_15)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_16 = QSpacerItem(40, 10, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_16)

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

        self.add_btn = QPushButton(self.main_frame)
        self.add_btn.setObjectName(u"add_btn")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        self.add_btn.setFont(font3)
        self.add_btn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_4.addWidget(self.add_btn)

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


        self.retranslateUi(add_campaign)

        QMetaObject.connectSlotsByName(add_campaign)
    # setupUi

    def retranslateUi(self, add_campaign):
        add_campaign.setWindowTitle(QCoreApplication.translate("add_campaign", u"add_campaign", None))
        self.label.setText(QCoreApplication.translate("add_campaign", u"Add Campaign", None))
        self.opportunity_line.setText(QCoreApplication.translate("add_campaign", u"Opportunity:", None))
        self.label_3.setText(QCoreApplication.translate("add_campaign", u"Date:", None))
        self.date_edit.setDisplayFormat(QCoreApplication.translate("add_campaign", u"yyyy/MM/dd", None))
        self.label_4.setText(QCoreApplication.translate("add_campaign", u"Action:", None))
        self.label_6.setText(QCoreApplication.translate("add_campaign", u"Type:", None))
        self.campaign_type_combo.setItemText(0, QCoreApplication.translate("add_campaign", u"Email", None))
        self.campaign_type_combo.setItemText(1, QCoreApplication.translate("add_campaign", u"Social Media", None))
        self.campaign_type_combo.setItemText(2, QCoreApplication.translate("add_campaign", u"Referral", None))
        self.campaign_type_combo.setItemText(3, QCoreApplication.translate("add_campaign", u"Text Message", None))
        self.campaign_type_combo.setItemText(4, QCoreApplication.translate("add_campaign", u"Call", None))
        self.campaign_type_combo.setItemText(5, QCoreApplication.translate("add_campaign", u"Online Advertising ", None))
        self.campaign_type_combo.setItemText(6, QCoreApplication.translate("add_campaign", u"Webinar", None))
        self.campaign_type_combo.setItemText(7, QCoreApplication.translate("add_campaign", u"Other", None))

        self.label_5.setText(QCoreApplication.translate("add_campaign", u"Details:", None))
        self.add_btn.setText(QCoreApplication.translate("add_campaign", u"Add", None))
        self.cancel_btn.setText(QCoreApplication.translate("add_campaign", u"Cancel", None))
    # retranslateUi

