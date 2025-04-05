# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'leads_profile.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QProgressBar,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import views.py.icons_rc

class Ui_leads_profile(object):
    def setupUi(self, leads_profile):
        if not leads_profile.objectName():
            leads_profile.setObjectName(u"leads_profile")
        leads_profile.resize(1201, 680)
        leads_profile.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.gridLayout = QGridLayout(leads_profile)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(leads_profile)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border: none;\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none;")

        self.horizontalLayout_17.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"border: none;\n"
"")
        self.label_14.setPixmap(QPixmap(u":/Resources/company_logo.png"))

        self.horizontalLayout_9.addWidget(self.label_14)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_6.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        font2 = QFont()
        font2.setPointSize(11)
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_6.addWidget(self.label_17)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_3.addWidget(self.label_2)

        self.info_bar = QProgressBar(self.frame)
        self.info_bar.setObjectName(u"info_bar")
        self.info_bar.setStyleSheet(u"QProgressBar {\n"
"    background-color: #2e2e2e;\n"
"    border: 1px solid #737373;\n"
"    border-radius: 30px;\n"
"    text-align: center;\n"
"    color: white;\n"
"    font: 10pt \"Segoe UI\";\n"
"    height: 20px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #A3E635;  /* Green chunk color */\n"
"    border-radius: 80px;  /* Match the outer radius */\n"
"    margin: 1px;\n"
"}\n"
"")
        self.info_bar.setValue(81)

        self.verticalLayout_3.addWidget(self.info_bar)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radioButton = QRadioButton(self.frame)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font2)
        self.radioButton.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.radioButton.setStyleSheet(u"QRadioButton {\n"
"    background: transparent;\n"
"    color: #fff;\n"
"	border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #A3E635; \n"
"    border-color: #A3E635;   \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;         \n"
"    height: 16px;       \n"
"    border-radius: 8px; \n"
"    background-color: white; \n"
"}\n"
"")
        self.radioButton.setChecked(False)

        self.horizontalLayout_8.addWidget(self.radioButton, 0, Qt.AlignmentFlag.AlignRight)

        self.radioButton_9 = QRadioButton(self.frame)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setFont(font2)
        self.radioButton_9.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.radioButton_9.setStyleSheet(u"QRadioButton {\n"
"    background: transparent;\n"
"    color: #fff;\n"
"	border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #A3E635; \n"
"    border-color: #A3E635;   \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;         \n"
"    height: 16px;       \n"
"    border-radius: 8px; \n"
"    background-color: white; \n"
"}\n"
"")
        self.radioButton_9.setChecked(False)

        self.horizontalLayout_8.addWidget(self.radioButton_9, 0, Qt.AlignmentFlag.AlignRight)

        self.radioButton_8 = QRadioButton(self.frame)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setFont(font2)
        self.radioButton_8.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.radioButton_8.setStyleSheet(u"QRadioButton {\n"
"    background: transparent;\n"
"    color: #fff;\n"
"	border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #A3E635; \n"
"    border-color: #A3E635;   \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;         \n"
"    height: 16px;       \n"
"    border-radius: 8px; \n"
"    background-color: white; \n"
"}\n"
"")
        self.radioButton_8.setChecked(False)

        self.horizontalLayout_8.addWidget(self.radioButton_8, 0, Qt.AlignmentFlag.AlignRight)

        self.radioButton_10 = QRadioButton(self.frame)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setFont(font2)
        self.radioButton_10.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.radioButton_10.setStyleSheet(u"QRadioButton {\n"
"    background: transparent;\n"
"    color: #fff;\n"
"	border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #A3E635; \n"
"    border-color: #A3E635;   \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;         \n"
"    height: 16px;       \n"
"    border-radius: 8px; \n"
"    background-color: white; \n"
"}\n"
"")
        self.radioButton_10.setChecked(False)

        self.horizontalLayout_8.addWidget(self.radioButton_10, 0, Qt.AlignmentFlag.AlignRight)

        self.radioButton_12 = QRadioButton(self.frame)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setFont(font2)
        self.radioButton_12.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.radioButton_12.setStyleSheet(u"QRadioButton {\n"
"    background: transparent;\n"
"    color: #fff;\n"
"	border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #A3E635; \n"
"    border-color: #A3E635;   \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;         \n"
"    height: 16px;       \n"
"    border-radius: 8px; \n"
"    background-color: white; \n"
"}\n"
"")
        self.radioButton_12.setChecked(False)

        self.horizontalLayout_8.addWidget(self.radioButton_12, 0, Qt.AlignmentFlag.AlignRight)

        self.radioButton_11 = QRadioButton(self.frame)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setFont(font2)
        self.radioButton_11.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.radioButton_11.setStyleSheet(u"QRadioButton {\n"
"    background: transparent;\n"
"    color: #fff;\n"
"	border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #A3E635; \n"
"    border-color: #A3E635;   \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;         \n"
"    height: 16px;       \n"
"    border-radius: 8px; \n"
"    background-color: white; \n"
"}\n"
"")
        self.radioButton_11.setCheckable(True)
        self.radioButton_11.setChecked(False)

        self.horizontalLayout_8.addWidget(self.radioButton_11, 0, Qt.AlignmentFlag.AlignRight)

        self.radioButton_4 = QRadioButton(self.frame)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font2)
        self.radioButton_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.radioButton_4.setStyleSheet(u"QRadioButton {\n"
"    background: transparent;\n"
"    color: #fff;\n"
"	border: none;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #A3E635; \n"
"    border-color: #A3E635;   \n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;         \n"
"    height: 16px;       \n"
"    border-radius: 8px; \n"
"    background-color: white; \n"
"}\n"
"")
        self.radioButton_4.setChecked(False)

        self.horizontalLayout_8.addWidget(self.radioButton_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: 1px solid rgb(226, 226, 226);\n"
"border-radius: 15px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.horizontalLayout_5.addWidget(self.label_23)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"    color: white;\n"
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
"    background-color: #262626;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* Down Arrow (Icon) */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/Resources/dropdown_white.svg);\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    margin-right: 15px; /* Space from the left */\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_5.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_10.addWidget(self.label_7)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_10.addWidget(self.label_9)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_10.addWidget(self.label_8)


        self.horizontalLayout_2.addLayout(self.verticalLayout_10)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_11.addWidget(self.label_15)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_40 = QLabel(self.frame_2)
        self.label_40.setObjectName(u"label_40")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy1)
        self.label_40.setStyleSheet(u"background: transparent;\n"
"color: #A3E635;\n"
"border: none")

        self.verticalLayout_24.addWidget(self.label_40)

        self.label_41 = QLabel(self.frame_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"background: transparent;\n"
"color: #FCA5A5;\n"
"border: none")

        self.verticalLayout_24.addWidget(self.label_41)


        self.horizontalLayout_21.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setStyleSheet(u"border: none;")
        self.label_4.setPixmap(QPixmap(u":/Resources/box_up.png"))

        self.verticalLayout_25.addWidget(self.label_4)

        self.label_39 = QLabel(self.frame_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"border: none;")
        self.label_39.setPixmap(QPixmap(u":/Resources/box_down.png"))

        self.verticalLayout_25.addWidget(self.label_39)


        self.horizontalLayout_21.addLayout(self.verticalLayout_25)


        self.verticalLayout_11.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_3.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_12.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_12.addWidget(self.label_6)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_12.addWidget(self.label_10)


        self.horizontalLayout_3.addLayout(self.verticalLayout_12)


        self.verticalLayout_13.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_13)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"    alternate-background-color: rgb(235, 235, 235);\n"
