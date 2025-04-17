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
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import views.py.icons_rc

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if not dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(1201, 680)
        dashboard.setStyleSheet(u"background-color: transparent;")
        self.gridLayout = QGridLayout(dashboard)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(dashboard)
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

        self.horizontalSpacer_5 = QSpacerItem(40, 10, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: 2px solid rgb(226, 226, 226);\n"
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
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.totalleadhead_lbl.setFont(font1)
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
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.lead_combo.setFont(font2)
        self.lead_combo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.totalleadmini_lbl = QLabel(self.frame_2)
        self.totalleadmini_lbl.setObjectName(u"totalleadmini_lbl")
        font3 = QFont()
        font3.setPointSize(11)
        self.totalleadmini_lbl.setFont(font3)
        self.totalleadmini_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_10.addWidget(self.totalleadmini_lbl)

        self.leadmini2_lbl = QLabel(self.frame_2)
        self.leadmini2_lbl.setObjectName(u"leadmini2_lbl")
        self.leadmini2_lbl.setFont(font3)
        self.leadmini2_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_10.addWidget(self.leadmini2_lbl)

        self.leadmini1_lbl = QLabel(self.frame_2)
        self.leadmini1_lbl.setObjectName(u"leadmini1_lbl")
        self.leadmini1_lbl.setFont(font3)
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
        self.equal_lbl.setFont(font3)
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
        self.green50_lbl.setFont(font3)
        self.green50_lbl.setStyleSheet(u"background: transparent;\n"
"color: #A3E635;\n"
"border: none")

        self.verticalLayout_24.addWidget(self.green50_lbl)

        self.red50_lbl = QLabel(self.frame_2)
        self.red50_lbl.setObjectName(u"red50_lbl")
        self.red50_lbl.setFont(font3)
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
        self.total_leads_qty_lbl.setFont(font3)
        self.total_leads_qty_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_12.addWidget(self.total_leads_qty_lbl)

        self.leads_50_up_lbl = QLabel(self.frame_2)
        self.leads_50_up_lbl.setObjectName(u"leads_50_up_lbl")
        self.leads_50_up_lbl.setFont(font3)
        self.leads_50_up_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_12.addWidget(self.leads_50_up_lbl)

        self.leads_50_down_lbl = QLabel(self.frame_2)
        self.leads_50_down_lbl.setObjectName(u"leads_50_down_lbl")
        self.leads_50_down_lbl.setFont(font3)
        self.leads_50_down_lbl.setStyleSheet(u"background: transparent;\n"
"color: #fff;\n"
"border: none")

        self.verticalLayout_12.addWidget(self.leads_50_down_lbl)


        self.horizontalLayout_3.addLayout(self.verticalLayout_12)


        self.verticalLayout_13.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_13)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addWidget(self.frame_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_7)


        self.horizontalLayout_16.addLayout(self.verticalLayout_4)


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


        self.retranslateUi(dashboard)

        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"Dashboard", None))
        self.leadprofile_lbl.setText(QCoreApplication.translate("dashboard", u"Dashboard", None))
        self.totalleadhead_lbl.setText(QCoreApplication.translate("dashboard", u"Total Leads", None))
        self.lead_combo.setItemText(0, QCoreApplication.translate("dashboard", u"View All", None))
        self.lead_combo.setItemText(1, QCoreApplication.translate("dashboard", u"Last 3 Days", None))
        self.lead_combo.setItemText(2, QCoreApplication.translate("dashboard", u"Last 7 Days", None))
        self.lead_combo.setItemText(3, QCoreApplication.translate("dashboard", u"Last 30 Days", None))

        self.lead_combo.setPlaceholderText(QCoreApplication.translate("dashboard", u"View All", None))
        self.totalleadmini_lbl.setText(QCoreApplication.translate("dashboard", u"Total Leads", None))
        self.leadmini2_lbl.setText(QCoreApplication.translate("dashboard", u"Leads", None))
        self.leadmini1_lbl.setText(QCoreApplication.translate("dashboard", u"Leads ", None))
        self.equal_lbl.setText(QCoreApplication.translate("dashboard", u"=", None))
        self.green50_lbl.setText(QCoreApplication.translate("dashboard", u"50", None))
        self.red50_lbl.setText(QCoreApplication.translate("dashboard", u"50", None))
        self.up50_lbl.setText("")
        self.down50_lbl.setText("")
        self.total_leads_qty_lbl.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.leads_50_up_lbl.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.leads_50_down_lbl.setText(QCoreApplication.translate("dashboard", u"0", None))
    # retranslateUi

