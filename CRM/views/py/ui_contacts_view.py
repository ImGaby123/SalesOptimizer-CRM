# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts_view.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_contacts_view(object):
    def setupUi(self, contacts_view):
        if not contacts_view.objectName():
            contacts_view.setObjectName(u"contacts_view")
        contacts_view.resize(1118, 1106)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(contacts_view.sizePolicy().hasHeightForWidth())
        contacts_view.setSizePolicy(sizePolicy)
        contacts_view.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QVBoxLayout(contacts_view)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_4 = QScrollArea(contacts_view)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1094, 1082))
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
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.email_line = QLineEdit(self.frame_4)
        self.email_line.setObjectName(u"email_line")
        self.email_line.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.email_line.sizePolicy().hasHeightForWidth())
        self.email_line.setSizePolicy(sizePolicy1)
        self.email_line.setMinimumSize(QSize(0, 0))
        self.email_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.email_line, 5, 0, 1, 1)

        self.TitleLabel_4 = QLabel(self.frame_4)
        self.TitleLabel_4.setObjectName(u"TitleLabel_4")
        sizePolicy1.setHeightForWidth(self.TitleLabel_4.sizePolicy().hasHeightForWidth())
        self.TitleLabel_4.setSizePolicy(sizePolicy1)
        self.TitleLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.TitleLabel_4, 2, 0, 1, 1)

        self.DateOfBirthLabel_4 = QLabel(self.frame_4)
        self.DateOfBirthLabel_4.setObjectName(u"DateOfBirthLabel_4")
        sizePolicy1.setHeightForWidth(self.DateOfBirthLabel_4.sizePolicy().hasHeightForWidth())
        self.DateOfBirthLabel_4.setSizePolicy(sizePolicy1)
        self.DateOfBirthLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.DateOfBirthLabel_4, 0, 0, 1, 1)

        self.title_line = QLineEdit(self.frame_4)
        self.title_line.setObjectName(u"title_line")
        self.title_line.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.title_line.sizePolicy().hasHeightForWidth())
        self.title_line.setSizePolicy(sizePolicy1)
        self.title_line.setMinimumSize(QSize(0, 0))
        self.title_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.title_line, 3, 0, 1, 1)

        self.phone_line = QLineEdit(self.frame_4)
        self.phone_line.setObjectName(u"phone_line")
        self.phone_line.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.phone_line.sizePolicy().hasHeightForWidth())
        self.phone_line.setSizePolicy(sizePolicy1)
        self.phone_line.setMinimumSize(QSize(0, 0))
        self.phone_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.phone_line, 7, 0, 1, 1)

        self.MiddleNameLabel_8 = QLabel(self.frame_4)
        self.MiddleNameLabel_8.setObjectName(u"MiddleNameLabel_8")
        sizePolicy1.setHeightForWidth(self.MiddleNameLabel_8.sizePolicy().hasHeightForWidth())
        self.MiddleNameLabel_8.setSizePolicy(sizePolicy1)
        self.MiddleNameLabel_8.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.MiddleNameLabel_8, 4, 0, 1, 1)

        self.SuffixLabel_8 = QLabel(self.frame_4)
        self.SuffixLabel_8.setObjectName(u"SuffixLabel_8")
        sizePolicy1.setHeightForWidth(self.SuffixLabel_8.sizePolicy().hasHeightForWidth())
        self.SuffixLabel_8.setSizePolicy(sizePolicy1)
        self.SuffixLabel_8.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.SuffixLabel_8, 6, 0, 1, 1)

        self.dob_date = QDateEdit(self.frame_4)
        self.dob_date.setObjectName(u"dob_date")
        self.dob_date.setEnabled(False)

        self.gridLayout_9.addWidget(self.dob_date, 1, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout_8.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.suffix_line = QLineEdit(self.frame_4)
        self.suffix_line.setObjectName(u"suffix_line")
        self.suffix_line.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.suffix_line.sizePolicy().hasHeightForWidth())
        self.suffix_line.setSizePolicy(sizePolicy1)
        self.suffix_line.setMinimumSize(QSize(0, 0))
        self.suffix_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_10.addWidget(self.suffix_line, 7, 0, 1, 1)

        self.FirstNameLabel_4 = QLabel(self.frame_4)
        self.FirstNameLabel_4.setObjectName(u"FirstNameLabel_4")
        sizePolicy1.setHeightForWidth(self.FirstNameLabel_4.sizePolicy().hasHeightForWidth())
        self.FirstNameLabel_4.setSizePolicy(sizePolicy1)
        self.FirstNameLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.FirstNameLabel_4, 0, 0, 1, 1)

        self.LastNameLabel_4 = QLabel(self.frame_4)
        self.LastNameLabel_4.setObjectName(u"LastNameLabel_4")
        sizePolicy1.setHeightForWidth(self.LastNameLabel_4.sizePolicy().hasHeightForWidth())
        self.LastNameLabel_4.setSizePolicy(sizePolicy1)
        self.LastNameLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.LastNameLabel_4, 2, 0, 1, 1)

        self.lastname_line = QLineEdit(self.frame_4)
        self.lastname_line.setObjectName(u"lastname_line")
        self.lastname_line.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lastname_line.sizePolicy().hasHeightForWidth())
        self.lastname_line.setSizePolicy(sizePolicy1)
        self.lastname_line.setMinimumSize(QSize(0, 0))
        self.lastname_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_10.addWidget(self.lastname_line, 3, 0, 1, 1)

        self.SalutationLabel_4 = QLabel(self.frame_4)
        self.SalutationLabel_4.setObjectName(u"SalutationLabel_4")
        sizePolicy1.setHeightForWidth(self.SalutationLabel_4.sizePolicy().hasHeightForWidth())
        self.SalutationLabel_4.setSizePolicy(sizePolicy1)
        self.SalutationLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.SalutationLabel_4, 4, 0, 1, 1)

        self.firstname_line = QLineEdit(self.frame_4)
        self.firstname_line.setObjectName(u"firstname_line")
        self.firstname_line.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.firstname_line.sizePolicy().hasHeightForWidth())
        self.firstname_line.setSizePolicy(sizePolicy1)
        self.firstname_line.setMinimumSize(QSize(0, 0))
        self.firstname_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_10.addWidget(self.firstname_line, 1, 0, 1, 1)

        self.SuffixLabel_7 = QLabel(self.frame_4)
        self.SuffixLabel_7.setObjectName(u"SuffixLabel_7")
        sizePolicy1.setHeightForWidth(self.SuffixLabel_7.sizePolicy().hasHeightForWidth())
        self.SuffixLabel_7.setSizePolicy(sizePolicy1)
        self.SuffixLabel_7.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.SuffixLabel_7, 6, 0, 1, 1)

        self.middlename = QLineEdit(self.frame_4)
        self.middlename.setObjectName(u"middlename")
        self.middlename.setEnabled(False)

        self.gridLayout_10.addWidget(self.middlename, 5, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_10, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_8, 3, 0, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_19 = QWidget(self.frame_4)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy1.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy1)
        self.widget_19.setMinimumSize(QSize(0, 25))
        self.widget_19.setStyleSheet(u"background-color: rgb(221, 221, 221);")
        self.verticalLayout_10 = QVBoxLayout(self.widget_19)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.ContactsInformation_4 = QLabel(self.widget_19)
        self.ContactsInformation_4.setObjectName(u"ContactsInformation_4")
        sizePolicy1.setHeightForWidth(self.ContactsInformation_4.sizePolicy().hasHeightForWidth())
        self.ContactsInformation_4.setSizePolicy(sizePolicy1)
        self.ContactsInformation_4.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.ContactsInformation_4.setFont(font1)
        self.ContactsInformation_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_10.addWidget(self.ContactsInformation_4)


        self.verticalLayout_19.addWidget(self.widget_19)


        self.gridLayout.addLayout(self.verticalLayout_19, 2, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.country_line = QLineEdit(self.frame_4)
        self.country_line.setObjectName(u"country_line")
        self.country_line.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.country_line.sizePolicy().hasHeightForWidth())
        self.country_line.setSizePolicy(sizePolicy1)
        self.country_line.setMinimumSize(QSize(0, 0))
        self.country_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.country_line, 1, 0, 1, 1)

        self.CountryLabel_4 = QLabel(self.frame_4)
        self.CountryLabel_4.setObjectName(u"CountryLabel_4")
        sizePolicy1.setHeightForWidth(self.CountryLabel_4.sizePolicy().hasHeightForWidth())
        self.CountryLabel_4.setSizePolicy(sizePolicy1)
        self.CountryLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_3.addWidget(self.CountryLabel_4, 0, 0, 1, 1)

        self.zip_line = QLineEdit(self.frame_4)
        self.zip_line.setObjectName(u"zip_line")
        self.zip_line.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.zip_line.sizePolicy().hasHeightForWidth())
        self.zip_line.setSizePolicy(sizePolicy1)
        self.zip_line.setMinimumSize(QSize(0, 0))
        self.zip_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.zip_line, 5, 0, 1, 1)

        self.state_line = QLineEdit(self.frame_4)
        self.state_line.setObjectName(u"state_line")
        self.state_line.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.state_line.sizePolicy().hasHeightForWidth())
        self.state_line.setSizePolicy(sizePolicy1)
        self.state_line.setMinimumSize(QSize(0, 0))
        self.state_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.state_line, 3, 0, 1, 1)

        self.State_ProvinceLabel_4 = QLabel(self.frame_4)
        self.State_ProvinceLabel_4.setObjectName(u"State_ProvinceLabel_4")
        sizePolicy1.setHeightForWidth(self.State_ProvinceLabel_4.sizePolicy().hasHeightForWidth())
        self.State_ProvinceLabel_4.setSizePolicy(sizePolicy1)
        self.State_ProvinceLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_3.addWidget(self.State_ProvinceLabel_4, 2, 0, 1, 1)

        self.ZipPostalCodeLabel_4 = QLabel(self.frame_4)
        self.ZipPostalCodeLabel_4.setObjectName(u"ZipPostalCodeLabel_4")
        sizePolicy1.setHeightForWidth(self.ZipPostalCodeLabel_4.sizePolicy().hasHeightForWidth())
        self.ZipPostalCodeLabel_4.setSizePolicy(sizePolicy1)
        self.ZipPostalCodeLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_3.addWidget(self.ZipPostalCodeLabel_4, 4, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")

        self.gridLayout_23.addLayout(self.verticalLayout_25, 7, 0, 1, 1)

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

        self.street_line = QLineEdit(self.frame_4)
        self.street_line.setObjectName(u"street_line")
        self.street_line.setEnabled(False)

        self.gridLayout_23.addWidget(self.street_line, 5, 0, 1, 1)

        self.city_line = QLineEdit(self.frame_4)
        self.city_line.setObjectName(u"city_line")
        self.city_line.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.city_line.sizePolicy().hasHeightForWidth())
        self.city_line.setSizePolicy(sizePolicy1)

        self.gridLayout_23.addWidget(self.city_line, 1, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.gridLayout_23.addLayout(self.verticalLayout_9, 6, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_23, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_18, 7, 0, 1, 1)

        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.widget_18 = QWidget(self.frame_4)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy1.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy1)
        self.widget_18.setMinimumSize(QSize(0, 40))
        self.widget_18.setStyleSheet(u"background-color: rgb(221, 221, 221);")
        self.gridLayout_7 = QGridLayout(self.widget_18)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.AdditionalInformation_5 = QLabel(self.widget_18)
        self.AdditionalInformation_5.setObjectName(u"AdditionalInformation_5")
        sizePolicy1.setHeightForWidth(self.AdditionalInformation_5.sizePolicy().hasHeightForWidth())
        self.AdditionalInformation_5.setSizePolicy(sizePolicy1)
        self.AdditionalInformation_5.setFont(font1)
        self.AdditionalInformation_5.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_7.addWidget(self.AdditionalInformation_5, 0, 0, 1, 1)


        self.gridLayout_27.addWidget(self.widget_18, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_27, 4, 0, 1, 1)

        self.back_line = QPushButton(self.frame_4)
        self.back_line.setObjectName(u"back_line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.back_line.sizePolicy().hasHeightForWidth())
        self.back_line.setSizePolicy(sizePolicy2)
        self.back_line.setStyleSheet(u"background-color: {rgb(255, 255, 255);\n"
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
        self.back_line.setIcon(icon)

        self.gridLayout.addWidget(self.back_line, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 0, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.widget_20 = QWidget(self.frame_4)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy1.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy1)
        self.widget_20.setMinimumSize(QSize(0, 40))
        self.widget_20.setStyleSheet(u"background-color: rgb(221, 221, 221);")
        self.gridLayout_4 = QGridLayout(self.widget_20)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.AdditionalInformation_14 = QLabel(self.widget_20)
        self.AdditionalInformation_14.setObjectName(u"AdditionalInformation_14")
        sizePolicy1.setHeightForWidth(self.AdditionalInformation_14.sizePolicy().hasHeightForWidth())
        self.AdditionalInformation_14.setSizePolicy(sizePolicy1)
        self.AdditionalInformation_14.setFont(font1)
        self.AdditionalInformation_14.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_4.addWidget(self.AdditionalInformation_14, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.widget_20, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_14, 6, 0, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.company_line = QLineEdit(self.frame_4)
        self.company_line.setObjectName(u"company_line")
        self.company_line.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.company_line.sizePolicy().hasHeightForWidth())
        self.company_line.setSizePolicy(sizePolicy1)
        self.company_line.setMinimumSize(QSize(0, 0))
        self.company_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_17.addWidget(self.company_line, 1, 0, 1, 1)

        self.CompanyLabel_4 = QLabel(self.frame_4)
        self.CompanyLabel_4.setObjectName(u"CompanyLabel_4")
        sizePolicy1.setHeightForWidth(self.CompanyLabel_4.sizePolicy().hasHeightForWidth())
        self.CompanyLabel_4.setSizePolicy(sizePolicy1)
        self.CompanyLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_17.addWidget(self.CompanyLabel_4, 0, 0, 1, 1)

        self.fax_line = QLineEdit(self.frame_4)
        self.fax_line.setObjectName(u"fax_line")
        self.fax_line.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.fax_line.sizePolicy().hasHeightForWidth())
        self.fax_line.setSizePolicy(sizePolicy1)
        self.fax_line.setMinimumSize(QSize(0, 0))
        self.fax_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_17.addWidget(self.fax_line, 3, 0, 1, 1)

        self.FaxLabel_4 = QLabel(self.frame_4)
        self.FaxLabel_4.setObjectName(u"FaxLabel_4")
        sizePolicy1.setHeightForWidth(self.FaxLabel_4.sizePolicy().hasHeightForWidth())
        self.FaxLabel_4.setSizePolicy(sizePolicy1)
        self.FaxLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_17.addWidget(self.FaxLabel_4, 2, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")

        self.gridLayout_17.addLayout(self.verticalLayout_14, 8, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.gridLayout_17.addLayout(self.verticalLayout_8, 4, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_17, 0, 2, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.OtherPhoneNumLabel_4 = QLabel(self.frame_4)
        self.OtherPhoneNumLabel_4.setObjectName(u"OtherPhoneNumLabel_4")
        sizePolicy1.setHeightForWidth(self.OtherPhoneNumLabel_4.sizePolicy().hasHeightForWidth())
        self.OtherPhoneNumLabel_4.setSizePolicy(sizePolicy1)
        self.OtherPhoneNumLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_16.addWidget(self.OtherPhoneNumLabel_4, 3, 0, 1, 1)

        self.gender_combo = QComboBox(self.frame_4)
        self.gender_combo.addItem("")
        self.gender_combo.addItem("")
        self.gender_combo.addItem("")
        self.gender_combo.addItem("")
        self.gender_combo.setObjectName(u"gender_combo")
        self.gender_combo.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.gender_combo.sizePolicy().hasHeightForWidth())
        self.gender_combo.setSizePolicy(sizePolicy1)

        self.gridLayout_16.addWidget(self.gender_combo, 7, 0, 1, 1)

        self.otherphone_line = QLineEdit(self.frame_4)
        self.otherphone_line.setObjectName(u"otherphone_line")
        self.otherphone_line.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.otherphone_line.sizePolicy().hasHeightForWidth())
        self.otherphone_line.setSizePolicy(sizePolicy1)
        self.otherphone_line.setMinimumSize(QSize(0, 0))
        self.otherphone_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_16.addWidget(self.otherphone_line, 4, 0, 1, 1)

        self.SecondaryEmailLabel_4 = QLabel(self.frame_4)
        self.SecondaryEmailLabel_4.setObjectName(u"SecondaryEmailLabel_4")
        sizePolicy1.setHeightForWidth(self.SecondaryEmailLabel_4.sizePolicy().hasHeightForWidth())
        self.SecondaryEmailLabel_4.setSizePolicy(sizePolicy1)
        self.SecondaryEmailLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_16.addWidget(self.SecondaryEmailLabel_4, 0, 0, 1, 1)

        self.secondaryemail_line = QLineEdit(self.frame_4)
        self.secondaryemail_line.setObjectName(u"secondaryemail_line")
        self.secondaryemail_line.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.secondaryemail_line.sizePolicy().hasHeightForWidth())
        self.secondaryemail_line.setSizePolicy(sizePolicy1)
        self.secondaryemail_line.setMinimumSize(QSize(0, 0))
        self.secondaryemail_line.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_16.addWidget(self.secondaryemail_line, 1, 0, 1, 1)

        self.GenderLabel_4 = QLabel(self.frame_4)
        self.GenderLabel_4.setObjectName(u"GenderLabel_4")
        sizePolicy1.setHeightForWidth(self.GenderLabel_4.sizePolicy().hasHeightForWidth())
        self.GenderLabel_4.setSizePolicy(sizePolicy1)
        self.GenderLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_16.addWidget(self.GenderLabel_4, 6, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_16, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_11, 5, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_4, 0, 1, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_3.addWidget(self.scrollArea_4)


        self.retranslateUi(contacts_view)

        QMetaObject.connectSlotsByName(contacts_view)
    # setupUi

    def retranslateUi(self, contacts_view):
        contacts_view.setWindowTitle(QCoreApplication.translate("contacts_view", u"Contact Details", None))
        self.label.setText(QCoreApplication.translate("contacts_view", u"CONTACT DETAILS", None))
        self.TitleLabel_4.setText(QCoreApplication.translate("contacts_view", u"Title :", None))
        self.DateOfBirthLabel_4.setText(QCoreApplication.translate("contacts_view", u"Date of Birth :", None))
        self.MiddleNameLabel_8.setText(QCoreApplication.translate("contacts_view", u"Email :", None))
        self.SuffixLabel_8.setText(QCoreApplication.translate("contacts_view", u"Phone Number :", None))
        self.FirstNameLabel_4.setText(QCoreApplication.translate("contacts_view", u"First Name :", None))
        self.LastNameLabel_4.setText(QCoreApplication.translate("contacts_view", u"Last Name :", None))
        self.SalutationLabel_4.setText(QCoreApplication.translate("contacts_view", u"Middle Name :", None))
        self.SuffixLabel_7.setText(QCoreApplication.translate("contacts_view", u"Suffix :", None))
        self.ContactsInformation_4.setText(QCoreApplication.translate("contacts_view", u"CONTACT INFORMATION", None))
        self.CountryLabel_4.setText(QCoreApplication.translate("contacts_view", u"Country  :", None))
        self.State_ProvinceLabel_4.setText(QCoreApplication.translate("contacts_view", u"State/Province :", None))
        self.ZipPostalCodeLabel_4.setText(QCoreApplication.translate("contacts_view", u"Zip/Postal Code :", None))
        self.StreetLabel_4.setText(QCoreApplication.translate("contacts_view", u"Street :", None))
        self.CityLabel_4.setText(QCoreApplication.translate("contacts_view", u"City :", None))
        self.AdditionalInformation_5.setText(QCoreApplication.translate("contacts_view", u"ADDITIONAL INFORMATION", None))
        self.back_line.setText(QCoreApplication.translate("contacts_view", u"Back to Contacts", None))
        self.AdditionalInformation_14.setText(QCoreApplication.translate("contacts_view", u"ADDRESS INFORMATION", None))
        self.CompanyLabel_4.setText(QCoreApplication.translate("contacts_view", u"Company :", None))
        self.FaxLabel_4.setText(QCoreApplication.translate("contacts_view", u"Fax :", None))
        self.OtherPhoneNumLabel_4.setText(QCoreApplication.translate("contacts_view", u"Other Phone Number  :", None))
        self.gender_combo.setItemText(0, "")
        self.gender_combo.setItemText(1, QCoreApplication.translate("contacts_view", u"Male", None))
        self.gender_combo.setItemText(2, QCoreApplication.translate("contacts_view", u"Female", None))
        self.gender_combo.setItemText(3, QCoreApplication.translate("contacts_view", u"Other", None))

        self.SecondaryEmailLabel_4.setText(QCoreApplication.translate("contacts_view", u"Secondary Email :", None))
        self.GenderLabel_4.setText(QCoreApplication.translate("contacts_view", u"Gender :", None))
    # retranslateUi

