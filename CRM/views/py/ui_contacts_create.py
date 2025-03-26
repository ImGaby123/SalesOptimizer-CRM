# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts_create.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_contacts_create(object):
    def setupUi(self, contacts_create):
        if not contacts_create.objectName():
            contacts_create.setObjectName(u"contacts_create")
        contacts_create.resize(1135, 869)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(contacts_create.sizePolicy().hasHeightForWidth())
        contacts_create.setSizePolicy(sizePolicy)
        contacts_create.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_6 = QGridLayout(contacts_create)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollArea_4 = QScrollArea(contacts_create)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1111, 845))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_4.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.save_btn = QPushButton(self.scrollAreaWidgetContents_4)
        self.save_btn.setObjectName(u"save_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet(u"QPushButton {\n"
"    background: #d9d9d9;\n"
"    padding: 5px 20px; /* Adjusted for a more natural size */\n"
"    border-radius: 5px;\n"
"    transition: background 0.3s ease-in-out, color 0.3s ease-in-out;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #000;\n"
"    color: #d3d3d9;\n"
"    border: 1px solid #555; /* Optional for visibility */\n"
"}")
        self.save_btn.setFlat(True)

        self.horizontalLayout_6.addWidget(self.save_btn)

        self.horizontalSpacer_9 = QSpacerItem(45, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer = QSpacerItem(90, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gender_combo = QComboBox(self.frame_4)
        self.gender_combo.addItem("")
        self.gender_combo.addItem("")
        self.gender_combo.addItem("")
        self.gender_combo.setObjectName(u"gender_combo")
        sizePolicy2.setHeightForWidth(self.gender_combo.sizePolicy().hasHeightForWidth())
        self.gender_combo.setSizePolicy(sizePolicy2)
        self.gender_combo.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.gender_combo, 3, 0, 1, 1)

        self.GenderLabel_4 = QLabel(self.frame_4)
        self.GenderLabel_4.setObjectName(u"GenderLabel_4")
        sizePolicy2.setHeightForWidth(self.GenderLabel_4.sizePolicy().hasHeightForWidth())
        self.GenderLabel_4.setSizePolicy(sizePolicy2)
        self.GenderLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.GenderLabel_4, 2, 0, 1, 1)

        self.TitleLabel_4 = QLabel(self.frame_4)
        self.TitleLabel_4.setObjectName(u"TitleLabel_4")
        sizePolicy2.setHeightForWidth(self.TitleLabel_4.sizePolicy().hasHeightForWidth())
        self.TitleLabel_4.setSizePolicy(sizePolicy2)
        self.TitleLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.TitleLabel_4, 4, 0, 1, 1)

        self.CompanyLabel_4 = QLabel(self.frame_4)
        self.CompanyLabel_4.setObjectName(u"CompanyLabel_4")
        sizePolicy2.setHeightForWidth(self.CompanyLabel_4.sizePolicy().hasHeightForWidth())
        self.CompanyLabel_4.setSizePolicy(sizePolicy2)
        self.CompanyLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.CompanyLabel_4, 0, 0, 1, 1)

        self.company_line = QLineEdit(self.frame_4)
        self.company_line.setObjectName(u"company_line")
        sizePolicy2.setHeightForWidth(self.company_line.sizePolicy().hasHeightForWidth())
        self.company_line.setSizePolicy(sizePolicy2)
        self.company_line.setMinimumSize(QSize(0, 0))
        self.company_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.company_line, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.gridLayout_9.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)

        self.title_line = QLineEdit(self.frame_4)
        self.title_line.setObjectName(u"title_line")
        sizePolicy2.setHeightForWidth(self.title_line.sizePolicy().hasHeightForWidth())
        self.title_line.setSizePolicy(sizePolicy2)
        self.title_line.setMinimumSize(QSize(0, 0))
        self.title_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.title_line, 5, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_5, 2, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 2, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.SuffixLabel_8 = QLabel(self.frame_4)
        self.SuffixLabel_8.setObjectName(u"SuffixLabel_8")
        sizePolicy2.setHeightForWidth(self.SuffixLabel_8.sizePolicy().hasHeightForWidth())
        self.SuffixLabel_8.setSizePolicy(sizePolicy2)
        self.SuffixLabel_8.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.SuffixLabel_8, 6, 1, 1, 1)

        self.FirstNameLabel_4 = QLabel(self.frame_4)
        self.FirstNameLabel_4.setObjectName(u"FirstNameLabel_4")
        sizePolicy2.setHeightForWidth(self.FirstNameLabel_4.sizePolicy().hasHeightForWidth())
        self.FirstNameLabel_4.setSizePolicy(sizePolicy2)
        self.FirstNameLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.FirstNameLabel_4, 0, 1, 1, 1)

        self.phone_line = QLineEdit(self.frame_4)
        self.phone_line.setObjectName(u"phone_line")
        sizePolicy2.setHeightForWidth(self.phone_line.sizePolicy().hasHeightForWidth())
        self.phone_line.setSizePolicy(sizePolicy2)
        self.phone_line.setMinimumSize(QSize(0, 0))
        self.phone_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_10.addWidget(self.phone_line, 7, 1, 1, 1)

        self.lastname_line = QLineEdit(self.frame_4)
        self.lastname_line.setObjectName(u"lastname_line")
        sizePolicy2.setHeightForWidth(self.lastname_line.sizePolicy().hasHeightForWidth())
        self.lastname_line.setSizePolicy(sizePolicy2)
        self.lastname_line.setMinimumSize(QSize(0, 0))
        self.lastname_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_10.addWidget(self.lastname_line, 3, 1, 1, 1)

        self.firstname_line = QLineEdit(self.frame_4)
        self.firstname_line.setObjectName(u"firstname_line")
        sizePolicy2.setHeightForWidth(self.firstname_line.sizePolicy().hasHeightForWidth())
        self.firstname_line.setSizePolicy(sizePolicy2)
        self.firstname_line.setMinimumSize(QSize(0, 0))
        self.firstname_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_10.addWidget(self.firstname_line, 1, 1, 1, 1)

        self.MiddleNameLabel_8 = QLabel(self.frame_4)
        self.MiddleNameLabel_8.setObjectName(u"MiddleNameLabel_8")
        sizePolicy2.setHeightForWidth(self.MiddleNameLabel_8.sizePolicy().hasHeightForWidth())
        self.MiddleNameLabel_8.setSizePolicy(sizePolicy2)
        self.MiddleNameLabel_8.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.MiddleNameLabel_8, 4, 1, 1, 1)

        self.email_line = QLineEdit(self.frame_4)
        self.email_line.setObjectName(u"email_line")
        sizePolicy2.setHeightForWidth(self.email_line.sizePolicy().hasHeightForWidth())
        self.email_line.setSizePolicy(sizePolicy2)
        self.email_line.setMinimumSize(QSize(0, 0))
        self.email_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_10.addWidget(self.email_line, 5, 1, 1, 1)

        self.LastNameLabel_4 = QLabel(self.frame_4)
        self.LastNameLabel_4.setObjectName(u"LastNameLabel_4")
        sizePolicy2.setHeightForWidth(self.LastNameLabel_4.sizePolicy().hasHeightForWidth())
        self.LastNameLabel_4.setSizePolicy(sizePolicy2)
        self.LastNameLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.LastNameLabel_4, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_10, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_8, 6, 1, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.StreetLabel_4 = QLabel(self.frame_4)
        self.StreetLabel_4.setObjectName(u"StreetLabel_4")
        sizePolicy2.setHeightForWidth(self.StreetLabel_4.sizePolicy().hasHeightForWidth())
        self.StreetLabel_4.setSizePolicy(sizePolicy2)
        self.StreetLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_23.addWidget(self.StreetLabel_4, 4, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_7, 4, 1, 1, 1)

        self.ZipPostalCodeLabel_4 = QLabel(self.frame_4)
        self.ZipPostalCodeLabel_4.setObjectName(u"ZipPostalCodeLabel_4")
        sizePolicy2.setHeightForWidth(self.ZipPostalCodeLabel_4.sizePolicy().hasHeightForWidth())
        self.ZipPostalCodeLabel_4.setSizePolicy(sizePolicy2)
        self.ZipPostalCodeLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_23.addWidget(self.ZipPostalCodeLabel_4, 7, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.gridLayout_23.addLayout(self.horizontalLayout_2, 11, 0, 1, 1)

        self.zip_line = QLineEdit(self.frame_4)
        self.zip_line.setObjectName(u"zip_line")
        sizePolicy2.setHeightForWidth(self.zip_line.sizePolicy().hasHeightForWidth())
        self.zip_line.setSizePolicy(sizePolicy2)
        self.zip_line.setMinimumSize(QSize(0, 0))
        self.zip_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_23.addWidget(self.zip_line, 8, 0, 1, 1)

        self.street_line = QLineEdit(self.frame_4)
        self.street_line.setObjectName(u"street_line")

        self.gridLayout_23.addWidget(self.street_line, 5, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_23, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(90, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.city_line = QLineEdit(self.frame_4)
        self.city_line.setObjectName(u"city_line")
        sizePolicy2.setHeightForWidth(self.city_line.sizePolicy().hasHeightForWidth())
        self.city_line.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.city_line, 6, 1, 1, 1)

        self.State_ProvinceLabel_4 = QLabel(self.frame_4)
        self.State_ProvinceLabel_4.setObjectName(u"State_ProvinceLabel_4")
        sizePolicy2.setHeightForWidth(self.State_ProvinceLabel_4.sizePolicy().hasHeightForWidth())
        self.State_ProvinceLabel_4.setSizePolicy(sizePolicy2)
        self.State_ProvinceLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_3.addWidget(self.State_ProvinceLabel_4, 2, 1, 1, 1)

        self.CityLabel_4 = QLabel(self.frame_4)
        self.CityLabel_4.setObjectName(u"CityLabel_4")
        sizePolicy2.setHeightForWidth(self.CityLabel_4.sizePolicy().hasHeightForWidth())
        self.CityLabel_4.setSizePolicy(sizePolicy2)
        self.CityLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_3.addWidget(self.CityLabel_4, 5, 1, 1, 1)

        self.country_line = QLineEdit(self.frame_4)
        self.country_line.setObjectName(u"country_line")
        sizePolicy2.setHeightForWidth(self.country_line.sizePolicy().hasHeightForWidth())
        self.country_line.setSizePolicy(sizePolicy2)
        self.country_line.setMinimumSize(QSize(0, 0))
        self.country_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.country_line, 1, 1, 1, 1)

        self.state_line = QLineEdit(self.frame_4)
        self.state_line.setObjectName(u"state_line")
        sizePolicy2.setHeightForWidth(self.state_line.sizePolicy().hasHeightForWidth())
        self.state_line.setSizePolicy(sizePolicy2)
        self.state_line.setMinimumSize(QSize(0, 0))
        self.state_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.state_line, 3, 1, 1, 1)

        self.CountryLabel_4 = QLabel(self.frame_4)
        self.CountryLabel_4.setObjectName(u"CountryLabel_4")
        sizePolicy2.setHeightForWidth(self.CountryLabel_4.sizePolicy().hasHeightForWidth())
        self.CountryLabel_4.setSizePolicy(sizePolicy2)
        self.CountryLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_3.addWidget(self.CountryLabel_4, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_18, 8, 1, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_21 = QWidget(self.frame_4)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy2.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy2)
        self.widget_21.setMinimumSize(QSize(0, 40))
        self.widget_21.setStyleSheet(u"background-color: rgb(235, 235, 235);\n"
"\n"
"")
        self.gridLayout_5 = QGridLayout(self.widget_21)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.AdditionalInformation_15 = QLabel(self.widget_21)
        self.AdditionalInformation_15.setObjectName(u"AdditionalInformation_15")
        sizePolicy2.setHeightForWidth(self.AdditionalInformation_15.sizePolicy().hasHeightForWidth())
        self.AdditionalInformation_15.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.AdditionalInformation_15.setFont(font1)
        self.AdditionalInformation_15.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.AdditionalInformation_15, 1, 0, 1, 1)


        self.verticalLayout_19.addWidget(self.widget_21)


        self.gridLayout.addLayout(self.verticalLayout_19, 5, 1, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.widget_20 = QWidget(self.frame_4)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy2.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy2)
        self.widget_20.setMinimumSize(QSize(0, 40))
        self.widget_20.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.gridLayout_4 = QGridLayout(self.widget_20)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.AdditionalInformation_14 = QLabel(self.widget_20)
        self.AdditionalInformation_14.setObjectName(u"AdditionalInformation_14")
        sizePolicy2.setHeightForWidth(self.AdditionalInformation_14.sizePolicy().hasHeightForWidth())
        self.AdditionalInformation_14.setSizePolicy(sizePolicy2)
        self.AdditionalInformation_14.setFont(font1)
        self.AdditionalInformation_14.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.AdditionalInformation_14, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.widget_20, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_14, 7, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.back_line = QPushButton(self.frame_4)
        self.back_line.setObjectName(u"back_line")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.back_line.sizePolicy().hasHeightForWidth())
        self.back_line.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.back_line.setFont(font2)
        self.back_line.setStyleSheet(u"QPushButton {\n"
"    border: none;          /* Removes the button border */\n"
"    background: transparent; /* Makes it blend with the background */\n"
"    color: black;          /* Matches QLabel text color */\n"
"    text-align: left;      /* Aligns text like a QLabel (optional) */\n"
"    padding: 0px;          /* Removes extra spacing */\n"
"}")
        icon = QIcon()
        icon.addFile(u":/new/newPrefix/Resources/left-arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/new/newPrefix/Resources/left-arrow.png", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.back_line.setIcon(icon)
        self.back_line.setFlat(True)

        self.horizontalLayout.addWidget(self.back_line)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 4, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_6.addWidget(self.scrollArea_4, 0, 0, 1, 1)


        self.retranslateUi(contacts_create)

        self.gender_combo.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(contacts_create)
    # setupUi

    def retranslateUi(self, contacts_create):
        contacts_create.setWindowTitle(QCoreApplication.translate("contacts_create", u"Edit Contact", None))
        self.save_btn.setText(QCoreApplication.translate("contacts_create", u"Confirm", None))
        self.gender_combo.setItemText(0, QCoreApplication.translate("contacts_create", u"Male", None))
        self.gender_combo.setItemText(1, QCoreApplication.translate("contacts_create", u"Female", None))
        self.gender_combo.setItemText(2, QCoreApplication.translate("contacts_create", u"Other", None))

        self.gender_combo.setPlaceholderText(QCoreApplication.translate("contacts_create", u"Select a gender", None))
        self.GenderLabel_4.setText(QCoreApplication.translate("contacts_create", u"Gender (Optional):", None))
        self.TitleLabel_4.setText(QCoreApplication.translate("contacts_create", u"Job Title (Optional):", None))
        self.CompanyLabel_4.setText(QCoreApplication.translate("contacts_create", u"Company :", None))
        self.SuffixLabel_8.setText(QCoreApplication.translate("contacts_create", u"Phone Number :", None))
        self.FirstNameLabel_4.setText(QCoreApplication.translate("contacts_create", u"First Name :", None))
        self.MiddleNameLabel_8.setText(QCoreApplication.translate("contacts_create", u"Email :", None))
        self.LastNameLabel_4.setText(QCoreApplication.translate("contacts_create", u"Last Name :", None))
        self.StreetLabel_4.setText(QCoreApplication.translate("contacts_create", u"Street :", None))
        self.ZipPostalCodeLabel_4.setText(QCoreApplication.translate("contacts_create", u"Zip/Postal Code :", None))
        self.State_ProvinceLabel_4.setText(QCoreApplication.translate("contacts_create", u"State/Province (Optional):", None))
        self.CityLabel_4.setText(QCoreApplication.translate("contacts_create", u"City :", None))
        self.CountryLabel_4.setText(QCoreApplication.translate("contacts_create", u"Country (Optional) :", None))
        self.AdditionalInformation_15.setText(QCoreApplication.translate("contacts_create", u"Address Information", None))
        self.AdditionalInformation_14.setText(QCoreApplication.translate("contacts_create", u"Address Information", None))
        self.back_line.setText(QCoreApplication.translate("contacts_create", u"< Back to Contacts", None))
    # retranslateUi

