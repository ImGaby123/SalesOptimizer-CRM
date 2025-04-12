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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_add_opportunity(object):
    def setupUi(self, add_opportunity):
        if not add_opportunity.objectName():
            add_opportunity.setObjectName(u"add_opportunity")
        add_opportunity.resize(590, 513)
        add_opportunity.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #171717;")
        self.gridLayout = QGridLayout(add_opportunity)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_frame = QFrame(add_opportunity)
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
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_13 = QSpacerItem(10, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)

        self.title_line = QLineEdit(self.main_frame)
        self.title_line.setObjectName(u"title_line")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_line.sizePolicy().hasHeightForWidth())
        self.title_line.setSizePolicy(sizePolicy)
        self.title_line.setMinimumSize(QSize(245, 0))
        self.title_line.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        self.title_line.setFont(font2)
        self.title_line.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E5E5E5;\n"
"    border: 1px solid #737373;\n"
"    border-radius: 5px;\n"
"	padding: 5px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.title_line)

        self.horizontalSpacer_11 = QSpacerItem(25, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)

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
        self.date_edit.setMaximumSize(QSize(190, 16777215))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        self.date_edit.setFont(font3)
        self.date_edit.setStyleSheet(u"QDateEdit {\n"
"    background-color: #FFFFFF;    /* White background */\n"
"    color: black;                 /* Black text */\n"
"    border: 1px solid #BFBFBF;    /* Light gray border */\n"
"    border-radius: 5px;\n"
"    padding: 5px 25px 5px 10px;   /* Extra padding for the drop-down icon */\n"
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
"/* Calendar icon (set the path to your calendar icon) */\n"
"QDateEdit::down-arrow {\n"
"    image: url(:/Resources/calendar.png);  /* Replace with your own icon */\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin-right: 14px;\n"
"}\n"
"\n"
"/* Hover effect */\n"
"QDateEdit:hover {\n"
"    background-color: #F0F0F0;     /* Light gray background on hover */\n"
"    color: black;\n"
"    border: 1px solid #16D4FF;      /* Border turns blue when hovered */\n"
"}\n"
"\n"
"/* Focus effect (when clicked)"
                        " */\n"
"QDateEdit:focus {\n"
"    border: 1px solid #16D4FF;      /* Blue border when focused */\n"
"    background-color: #F9F9F9;      /* Slightly lighter background */\n"
"}\n"
"\n"
"/* Calendar popup container (QCalendarWidget) */\n"
"QCalendarWidget {\n"
"    background-color: #FFFFFF;\n"
"    color: #000000;\n"
"    border: 1px solid #BFBFBF;\n"
"    border-radius: 6px;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* Header navigation bar (month/year buttons & arrows) */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #F0F0F0;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    background-color: #E5E5E5;\n"
"    color: #000000;\n"
"    border: none;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #DADADA;\n"
"}\n"
"\n"
"/* Remove down arrow on month/year combo (optional) */\n"
"QCalendarWidget QToolButton::menu-indicator {\n"
"    image: none;\n"
"}\n"
"\n"
"/* Weekday labels (Mon-Sun) */\n"
""
                        "QCalendarWidget QHeaderView {\n"
"    background-color: #F5F5F5;\n"
"}\n"
"\n"
"QCalendarWidget QHeaderView::section {\n"
"    color: #555555;\n"
"    background-color: #F5F5F5;\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Day numbers */\n"
"QCalendarWidget QAbstractItemView {\n"
"    background-color: #FFFFFF;\n"
"    color: #000000;\n"
"    selection-background-color: #16D4FF;  /* Highlighted date */\n"
"    selection-color: #000000;\n"
"    gridline-color: #D0D0D0;\n"
"}\n"
"\n"
"/* Today highlight */\n"
"QCalendarWidget QWidget#qt_calendar_today {\n"
"    border: 1px solid #16D4FF;\n"
"    background-color: #F0F0F0;\n"
"    border-radius: 4px;\n"
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

        self.horizontalSpacer_14 = QSpacerItem(10, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_14)

        self.cost_line = QLineEdit(self.main_frame)
        self.cost_line.setObjectName(u"cost_line")
        sizePolicy.setHeightForWidth(self.cost_line.sizePolicy().hasHeightForWidth())
        self.cost_line.setSizePolicy(sizePolicy)
        self.cost_line.setMinimumSize(QSize(245, 0))
        self.cost_line.setMaximumSize(QSize(16777215, 16777215))
        self.cost_line.setFont(font2)
        self.cost_line.setStyleSheet(u"QLineEdit {\n"
"    background-color: #E5E5E5;\n"
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
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setItalic(False)
        self.add_btn.setFont(font4)
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

        self.cancel_btn = QPushButton(self.main_frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setFont(font4)
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


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(483, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 6, 1, 1, 1)


        self.gridLayout.addWidget(self.main_frame, 0, 0, 1, 1)


        self.retranslateUi(add_opportunity)

        QMetaObject.connectSlotsByName(add_opportunity)
    # setupUi

    def retranslateUi(self, add_opportunity):
        add_opportunity.setWindowTitle(QCoreApplication.translate("add_opportunity", u"add_opportunity", None))
        self.label.setText(QCoreApplication.translate("add_opportunity", u"Add Opportunity", None))
        self.label_2.setText(QCoreApplication.translate("add_opportunity", u"Title:", None))
        self.label_3.setText(QCoreApplication.translate("add_opportunity", u"Date:", None))
        self.date_edit.setDisplayFormat(QCoreApplication.translate("add_opportunity", u"yyyy/M/d", None))
        self.label_4.setText(QCoreApplication.translate("add_opportunity", u"Cost:", None))
        self.label_5.setText(QCoreApplication.translate("add_opportunity", u"Details:", None))
        self.add_btn.setText(QCoreApplication.translate("add_opportunity", u"Add", None))
        self.cancel_btn.setText(QCoreApplication.translate("add_opportunity", u"Cancel", None))
    # retranslateUi

