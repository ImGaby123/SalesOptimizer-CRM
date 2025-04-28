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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1073, 1168)
        self.gridLayout_5 = QGridLayout(Form)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.leadPrioritization_page = QWidget()
        self.leadPrioritization_page.setObjectName(u"leadPrioritization_page")
        self.gridLayout_3 = QGridLayout(self.leadPrioritization_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea = QScrollArea(self.leadPrioritization_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1018, 1268))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_7 = QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 1250))
        self.gridLayout_2 = QGridLayout(self.widget_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 6, 1, 1, 1)

        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"QWidget {\n"
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
        self.gridLayout_9 = QGridLayout(self.widget_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.LVT_gridLayout = QGridLayout()
        self.LVT_gridLayout.setObjectName(u"LVT_gridLayout")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.LVT_gridLayout.addItem(self.verticalSpacer_5, 0, 0, 1, 1)


        self.gridLayout_9.addLayout(self.LVT_gridLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_8, 1, 1, 1, 1)

        self.widget_2 = QWidget(self.widget_7)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(75, 90, 110);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_10, 0, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 1)

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
        self.PVLS_gridLayout = QGridLayout()
        self.PVLS_gridLayout.setObjectName(u"PVLS_gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.PVLS_gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.PVLS_gridLayout)


        self.gridLayout_2.addWidget(self.widget_6, 3, 0, 1, 1)

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
        self.SWVLS_gridLayout = QGridLayout()
        self.SWVLS_gridLayout.setObjectName(u"SWVLS_gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.comboBox_3 = QComboBox(self.widget_4)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_3.addWidget(self.comboBox_3)


        self.SWVLS_gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.SWVLS_gridLayout.addItem(self.verticalSpacer_3, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.SWVLS_gridLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_4, 4, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 5, 1, 1, 1)

        self.widget_3 = QWidget(self.widget_7)
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
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.TSVLS_gridLayout = QGridLayout()
        self.TSVLS_gridLayout.setObjectName(u"TSVLS_gridLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.TSVLS_gridLayout.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
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

        self.comboBox_2 = QComboBox(self.widget_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_2.addWidget(self.comboBox_2)


        self.TSVLS_gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.TSVLS_gridLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 4, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 1, 2, 1, 1)

        self.widget_5 = QWidget(self.widget_7)
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
        self.gridLayout_7 = QGridLayout(self.widget_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.CVLS_gridLayout = QGridLayout()
        self.CVLS_gridLayout.setObjectName(u"CVLS_gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.CVLS_gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.CVLS_gridLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_5, 3, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 4, 2, 1, 1)


        self.gridLayout_8.addWidget(self.widget_7, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 1, 0, 1, 1)

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

        self.stackedWidget.addWidget(self.leadPrioritization_page)
        self.page2_page = QWidget()
        self.page2_page.setObjectName(u"page2_page")
        self.label = QLabel(self.page2_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(580, 20, 131, 16))
        self.stackedWidget.addWidget(self.page2_page)

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Setup ICP", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Sales Amount (Won) Per Lead Score Range Last", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"All time", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"Last Month", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Form", u"Last Quarter", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Form", u"Last Year", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"Opportunities", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Won", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Lost", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Pending", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"Per Lead Score Range Last", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"All time", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"Last Month", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form", u"Last Quarter", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Form", u"Last Year", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"Lead Score Statistics", None))
        self.label.setText(QCoreApplication.translate("Form", u"Some Content Here", None))
    # retranslateUi

