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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QProgressBar,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import views.py.icons_rc

class Ui_leads_profile(object):
    def setupUi(self, leads_profile):
        if not leads_profile.objectName():
            leads_profile.setObjectName(u"leads_profile")
        leads_profile.resize(1101, 975)
        leads_profile.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
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

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_6)

        self.back_btn = QPushButton(self.frame)
        self.back_btn.setObjectName(u"back_btn")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.back_btn.setFont(font1)
        self.back_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.back_btn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_17.addWidget(self.back_btn)


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
        self.name_lbl_2 = QLabel(self.frame)
        self.name_lbl_2.setObjectName(u"name_lbl_2")
        sizePolicy.setHeightForWidth(self.name_lbl_2.sizePolicy().hasHeightForWidth())
        self.name_lbl_2.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.name_lbl_2.setFont(font2)
        self.name_lbl_2.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_6.addWidget(self.name_lbl_2)

        self.company_lbl = QLabel(self.frame)
        self.company_lbl.setObjectName(u"company_lbl")
        font3 = QFont()
        font3.setPointSize(11)
        self.company_lbl.setFont(font3)
        self.company_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_6.addWidget(self.company_lbl)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_5)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"border: 2px solid #737373;\n"
"background-color: #171717;\n"
"border-radius: 10px;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_6)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.salespipe_lbl = QLabel(self.frame_6)
        self.salespipe_lbl.setObjectName(u"salespipe_lbl")
        sizePolicy.setHeightForWidth(self.salespipe_lbl.sizePolicy().hasHeightForWidth())
        self.salespipe_lbl.setSizePolicy(sizePolicy)
        self.salespipe_lbl.setFont(font2)
        self.salespipe_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_29.addWidget(self.salespipe_lbl)

        self.opportunity_status_bar = QProgressBar(self.frame_6)
        self.opportunity_status_bar.setObjectName(u"opportunity_status_bar")
        self.opportunity_status_bar.setStyleSheet(u"                QProgressBar {\n"
"                    background-color: #E5E5E5;\n"
"                    border: 1px solid #000;\n"
"                    border-radius: 10px;\n"
"                    text-align: center;\n"
"                    height: 20px;\n"
"                }\n"
"                QProgressBar::chunk {\n"
"                    background-color: #A3E635;\n"
"                    border-radius: 10px;\n"
"                }\n"
"\n"
"		                QRadioButton {\n"
"                    background: transparent;\n"
"                    color: #fff;\n"
"                    border: none;\n"
"                }\n"
"\n"
"                QRadioButton::indicator {\n"
"                    width: 16px;\n"
"                    height: 16px;\n"
"                    border-radius: 8px;\n"
"                    background-color: white;\n"
"                }\n"
"\n"
"                QRadioButton::indicator:checked {\n"
"                    background-color: #A3E635;\n"
"                    border-color: #A3E635;\n"
""
                        "                }")
        self.opportunity_status_bar.setValue(0)

        self.verticalLayout_29.addWidget(self.opportunity_status_bar)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.prospecting_radio = QRadioButton(self.frame_6)
        self.prospecting_radio.setObjectName(u"prospecting_radio")
        self.prospecting_radio.setEnabled(False)
        self.prospecting_radio.setFont(font3)
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
        self.prospecting_radio.setCheckable(True)
        self.prospecting_radio.setChecked(False)
        self.prospecting_radio.setAutoExclusive(False)

        self.horizontalLayout_8.addWidget(self.prospecting_radio, 0, Qt.AlignmentFlag.AlignRight)

        self.qualification_radio = QRadioButton(self.frame_6)
        self.qualification_radio.setObjectName(u"qualification_radio")
        self.qualification_radio.setEnabled(True)
        self.qualification_radio.setFont(font3)
        self.qualification_radio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.qualification_radio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.qualification_radio.setStyleSheet(u"QRadioButton {\n"
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
        self.qualification_radio.setCheckable(True)
        self.qualification_radio.setChecked(False)
        self.qualification_radio.setAutoExclusive(False)

        self.horizontalLayout_8.addWidget(self.qualification_radio, 0, Qt.AlignmentFlag.AlignRight)

        self.negotiating_radio = QRadioButton(self.frame_6)
        self.negotiating_radio.setObjectName(u"negotiating_radio")
        self.negotiating_radio.setEnabled(True)
        self.negotiating_radio.setFont(font3)
        self.negotiating_radio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.negotiating_radio.setCheckable(True)
        self.negotiating_radio.setChecked(False)
        self.negotiating_radio.setAutoExclusive(False)

        self.horizontalLayout_8.addWidget(self.negotiating_radio, 0, Qt.AlignmentFlag.AlignRight)

        self.approval_radio = QRadioButton(self.frame_6)
        self.approval_radio.setObjectName(u"approval_radio")
        self.approval_radio.setEnabled(True)
        self.approval_radio.setFont(font3)
        self.approval_radio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.approval_radio.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.approval_radio.setStyleSheet(u"QRadioButton {\n"
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
        self.approval_radio.setCheckable(True)
        self.approval_radio.setChecked(False)
        self.approval_radio.setAutoExclusive(False)

        self.horizontalLayout_8.addWidget(self.approval_radio, 0, Qt.AlignmentFlag.AlignRight)

        self.loss_radio = QRadioButton(self.frame_6)
        self.loss_radio.setObjectName(u"loss_radio")
        self.loss_radio.setEnabled(False)
        self.loss_radio.setFont(font3)
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
        self.loss_radio.setAutoExclusive(False)

        self.horizontalLayout_8.addWidget(self.loss_radio, 0, Qt.AlignmentFlag.AlignRight)

        self.won_radio = QRadioButton(self.frame_6)
        self.won_radio.setObjectName(u"won_radio")
        self.won_radio.setEnabled(False)
        self.won_radio.setFont(font3)
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
        self.won_radio.setAutoExclusive(False)

        self.horizontalLayout_8.addWidget(self.won_radio, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_29.addLayout(self.horizontalLayout_8)


        self.verticalLayout_28.addWidget(self.frame_6)


        self.verticalLayout_3.addLayout(self.verticalLayout_28)

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
        self.frame_2.setStyleSheet(u"border: 2px solid #737373;\n"
"background-color: #171717;\n"
"border-radius: 10px;")
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
        self.totalleadhead_lbl.setFont(font2)
        self.totalleadhead_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.horizontalLayout_5.addWidget(self.totalleadhead_lbl)

        self.add_btn = QPushButton(self.frame_2)
        self.add_btn.setObjectName(u"add_btn")
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        self.add_btn.setFont(font4)
        self.add_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"    color: #22C55E;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"	padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #393939;\n"
"    color: #22C55E;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #262626;\n"
"    color: #22C55E;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/Resources/plus (1).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_btn.setIcon(icon)
        self.add_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.add_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.linelead = QFrame(self.frame_2)
        self.linelead.setObjectName(u"linelead")
        self.linelead.setStyleSheet(u"\n"
"    background-color: white;\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"    border: none;\n"
"")
        self.linelead.setFrameShadow(QFrame.Shadow.Sunken)
        self.linelead.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_5.addWidget(self.linelead)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.opportunities_tbl = QTableWidget(self.frame_2)
        self.opportunities_tbl.setObjectName(u"opportunities_tbl")
        self.opportunities_tbl.setStyleSheet(u"QTableWidget {\n"
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
        self.opportunities_tbl.horizontalHeader().setVisible(False)

        self.horizontalLayout_3.addWidget(self.opportunities_tbl)


        self.verticalLayout_13.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_13)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.horizontalSpacer_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border: 2px solid #737373;\n"
"background-color: #171717;\n"
"border-radius: 10px;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.leadinfohead_lbl_3 = QLabel(self.frame_5)
        self.leadinfohead_lbl_3.setObjectName(u"leadinfohead_lbl_3")
        sizePolicy.setHeightForWidth(self.leadinfohead_lbl_3.sizePolicy().hasHeightForWidth())
        self.leadinfohead_lbl_3.setSizePolicy(sizePolicy)
        self.leadinfohead_lbl_3.setFont(font2)
        self.leadinfohead_lbl_3.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")
        self.leadinfohead_lbl_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_18.addWidget(self.leadinfohead_lbl_3)


        self.verticalLayout_12.addLayout(self.horizontalLayout_18)

        self.line_6 = QFrame(self.frame_5)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"\n"
"    background-color: white;\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"    border: none;\n"
"")
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_6.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_12.addWidget(self.line_6)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.pending_btn = QPushButton(self.frame_5)
        self.pending_btn.setObjectName(u"pending_btn")
        self.pending_btn.setEnabled(False)
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(False)
        self.pending_btn.setFont(font5)
        self.pending_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pending_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"	padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #393939;\n"
"    color: #FFF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #262626;\n"
"    color: #FFF;\n"
"}")

        self.verticalLayout_26.addWidget(self.pending_btn)

        self.won_btn = QPushButton(self.frame_5)
        self.won_btn.setObjectName(u"won_btn")
        self.won_btn.setFont(font5)
        self.won_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.won_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"    color: #22C55E;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"	padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #393939;\n"
"    color: #22C55E;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #262626;\n"
"    color: #22C55E;\n"
"}")

        self.verticalLayout_26.addWidget(self.won_btn)

        self.loss_btn = QPushButton(self.frame_5)
        self.loss_btn.setObjectName(u"loss_btn")
        self.loss_btn.setFont(font5)
        self.loss_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.loss_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"    color: #E11D48;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"	padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #393939;\n"