"    gridline-color: rgb(200, 200, 200);\n"
"    color: black;\n"
"    font: 10pt \"Segoe UI\";\n"
"    selection-background-color: rgb(100, 149, 237);  /* Light blue selection */\n"
"    selection-color: white;\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(240, 240, 240);\n"
"    color: black;\n"
"    padding: 6px;\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: rgb(240, 240, 240);\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.tableWidget)


        self.verticalLayout_4.addLayout(self.verticalLayout_7)


        self.horizontalLayout_16.addLayout(self.verticalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_16.addItem(self.verticalSpacer_3)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 20px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(-16, 0, 406, 264))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.horizontalLayout_13.addWidget(self.label_18)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_13)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(True)
        font4.setItalic(False)
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E; /* Darker background for the button */\n"
"    border: 1px solid #16D4FF; /* Blue border */\n"
"    color: #16D4FF; /* Blue text */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"    padding: 8px 16px; /* Padding to give some space */\n"
"    text-align: center; /* Center the text */\n"
"    font-size: 14px; /* Adjust font size */\n"
"    font-weight: bold; /* Bold text */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3A3A3A; /* Dark gray background on hover */\n"
"    color: #FFFFFF; /* White text on hover */\n"
"    border-color: #1E90FF; /* Slightly lighter blue border on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5A5A5A; /* Darker gray background on press */\n"
"    color: #FFFFFF; /* White text on press */\n"
"    border-color: #1E90FF; /* Keep the blue border color when pressed */\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/Resources/arrow_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(30, 30))
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_19.addWidget(self.pushButton_2)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_19)


        self.verticalLayout_21.addLayout(self.horizontalLayout_20)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_21.addWidget(self.line_4)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border-radius: 10px;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_38 = QLabel(self.frame_5)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.horizontalLayout_15.addWidget(self.label_38)


        self.horizontalLayout_14.addWidget(self.frame_5)


        self.verticalLayout_21.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_5)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_20.addWidget(self.scrollArea)


        self.horizontalLayout_16.addLayout(self.verticalLayout_20)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_16.addItem(self.verticalSpacer_4)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border: 1px solid rgb(226, 226, 226);\n"
