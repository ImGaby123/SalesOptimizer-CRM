# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard_landing.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if not dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(1201, 680)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dashboard.sizePolicy().hasHeightForWidth())
        dashboard.setSizePolicy(sizePolicy)
        dashboard.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(25)
        dashboard.setFont(font)
        dashboard.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.gridLayout = QGridLayout(dashboard)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_ = QLabel(dashboard)
        self.label_.setObjectName(u"label_")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_.setFont(font1)
        self.label_.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")

        self.horizontalLayout_3.addWidget(self.label_)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(dashboard)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: transparent;\n"
"color: White;\n"
"border: none;")

        self.horizontalLayout.addWidget(self.label)

        self.sort_combo = QComboBox(dashboard)
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.setObjectName(u"sort_combo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sort_combo.sizePolicy().hasHeightForWidth())
        self.sort_combo.setSizePolicy(sizePolicy1)
        self.sort_combo.setMinimumSize(QSize(0, 10))
        self.sort_combo.setMaximumSize(QSize(150, 16777215))
        self.sort_combo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sort_combo.setStyleSheet(u"QComboBox {\n"
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
        self.sort_combo.setEditable(False)
        self.sort_combo.setFrame(True)

        self.horizontalLayout.addWidget(self.sort_combo)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.horizontalSpacer_5 = QSpacerItem(40, 10, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(dashboard)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 200))
        self.frame.setStyleSheet(u"border: 2px solid #737373;\n"
"background-color: #171717;\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"background-color: transparent;\n"
"color: White;\n"
"border: none;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"\n"
"    background-color: white;\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"    border: none;\n"
"")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.leads_lbl = QLabel(self.frame)
        self.leads_lbl.setObjectName(u"leads_lbl")
        font4 = QFont()
        font4.setPointSize(25)
        font4.setBold(True)
        self.leads_lbl.setFont(font4)
        self.leads_lbl.setStyleSheet(u"background-color: transparent;\n"
"color: White;\n"
"border: none;")
        self.leads_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.leads_lbl)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(dashboard)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(16777215, 200))
        self.frame_2.setStyleSheet(u"border: 2px solid #737373;\n"
"background-color: #171717;\n"
"border-radius: 10px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background-color: transparent;\n"
"color: White;\n"
"border: none;")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"\n"
"    background-color: white;\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"    border: none;\n"
"")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.opportunities_lbl = QLabel(self.frame_2)
        self.opportunities_lbl.setObjectName(u"opportunities_lbl")
        self.opportunities_lbl.setFont(font4)
        self.opportunities_lbl.setStyleSheet(u"background-color: transparent;\n"
"color: White;\n"
"border: none;")
        self.opportunities_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.opportunities_lbl)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer_5)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(dashboard)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QSize(16777215, 200))
        self.frame_3.setStyleSheet(u"border: 2px solid #737373;\n"
"background-color: #171717;\n"
"border-radius: 10px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"background-color: transparent;\n"
"color: White;\n"
"border: none;")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        self.line_3 = QFrame(self.frame_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"\n"
"    background-color: white;\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"    border: none;\n"
"")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_3)

        self.won_lbl = QLabel(self.frame_3)
        self.won_lbl.setObjectName(u"won_lbl")
        self.won_lbl.setFont(font4)
        self.won_lbl.setStyleSheet(u"background-color: transparent;\n"
"color: #22C55E;\n"
"border: none;")
        self.won_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.won_lbl)


        self.verticalLayout_5.addWidget(self.frame_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(dashboard)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 200))
        font5 = QFont()
        font5.setBold(False)
        self.frame_4.setFont(font5)
        self.frame_4.setStyleSheet(u"border: 2px solid #737373;\n"
"background-color: #171717;\n"
"border-radius: 10px;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"background-color: transparent;\n"
"color: White;\n"
"border: none;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.line_4 = QFrame(self.frame_4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"\n"
"    background-color: white;\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"    border: none;\n"
"")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_4)

        self.loss_lbl = QLabel(self.frame_4)
        self.loss_lbl.setObjectName(u"loss_lbl")
        self.loss_lbl.setFont(font4)
        self.loss_lbl.setStyleSheet(u"background-color: transparent;\n"
"color: #FF0000;\n"
"border: none;")
        self.loss_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.loss_lbl)


        self.verticalLayout_7.addWidget(self.frame_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_9, 1, 1, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 4, 1, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_9 = QLabel(dashboard)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"background-color: transparent;\n"
"color: White;\n"
"border: none;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_9)

        self.line_5 = QFrame(dashboard)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"\n"
"    background-color: white;\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"    border: none;\n"
"")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line_5)

        self.lead_tbl = QTableWidget(dashboard)
        self.lead_tbl.setObjectName(u"lead_tbl")
        self.lead_tbl.setStyleSheet(u"QTableWidget {\n"
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

        self.verticalLayout_10.addWidget(self.lead_tbl)


        self.gridLayout.addLayout(self.verticalLayout_10, 3, 1, 1, 1)


        self.retranslateUi(dashboard)

        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"Dashboard", None))
        self.label_.setText(QCoreApplication.translate("dashboard", u"Dashboard", None))
        self.label.setText(QCoreApplication.translate("dashboard", u"Filter by: ", None))
        self.sort_combo.setItemText(0, QCoreApplication.translate("dashboard", u"All Time", None))
        self.sort_combo.setItemText(1, QCoreApplication.translate("dashboard", u"Last 3 Days", None))
        self.sort_combo.setItemText(2, QCoreApplication.translate("dashboard", u"Last 7 Days", None))
        self.sort_combo.setItemText(3, QCoreApplication.translate("dashboard", u"Last 30 Days", None))

        self.sort_combo.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("dashboard", u"Leads", None))
        self.leads_lbl.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.label_4.setText(QCoreApplication.translate("dashboard", u"Active Opportunities", None))
        self.opportunities_lbl.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.label_6.setText(QCoreApplication.translate("dashboard", u"Won Opportunities", None))
        self.won_lbl.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.label_8.setText(QCoreApplication.translate("dashboard", u"Lost Opportunities", None))
        self.loss_lbl.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.label_9.setText(QCoreApplication.translate("dashboard", u"Lead Prioritization", None))
    # retranslateUi

