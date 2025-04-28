# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'market_dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1135, 603)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.leadPrioritization_page = QWidget()
        self.leadPrioritization_page.setObjectName(u"leadPrioritization_page")
        self.gridLayout_3 = QGridLayout(self.leadPrioritization_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(self.leadPrioritization_page)
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


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.leadPrioritization_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1097, 478))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QWidget {\n"
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
        self.verticalLayout_6 = QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer_12)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.comboBox = QComboBox(self.widget_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer_13)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
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
        self.verticalLayout_7 = QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_3.addItem(self.verticalSpacer_9)

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_3.addItem(self.verticalSpacer_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"QWidget {\n"
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
        self.verticalLayout_8 = QVBoxLayout(self.widget_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_4.addItem(self.verticalSpacer_6)

        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_4.addItem(self.verticalSpacer_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addWidget(self.widget_5)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 2, 1)

        self.widget_6 = QWidget(self.scrollAreaWidgetContents)
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
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_5.addItem(self.verticalSpacer_7)

        self.label_7 = QLabel(self.widget_6)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_5.addItem(self.verticalSpacer_8)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.widget_6, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(75, 90, 110);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_10, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.leadPrioritization_page)
        self.page2_page = QWidget()
        self.page2_page.setObjectName(u"page2_page")
        self.label = QLabel(self.page2_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(580, 20, 131, 16))
        self.stackedWidget.addWidget(self.page2_page)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Lead Score Statistics", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Total Number of Opportunity ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Won", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Lost", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Pending", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"Per Lead Score Range", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Total Sales Amount (Opportunity Won) Per Lead Score Range", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Conversion Rate (%) Per Lead Score Range", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Total Number of Prospects Per Lead Score Range ", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Setup ICP", None))
        self.label.setText(QCoreApplication.translate("Form", u"Some Content Here", None))
    # retranslateUi