"    color: #E11D48;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #262626;\n"
"    color: #E11D48;\n"
"}")

        self.verticalLayout_26.addWidget(self.loss_btn)


        self.horizontalLayout_21.addLayout(self.verticalLayout_26)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.pending_lbl = QLabel(self.frame_5)
        self.pending_lbl.setObjectName(u"pending_lbl")
        sizePolicy.setHeightForWidth(self.pending_lbl.sizePolicy().hasHeightForWidth())
        self.pending_lbl.setSizePolicy(sizePolicy)
        self.pending_lbl.setFont(font2)
        self.pending_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")
        self.pending_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.pending_lbl)

        self.won_lbl = QLabel(self.frame_5)
        self.won_lbl.setObjectName(u"won_lbl")
        sizePolicy.setHeightForWidth(self.won_lbl.sizePolicy().hasHeightForWidth())
        self.won_lbl.setSizePolicy(sizePolicy)
        self.won_lbl.setFont(font2)
        self.won_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")
        self.won_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.won_lbl)

        self.loss_lbl = QLabel(self.frame_5)
        self.loss_lbl.setObjectName(u"loss_lbl")
        sizePolicy.setHeightForWidth(self.loss_lbl.sizePolicy().hasHeightForWidth())
        self.loss_lbl.setSizePolicy(sizePolicy)
        self.loss_lbl.setFont(font2)
        self.loss_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")
        self.loss_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.loss_lbl)


        self.horizontalLayout_21.addLayout(self.verticalLayout_27)


        self.verticalLayout_12.addLayout(self.horizontalLayout_21)


        self.verticalLayout_11.addWidget(self.frame_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_11)


        self.verticalLayout_4.addLayout(self.verticalLayout_7)


        self.horizontalLayout_16.addLayout(self.verticalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_16.addItem(self.verticalSpacer_3)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 356, 486))
        self.scrollAreaWidgetContents.setStyleSheet(u"border: 2px solid #737373;\n"
"background-color: #171717;\n"
"border-radius: 10px;")
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.campaignhead_lbl = QLabel(self.scrollAreaWidgetContents)
        self.campaignhead_lbl.setObjectName(u"campaignhead_lbl")
        sizePolicy.setHeightForWidth(self.campaignhead_lbl.sizePolicy().hasHeightForWidth())
        self.campaignhead_lbl.setSizePolicy(sizePolicy)
        self.campaignhead_lbl.setFont(font2)
        self.campaignhead_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")
        self.campaignhead_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.campaignhead_lbl)

        self.opportunity_name = QLabel(self.scrollAreaWidgetContents)
        self.opportunity_name.setObjectName(u"opportunity_name")
        self.opportunity_name.setFont(font3)
        self.opportunity_name.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")
        self.opportunity_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.opportunity_name)


        self.horizontalLayout_19.addLayout(self.verticalLayout)


        self.verticalLayout_21.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.add_campaign_btn = QPushButton(self.scrollAreaWidgetContents)
        self.add_campaign_btn.setObjectName(u"add_campaign_btn")
        font6 = QFont()
        font6.setBold(True)
        self.add_campaign_btn.setFont(font6)
        self.add_campaign_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"    color: #22C55E;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"	padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #393939;\n"
