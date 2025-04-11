# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import views.py.icons_rc

class Ui_sidebar(object):
    def setupUi(self, sidebar):
        if not sidebar.objectName():
            sidebar.setObjectName(u"sidebar")
        sidebar.resize(172, 702)
        sidebar.setStyleSheet(u"")
        self.verticalLayoutWidget = QWidget(sidebar)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 171, 701))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.crm_lbl = QLabel(self.verticalLayoutWidget)
        self.crm_lbl.setObjectName(u"crm_lbl")
        self.crm_lbl.setStyleSheet(u"QLabel {\n"
"    border-top: none;   /* Change color/width as needed */\n"
"    border-bottom: 2px solid #737373;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"	margin-bottom: 20px;\n"
"}\n"
"")
        self.crm_lbl.setPixmap(QPixmap(u":/Resources/crm_logo.png"))

        self.verticalLayout.addWidget(self.crm_lbl)

        self.dashboard_btn = QPushButton(self.verticalLayoutWidget)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashboard_btn.sizePolicy().hasHeightForWidth())
        self.dashboard_btn.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.dashboard_btn.setFont(font)
        self.dashboard_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dashboard_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.dashboard_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(30, 30, 30);  /* Dark grey background */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Slightly lighter border */\n"
"    padding: 8px;  /* Slightly larger padding for better spacing */\n"
"    color: rgb(220, 220, 220);  /* Light grey text for contrast */\n"
"    border-radius: 5px;  /* Smooth rounded corners */\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Slightly lighter on hover */\n"
"    border: 1px solid rgb(255, 255, 255);  /* White border for highlight */\n"
"    color: rgb(255, 255, 255);  /* Pure white text */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 20, 20);  /* Darker when pressed */\n"
"    border: 1px solid rgb(180, 180, 180);  /* Less intense white border */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(50, 50, 50);  /* Muted grey */\n"
"    color: rgb(130, 130, 130);  /* Dull text for disabled state */\n"
"    border: 1px solid rgb(80, "
                        "80, 80);  /* Less contrast */\n"
"}\n"
"")
        self.dashboard_btn.setFlat(True)

        self.verticalLayout.addWidget(self.dashboard_btn)

        self.contacts_btn = QPushButton(self.verticalLayoutWidget)
        self.contacts_btn.setObjectName(u"contacts_btn")
        sizePolicy.setHeightForWidth(self.contacts_btn.sizePolicy().hasHeightForWidth())
        self.contacts_btn.setSizePolicy(sizePolicy)
        self.contacts_btn.setFont(font)
        self.contacts_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.contacts_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(30, 30, 30);  /* Dark grey background */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Slightly lighter border */\n"
"    padding: 8px;  /* Slightly larger padding for better spacing */\n"
"    color: rgb(220, 220, 220);  /* Light grey text for contrast */\n"
"    border-radius: 5px;  /* Smooth rounded corners */\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Slightly lighter on hover */\n"
"    border: 1px solid rgb(255, 255, 255);  /* White border for highlight */\n"
"    color: rgb(255, 255, 255);  /* Pure white text */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 20, 20);  /* Darker when pressed */\n"
"    border: 1px solid rgb(180, 180, 180);  /* Less intense white border */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(50, 50, 50);  /* Muted grey */\n"
"    color: rgb(130, 130, 130);  /* Dull text for disabled state */\n"
"    border: 1px solid rgb(80, "
                        "80, 80);  /* Less contrast */\n"
"}\n"
"")
        self.contacts_btn.setFlat(True)

        self.verticalLayout.addWidget(self.contacts_btn)

        self.leads_btn = QPushButton(self.verticalLayoutWidget)
        self.leads_btn.setObjectName(u"leads_btn")
        sizePolicy.setHeightForWidth(self.leads_btn.sizePolicy().hasHeightForWidth())
        self.leads_btn.setSizePolicy(sizePolicy)
        self.leads_btn.setFont(font)
        self.leads_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.leads_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(30, 30, 30);  /* Dark grey background */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Slightly lighter border */\n"