"border-radius: 15px;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_26 = QLabel(self.frame_4)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_26)


        self.verticalLayout_17.addLayout(self.horizontalLayout_11)

        self.line_3 = QFrame(self.frame_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_17.addWidget(self.line_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_28 = QLabel(self.frame_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_18.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_18.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_18.addWidget(self.label_30)

        self.label_34 = QLabel(self.frame_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_18.addWidget(self.label_34)

        self.label_35 = QLabel(self.frame_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_18.addWidget(self.label_35)


        self.horizontalLayout_12.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_31 = QLabel(self.frame_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_19.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_19.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_19.addWidget(self.label_33)

        self.label_36 = QLabel(self.frame_4)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_19.addWidget(self.label_36)

        self.label_37 = QLabel(self.frame_4)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_19.addWidget(self.label_37)


        self.horizontalLayout_12.addLayout(self.verticalLayout_19)


        self.verticalLayout_17.addLayout(self.horizontalLayout_12)


        self.verticalLayout_16.addWidget(self.frame_4)


        self.verticalLayout_22.addLayout(self.verticalLayout_16)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: 1px solid rgb(226, 226, 226);\n"
"border-radius: 15px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_20)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_9.addWidget(self.line_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_14.addWidget(self.label_19)

        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_14.addWidget(self.label_22)

        self.label_25 = QLabel(self.frame_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_14.addWidget(self.label_25)


        self.horizontalLayout_4.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_15.addWidget(self.label_21)

        self.label_24 = QLabel(self.frame_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_15.addWidget(self.label_24)

        self.label_27 = QLabel(self.frame_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_15.addWidget(self.label_27)


        self.horizontalLayout_4.addLayout(self.verticalLayout_15)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addWidget(self.frame_3)


        self.verticalLayout_22.addLayout(self.verticalLayout_8)


        self.horizontalLayout_16.addLayout(self.verticalLayout_22)


        self.verticalLayout_3.addLayout(self.horizontalLayout_16)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout_23.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_23, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)


        self.retranslateUi(leads_profile)

        QMetaObject.connectSlotsByName(leads_profile)
    # setupUi

    def retranslateUi(self, leads_profile):
        leads_profile.setWindowTitle(QCoreApplication.translate("leads_profile", u"Lead ", None))
        self.label.setText(QCoreApplication.translate("leads_profile", u"Lead Profile", None))
        self.label_14.setText("")
        self.label_16.setText(QCoreApplication.translate("leads_profile", u"Company Name:", None))
        self.label_17.setText(QCoreApplication.translate("leads_profile", u"Hudson - Homenick", None))
        self.label_2.setText(QCoreApplication.translate("leads_profile", u"Sales Pipeline", None))
        self.info_bar.setFormat("")
        self.radioButton.setText(QCoreApplication.translate("leads_profile", u"Lead", None))
        self.radioButton_9.setText(QCoreApplication.translate("leads_profile", u"Prospecting", None))
        self.radioButton_8.setText(QCoreApplication.translate("leads_profile", u"Qualifications", None))
        self.radioButton_10.setText(QCoreApplication.translate("leads_profile", u"Contacting", None))
        self.radioButton_12.setText(QCoreApplication.translate("leads_profile", u"Negotiating", None))
        self.radioButton_11.setText(QCoreApplication.translate("leads_profile", u"Closed Loss", None))
        self.radioButton_4.setText(QCoreApplication.translate("leads_profile", u"Closed Won", None))
        self.label_23.setText(QCoreApplication.translate("leads_profile", u"Total Lead", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("leads_profile", u"View All", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("leads_profile", u"Last Week", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("leads_profile", u"Last Month", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("leads_profile", u"New Year", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("leads_profile", u"view all", None))
        self.label_7.setText(QCoreApplication.translate("leads_profile", u"Total Leads", None))
        self.label_9.setText(QCoreApplication.translate("leads_profile", u"Leads", None))
        self.label_8.setText(QCoreApplication.translate("leads_profile", u"Leads ", None))
        self.label_15.setText(QCoreApplication.translate("leads_profile", u"=", None))
        self.label_40.setText(QCoreApplication.translate("leads_profile", u"50", None))
        self.label_41.setText(QCoreApplication.translate("leads_profile", u"50", None))
        self.label_4.setText("")
        self.label_39.setText("")
        self.label_5.setText(QCoreApplication.translate("leads_profile", u"100", None))
        self.label_6.setText(QCoreApplication.translate("leads_profile", u"100", None))
        self.label_10.setText(QCoreApplication.translate("leads_profile", u"100", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("leads_profile", u"Lead List", None));
        self.label_18.setText(QCoreApplication.translate("leads_profile", u"Campaign Timeline", None))
        self.pushButton_2.setText(QCoreApplication.translate("leads_profile", u"Promote to Prospect", None))
        self.label_38.setText(QCoreApplication.translate("leads_profile", u"Hudson - Homenick Has been promoted to Prospect!.", None))
        self.label_26.setText(QCoreApplication.translate("leads_profile", u"Contact Information", None))
        self.label_28.setText(QCoreApplication.translate("leads_profile", u"Account Name:", None))
        self.label_29.setText(QCoreApplication.translate("leads_profile", u"Company Name:", None))
        self.label_30.setText(QCoreApplication.translate("leads_profile", u"Company Role:", None))
        self.label_34.setText(QCoreApplication.translate("leads_profile", u"Email:", None))
        self.label_35.setText(QCoreApplication.translate("leads_profile", u"Contact Number:", None))
        self.label_31.setText(QCoreApplication.translate("leads_profile", u"Ken Antonico", None))
        self.label_32.setText(QCoreApplication.translate("leads_profile", u"Hudson Homenick", None))
        self.label_33.setText(QCoreApplication.translate("leads_profile", u"Programmer", None))
        self.label_36.setText(QCoreApplication.translate("leads_profile", u"antonico@gmail.com", None))
        self.label_37.setText(QCoreApplication.translate("leads_profile", u"09876543211", None))
        self.label_20.setText(QCoreApplication.translate("leads_profile", u"Lead Information", None))
        self.label_19.setText(QCoreApplication.translate("leads_profile", u"Lead Score:", None))
        self.label_22.setText(QCoreApplication.translate("leads_profile", u"Engagement Score:", None))
        self.label_25.setText(QCoreApplication.translate("leads_profile", u"Lead Quality:", None))
        self.label_21.setText(QCoreApplication.translate("leads_profile", u"56", None))
        self.label_24.setText(QCoreApplication.translate("leads_profile", u"1", None))
        self.label_27.setText(QCoreApplication.translate("leads_profile", u"1/10", None))
    # retranslateUi