"    color: #22C55E;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #262626;\n"
"    color: #22C55E;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Resources/add_campaign.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_campaign_btn.setIcon(icon1)
        self.add_campaign_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_13.addWidget(self.add_campaign_btn)

        self.edit_campaign_btn = QPushButton(self.scrollAreaWidgetContents)
        self.edit_campaign_btn.setObjectName(u"edit_campaign_btn")
        self.edit_campaign_btn.setFont(font6)
        self.edit_campaign_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"	color: rgb(239, 207, 27);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"	padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #393939;\n"
"	color: rgb(239, 207, 27);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #262626;\n"
"	color: rgb(239, 207, 27);\n"
"}")
        self.edit_campaign_btn.setIcon(icon1)
        self.edit_campaign_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_13.addWidget(self.edit_campaign_btn)

        self.delete_campaign_btn = QPushButton(self.scrollAreaWidgetContents)
        self.delete_campaign_btn.setObjectName(u"delete_campaign_btn")
        self.delete_campaign_btn.setFont(font6)
        self.delete_campaign_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"	color: rgb(255, 93, 78);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"	padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #393939;\n"
"    color: #E11D48;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #262626;\n"
"    color: #E11D48;\n"
"}\n"
"")
        self.delete_campaign_btn.setIcon(icon1)
        self.delete_campaign_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_13.addWidget(self.delete_campaign_btn)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_24.addLayout(self.horizontalLayout_25)


        self.verticalLayout_21.addLayout(self.horizontalLayout_24)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"\n"
