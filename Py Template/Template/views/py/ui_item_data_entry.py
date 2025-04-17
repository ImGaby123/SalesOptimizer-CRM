# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_data_entry.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_item_data_entry(object):
    def setupUi(self, item_data_entry):
        if not item_data_entry.objectName():
            item_data_entry.setObjectName(u"item_data_entry")
        item_data_entry.resize(1135, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(item_data_entry.sizePolicy().hasHeightForWidth())
        item_data_entry.setSizePolicy(sizePolicy)
        item_data_entry.setStyleSheet(u"background-color: transparent;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.verticalLayout = QVBoxLayout(item_data_entry)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea_4 = QScrollArea(item_data_entry)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setStyleSheet(u"background-color: transparent;\n"
"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1098, 482))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_4.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_4.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setStyleSheet(u"/*  Put Here the Style Sheeeeeeeeeeettttttttttttt for le Beuton - Gaby Plaza  */\n"
"\n"
"/*\n"
"This is the Order of Stuff:\n"
"- Line Edit\n"
"- Labels\n"
"- Button\n"
"- Combo Box\n"
"*/\n"
"\n"
"\n"
"\n"
"/* Line Edit Design Here*/\n"
"QLineEdit {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"    color: white;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* Labels Design Here*/\n"
"QLabel {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);               \n"
"}\n"
"\n"
"\n"
"/* Button Design Here*/\n"
"QPushButton {\n"
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
""
                        "\n"
"QPushButton:pressed {\n"
"    background-color: rgb(180, 180, 180);  /* Darker gray on press */\n"
"}\n"
"\n"
"\n"
"\n"
"/* Combo Boxes Design Here*/\n"
"QComboBox {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
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
"    border-radius: 10px;\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.back_btn = QPushButton(self.frame_4)
        self.back_btn.setObjectName(u"back_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.back_btn.setFont(font)
        self.back_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.back_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/new/newPrefix/Resources/left-arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/new/newPrefix/Resources/left-arrow.png", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.back_btn.setIcon(icon)
        self.back_btn.setFlat(True)

        self.horizontalLayout.addWidget(self.back_btn)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.save_btn = QPushButton(self.frame_4)
        self.save_btn.setObjectName(u"save_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy3)
        self.save_btn.setFont(font)
        self.save_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_btn.setStyleSheet(u"")
        self.save_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.save_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_21 = QWidget(self.frame_4)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy1.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy1)
        self.widget_21.setMinimumSize(QSize(0, 40))
        self.widget_21.setStyleSheet(u"QWidget {\n"
"    background-color: #171717;\n"
"    border-top: 2px solid #ffffff;   /* Change color/width as needed */\n"
"    border-bottom: 2px solid #ffffff;\n"
"    border-left: none;\n"
"    border-right: none;\n"
"}\n"
"")
        self.gridLayout_5 = QGridLayout(self.widget_21)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.AdditionalInformation_15 = QLabel(self.widget_21)
        self.AdditionalInformation_15.setObjectName(u"AdditionalInformation_15")
        sizePolicy1.setHeightForWidth(self.AdditionalInformation_15.sizePolicy().hasHeightForWidth())
        self.AdditionalInformation_15.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setWeight(QFont.Black)
        font1.setItalic(False)
        self.AdditionalInformation_15.setFont(font1)
        self.AdditionalInformation_15.setStyleSheet(u"QLabel {\n"
"    border: none;\n"
"    color: white;\n"
"	font: 900 12pt \"Segoe UI\";\n"
"}")

        self.gridLayout_5.addWidget(self.AdditionalInformation_15, 1, 0, 1, 1)


        self.verticalLayout_19.addWidget(self.widget_21)


        self.verticalLayout_3.addLayout(self.verticalLayout_19)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.phone_line = QLineEdit(self.frame_4)
        self.phone_line.setObjectName(u"phone_line")
        sizePolicy1.setHeightForWidth(self.phone_line.sizePolicy().hasHeightForWidth())
        self.phone_line.setSizePolicy(sizePolicy1)
        self.phone_line.setMinimumSize(QSize(0, 0))
        self.phone_line.setMaximumSize(QSize(16777215, 16777215))
        self.phone_line.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.phone_line, 8, 1, 1, 1)

        self.email_line = QLineEdit(self.frame_4)
        self.email_line.setObjectName(u"email_line")
        sizePolicy1.setHeightForWidth(self.email_line.sizePolicy().hasHeightForWidth())
        self.email_line.setSizePolicy(sizePolicy1)
        self.email_line.setMinimumSize(QSize(0, 0))
        self.email_line.setMaximumSize(QSize(16777215, 16777215))
        self.email_line.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.email_line, 6, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.FirstNameLabel_7 = QLabel(self.frame_4)
        self.FirstNameLabel_7.setObjectName(u"FirstNameLabel_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.FirstNameLabel_7.sizePolicy().hasHeightForWidth())
        self.FirstNameLabel_7.setSizePolicy(sizePolicy4)
        self.FirstNameLabel_7.setStyleSheet(u"color: red;")

        self.horizontalLayout_6.addWidget(self.FirstNameLabel_7)

        self.MiddleNameLabel_8 = QLabel(self.frame_4)
        self.MiddleNameLabel_8.setObjectName(u"MiddleNameLabel_8")
        sizePolicy1.setHeightForWidth(self.MiddleNameLabel_8.sizePolicy().hasHeightForWidth())
        self.MiddleNameLabel_8.setSizePolicy(sizePolicy1)
        self.MiddleNameLabel_8.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.MiddleNameLabel_8)


        self.gridLayout_10.addLayout(self.horizontalLayout_6, 5, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.FirstNameLabel_8 = QLabel(self.frame_4)
        self.FirstNameLabel_8.setObjectName(u"FirstNameLabel_8")
        sizePolicy4.setHeightForWidth(self.FirstNameLabel_8.sizePolicy().hasHeightForWidth())
        self.FirstNameLabel_8.setSizePolicy(sizePolicy4)
        self.FirstNameLabel_8.setStyleSheet(u"color: red;")

        self.horizontalLayout_7.addWidget(self.FirstNameLabel_8)

        self.SuffixLabel_8 = QLabel(self.frame_4)
        self.SuffixLabel_8.setObjectName(u"SuffixLabel_8")
        sizePolicy1.setHeightForWidth(self.SuffixLabel_8.sizePolicy().hasHeightForWidth())
        self.SuffixLabel_8.setSizePolicy(sizePolicy1)
        self.SuffixLabel_8.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.SuffixLabel_8)


        self.gridLayout_10.addLayout(self.horizontalLayout_7, 7, 1, 1, 1)

        self.gender_combo = QComboBox(self.frame_4)
        self.gender_combo.addItem("")
        self.gender_combo.addItem("")
        self.gender_combo.addItem("")
        self.gender_combo.setObjectName(u"gender_combo")
        sizePolicy1.setHeightForWidth(self.gender_combo.sizePolicy().hasHeightForWidth())
        self.gender_combo.setSizePolicy(sizePolicy1)
        self.gender_combo.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.gender_combo, 10, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.FirstNameLabel_5 = QLabel(self.frame_4)
        self.FirstNameLabel_5.setObjectName(u"FirstNameLabel_5")
        sizePolicy4.setHeightForWidth(self.FirstNameLabel_5.sizePolicy().hasHeightForWidth())
        self.FirstNameLabel_5.setSizePolicy(sizePolicy4)
        self.FirstNameLabel_5.setStyleSheet(u"color: red;")

        self.horizontalLayout_4.addWidget(self.FirstNameLabel_5)

        self.FirstNameLabel_4 = QLabel(self.frame_4)
        self.FirstNameLabel_4.setObjectName(u"FirstNameLabel_4")
        sizePolicy1.setHeightForWidth(self.FirstNameLabel_4.sizePolicy().hasHeightForWidth())
        self.FirstNameLabel_4.setSizePolicy(sizePolicy1)
        self.FirstNameLabel_4.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.FirstNameLabel_4)


        self.gridLayout_10.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.firstname_line = QLineEdit(self.frame_4)
        self.firstname_line.setObjectName(u"firstname_line")
        sizePolicy1.setHeightForWidth(self.firstname_line.sizePolicy().hasHeightForWidth())
        self.firstname_line.setSizePolicy(sizePolicy1)
        self.firstname_line.setMinimumSize(QSize(0, 0))
        self.firstname_line.setMaximumSize(QSize(16777215, 16777215))
        self.firstname_line.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.firstname_line, 2, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.FirstNameLabel_6 = QLabel(self.frame_4)
        self.FirstNameLabel_6.setObjectName(u"FirstNameLabel_6")
        sizePolicy4.setHeightForWidth(self.FirstNameLabel_6.sizePolicy().hasHeightForWidth())
        self.FirstNameLabel_6.setSizePolicy(sizePolicy4)
        self.FirstNameLabel_6.setStyleSheet(u"color: red;")

        self.horizontalLayout_5.addWidget(self.FirstNameLabel_6)

        self.LastNameLabel_4 = QLabel(self.frame_4)
        self.LastNameLabel_4.setObjectName(u"LastNameLabel_4")
        sizePolicy1.setHeightForWidth(self.LastNameLabel_4.sizePolicy().hasHeightForWidth())
        self.LastNameLabel_4.setSizePolicy(sizePolicy1)
        self.LastNameLabel_4.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.LastNameLabel_4)


        self.gridLayout_10.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)

        self.GenderLabel_4 = QLabel(self.frame_4)
        self.GenderLabel_4.setObjectName(u"GenderLabel_4")
        sizePolicy1.setHeightForWidth(self.GenderLabel_4.sizePolicy().hasHeightForWidth())
        self.GenderLabel_4.setSizePolicy(sizePolicy1)
        self.GenderLabel_4.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.GenderLabel_4, 9, 1, 1, 1)

        self.lastname_line = QLineEdit(self.frame_4)
        self.lastname_line.setObjectName(u"lastname_line")
        sizePolicy1.setHeightForWidth(self.lastname_line.sizePolicy().hasHeightForWidth())
        self.lastname_line.setSizePolicy(sizePolicy1)
        self.lastname_line.setMinimumSize(QSize(0, 0))
        self.lastname_line.setMaximumSize(QSize(16777215, 16777215))
        self.lastname_line.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.lastname_line, 4, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 6, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.CompanyLabel_6 = QLabel(self.frame_4)
        self.CompanyLabel_6.setObjectName(u"CompanyLabel_6")
        sizePolicy1.setHeightForWidth(self.CompanyLabel_6.sizePolicy().hasHeightForWidth())
        self.CompanyLabel_6.setSizePolicy(sizePolicy1)
        self.CompanyLabel_6.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.CompanyLabel_6, 6, 0, 1, 1)

        self.company_industry_line = QLineEdit(self.frame_4)
        self.company_industry_line.setObjectName(u"company_industry_line")
        sizePolicy1.setHeightForWidth(self.company_industry_line.sizePolicy().hasHeightForWidth())
        self.company_industry_line.setSizePolicy(sizePolicy1)
        self.company_industry_line.setMinimumSize(QSize(0, 0))
        self.company_industry_line.setMaximumSize(QSize(16777215, 16777215))
        self.company_industry_line.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.company_industry_line, 9, 0, 1, 1)

        self.company_email_line = QLineEdit(self.frame_4)
        self.company_email_line.setObjectName(u"company_email_line")
        sizePolicy1.setHeightForWidth(self.company_email_line.sizePolicy().hasHeightForWidth())
        self.company_email_line.setSizePolicy(sizePolicy1)
        self.company_email_line.setMinimumSize(QSize(0, 0))
        self.company_email_line.setMaximumSize(QSize(16777215, 16777215))
        self.company_email_line.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.company_email_line, 4, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.FirstNameLabel_9 = QLabel(self.frame_4)
        self.FirstNameLabel_9.setObjectName(u"FirstNameLabel_9")
        sizePolicy4.setHeightForWidth(self.FirstNameLabel_9.sizePolicy().hasHeightForWidth())
        self.FirstNameLabel_9.setSizePolicy(sizePolicy4)
        self.FirstNameLabel_9.setStyleSheet(u"color: red;")

        self.horizontalLayout_8.addWidget(self.FirstNameLabel_9)

        self.CompanyLabel = QLabel(self.frame_4)
        self.CompanyLabel.setObjectName(u"CompanyLabel")
        sizePolicy1.setHeightForWidth(self.CompanyLabel.sizePolicy().hasHeightForWidth())
        self.CompanyLabel.setSizePolicy(sizePolicy1)
        self.CompanyLabel.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.CompanyLabel)


        self.gridLayout_9.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.company_line = QLineEdit(self.frame_4)
        self.company_line.setObjectName(u"company_line")
        sizePolicy1.setHeightForWidth(self.company_line.sizePolicy().hasHeightForWidth())
        self.company_line.setSizePolicy(sizePolicy1)
        self.company_line.setMinimumSize(QSize(0, 0))
        self.company_line.setMaximumSize(QSize(16777215, 16777215))
        self.company_line.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.company_line, 1, 0, 1, 1)

        self.company_website_line = QLineEdit(self.frame_4)
        self.company_website_line.setObjectName(u"company_website_line")
        sizePolicy1.setHeightForWidth(self.company_website_line.sizePolicy().hasHeightForWidth())
        self.company_website_line.setSizePolicy(sizePolicy1)
        self.company_website_line.setMinimumSize(QSize(0, 0))
        self.company_website_line.setMaximumSize(QSize(16777215, 16777215))
        self.company_website_line.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.company_website_line, 7, 0, 1, 1)

        self.CompanyLabel_7 = QLabel(self.frame_4)
        self.CompanyLabel_7.setObjectName(u"CompanyLabel_7")
        sizePolicy1.setHeightForWidth(self.CompanyLabel_7.sizePolicy().hasHeightForWidth())
        self.CompanyLabel_7.setSizePolicy(sizePolicy1)
        self.CompanyLabel_7.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.CompanyLabel_7, 8, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.FirstNameLabel_11 = QLabel(self.frame_4)
        self.FirstNameLabel_11.setObjectName(u"FirstNameLabel_11")
        sizePolicy4.setHeightForWidth(self.FirstNameLabel_11.sizePolicy().hasHeightForWidth())
        self.FirstNameLabel_11.setSizePolicy(sizePolicy4)
        self.FirstNameLabel_11.setStyleSheet(u"color: red;")

        self.horizontalLayout_9.addWidget(self.FirstNameLabel_11)

        self.CompanyLabel_5 = QLabel(self.frame_4)
        self.CompanyLabel_5.setObjectName(u"CompanyLabel_5")
        sizePolicy1.setHeightForWidth(self.CompanyLabel_5.sizePolicy().hasHeightForWidth())
        self.CompanyLabel_5.setSizePolicy(sizePolicy1)
        self.CompanyLabel_5.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.CompanyLabel_5)


        self.gridLayout_9.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_5, 5, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_8)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")

        self.verticalLayout_3.addLayout(self.gridLayout_14)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout.addWidget(self.scrollArea_4)

        QWidget.setTabOrder(self.firstname_line, self.lastname_line)
        QWidget.setTabOrder(self.lastname_line, self.email_line)
        QWidget.setTabOrder(self.email_line, self.phone_line)
        QWidget.setTabOrder(self.phone_line, self.gender_combo)
        QWidget.setTabOrder(self.gender_combo, self.company_line)
        QWidget.setTabOrder(self.company_line, self.company_email_line)
        QWidget.setTabOrder(self.company_email_line, self.company_website_line)
        QWidget.setTabOrder(self.company_website_line, self.company_industry_line)
        QWidget.setTabOrder(self.company_industry_line, self.save_btn)
        QWidget.setTabOrder(self.save_btn, self.back_btn)
        QWidget.setTabOrder(self.back_btn, self.scrollArea_4)

        self.retranslateUi(item_data_entry)

        self.gender_combo.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(item_data_entry)
    # setupUi

    def retranslateUi(self, item_data_entry):
        item_data_entry.setWindowTitle(QCoreApplication.translate("item_data_entry", u"Add Contact", None))
        self.back_btn.setText(QCoreApplication.translate("item_data_entry", u"< Back to Items", None))
        self.save_btn.setText(QCoreApplication.translate("item_data_entry", u"Confirm", None))
        self.AdditionalInformation_15.setText(QCoreApplication.translate("item_data_entry", u"Item Information", None))
        self.FirstNameLabel_7.setText(QCoreApplication.translate("item_data_entry", u"*", None))
        self.MiddleNameLabel_8.setText(QCoreApplication.translate("item_data_entry", u"Email :", None))
        self.FirstNameLabel_8.setText(QCoreApplication.translate("item_data_entry", u"*", None))
        self.SuffixLabel_8.setText(QCoreApplication.translate("item_data_entry", u"Phone Number :", None))
        self.gender_combo.setItemText(0, QCoreApplication.translate("item_data_entry", u"Male", None))
        self.gender_combo.setItemText(1, QCoreApplication.translate("item_data_entry", u"Female", None))
        self.gender_combo.setItemText(2, QCoreApplication.translate("item_data_entry", u"Other", None))

        self.gender_combo.setPlaceholderText(QCoreApplication.translate("item_data_entry", u"Select a gender", None))
        self.FirstNameLabel_5.setText(QCoreApplication.translate("item_data_entry", u"*", None))
        self.FirstNameLabel_4.setText(QCoreApplication.translate("item_data_entry", u"First Name :", None))
        self.FirstNameLabel_6.setText(QCoreApplication.translate("item_data_entry", u"*", None))
        self.LastNameLabel_4.setText(QCoreApplication.translate("item_data_entry", u"Last Name :", None))
        self.GenderLabel_4.setText(QCoreApplication.translate("item_data_entry", u"Gender (Optional):", None))
        self.CompanyLabel_6.setText(QCoreApplication.translate("item_data_entry", u"Company Website (Optional):", None))
        self.FirstNameLabel_9.setText(QCoreApplication.translate("item_data_entry", u"*", None))
        self.CompanyLabel.setText(QCoreApplication.translate("item_data_entry", u"Company :", None))
        self.CompanyLabel_7.setText(QCoreApplication.translate("item_data_entry", u"Industry (Optional):", None))
        self.FirstNameLabel_11.setText(QCoreApplication.translate("item_data_entry", u"*", None))
        self.CompanyLabel_5.setText(QCoreApplication.translate("item_data_entry", u"Company Email :", None))
    # retranslateUi

