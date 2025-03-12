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
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_contacts_create(object):
    def setupUi(self, contacts_create):
        if not contacts_create.objectName():
            contacts_create.setObjectName(u"contacts_create")
        contacts_create.resize(1118, 1106)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(contacts_create.sizePolicy().hasHeightForWidth())
        contacts_create.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(contacts_create)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_4 = QScrollArea(contacts_create)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1077, 1130))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_4.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_4 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")

        self.gridLayout.addLayout(self.verticalLayout_11, 7, 0, 1, 1)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")

        self.gridLayout.addLayout(self.verticalLayout_31, 5, 0, 1, 1)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")

        self.gridLayout.addLayout(self.verticalLayout_20, 9, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 13, 0, 1, 1)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")

        self.gridLayout_19.addLayout(self.verticalLayout_29, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_19, 12, 0, 1, 1)

        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.widget_18 = QWidget(self.frame_4)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy1.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy1)
        self.widget_18.setMinimumSize(QSize(0, 40))
        self.widget_18.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.gridLayout_7 = QGridLayout(self.widget_18)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.AdditionalInformation_5 = QLabel(self.widget_18)
        self.AdditionalInformation_5.setObjectName(u"AdditionalInformation_5")
        sizePolicy1.setHeightForWidth(self.AdditionalInformation_5.sizePolicy().hasHeightForWidth())
        self.AdditionalInformation_5.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.AdditionalInformation_5.setFont(font)
        self.AdditionalInformation_5.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_7.addWidget(self.AdditionalInformation_5, 0, 0, 1, 1)


        self.gridLayout_27.addWidget(self.widget_18, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_27, 6, 0, 1, 1)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")

        self.gridLayout.addLayout(self.verticalLayout_39, 4, 0, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_19 = QWidget(self.frame_4)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy1.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy1)
        self.widget_19.setMinimumSize(QSize(0, 25))
        self.widget_19.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.verticalLayout_10 = QVBoxLayout(self.widget_19)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.ContactsInformation_4 = QLabel(self.widget_19)
        self.ContactsInformation_4.setObjectName(u"ContactsInformation_4")
        sizePolicy1.setHeightForWidth(self.ContactsInformation_4.sizePolicy().hasHeightForWidth())
        self.ContactsInformation_4.setSizePolicy(sizePolicy1)
        self.ContactsInformation_4.setMinimumSize(QSize(0, 30))
        self.ContactsInformation_4.setFont(font)
        self.ContactsInformation_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_10.addWidget(self.ContactsInformation_4)


        self.verticalLayout_19.addWidget(self.widget_19)


        self.gridLayout.addLayout(self.verticalLayout_19, 2, 0, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")

        self.gridLayout_17.addLayout(self.verticalLayout_12, 4, 0, 1, 1)

        self.Company_4 = QLineEdit(self.frame_4)
        self.Company_4.setObjectName(u"Company_4")
        sizePolicy1.setHeightForWidth(self.Company_4.sizePolicy().hasHeightForWidth())
        self.Company_4.setSizePolicy(sizePolicy1)
        self.Company_4.setMinimumSize(QSize(0, 0))
        self.Company_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_17.addWidget(self.Company_4, 1, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")

        self.gridLayout_17.addLayout(self.verticalLayout_14, 10, 0, 1, 1)

        self.Fax_4 = QLineEdit(self.frame_4)
        self.Fax_4.setObjectName(u"Fax_4")
        sizePolicy1.setHeightForWidth(self.Fax_4.sizePolicy().hasHeightForWidth())
        self.Fax_4.setSizePolicy(sizePolicy1)
        self.Fax_4.setMinimumSize(QSize(0, 0))
        self.Fax_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_17.addWidget(self.Fax_4, 3, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")

        self.gridLayout_17.addLayout(self.verticalLayout_13, 6, 0, 1, 1)

        self.CompanyLabel_4 = QLabel(self.frame_4)
        self.CompanyLabel_4.setObjectName(u"CompanyLabel_4")
        sizePolicy1.setHeightForWidth(self.CompanyLabel_4.sizePolicy().hasHeightForWidth())
        self.CompanyLabel_4.setSizePolicy(sizePolicy1)
        self.CompanyLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_17.addWidget(self.CompanyLabel_4, 0, 0, 1, 1)

        self.FaxLabel_4 = QLabel(self.frame_4)
        self.FaxLabel_4.setObjectName(u"FaxLabel_4")
        sizePolicy1.setHeightForWidth(self.FaxLabel_4.sizePolicy().hasHeightForWidth())
        self.FaxLabel_4.setSizePolicy(sizePolicy1)
        self.FaxLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_17.addWidget(self.FaxLabel_4, 2, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_17, 0, 2, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")

        self.gridLayout_16.addLayout(self.verticalLayout_15, 9, 0, 1, 1)

        self.OtherPhoneNumLabel_4 = QLabel(self.frame_4)
        self.OtherPhoneNumLabel_4.setObjectName(u"OtherPhoneNumLabel_4")
        sizePolicy1.setHeightForWidth(self.OtherPhoneNumLabel_4.sizePolicy().hasHeightForWidth())
        self.OtherPhoneNumLabel_4.setSizePolicy(sizePolicy1)
        self.OtherPhoneNumLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_16.addWidget(self.OtherPhoneNumLabel_4, 3, 0, 1, 1)

        self.OtherPhoneNum_4 = QLineEdit(self.frame_4)
        self.OtherPhoneNum_4.setObjectName(u"OtherPhoneNum_4")
        sizePolicy1.setHeightForWidth(self.OtherPhoneNum_4.sizePolicy().hasHeightForWidth())
        self.OtherPhoneNum_4.setSizePolicy(sizePolicy1)
        self.OtherPhoneNum_4.setMinimumSize(QSize(0, 0))
        self.OtherPhoneNum_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_16.addWidget(self.OtherPhoneNum_4, 4, 0, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")

        self.gridLayout_16.addLayout(self.verticalLayout_16, 11, 0, 1, 1)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)

        self.gridLayout_16.addWidget(self.comboBox, 8, 0, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")

        self.gridLayout_16.addLayout(self.verticalLayout_18, 5, 0, 1, 1)

        self.SecondaryEmailLabel_4 = QLabel(self.frame_4)
        self.SecondaryEmailLabel_4.setObjectName(u"SecondaryEmailLabel_4")
        sizePolicy1.setHeightForWidth(self.SecondaryEmailLabel_4.sizePolicy().hasHeightForWidth())
        self.SecondaryEmailLabel_4.setSizePolicy(sizePolicy1)
        self.SecondaryEmailLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_16.addWidget(self.SecondaryEmailLabel_4, 0, 0, 1, 1)

        self.SecondaryEmail_4 = QLineEdit(self.frame_4)
        self.SecondaryEmail_4.setObjectName(u"SecondaryEmail_4")
        sizePolicy1.setHeightForWidth(self.SecondaryEmail_4.sizePolicy().hasHeightForWidth())
        self.SecondaryEmail_4.setSizePolicy(sizePolicy1)
        self.SecondaryEmail_4.setMinimumSize(QSize(0, 0))
        self.SecondaryEmail_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_16.addWidget(self.SecondaryEmail_4, 1, 0, 1, 1)

        self.GenderLabel_4 = QLabel(self.frame_4)
        self.GenderLabel_4.setObjectName(u"GenderLabel_4")
        sizePolicy1.setHeightForWidth(self.GenderLabel_4.sizePolicy().hasHeightForWidth())
        self.GenderLabel_4.setSizePolicy(sizePolicy1)
        self.GenderLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_16.addWidget(self.GenderLabel_4, 7, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_16, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_11, 8, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")

        self.gridLayout_18.addLayout(self.verticalLayout_32, 1, 0, 1, 1)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.State_ProvinceLabel_4 = QLabel(self.frame_4)
        self.State_ProvinceLabel_4.setObjectName(u"State_ProvinceLabel_4")
        sizePolicy1.setHeightForWidth(self.State_ProvinceLabel_4.sizePolicy().hasHeightForWidth())
        self.State_ProvinceLabel_4.setSizePolicy(sizePolicy1)
        self.State_ProvinceLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_24.addWidget(self.State_ProvinceLabel_4, 4, 0, 1, 1)

        self.StateProvince_4 = QLineEdit(self.frame_4)
        self.StateProvince_4.setObjectName(u"StateProvince_4")
        self.StateProvince_4.setMinimumSize(QSize(0, 0))
        self.StateProvince_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_24.addWidget(self.StateProvince_4, 5, 0, 1, 1)

        self.Country_4 = QLineEdit(self.frame_4)
        self.Country_4.setObjectName(u"Country_4")
        self.Country_4.setMinimumSize(QSize(0, 0))
        self.Country_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_24.addWidget(self.Country_4, 2, 0, 1, 1)

        self.ZipPostalCode_4 = QLineEdit(self.frame_4)
        self.ZipPostalCode_4.setObjectName(u"ZipPostalCode_4")
        self.ZipPostalCode_4.setMinimumSize(QSize(0, 0))
        self.ZipPostalCode_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_24.addWidget(self.ZipPostalCode_4, 8, 0, 1, 1)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")

        self.gridLayout_24.addLayout(self.verticalLayout_22, 3, 0, 1, 1)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")

        self.gridLayout_24.addLayout(self.verticalLayout_24, 6, 0, 1, 1)

        self.ZipPostalCodeLabel_4 = QLabel(self.frame_4)
        self.ZipPostalCodeLabel_4.setObjectName(u"ZipPostalCodeLabel_4")
        sizePolicy1.setHeightForWidth(self.ZipPostalCodeLabel_4.sizePolicy().hasHeightForWidth())
        self.ZipPostalCodeLabel_4.setSizePolicy(sizePolicy1)
        self.ZipPostalCodeLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_24.addWidget(self.ZipPostalCodeLabel_4, 7, 0, 1, 1)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")

        self.gridLayout_24.addLayout(self.verticalLayout_21, 0, 0, 1, 1)

        self.CountryLabel_4 = QLabel(self.frame_4)
        self.CountryLabel_4.setObjectName(u"CountryLabel_4")
        sizePolicy1.setHeightForWidth(self.CountryLabel_4.sizePolicy().hasHeightForWidth())
        self.CountryLabel_4.setSizePolicy(sizePolicy1)
        self.CountryLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_24.addWidget(self.CountryLabel_4, 1, 0, 1, 1)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")

        self.gridLayout_24.addLayout(self.verticalLayout_23, 9, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_24, 0, 0, 1, 1)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.StreetLabel_4 = QLabel(self.frame_4)
        self.StreetLabel_4.setObjectName(u"StreetLabel_4")
        sizePolicy1.setHeightForWidth(self.StreetLabel_4.sizePolicy().hasHeightForWidth())
        self.StreetLabel_4.setSizePolicy(sizePolicy1)
        self.StreetLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_23.addWidget(self.StreetLabel_4, 4, 0, 1, 1)

        self.CityLabel_4 = QLabel(self.frame_4)
        self.CityLabel_4.setObjectName(u"CityLabel_4")
        sizePolicy1.setHeightForWidth(self.CityLabel_4.sizePolicy().hasHeightForWidth())
        self.CityLabel_4.setSizePolicy(sizePolicy1)
        self.CityLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_23.addWidget(self.CityLabel_4, 0, 0, 1, 1)

        self.City_4 = QLineEdit(self.frame_4)
        self.City_4.setObjectName(u"City_4")
        self.City_4.setMinimumSize(QSize(0, 0))
        self.City_4.setMaximumSize(QSize(16777215, 300))

        self.gridLayout_23.addWidget(self.City_4, 6, 0, 1, 1)

        self.Street_4 = QLineEdit(self.frame_4)
        self.Street_4.setObjectName(u"Street_4")
        sizePolicy1.setHeightForWidth(self.Street_4.sizePolicy().hasHeightForWidth())
        self.Street_4.setSizePolicy(sizePolicy1)

        self.gridLayout_23.addWidget(self.Street_4, 1, 0, 1, 1)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")

        self.gridLayout_23.addLayout(self.verticalLayout_25, 7, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_23, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_18, 11, 0, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.widget_20 = QWidget(self.frame_4)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy1.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy1)
        self.widget_20.setMinimumSize(QSize(0, 40))
        self.widget_20.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.gridLayout_4 = QGridLayout(self.widget_20)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.AdditionalInformation_14 = QLabel(self.widget_20)
        self.AdditionalInformation_14.setObjectName(u"AdditionalInformation_14")
        sizePolicy1.setHeightForWidth(self.AdditionalInformation_14.sizePolicy().hasHeightForWidth())
        self.AdditionalInformation_14.setSizePolicy(sizePolicy1)
        self.AdditionalInformation_14.setFont(font)
        self.AdditionalInformation_14.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_4.addWidget(self.AdditionalInformation_14, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.widget_20, 1, 0, 1, 1)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")

        self.gridLayout_14.addLayout(self.verticalLayout_33, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_14, 10, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.LastNameLabel_4 = QLabel(self.frame_4)
        self.LastNameLabel_4.setObjectName(u"LastNameLabel_4")
        sizePolicy1.setHeightForWidth(self.LastNameLabel_4.sizePolicy().hasHeightForWidth())
        self.LastNameLabel_4.setSizePolicy(sizePolicy1)
        self.LastNameLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.LastNameLabel_4, 4, 0, 1, 1)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")

        self.gridLayout_10.addLayout(self.verticalLayout_36, 6, 0, 1, 1)

        self.FirstNameLabel_4 = QLabel(self.frame_4)
        self.FirstNameLabel_4.setObjectName(u"FirstNameLabel_4")
        sizePolicy1.setHeightForWidth(self.FirstNameLabel_4.sizePolicy().hasHeightForWidth())
        self.FirstNameLabel_4.setSizePolicy(sizePolicy1)
        self.FirstNameLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.FirstNameLabel_4, 1, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.gridLayout_10.addLayout(self.verticalLayout_8, 3, 0, 1, 1)

        self.SalutationLabel_4 = QLabel(self.frame_4)
        self.SalutationLabel_4.setObjectName(u"SalutationLabel_4")
        sizePolicy1.setHeightForWidth(self.SalutationLabel_4.sizePolicy().hasHeightForWidth())
        self.SalutationLabel_4.setSizePolicy(sizePolicy1)
        self.SalutationLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.SalutationLabel_4, 7, 0, 1, 1)

        self.SuffixLabel_7 = QLabel(self.frame_4)
        self.SuffixLabel_7.setObjectName(u"SuffixLabel_7")
        sizePolicy1.setHeightForWidth(self.SuffixLabel_7.sizePolicy().hasHeightForWidth())
        self.SuffixLabel_7.setSizePolicy(sizePolicy1)
        self.SuffixLabel_7.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.SuffixLabel_7, 11, 0, 1, 1)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")

        self.gridLayout_10.addLayout(self.verticalLayout_37, 13, 0, 1, 1)

        self.FirstName_4 = QLineEdit(self.frame_4)
        self.FirstName_4.setObjectName(u"FirstName_4")
        sizePolicy1.setHeightForWidth(self.FirstName_4.sizePolicy().hasHeightForWidth())
        self.FirstName_4.setSizePolicy(sizePolicy1)
        self.FirstName_4.setMinimumSize(QSize(0, 0))
        self.FirstName_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_10.addWidget(self.FirstName_4, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_10.addWidget(self.lineEdit, 8, 0, 1, 1)

        self.Suffix_7 = QLineEdit(self.frame_4)
        self.Suffix_7.setObjectName(u"Suffix_7")
        sizePolicy1.setHeightForWidth(self.Suffix_7.sizePolicy().hasHeightForWidth())
        self.Suffix_7.setSizePolicy(sizePolicy1)
        self.Suffix_7.setMinimumSize(QSize(0, 0))
        self.Suffix_7.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_10.addWidget(self.Suffix_7, 12, 0, 1, 1)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")

        self.gridLayout_10.addLayout(self.verticalLayout_38, 0, 0, 1, 1)

        self.LastName_4 = QLineEdit(self.frame_4)
        self.LastName_4.setObjectName(u"LastName_4")
        sizePolicy1.setHeightForWidth(self.LastName_4.sizePolicy().hasHeightForWidth())
        self.LastName_4.setSizePolicy(sizePolicy1)
        self.LastName_4.setMinimumSize(QSize(0, 0))
        self.LastName_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_10.addWidget(self.LastName_4, 5, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.gridLayout_10.addLayout(self.verticalLayout_6, 10, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.gridLayout_10.addLayout(self.verticalLayout_7, 9, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.DateOfBIrth_4 = QLineEdit(self.frame_4)
        self.DateOfBIrth_4.setObjectName(u"DateOfBIrth_4")
        sizePolicy1.setHeightForWidth(self.DateOfBIrth_4.sizePolicy().hasHeightForWidth())
        self.DateOfBIrth_4.setSizePolicy(sizePolicy1)
        self.DateOfBIrth_4.setMinimumSize(QSize(0, 0))
        self.DateOfBIrth_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.DateOfBIrth_4, 2, 0, 1, 1)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")

        self.gridLayout_9.addLayout(self.verticalLayout_35, 0, 0, 1, 1)

        self.Title_4 = QLineEdit(self.frame_4)
        self.Title_4.setObjectName(u"Title_4")
        sizePolicy1.setHeightForWidth(self.Title_4.sizePolicy().hasHeightForWidth())
        self.Title_4.setSizePolicy(sizePolicy1)
        self.Title_4.setMinimumSize(QSize(0, 0))
        self.Title_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.Title_4, 6, 0, 1, 1)

        self.Email_4 = QLineEdit(self.frame_4)
        self.Email_4.setObjectName(u"Email_4")
        sizePolicy1.setHeightForWidth(self.Email_4.sizePolicy().hasHeightForWidth())
        self.Email_4.setSizePolicy(sizePolicy1)
        self.Email_4.setMinimumSize(QSize(0, 0))
        self.Email_4.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.Email_4, 9, 0, 1, 1)

        self.Suffix_8 = QLineEdit(self.frame_4)
        self.Suffix_8.setObjectName(u"Suffix_8")
        sizePolicy1.setHeightForWidth(self.Suffix_8.sizePolicy().hasHeightForWidth())
        self.Suffix_8.setSizePolicy(sizePolicy1)
        self.Suffix_8.setMinimumSize(QSize(0, 0))
        self.Suffix_8.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.Suffix_8, 12, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.gridLayout_9.addLayout(self.verticalLayout_4, 3, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout_9.addLayout(self.verticalLayout, 10, 0, 1, 1)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")

        self.gridLayout_9.addLayout(self.verticalLayout_34, 13, 0, 1, 1)

        self.DateOfBirthLabel_4 = QLabel(self.frame_4)
        self.DateOfBirthLabel_4.setObjectName(u"DateOfBirthLabel_4")
        sizePolicy1.setHeightForWidth(self.DateOfBirthLabel_4.sizePolicy().hasHeightForWidth())
        self.DateOfBirthLabel_4.setSizePolicy(sizePolicy1)
        self.DateOfBirthLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.DateOfBirthLabel_4, 1, 0, 1, 1)

        self.TitleLabel_4 = QLabel(self.frame_4)
        self.TitleLabel_4.setObjectName(u"TitleLabel_4")
        sizePolicy1.setHeightForWidth(self.TitleLabel_4.sizePolicy().hasHeightForWidth())
        self.TitleLabel_4.setSizePolicy(sizePolicy1)
        self.TitleLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.TitleLabel_4, 5, 0, 1, 1)

        self.SuffixLabel_8 = QLabel(self.frame_4)
        self.SuffixLabel_8.setObjectName(u"SuffixLabel_8")
        sizePolicy1.setHeightForWidth(self.SuffixLabel_8.sizePolicy().hasHeightForWidth())
        self.SuffixLabel_8.setSizePolicy(sizePolicy1)
        self.SuffixLabel_8.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.SuffixLabel_8, 11, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.gridLayout_9.addLayout(self.verticalLayout_2, 7, 0, 1, 1)

        self.MiddleNameLabel_8 = QLabel(self.frame_4)
        self.MiddleNameLabel_8.setObjectName(u"MiddleNameLabel_8")
        sizePolicy1.setHeightForWidth(self.MiddleNameLabel_8.sizePolicy().hasHeightForWidth())
        self.MiddleNameLabel_8.setSizePolicy(sizePolicy1)
        self.MiddleNameLabel_8.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.MiddleNameLabel_8, 8, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.gridLayout_9.addLayout(self.verticalLayout_5, 4, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_8, 3, 0, 1, 1)

        self.BackToContactsBtn_4 = QPushButton(self.frame_4)
        self.BackToContactsBtn_4.setObjectName(u"BackToContactsBtn_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.BackToContactsBtn_4.sizePolicy().hasHeightForWidth())
        self.BackToContactsBtn_4.setSizePolicy(sizePolicy2)
        self.BackToContactsBtn_4.setStyleSheet(u"background-color: {rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: blue;\n"
" text-decoration: underline; \n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/new/newPrefix/Resources/left-arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/new/newPrefix/Resources/left-arrow.png", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.BackToContactsBtn_4.setIcon(icon)

        self.gridLayout.addWidget(self.BackToContactsBtn_4, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_4, 0, 1, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_3.addWidget(self.scrollArea_4)


        self.retranslateUi(contacts_create)

        QMetaObject.connectSlotsByName(contacts_create)
    # setupUi

    def retranslateUi(self, contacts_create):
        contacts_create.setWindowTitle(QCoreApplication.translate("contacts_create", u"Add Contact", None))
        self.AdditionalInformation_5.setText(QCoreApplication.translate("contacts_create", u"ADDITIONAL INFORMATION", None))
        self.ContactsInformation_4.setText(QCoreApplication.translate("contacts_create", u"Contact Information", None))
        self.CompanyLabel_4.setText(QCoreApplication.translate("contacts_create", u"Company :", None))
        self.FaxLabel_4.setText(QCoreApplication.translate("contacts_create", u"Fax :", None))
        self.OtherPhoneNumLabel_4.setText(QCoreApplication.translate("contacts_create", u"Other Phone Number  :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("contacts_create", u"Male", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("contacts_create", u"Female", None))

        self.SecondaryEmailLabel_4.setText(QCoreApplication.translate("contacts_create", u"Secondary Email :", None))
        self.GenderLabel_4.setText(QCoreApplication.translate("contacts_create", u"Gender :", None))
        self.State_ProvinceLabel_4.setText(QCoreApplication.translate("contacts_create", u"State/Province :", None))
        self.ZipPostalCodeLabel_4.setText(QCoreApplication.translate("contacts_create", u"Zip/Postal Code :", None))
        self.CountryLabel_4.setText(QCoreApplication.translate("contacts_create", u"Country  :", None))
        self.StreetLabel_4.setText(QCoreApplication.translate("contacts_create", u"Street :", None))
        self.CityLabel_4.setText(QCoreApplication.translate("contacts_create", u"City :", None))
        self.AdditionalInformation_14.setText(QCoreApplication.translate("contacts_create", u"ADDRESS INFORMATION", None))
        self.LastNameLabel_4.setText(QCoreApplication.translate("contacts_create", u"Last Name :", None))
        self.FirstNameLabel_4.setText(QCoreApplication.translate("contacts_create", u"First Name :", None))
        self.SalutationLabel_4.setText(QCoreApplication.translate("contacts_create", u"Middle Name :", None))
        self.SuffixLabel_7.setText(QCoreApplication.translate("contacts_create", u"Suffix :", None))
        self.DateOfBirthLabel_4.setText(QCoreApplication.translate("contacts_create", u"Date of Birth :", None))
        self.TitleLabel_4.setText(QCoreApplication.translate("contacts_create", u"Title :", None))
        self.SuffixLabel_8.setText(QCoreApplication.translate("contacts_create", u"Phone Number :", None))
        self.MiddleNameLabel_8.setText(QCoreApplication.translate("contacts_create", u"Email :", None))
        self.BackToContactsBtn_4.setText(QCoreApplication.translate("contacts_create", u"Back to Contacts", None))
    # retranslateUi