"    background-color: white;\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"    border: none;\n"
"")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_21.addWidget(self.line_4)

        self.campaign_tbl = QTableWidget(self.scrollAreaWidgetContents)
        self.campaign_tbl.setObjectName(u"campaign_tbl")
        self.campaign_tbl.setStyleSheet(u"QTableWidget {\n"
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
        self.campaign_tbl.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)

        self.verticalLayout_21.addWidget(self.campaign_tbl)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.verticalLayout_21.addLayout(self.horizontalLayout_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_20.addWidget(self.scrollArea)


        self.horizontalLayout_16.addLayout(self.verticalLayout_20)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_16.addItem(self.verticalSpacer_4)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: 2px solid #737373;\n"
"background-color: #171717;\n"
"border-radius: 10px;")
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
        self.leadinfohead_lbl.setFont(font2)
        self.leadinfohead_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")
        self.leadinfohead_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.leadinfohead_lbl)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"\n"
"    background-color: white;\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"    border: none;\n"
"")
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_9.addWidget(self.line_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.accname_lbl = QLabel(self.frame_3)
        self.accname_lbl.setObjectName(u"accname_lbl")
        self.accname_lbl.setFont(font3)
        self.accname_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_14.addWidget(self.accname_lbl)

        self.emailadd_lbl = QLabel(self.frame_3)
        self.emailadd_lbl.setObjectName(u"emailadd_lbl")
        self.emailadd_lbl.setFont(font3)
        self.emailadd_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_14.addWidget(self.emailadd_lbl)

        self.leadsource_lbl = QLabel(self.frame_3)
        self.leadsource_lbl.setObjectName(u"leadsource_lbl")
        self.leadsource_lbl.setFont(font3)
        self.leadsource_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_14.addWidget(self.leadsource_lbl)

        self.leadscore_lbl = QLabel(self.frame_3)
        self.leadscore_lbl.setObjectName(u"leadscore_lbl")
        self.leadscore_lbl.setFont(font3)
        self.leadscore_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_14.addWidget(self.leadscore_lbl)

        self.leadquality_lbl = QLabel(self.frame_3)
        self.leadquality_lbl.setObjectName(u"leadquality_lbl")
        self.leadquality_lbl.setFont(font3)
        self.leadquality_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_14.addWidget(self.leadquality_lbl)


        self.horizontalLayout_4.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.name_lbl = QLabel(self.frame_3)
        self.name_lbl.setObjectName(u"name_lbl")
        self.name_lbl.setFont(font3)
        self.name_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_15.addWidget(self.name_lbl)

        self.email_lbl = QLabel(self.frame_3)
        self.email_lbl.setObjectName(u"email_lbl")
        self.email_lbl.setFont(font3)
        self.email_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_15.addWidget(self.email_lbl)

        self.lead_source_value_lbl = QLabel(self.frame_3)
        self.lead_source_value_lbl.setObjectName(u"lead_source_value_lbl")
        self.lead_source_value_lbl.setFont(font3)
        self.lead_source_value_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_15.addWidget(self.lead_source_value_lbl)

        self.score_value_lbl = QLabel(self.frame_3)
        self.score_value_lbl.setObjectName(u"score_value_lbl")
        self.score_value_lbl.setFont(font3)
        self.score_value_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_15.addWidget(self.score_value_lbl)

        self.quality_value_lbl = QLabel(self.frame_3)
        self.quality_value_lbl.setObjectName(u"quality_value_lbl")
        self.quality_value_lbl.setFont(font3)
        self.quality_value_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_15.addWidget(self.quality_value_lbl)


        self.horizontalLayout_4.addLayout(self.verticalLayout_15)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addWidget(self.frame_3)


        self.verticalLayout_22.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_22.addItem(self.horizontalSpacer_11)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border: 2px solid #737373;\n"
"background-color: #171717;\n"
"border-radius: 10px;")
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
        self.contactinfohead_lbl.setFont(font2)
        self.contactinfohead_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")
        self.contactinfohead_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.contactinfohead_lbl)

        self.edit_btn = QPushButton(self.frame_4)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setFont(font6)
        self.edit_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.edit_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"	color: rgb(239, 207, 27);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"	padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #393939;\n"
