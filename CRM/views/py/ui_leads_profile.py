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
        leads_profile.resize(1201, 748)
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
        self.leadprofile_lbl = QLabel(self.frame)
        self.leadprofile_lbl.setObjectName(u"leadprofile_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leadprofile_lbl.sizePolicy().hasHeightForWidth())
        self.leadprofile_lbl.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.leadprofile_lbl.setFont(font)
        self.leadprofile_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none;")

        self.horizontalLayout_17.addWidget(self.leadprofile_lbl)


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
        self.compheader_lbl = QLabel(self.frame)
        self.compheader_lbl.setObjectName(u"compheader_lbl")
        sizePolicy.setHeightForWidth(self.compheader_lbl.sizePolicy().hasHeightForWidth())
        self.compheader_lbl.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.compheader_lbl.setFont(font1)
        self.compheader_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_6.addWidget(self.compheader_lbl)

        self.company_lbl = QLabel(self.frame)
        self.company_lbl.setObjectName(u"company_lbl")
        font2 = QFont()
        font2.setPointSize(11)
        self.company_lbl.setFont(font2)
        self.company_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_6.addWidget(self.company_lbl)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_5)

        self.salespipe_lbl = QLabel(self.frame)
        self.salespipe_lbl.setObjectName(u"salespipe_lbl")
        sizePolicy.setHeightForWidth(self.salespipe_lbl.sizePolicy().hasHeightForWidth())
        self.salespipe_lbl.setSizePolicy(sizePolicy)
        self.salespipe_lbl.setFont(font1)
        self.salespipe_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_3.addWidget(self.salespipe_lbl)

        self.sales_bar = QProgressBar(self.frame)
        self.sales_bar.setObjectName(u"sales_bar")
        self.sales_bar.setStyleSheet(u"QProgressBar {\n"
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
        self.sales_bar.setValue(81)

        self.verticalLayout_3.addWidget(self.sales_bar)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lead_radio = QRadioButton(self.frame)
        self.lead_radio.setObjectName(u"lead_radio")
        self.lead_radio.setFont(font2)
        self.lead_radio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lead_radio.setStyleSheet(u"QRadioButton {\n"
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
        self.lead_radio.setChecked(False)

        self.horizontalLayout_8.addWidget(self.lead_radio, 0, Qt.AlignmentFlag.AlignRight)

        self.prospecting_radio = QRadioButton(self.frame)
        self.prospecting_radio.setObjectName(u"prospecting_radio")
        self.prospecting_radio.setFont(font2)
        self.prospecting_radio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.prospecting_radio.setStyleSheet(u"QRadioButton {\n"
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
        self.prospecting_radio.setChecked(False)

        self.horizontalLayout_8.addWidget(self.prospecting_radio, 0, Qt.AlignmentFlag.AlignRight)

        self.qualifications_radio = QRadioButton(self.frame)
        self.qualifications_radio.setObjectName(u"qualifications_radio")
        self.qualifications_radio.setFont(font2)
        self.qualifications_radio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.qualifications_radio.setStyleSheet(u"QRadioButton {\n"
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
        self.qualifications_radio.setChecked(False)

        self.horizontalLayout_8.addWidget(self.qualifications_radio, 0, Qt.AlignmentFlag.AlignRight)

        self.contacting_radio = QRadioButton(self.frame)
        self.contacting_radio.setObjectName(u"contacting_radio")
        self.contacting_radio.setFont(font2)
        self.contacting_radio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.contacting_radio.setStyleSheet(u"QRadioButton {\n"
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
        self.contacting_radio.setChecked(False)

        self.horizontalLayout_8.addWidget(self.contacting_radio, 0, Qt.AlignmentFlag.AlignRight)

        self.negotiating_radio = QRadioButton(self.frame)
        self.negotiating_radio.setObjectName(u"negotiating_radio")
        self.negotiating_radio.setFont(font2)
        self.negotiating_radio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.negotiating_radio.setStyleSheet(u"QRadioButton {\n"
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
        self.negotiating_radio.setChecked(False)

        self.horizontalLayout_8.addWidget(self.negotiating_radio, 0, Qt.AlignmentFlag.AlignRight)

        self.loss_radio = QRadioButton(self.frame)
        self.loss_radio.setObjectName(u"loss_radio")
        self.loss_radio.setFont(font2)
        self.loss_radio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.loss_radio.setStyleSheet(u"QRadioButton {\n"
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
        self.loss_radio.setCheckable(True)
        self.loss_radio.setChecked(False)

        self.horizontalLayout_8.addWidget(self.loss_radio, 0, Qt.AlignmentFlag.AlignRight)

        self.won_radio = QRadioButton(self.frame)
        self.won_radio.setObjectName(u"won_radio")
        self.won_radio.setFont(font2)
        self.won_radio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.won_radio.setStyleSheet(u"QRadioButton {\n"
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
        self.won_radio.setChecked(False)

        self.horizontalLayout_8.addWidget(self.won_radio)


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
        self.totalleadhead_lbl = QLabel(self.frame_2)
        self.totalleadhead_lbl.setObjectName(u"totalleadhead_lbl")
        sizePolicy.setHeightForWidth(self.totalleadhead_lbl.sizePolicy().hasHeightForWidth())
        self.totalleadhead_lbl.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.totalleadhead_lbl.setFont(font3)
        self.totalleadhead_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.horizontalLayout_5.addWidget(self.totalleadhead_lbl)

        self.lead_combo = QComboBox(self.frame_2)
        self.lead_combo.addItem("")
        self.lead_combo.addItem("")
        self.lead_combo.addItem("")
        self.lead_combo.addItem("")
        self.lead_combo.setObjectName(u"lead_combo")
        self.lead_combo.setStyleSheet(u"QComboBox {\n"
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

        self.horizontalLayout_5.addWidget(self.lead_combo)


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
        self.totalleadmini_lbl = QLabel(self.frame_2)
        self.totalleadmini_lbl.setObjectName(u"totalleadmini_lbl")
        self.totalleadmini_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_10.addWidget(self.totalleadmini_lbl)

        self.leadmini2_lbl = QLabel(self.frame_2)
        self.leadmini2_lbl.setObjectName(u"leadmini2_lbl")
        self.leadmini2_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_10.addWidget(self.leadmini2_lbl)

        self.leadmini1_lbl = QLabel(self.frame_2)
        self.leadmini1_lbl.setObjectName(u"leadmini1_lbl")
        self.leadmini1_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_10.addWidget(self.leadmini1_lbl)


        self.horizontalLayout_2.addLayout(self.verticalLayout_10)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.equal_lbl = QLabel(self.frame_2)
        self.equal_lbl.setObjectName(u"equal_lbl")
        self.equal_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_11.addWidget(self.equal_lbl)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.green50_lbl = QLabel(self.frame_2)
        self.green50_lbl.setObjectName(u"green50_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.green50_lbl.sizePolicy().hasHeightForWidth())
        self.green50_lbl.setSizePolicy(sizePolicy1)
        self.green50_lbl.setStyleSheet(u"background: transparent;\n"
"color: #A3E635;\n"
"border: none")

        self.verticalLayout_24.addWidget(self.green50_lbl)

        self.red50_lbl = QLabel(self.frame_2)
        self.red50_lbl.setObjectName(u"red50_lbl")
        self.red50_lbl.setStyleSheet(u"background: transparent;\n"
"color: #FCA5A5;\n"
"border: none")

        self.verticalLayout_24.addWidget(self.red50_lbl)


        self.horizontalLayout_21.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.up50_lbl = QLabel(self.frame_2)
        self.up50_lbl.setObjectName(u"up50_lbl")
        sizePolicy1.setHeightForWidth(self.up50_lbl.sizePolicy().hasHeightForWidth())
        self.up50_lbl.setSizePolicy(sizePolicy1)
        self.up50_lbl.setStyleSheet(u"border: none;")
        self.up50_lbl.setPixmap(QPixmap(u":/Resources/box_up.png"))

        self.verticalLayout_25.addWidget(self.up50_lbl)

        self.down50_lbl = QLabel(self.frame_2)
        self.down50_lbl.setObjectName(u"down50_lbl")
        self.down50_lbl.setStyleSheet(u"border: none;")
        self.down50_lbl.setPixmap(QPixmap(u":/Resources/box_down.png"))

        self.verticalLayout_25.addWidget(self.down50_lbl)


        self.horizontalLayout_21.addLayout(self.verticalLayout_25)


        self.verticalLayout_11.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_3.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.total_leads_qty_lbl = QLabel(self.frame_2)
        self.total_leads_qty_lbl.setObjectName(u"total_leads_qty_lbl")
        self.total_leads_qty_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_12.addWidget(self.total_leads_qty_lbl)

        self.leads_50_up_lbl = QLabel(self.frame_2)
        self.leads_50_up_lbl.setObjectName(u"leads_50_up_lbl")
        self.leads_50_up_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_12.addWidget(self.leads_50_up_lbl)

        self.leads_50_down_lbl = QLabel(self.frame_2)
        self.leads_50_down_lbl.setObjectName(u"leads_50_down_lbl")
        self.leads_50_down_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_12.addWidget(self.leads_50_down_lbl)


        self.horizontalLayout_3.addLayout(self.verticalLayout_12)


        self.verticalLayout_13.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_13)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.lead_list_table = QTableWidget(self.frame)
        if (self.lead_list_table.columnCount() < 1):
            self.lead_list_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.lead_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.lead_list_table.setObjectName(u"lead_list_table")
        self.lead_list_table.setStyleSheet(u"QTableWidget {\n"
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

        self.verticalLayout_7.addWidget(self.lead_list_table)


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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 406, 332))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.campaignhead_lbl = QLabel(self.scrollAreaWidgetContents)
        self.campaignhead_lbl.setObjectName(u"campaignhead_lbl")
        sizePolicy.setHeightForWidth(self.campaignhead_lbl.sizePolicy().hasHeightForWidth())
        self.campaignhead_lbl.setSizePolicy(sizePolicy)
        self.campaignhead_lbl.setFont(font1)
        self.campaignhead_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.horizontalLayout_13.addWidget(self.campaignhead_lbl)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_13)

        self.promote_to_prospect_btn = QPushButton(self.scrollAreaWidgetContents)
        self.promote_to_prospect_btn.setObjectName(u"promote_to_prospect_btn")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(True)
        font4.setItalic(False)
        self.promote_to_prospect_btn.setFont(font4)
        self.promote_to_prospect_btn.setStyleSheet(u"QPushButton {\n"
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
        self.promote_to_prospect_btn.setIcon(icon)
        self.promote_to_prospect_btn.setIconSize(QSize(30, 30))
        self.promote_to_prospect_btn.setFlat(True)

        self.horizontalLayout_19.addWidget(self.promote_to_prospect_btn)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_19)


        self.verticalLayout_21.addLayout(self.horizontalLayout_20)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_21.addWidget(self.line_4)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.timeline_frame = QFrame(self.scrollAreaWidgetContents)
        self.timeline_frame.setObjectName(u"timeline_frame")
        self.timeline_frame.setStyleSheet(u"border-radius: 10px;")
        self.timeline_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.timeline_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.timeline_frame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.timeline_lbl = QLabel(self.timeline_frame)
        self.timeline_lbl.setObjectName(u"timeline_lbl")
        self.timeline_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.horizontalLayout_15.addWidget(self.timeline_lbl)


        self.horizontalLayout_14.addWidget(self.timeline_frame)


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
        self.contactinfohead_lbl = QLabel(self.frame_4)
        self.contactinfohead_lbl.setObjectName(u"contactinfohead_lbl")
        sizePolicy.setHeightForWidth(self.contactinfohead_lbl.sizePolicy().hasHeightForWidth())
        self.contactinfohead_lbl.setSizePolicy(sizePolicy)
        self.contactinfohead_lbl.setFont(font3)
        self.contactinfohead_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")
        self.contactinfohead_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.contactinfohead_lbl)


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
        self.accname_lbl = QLabel(self.frame_4)
        self.accname_lbl.setObjectName(u"accname_lbl")
        self.accname_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_18.addWidget(self.accname_lbl)

        self.compname_lbl = QLabel(self.frame_4)
        self.compname_lbl.setObjectName(u"compname_lbl")
        self.compname_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_18.addWidget(self.compname_lbl)

        self.comprole_lbl = QLabel(self.frame_4)
        self.comprole_lbl.setObjectName(u"comprole_lbl")
        self.comprole_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_18.addWidget(self.comprole_lbl)

        self.emailadd_lbl = QLabel(self.frame_4)
        self.emailadd_lbl.setObjectName(u"emailadd_lbl")
        self.emailadd_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_18.addWidget(self.emailadd_lbl)

        self.contnum_lbl = QLabel(self.frame_4)
        self.contnum_lbl.setObjectName(u"contnum_lbl")
        self.contnum_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_18.addWidget(self.contnum_lbl)


        self.horizontalLayout_12.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.name_lbl = QLabel(self.frame_4)
        self.name_lbl.setObjectName(u"name_lbl")
        self.name_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_19.addWidget(self.name_lbl)

        self.company_lbl_2 = QLabel(self.frame_4)
        self.company_lbl_2.setObjectName(u"company_lbl_2")
        self.company_lbl_2.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_19.addWidget(self.company_lbl_2)

        self.job_title_lbl = QLabel(self.frame_4)
        self.job_title_lbl.setObjectName(u"job_title_lbl")
        self.job_title_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_19.addWidget(self.job_title_lbl)

        self.email_lbl = QLabel(self.frame_4)
        self.email_lbl.setObjectName(u"email_lbl")
        self.email_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_19.addWidget(self.email_lbl)

        self.number_lbl = QLabel(self.frame_4)
        self.number_lbl.setObjectName(u"number_lbl")
        self.number_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_19.addWidget(self.number_lbl)


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
        self.leadinfohead_lbl = QLabel(self.frame_3)
        self.leadinfohead_lbl.setObjectName(u"leadinfohead_lbl")
        sizePolicy.setHeightForWidth(self.leadinfohead_lbl.sizePolicy().hasHeightForWidth())
        self.leadinfohead_lbl.setSizePolicy(sizePolicy)
        self.leadinfohead_lbl.setFont(font3)
        self.leadinfohead_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")
        self.leadinfohead_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.leadinfohead_lbl)


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
        self.leadscore_lbl = QLabel(self.frame_3)
        self.leadscore_lbl.setObjectName(u"leadscore_lbl")
        self.leadscore_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_14.addWidget(self.leadscore_lbl)

        self.engagement_lbl = QLabel(self.frame_3)
        self.engagement_lbl.setObjectName(u"engagement_lbl")
        self.engagement_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_14.addWidget(self.engagement_lbl)

        self.leadquality_lbl = QLabel(self.frame_3)
        self.leadquality_lbl.setObjectName(u"leadquality_lbl")
        self.leadquality_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_14.addWidget(self.leadquality_lbl)


        self.horizontalLayout_4.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.score_value_lbl = QLabel(self.frame_3)
        self.score_value_lbl.setObjectName(u"score_value_lbl")
        self.score_value_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_15.addWidget(self.score_value_lbl)

        self.engagement_value_lbl = QLabel(self.frame_3)
        self.engagement_value_lbl.setObjectName(u"engagement_value_lbl")
        self.engagement_value_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_15.addWidget(self.engagement_value_lbl)

        self.quality_lbl = QLabel(self.frame_3)
        self.quality_lbl.setObjectName(u"quality_lbl")
        self.quality_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_15.addWidget(self.quality_lbl)


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
        self.leadprofile_lbl.setText(QCoreApplication.translate("leads_profile", u"Lead Profile", None))
        self.label_14.setText("")
        self.compheader_lbl.setText(QCoreApplication.translate("leads_profile", u"Company Name:", None))
        self.company_lbl.setText(QCoreApplication.translate("leads_profile", u"Hudson - Homenick", None))
        self.salespipe_lbl.setText(QCoreApplication.translate("leads_profile", u"Sales Pipeline", None))
        self.sales_bar.setFormat("")
        self.lead_radio.setText(QCoreApplication.translate("leads_profile", u"Lead", None))
        self.prospecting_radio.setText(QCoreApplication.translate("leads_profile", u"Prospecting", None))
        self.qualifications_radio.setText(QCoreApplication.translate("leads_profile", u"Qualifications", None))
        self.contacting_radio.setText(QCoreApplication.translate("leads_profile", u"Contacting", None))
        self.negotiating_radio.setText(QCoreApplication.translate("leads_profile", u"Negotiating", None))
        self.loss_radio.setText(QCoreApplication.translate("leads_profile", u"Closed Loss", None))
        self.won_radio.setText(QCoreApplication.translate("leads_profile", u"Closed Won", None))
        self.totalleadhead_lbl.setText(QCoreApplication.translate("leads_profile", u"Total Lead", None))
        self.lead_combo.setItemText(0, QCoreApplication.translate("leads_profile", u"View All", None))
        self.lead_combo.setItemText(1, QCoreApplication.translate("leads_profile", u"Last Week", None))
        self.lead_combo.setItemText(2, QCoreApplication.translate("leads_profile", u"Last Month", None))
        self.lead_combo.setItemText(3, QCoreApplication.translate("leads_profile", u"New Year", None))

        self.lead_combo.setPlaceholderText(QCoreApplication.translate("leads_profile", u"view all", None))
        self.totalleadmini_lbl.setText(QCoreApplication.translate("leads_profile", u"Total Leads", None))
        self.leadmini2_lbl.setText(QCoreApplication.translate("leads_profile", u"Leads", None))
        self.leadmini1_lbl.setText(QCoreApplication.translate("leads_profile", u"Leads ", None))
        self.equal_lbl.setText(QCoreApplication.translate("leads_profile", u"=", None))
        self.green50_lbl.setText(QCoreApplication.translate("leads_profile", u"50", None))
        self.red50_lbl.setText(QCoreApplication.translate("leads_profile", u"50", None))
        self.up50_lbl.setText("")
        self.down50_lbl.setText("")
        self.total_leads_qty_lbl.setText(QCoreApplication.translate("leads_profile", u"100", None))
        self.leads_50_up_lbl.setText(QCoreApplication.translate("leads_profile", u"100", None))
        self.leads_50_down_lbl.setText(QCoreApplication.translate("leads_profile", u"100", None))
        ___qtablewidgetitem = self.lead_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("leads_profile", u"Lead List", None));
        self.campaignhead_lbl.setText(QCoreApplication.translate("leads_profile", u"Campaign Timeline", None))
        self.promote_to_prospect_btn.setText(QCoreApplication.translate("leads_profile", u"Promote to Prospect", None))
        self.timeline_lbl.setText(QCoreApplication.translate("leads_profile", u"Hudson - Homenick Has been promoted to Prospect!.", None))
        self.contactinfohead_lbl.setText(QCoreApplication.translate("leads_profile", u"Contact Information", None))
        self.accname_lbl.setText(QCoreApplication.translate("leads_profile", u"Account Name:", None))
        self.compname_lbl.setText(QCoreApplication.translate("leads_profile", u"Company Name:", None))
        self.comprole_lbl.setText(QCoreApplication.translate("leads_profile", u"Company Role:", None))
        self.emailadd_lbl.setText(QCoreApplication.translate("leads_profile", u"Email:", None))
        self.contnum_lbl.setText(QCoreApplication.translate("leads_profile", u"Contact Number:", None))
        self.name_lbl.setText(QCoreApplication.translate("leads_profile", u"Ken Antonico", None))
        self.company_lbl_2.setText(QCoreApplication.translate("leads_profile", u"Hudson Homenick", None))
        self.job_title_lbl.setText(QCoreApplication.translate("leads_profile", u"Programmer", None))
        self.email_lbl.setText(QCoreApplication.translate("leads_profile", u"antonico@gmail.com", None))
        self.number_lbl.setText(QCoreApplication.translate("leads_profile", u"09876543211", None))
        self.leadinfohead_lbl.setText(QCoreApplication.translate("leads_profile", u"Lead Information", None))
        self.leadscore_lbl.setText(QCoreApplication.translate("leads_profile", u"Lead Score:", None))
        self.engagement_lbl.setText(QCoreApplication.translate("leads_profile", u"Engagement Score:", None))
        self.leadquality_lbl.setText(QCoreApplication.translate("leads_profile", u"Lead Quality:", None))
        self.score_value_lbl.setText(QCoreApplication.translate("leads_profile", u"56", None))
        self.engagement_value_lbl.setText(QCoreApplication.translate("leads_profile", u"1", None))
        self.quality_lbl.setText(QCoreApplication.translate("leads_profile", u"1/10", None))
    # retranslateUi

