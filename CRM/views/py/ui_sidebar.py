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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_sidebar(object):
    def setupUi(self, sidebar):
        if not sidebar.objectName():
            sidebar.setObjectName(u"sidebar")
        sidebar.resize(172, 702)
        sidebar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayoutWidget = QWidget(sidebar)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 171, 701))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dashboard_btn = QPushButton(self.verticalLayoutWidget)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashboard_btn.sizePolicy().hasHeightForWidth())
        self.dashboard_btn.setSizePolicy(sizePolicy)
        self.dashboard_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    padding: 5px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.dashboard_btn.setFlat(True)

        self.verticalLayout.addWidget(self.dashboard_btn)

        self.contacts_btn = QPushButton(self.verticalLayoutWidget)
        self.contacts_btn.setObjectName(u"contacts_btn")
        sizePolicy.setHeightForWidth(self.contacts_btn.sizePolicy().hasHeightForWidth())
        self.contacts_btn.setSizePolicy(sizePolicy)
        self.contacts_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    padding: 5px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.contacts_btn.setFlat(True)

        self.verticalLayout.addWidget(self.contacts_btn)

        self.leads_btn = QPushButton(self.verticalLayoutWidget)
        self.leads_btn.setObjectName(u"leads_btn")
        sizePolicy.setHeightForWidth(self.leads_btn.sizePolicy().hasHeightForWidth())
        self.leads_btn.setSizePolicy(sizePolicy)
        self.leads_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    padding: 5px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.leads_btn.setFlat(True)

        self.verticalLayout.addWidget(self.leads_btn)

        self.account_btn = QPushButton(self.verticalLayoutWidget)
        self.account_btn.setObjectName(u"account_btn")
        sizePolicy.setHeightForWidth(self.account_btn.sizePolicy().hasHeightForWidth())
        self.account_btn.setSizePolicy(sizePolicy)
        self.account_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    padding: 5px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.account_btn.setFlat(True)

        self.verticalLayout.addWidget(self.account_btn)

        self.opportunities_btn = QPushButton(self.verticalLayoutWidget)
        self.opportunities_btn.setObjectName(u"opportunities_btn")
        sizePolicy.setHeightForWidth(self.opportunities_btn.sizePolicy().hasHeightForWidth())
        self.opportunities_btn.setSizePolicy(sizePolicy)
        self.opportunities_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    padding: 5px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.opportunities_btn.setFlat(True)

        self.verticalLayout.addWidget(self.opportunities_btn)

        self.settings_btn = QPushButton(self.verticalLayoutWidget)
        self.settings_btn.setObjectName(u"settings_btn")
        sizePolicy.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy)
        self.settings_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    padding: 5px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
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
        self.logout_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    padding: 5px;\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.logout_btn.setFlat(True)

        self.verticalLayout.addWidget(self.logout_btn)


        self.retranslateUi(sidebar)

        QMetaObject.connectSlotsByName(sidebar)
    # setupUi

    def retranslateUi(self, sidebar):
        sidebar.setWindowTitle(QCoreApplication.translate("sidebar", u"Form", None))
        self.dashboard_btn.setText(QCoreApplication.translate("sidebar", u"Dashboard", None))
        self.contacts_btn.setText(QCoreApplication.translate("sidebar", u"Contacts", None))
        self.leads_btn.setText(QCoreApplication.translate("sidebar", u"Leads", None))
        self.account_btn.setText(QCoreApplication.translate("sidebar", u"Account", None))
        self.opportunities_btn.setText(QCoreApplication.translate("sidebar", u"Opportunities", None))
        self.settings_btn.setText(QCoreApplication.translate("sidebar", u"Settings", None))
        self.logout_btn.setText(QCoreApplication.translate("sidebar", u"Logout", None))
    # retranslateUi