"	color: rgb(239, 207, 27);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #262626;\n"
"	color: rgb(239, 207, 27);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Resources/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.edit_btn.setIcon(icon2)
        self.edit_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.edit_btn)

        self.delete_btn = QPushButton(self.frame_4)
        self.delete_btn.setObjectName(u"delete_btn")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setBold(True)
        font7.setItalic(False)
        self.delete_btn.setFont(font7)
        self.delete_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"	color: rgb(255, 93, 78);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"	padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #393939;\n"
"    color: #E11D48;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #262626;\n"
"    color: #E11D48;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/Resources/delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_btn.setIcon(icon3)
        self.delete_btn.setIconSize(QSize(25, 25))
        self.delete_btn.setFlat(True)

        self.horizontalLayout_11.addWidget(self.delete_btn)


        self.verticalLayout_17.addLayout(self.horizontalLayout_11)

        self.line_3 = QFrame(self.frame_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"\n"
"    background-color: white;\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"    border: none;\n"
"")
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_17.addWidget(self.line_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.compname_lbl = QLabel(self.frame_4)
        self.compname_lbl.setObjectName(u"compname_lbl")
        self.compname_lbl.setFont(font3)
        self.compname_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_18.addWidget(self.compname_lbl)

        self.opp_cost_lbl = QLabel(self.frame_4)
        self.opp_cost_lbl.setObjectName(u"opp_cost_lbl")
        self.opp_cost_lbl.setFont(font3)
        self.opp_cost_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_18.addWidget(self.opp_cost_lbl)

        self.comprole_lbl = QLabel(self.frame_4)
        self.comprole_lbl.setObjectName(u"comprole_lbl")
        self.comprole_lbl.setFont(font3)
        self.comprole_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_18.addWidget(self.comprole_lbl)

        self.contnum_lbl = QLabel(self.frame_4)
        self.contnum_lbl.setObjectName(u"contnum_lbl")
        self.contnum_lbl.setFont(font3)
        self.contnum_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_18.addWidget(self.contnum_lbl)


        self.horizontalLayout_12.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.opportunity_title_lbl = QLabel(self.frame_4)
        self.opportunity_title_lbl.setObjectName(u"opportunity_title_lbl")
        self.opportunity_title_lbl.setFont(font3)
        self.opportunity_title_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_19.addWidget(self.opportunity_title_lbl)

        self.opportunity_cost_lbl = QLabel(self.frame_4)
        self.opportunity_cost_lbl.setObjectName(u"opportunity_cost_lbl")
        self.opportunity_cost_lbl.setFont(font3)
        self.opportunity_cost_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_19.addWidget(self.opportunity_cost_lbl)

        self.opportunity_date_lbl = QLabel(self.frame_4)
        self.opportunity_date_lbl.setObjectName(u"opportunity_date_lbl")
        self.opportunity_date_lbl.setFont(font3)
        self.opportunity_date_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_19.addWidget(self.opportunity_date_lbl)

        self.opportunity_details_lbl = QLabel(self.frame_4)
        self.opportunity_details_lbl.setObjectName(u"opportunity_details_lbl")
        self.opportunity_details_lbl.setFont(font3)
        self.opportunity_details_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_19.addWidget(self.opportunity_details_lbl)


        self.horizontalLayout_12.addLayout(self.verticalLayout_19)


        self.verticalLayout_17.addLayout(self.horizontalLayout_12)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.full_info_lbl = QLabel(self.frame_4)
        self.full_info_lbl.setObjectName(u"full_info_lbl")
        self.full_info_lbl.setFont(font3)
        self.full_info_lbl.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.full_info_lbl.setStyleSheet(u"background: transparent;\n"
"color: #16D4FF;\n"
"border: none")

        self.horizontalLayout.addWidget(self.full_info_lbl)


        self.verticalLayout_17.addLayout(self.horizontalLayout)


        self.verticalLayout_16.addWidget(self.frame_4)


        self.verticalLayout_22.addLayout(self.verticalLayout_16)


        self.horizontalLayout_16.addLayout(self.verticalLayout_22)


        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)


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
        self.back_btn.setText(QCoreApplication.translate("leads_profile", u"Back", None))
        self.label_14.setText("")
        self.name_lbl_2.setText(QCoreApplication.translate("leads_profile", u"Name:", None))
        self.company_lbl.setText(QCoreApplication.translate("leads_profile", u"Company Name", None))
        self.salespipe_lbl.setText(QCoreApplication.translate("leads_profile", u"Sales Pipeline", None))
        self.opportunity_status_bar.setFormat("")
        self.prospecting_radio.setText(QCoreApplication.translate("leads_profile", u"Prospecting", None))
        self.qualification_radio.setText(QCoreApplication.translate("leads_profile", u"Qualification", None))
        self.negotiating_radio.setText(QCoreApplication.translate("leads_profile", u"Negotiating", None))
        self.approval_radio.setText(QCoreApplication.translate("leads_profile", u"Approval", None))
        self.loss_radio.setText(QCoreApplication.translate("leads_profile", u"Closed Loss", None))
        self.won_radio.setText(QCoreApplication.translate("leads_profile", u"Closed Won", None))
        self.totalleadhead_lbl.setText(QCoreApplication.translate("leads_profile", u"Opportunities", None))