"    padding: 8px;  /* Slightly larger padding for better spacing */\n"
"    color: rgb(220, 220, 220);  /* Light grey text for contrast */\n"
"    border-radius: 5px;  /* Smooth rounded corners */\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Slightly lighter on hover */\n"
"    border: 1px solid rgb(255, 255, 255);  /* White border for highlight */\n"
"    color: rgb(255, 255, 255);  /* Pure white text */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 20, 20);  /* Darker when pressed */\n"
"    border: 1px solid rgb(180, 180, 180);  /* Less intense white border */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(50, 50, 50);  /* Muted grey */\n"
"    color: rgb(130, 130, 130);  /* Dull text for disabled state */\n"
"    border: 1px solid rgb(80, "
                        "80, 80);  /* Less contrast */\n"
"}\n"
"")
        self.leads_btn.setFlat(True)

        self.verticalLayout.addWidget(self.leads_btn)

        self.settings_btn = QPushButton(self.verticalLayoutWidget)
        self.settings_btn.setObjectName(u"settings_btn")
        sizePolicy.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy)
        self.settings_btn.setFont(font)
        self.settings_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settings_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(30, 30, 30);  /* Dark grey background */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Slightly lighter border */\n"
"    padding: 8px;  /* Slightly larger padding for better spacing */\n"
"    color: rgb(220, 220, 220);  /* Light grey text for contrast */\n"
"    border-radius: 5px;  /* Smooth rounded corners */\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Slightly lighter on hover */\n"
"    border: 1px solid rgb(255, 255, 255);  /* White border for highlight */\n"
"    color: rgb(255, 255, 255);  /* Pure white text */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 20, 20);  /* Darker when pressed */\n"
"    border: 1px solid rgb(180, 180, 180);  /* Less intense white border */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(50, 50, 50);  /* Muted grey */\n"
"    color: rgb(130, 130, 130);  /* Dull text for disabled state */\n"
"    border: 1px solid rgb(80, "
                        "80, 80);  /* Less contrast */\n"
"}\n"
"")
        self.settings_btn.setFlat(True)

        self.verticalLayout.addWidget(self.settings_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.logout_btn = QPushButton(self.verticalLayoutWidget)
        self.logout_btn.setObjectName(u"logout_btn")
        sizePolicy.setHeightForWidth(self.logout_btn.sizePolicy().hasHeightForWidth())
        self.logout_btn.setSizePolicy(sizePolicy)
        self.logout_btn.setMinimumSize(QSize(0, 0))
        self.logout_btn.setMaximumSize(QSize(16777215, 16777215))
        self.logout_btn.setFont(font)
        self.logout_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logout_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(30, 30, 30);  /* Dark grey background */\n"
"    border: 1px solid rgb(80, 80, 80);  /* Slightly lighter border */\n"
"    padding: 8px;  /* Slightly larger padding for better spacing */\n"
"    color: rgb(220, 220, 220);  /* Light grey text for contrast */\n"
"    border-radius: 5px;  /* Smooth rounded corners */\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);  /* Slightly lighter on hover */\n"
"    border: 1px solid rgb(255, 255, 255);  /* White border for highlight */\n"
"    color: rgb(255, 255, 255);  /* Pure white text */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 20, 20);  /* Darker when pressed */\n"
"    border: 1px solid rgb(180, 180, 180);  /* Less intense white border */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(50, 50, 50);  /* Muted grey */\n"
"    color: rgb(130, 130, 130);  /* Dull text for disabled state */\n"
"    border: 1px solid rgb(80, "
                        "80, 80);  /* Less contrast */\n"
"}\n"
"")
        self.logout_btn.setFlat(True)

        self.verticalLayout.addWidget(self.logout_btn)


        self.retranslateUi(sidebar)

        QMetaObject.connectSlotsByName(sidebar)
    # setupUi

    def retranslateUi(self, sidebar):
        sidebar.setWindowTitle(QCoreApplication.translate("sidebar", u"Form", None))
        self.crm_lbl.setText("")
        self.dashboard_btn.setText(QCoreApplication.translate("sidebar", u"Dashboard", None))
        self.contacts_btn.setText(QCoreApplication.translate("sidebar", u"Contacts", None))
        self.leads_btn.setText(QCoreApplication.translate("sidebar", u"Leads", None))
        self.settings_btn.setText(QCoreApplication.translate("sidebar", u"Settings", None))
        self.logout_btn.setText(QCoreApplication.translate("sidebar", u"Logout", None))
    # retranslateUi

