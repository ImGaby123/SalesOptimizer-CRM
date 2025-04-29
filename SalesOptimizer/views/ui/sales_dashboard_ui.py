# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sales_dashboard.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(917, 603)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(53, 59, 72);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"    font-size: 32px;      /* Bigger font size for the title */\n"
"    font-weight: bold;    /* Make it bold */\n"
"    letter-spacing: 1px;  /* Slight space between letters */\n"
"    padding: 10px;        /* Some breathing space around */\n"
"    text-align: center;   /* Centered text */\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.widget)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 880, 1268))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_7 = QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 1250))
        self.gridLayout_2 = QGridLayout(self.widget_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 4, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_7)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(231, 231, 231);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(53, 59, 72); /* Dark blue-gray for contrast */\n"
"    font-size: 14px;        /* Clear and professional size */\n"
"    font-weight: 600;       /* Semi-bold, not too heavy */\n"
"    letter-spacing: 0.5px;  /* Light spacing for elegance */\n"
"    padding: 5px 10px;      /* Neat padding */\n"
"    text-align: center;     /* Centered text */\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SalesWonForecast_gridLayout = QGridLayout()
        self.SalesWonForecast_gridLayout.setObjectName(u"SalesWonForecast_gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.SalesWonForecast_gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.widget_6)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.SG_pushButton = QPushButton(self.widget_6)
        self.SG_pushButton.setObjectName(u"SG_pushButton")

        self.horizontalLayout_2.addWidget(self.SG_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.SalesWonForecast_gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.SalesWonForecast_gridLayout)


        self.gridLayout_2.addWidget(self.widget_6, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 4, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 3, 2, 1, 1)

        self.widget_4 = QWidget(self.widget_7)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(231, 231, 231);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(53, 59, 72); /* Dark blue-gray for contrast */\n"
"    font-size: 14px;        /* Clear and professional size */\n"
"    font-weight: 600;       /* Semi-bold, not too heavy */\n"
"    letter-spacing: 0.5px;  /* Light spacing for elegance */\n"
"    padding: 5px 10px;      /* Neat padding */\n"
"    text-align: center;     /* Centered text */\n"
"}\n"
"")
        self.gridLayout_6 = QGridLayout(self.widget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.SalesLossForecast_gridLayout = QGridLayout()
        self.SalesLossForecast_gridLayout.setObjectName(u"SalesLossForecast_gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.SG_pushButton_2 = QPushButton(self.widget_4)
        self.SG_pushButton_2.setObjectName(u"SG_pushButton_2")

        self.horizontalLayout_3.addWidget(self.SG_pushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.SalesLossForecast_gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.SalesLossForecast_gridLayout.addItem(self.verticalSpacer_3, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.SalesLossForecast_gridLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_4, 3, 1, 1, 1)


        self.gridLayout_8.addWidget(self.widget_7, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Sales Dashboard", None))
        self.label.setText(QCoreApplication.translate("Form", u"Sales Forecast for Won", None))
        self.SG_pushButton.setText(QCoreApplication.translate("Form", u"Show Graph", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Sales Forecast for Loss", None))
        self.SG_pushButton_2.setText(QCoreApplication.translate("Form", u"Show Graph", None))
    # retranslateUi