#if QT_CONFIG(tooltip)
        self.add_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.add_btn.setText(QCoreApplication.translate("leads_profile", u"Add", None))
        self.leadinfohead_lbl_3.setText(QCoreApplication.translate("leads_profile", u"All Opportunities Cost", None))
#if QT_CONFIG(tooltip)
        self.pending_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pending_btn.setText(QCoreApplication.translate("leads_profile", u"Pending", None))
#if QT_CONFIG(tooltip)
        self.won_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.won_btn.setText(QCoreApplication.translate("leads_profile", u"Won", None))
#if QT_CONFIG(tooltip)
        self.loss_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.loss_btn.setText(QCoreApplication.translate("leads_profile", u"Loss", None))
        self.pending_lbl.setText(QCoreApplication.translate("leads_profile", u"-", None))
        self.won_lbl.setText(QCoreApplication.translate("leads_profile", u"-", None))
        self.loss_lbl.setText(QCoreApplication.translate("leads_profile", u"-", None))
        self.campaignhead_lbl.setText(QCoreApplication.translate("leads_profile", u"Campaign Timeline", None))
        self.opportunity_name.setText(QCoreApplication.translate("leads_profile", u"Opportunity Name", None))
#if QT_CONFIG(tooltip)
        self.add_campaign_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.add_campaign_btn.setText(QCoreApplication.translate("leads_profile", u"Add", None))
