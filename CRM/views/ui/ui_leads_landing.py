# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'leads_landing.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)
import rc_icons

class Ui_leads_landing(object):
    def setupUi(self, leads_landing):
        if not leads_landing.objectName():
            leads_landing.setObjectName(u"leads_landing")
        leads_landing.resize(1201, 680)
        leads_landing.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(leads_landing)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.leads_tbl = QTableWidget(leads_landing)
        self.leads_tbl.setObjectName(u"leads_tbl")
        self.leads_tbl.setMouseTracking(False)
        self.leads_tbl.setStyleSheet(u"QTableWidget {\n"
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
        self.leads_tbl.setAlternatingRowColors(True)
        self.leads_tbl.horizontalHeader().setCascadingSectionResizes(False)
        self.leads_tbl.horizontalHeader().setDefaultSectionSize(200)
        self.leads_tbl.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.leads_tbl, 10, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.gridLayout.addLayout(self.gridLayout_2, 6, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.sort_combo = QComboBox(leads_landing)
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.setObjectName(u"sort_combo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sort_combo.sizePolicy().hasHeightForWidth())
        self.sort_combo.setSizePolicy(sizePolicy)
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

        self.horizontalLayout_23.addWidget(self.sort_combo)

        self.set_icp_btn = QPushButton(leads_landing)
        self.set_icp_btn.setObjectName(u"set_icp_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.set_icp_btn.sizePolicy().hasHeightForWidth())
        self.set_icp_btn.setSizePolicy(sizePolicy1)
        self.set_icp_btn.setMinimumSize(QSize(0, 0))
        self.set_icp_btn.setMaximumSize(QSize(16777215, 16777215))
        self.set_icp_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.set_icp_btn.setStyleSheet(u"QPushButton {\n"
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
        self.set_icp_btn.setFlat(False)

        self.horizontalLayout_23.addWidget(self.set_icp_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_4)

        self.selecteditems_lbl = QLabel(leads_landing)
        self.selecteditems_lbl.setObjectName(u"selecteditems_lbl")
        self.selecteditems_lbl.setEnabled(True)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.selecteditems_lbl.setFont(font)
        self.selecteditems_lbl.setStyleSheet(u"color: white")
        self.selecteditems_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_23.addWidget(self.selecteditems_lbl)


        self.gridLayout.addLayout(self.horizontalLayout_23, 5, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.search_line = QLineEdit(leads_landing)
        self.search_line.setObjectName(u"search_line")
        sizePolicy.setHeightForWidth(self.search_line.sizePolicy().hasHeightForWidth())
        self.search_line.setSizePolicy(sizePolicy)
        self.search_line.setMinimumSize(QSize(0, 30))
        self.search_line.setMaximumSize(QSize(290, 16777215))
        self.search_line.setStyleSheet(u"QLineEdit {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"    color: white;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* Placeholder Text */\n"
"QLineEdit:placeholder {\n"
"    color: #888888;  /* Soft gray placeholder */\n"
"}")
        self.search_line.setFrame(True)
        self.search_line.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.search_line.setClearButtonEnabled(False)

        self.horizontalLayout_22.addWidget(self.search_line)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.delete_btn = QPushButton(leads_landing)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_btn.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgba(100, 100, 100, 0.2); /* Light gray with transparency */\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Resources/delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_btn.setIcon(icon)
        self.delete_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.delete_btn)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_6)


        self.gridLayout.addLayout(self.horizontalLayout_22, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 2, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 7, 0, 1, 1)

        self.leads_txt = QLabel(leads_landing)
        self.leads_txt.setObjectName(u"leads_txt")
        sizePolicy.setHeightForWidth(self.leads_txt.sizePolicy().hasHeightForWidth())
        self.leads_txt.setSizePolicy(sizePolicy)
        self.leads_txt.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(False)
        self.leads_txt.setFont(font1)
        self.leads_txt.setStyleSheet(u"background: transparent;\n"
"color: #fff;")

        self.gridLayout.addWidget(self.leads_txt, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 4, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 11, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 2, 1, 1)


        self.retranslateUi(leads_landing)

        QMetaObject.connectSlotsByName(leads_landing)
    # setupUi

    def retranslateUi(self, leads_landing):
        leads_landing.setWindowTitle(QCoreApplication.translate("leads_landing", u"Leads", None))
        self.sort_combo.setItemText(0, QCoreApplication.translate("leads_landing", u"Recently Added", None))
        self.sort_combo.setItemText(1, QCoreApplication.translate("leads_landing", u"Oldest", None))
        self.sort_combo.setItemText(2, QCoreApplication.translate("leads_landing", u"Alphabetical", None))

        self.sort_combo.setPlaceholderText(QCoreApplication.translate("leads_landing", u"All Leads", None))
        self.set_icp_btn.setText(QCoreApplication.translate("leads_landing", u"Setup ICP", None))
        self.selecteditems_lbl.setText(QCoreApplication.translate("leads_landing", u"Selected n Item", None))
        self.search_line.setPlaceholderText(QCoreApplication.translate("leads_landing", u"Search Leads by name, email, or company", None))
#if QT_CONFIG(tooltip)
        self.delete_btn.setToolTip(QCoreApplication.translate("leads_landing", u"Delete Contacts", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.delete_btn.setWhatsThis(QCoreApplication.translate("leads_landing", u"delete contact", None))
#endif // QT_CONFIG(whatsthis)
        self.delete_btn.setText("")
        self.leads_txt.setText(QCoreApplication.translate("leads_landing", u"Leads", None))
    # retranslateUi

