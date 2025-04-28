# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_sidebar(object):
    def setupUi(self, sidebar):
        if not sidebar.objectName():
            sidebar.setObjectName(u"sidebar")
        sidebar.resize(143, 702)
        sidebar.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"QPushButton {\n"
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
        self.verticalLayout_2 = QVBoxLayout(sidebar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.DashboardTitle = QLabel(sidebar)
        self.DashboardTitle.setObjectName(u"DashboardTitle")
        self.DashboardTitle.setAutoFillBackground(False)
        self.DashboardTitle.setStyleSheet(u"QLabel {\n"
"    background-color: transparent;\n"
"    color: rgb(53, 59, 72);\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    letter-spacing: 0.5px;\n"
"    padding: 5px;\n"
"    qproperty-alignment: 'AlignLeft';\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.DashboardTitle)

        self.line = QFrame(sidebar)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(10)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.line)

        self.home_btn = QPushButton(sidebar)
        self.home_btn.setObjectName(u"home_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_btn.sizePolicy().hasHeightForWidth())
        self.home_btn.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        self.home_btn.setFont(font)
        self.home_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    border-radius: 10px;   /* Rounded edges */\n"
"    padding: 6px 12px;     /* Balanced spacing */\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);  /* Slight press effect */\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.home_btn.setFlat(True)

        self.verticalLayout.addWidget(self.home_btn)

        self.item1_btn = QPushButton(sidebar)
        self.item1_btn.setObjectName(u"item1_btn")
        sizePolicy.setHeightForWidth(self.item1_btn.sizePolicy().hasHeightForWidth())
        self.item1_btn.setSizePolicy(sizePolicy)
        self.item1_btn.setFont(font)
        self.item1_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    border-radius: 10px;   /* Rounded edges */\n"
"    padding: 6px 12px;     /* Balanced spacing */\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);  /* Slight press effect */\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.item1_btn.setFlat(True)

        self.verticalLayout.addWidget(self.item1_btn)

        self.line_2 = QFrame(sidebar)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(10)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.item2_btn = QPushButton(sidebar)
        self.item2_btn.setObjectName(u"item2_btn")
        self.item2_btn.setFont(font)
        self.item2_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    border-radius: 10px;   /* Rounded edges */\n"
"    padding: 6px 12px;     /* Balanced spacing */\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);  /* Slight press effect */\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.item2_btn)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.logout_btn = QPushButton(sidebar)
        self.logout_btn.setObjectName(u"logout_btn")
        sizePolicy.setHeightForWidth(self.logout_btn.sizePolicy().hasHeightForWidth())
        self.logout_btn.setSizePolicy(sizePolicy)
        self.logout_btn.setMinimumSize(QSize(0, 0))
        self.logout_btn.setMaximumSize(QSize(16777215, 16777215))
        self.logout_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(200, 0, 0);    \n"
"    border-radius: 10px;                  \n"
"    padding: 6px 12px;                 \n"
"    color: rgb(200, 0, 0);                \n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 0, 0);\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(150, 0, 0);\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.logout_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.logout_btn)


        self.retranslateUi(sidebar)

        QMetaObject.connectSlotsByName(sidebar)
    # setupUi

    def retranslateUi(self, sidebar):
        sidebar.setWindowTitle(QCoreApplication.translate("sidebar", u"Form", None))
        self.DashboardTitle.setText(QCoreApplication.translate("sidebar", u"Dashboards", None))
        self.home_btn.setText(QCoreApplication.translate("sidebar", u"Market", None))
        self.item1_btn.setText(QCoreApplication.translate("sidebar", u"Sales", None))
        self.item2_btn.setText(QCoreApplication.translate("sidebar", u"Settings", None))
        self.logout_btn.setText(QCoreApplication.translate("sidebar", u"Logout", None))
    # retranslateUi