#if QT_CONFIG(tooltip)
        self.edit_campaign_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.edit_campaign_btn.setText(QCoreApplication.translate("leads_profile", u"Edit", None))
#if QT_CONFIG(tooltip)
        self.delete_campaign_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.delete_campaign_btn.setText(QCoreApplication.translate("leads_profile", u"Delete", None))
        self.leadinfohead_lbl.setText(QCoreApplication.translate("leads_profile", u"Lead Information", None))
        self.accname_lbl.setText(QCoreApplication.translate("leads_profile", u"Name:", None))
        self.emailadd_lbl.setText(QCoreApplication.translate("leads_profile", u"Email:", None))
        self.leadsource_lbl.setText(QCoreApplication.translate("leads_profile", u"Lead Source:", None))
        self.leadscore_lbl.setText(QCoreApplication.translate("leads_profile", u"Lead Score:", None))
        self.leadquality_lbl.setText(QCoreApplication.translate("leads_profile", u"Lead Quality:", None))
        self.name_lbl.setText(QCoreApplication.translate("leads_profile", u"N/A", None))
        self.email_lbl.setText(QCoreApplication.translate("leads_profile", u"N/A", None))
        self.lead_source_value_lbl.setText(QCoreApplication.translate("leads_profile", u"N/A", None))
        self.score_value_lbl.setText(QCoreApplication.translate("leads_profile", u"N/A", None))
        self.quality_value_lbl.setText(QCoreApplication.translate("leads_profile", u"N/A", None))
        self.contactinfohead_lbl.setText(QCoreApplication.translate("leads_profile", u"Opportunities Information", None))
        self.edit_btn.setText(QCoreApplication.translate("leads_profile", u"Edit", None))
#if QT_CONFIG(tooltip)
        self.delete_btn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.delete_btn.setText(QCoreApplication.translate("leads_profile", u"Delete", None))
        self.compname_lbl.setText(QCoreApplication.translate("leads_profile", u"Title:", None))
        self.opp_cost_lbl.setText(QCoreApplication.translate("leads_profile", u"Cost:", None))
        self.comprole_lbl.setText(QCoreApplication.translate("leads_profile", u"Date Created:", None))
        self.contnum_lbl.setText(QCoreApplication.translate("leads_profile", u"Details:", None))
        self.opportunity_title_lbl.setText(QCoreApplication.translate("leads_profile", u"N/A", None))
        self.opportunity_cost_lbl.setText(QCoreApplication.translate("leads_profile", u"N/A", None))
        self.opportunity_date_lbl.setText(QCoreApplication.translate("leads_profile", u"N/A", None))
        self.opportunity_details_lbl.setText(QCoreApplication.translate("leads_profile", u"N/A", None))
        self.full_info_lbl.setText(QCoreApplication.translate("leads_profile", u"View Full Contact Info", None))
    # retranslateUi

