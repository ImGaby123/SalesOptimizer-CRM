# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_contacts(object):
    def setupUi(self, contacts):
        if not contacts.objectName():
            contacts.setObjectName(u"contacts")
        contacts.resize(1201, 682)
        contacts.setStyleSheet(u"background-color: rgb(64, 65, 66);")
        self.verticalLayoutWidget = QWidget(contacts)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 1211, 691))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.verticalLayoutWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.contacts_1 = QWidget()
        self.contacts_1.setObjectName(u"contacts_1")
        self.verticalLayoutWidget_2 = QWidget(self.contacts_1)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 1201, 681))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -2072, 1218, 4018))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1200, 4000))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.BackToContactsBtn = QPushButton(self.frame)
        self.BackToContactsBtn.setObjectName(u"BackToContactsBtn")
        self.BackToContactsBtn.setGeometry(QRect(10, 10, 121, 24))
        self.BackToContactsBtn.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: rgb(0, 0, 0); \n"
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
        self.BackToContactsBtn.setIcon(icon)
        self.NewContacts = QLabel(self.frame)
        self.NewContacts.setObjectName(u"NewContacts")
        self.NewContacts.setGeometry(QRect(560, 70, 81, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.NewContacts.setFont(font)
        self.NewContacts.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(9, 90, 1181, 41))
        self.widget.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.ContactsInformation = QLabel(self.widget)
        self.ContactsInformation.setObjectName(u"ContactsInformation")
        self.ContactsInformation.setGeometry(QRect(20, 10, 131, 21))
        self.ContactsInformation.setFont(font)
        self.ContactsInformation.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.SearcAccount = QLineEdit(self.frame)
        self.SearcAccount.setObjectName(u"SearcAccount")
        self.SearcAccount.setGeometry(QRect(20, 140, 281, 41))
        self.ContactOwner = QLabel(self.frame)
        self.ContactOwner.setObjectName(u"ContactOwner")
        self.ContactOwner.setGeometry(QRect(20, 210, 91, 16))
        self.ContactOwner.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 230, 1121, 101))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ProfilePic = QLabel(self.horizontalLayoutWidget)
        self.ProfilePic.setObjectName(u"ProfilePic")
        self.ProfilePic.setEnabled(True)
        self.ProfilePic.setMaximumSize(QSize(50, 50))
        self.ProfilePic.setStyleSheet(u"QLabel#ProfilePic {\n"
"    width: 50px; /* Palitan ayon sa gusto mong laki */\n"
"    height: 50px;\n"
"    border-radius: 25px; /* Kalahati ng width/height para maging bilog */\n"
"    background-color: #E5DAFB; /* Light purple background */\n"
"    border: 1px solid #D0C4F0; /* Optional: Light border */\n"
"}\n"
"")
        self.ProfilePic.setPixmap(QPixmap(u":/new/newPrefix/Resources/user.png"))
        self.ProfilePic.setScaledContents(True)

        self.horizontalLayout.addWidget(self.ProfilePic)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ProfileName = QLabel(self.horizontalLayoutWidget)
        self.ProfileName.setObjectName(u"ProfileName")
        self.ProfileName.setFont(font)
        self.ProfileName.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.ProfileName.setScaledContents(True)

        self.horizontalLayout.addWidget(self.ProfileName)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.UploadPic = QLineEdit(self.horizontalLayoutWidget)
        self.UploadPic.setObjectName(u"UploadPic")
        self.UploadPic.setMinimumSize(QSize(0, 50))
        self.UploadPic.setStyleSheet(u"")
        self.UploadPic.setCursorPosition(0)

        self.horizontalLayout.addWidget(self.UploadPic)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1100, 320, 61, 24))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"	color: rgb(0, 0, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: blue;\n"
" text-decoration: underline; \n"
"}\n"
"\n"
"\n"
"")
        self.Picture = QLabel(self.frame)
        self.Picture.setObjectName(u"Picture")
        self.Picture.setGeometry(QRect(640, 210, 49, 16))
        self.Picture.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 380, 471, 561))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.NameLabel = QLabel(self.layoutWidget)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setFont(font)
        self.NameLabel.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_3.addWidget(self.NameLabel)

        self.verticalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.SalutationLabel = QLabel(self.layoutWidget)
        self.SalutationLabel.setObjectName(u"SalutationLabel")
        self.SalutationLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_3.addWidget(self.SalutationLabel)

        self.Salutation = QComboBox(self.layoutWidget)
        self.Salutation.addItem("")
        self.Salutation.addItem("")
        self.Salutation.addItem("")
        self.Salutation.addItem("")
        self.Salutation.setObjectName(u"Salutation")
        self.Salutation.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout_3.addWidget(self.Salutation)

        self.verticalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.FirstNameLabel = QLabel(self.layoutWidget)
        self.FirstNameLabel.setObjectName(u"FirstNameLabel")
        self.FirstNameLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_3.addWidget(self.FirstNameLabel)

        self.FirstName = QLineEdit(self.layoutWidget)
        self.FirstName.setObjectName(u"FirstName")
        self.FirstName.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_3.addWidget(self.FirstName)

        self.verticalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.LastNameLabel = QLabel(self.layoutWidget)
        self.LastNameLabel.setObjectName(u"LastNameLabel")
        self.LastNameLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_3.addWidget(self.LastNameLabel)

        self.LastName = QLineEdit(self.layoutWidget)
        self.LastName.setObjectName(u"LastName")
        self.LastName.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_3.addWidget(self.LastName)

        self.verticalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.MiddleNameLabel = QLabel(self.layoutWidget)
        self.MiddleNameLabel.setObjectName(u"MiddleNameLabel")
        self.MiddleNameLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_3.addWidget(self.MiddleNameLabel)

        self.MiddleName = QLineEdit(self.layoutWidget)
        self.MiddleName.setObjectName(u"MiddleName")
        self.MiddleName.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_3.addWidget(self.MiddleName)

        self.verticalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.SuffixLabel = QLabel(self.layoutWidget)
        self.SuffixLabel.setObjectName(u"SuffixLabel")
        self.SuffixLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_3.addWidget(self.SuffixLabel)

        self.Suffix = QLineEdit(self.layoutWidget)
        self.Suffix.setObjectName(u"Suffix")
        self.Suffix.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_3.addWidget(self.Suffix)

        self.layoutWidget_2 = QWidget(self.frame)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(670, 370, 481, 571))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.DateOfBirthLabel = QLabel(self.layoutWidget_2)
        self.DateOfBirthLabel.setObjectName(u"DateOfBirthLabel")
        self.DateOfBirthLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_5.addWidget(self.DateOfBirthLabel)

        self.DateOfBIrth = QLineEdit(self.layoutWidget_2)
        self.DateOfBIrth.setObjectName(u"DateOfBIrth")
        self.DateOfBIrth.setMinimumSize(QSize(0, 0))
        self.DateOfBIrth.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_5.addWidget(self.DateOfBIrth)

        self.verticalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)

        self.LeadStatusLabel = QLabel(self.layoutWidget_2)
        self.LeadStatusLabel.setObjectName(u"LeadStatusLabel")
        self.LeadStatusLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_5.addWidget(self.LeadStatusLabel)

        self.LeadStatus = QComboBox(self.layoutWidget_2)
        self.LeadStatus.addItem("")
        self.LeadStatus.addItem("")
        self.LeadStatus.addItem("")
        self.LeadStatus.addItem("")
        self.LeadStatus.setObjectName(u"LeadStatus")
        self.LeadStatus.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout_5.addWidget(self.LeadStatus)

        self.verticalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)

        self.TitleLabel = QLabel(self.layoutWidget_2)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_5.addWidget(self.TitleLabel)

        self.Title = QLineEdit(self.layoutWidget_2)
        self.Title.setObjectName(u"Title")
        self.Title.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_5.addWidget(self.Title)

        self.verticalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_5.addItem(self.verticalSpacer_9)

        self.MiddleNameLabel_2 = QLabel(self.layoutWidget_2)
        self.MiddleNameLabel_2.setObjectName(u"MiddleNameLabel_2")
        self.MiddleNameLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_5.addWidget(self.MiddleNameLabel_2)

        self.Email = QLineEdit(self.layoutWidget_2)
        self.Email.setObjectName(u"Email")
        self.Email.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_5.addWidget(self.Email)

        self.verticalSpacer_10 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_5.addItem(self.verticalSpacer_10)

        self.SuffixLabel_2 = QLabel(self.layoutWidget_2)
        self.SuffixLabel_2.setObjectName(u"SuffixLabel_2")
        self.SuffixLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_5.addWidget(self.SuffixLabel_2)

        self.Suffix_2 = QLineEdit(self.layoutWidget_2)
        self.Suffix_2.setObjectName(u"Suffix_2")
        self.Suffix_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_5.addWidget(self.Suffix_2)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 1040, 1181, 41))
        self.widget_2.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.AdditionalInformation = QLabel(self.widget_2)
        self.AdditionalInformation.setObjectName(u"AdditionalInformation")
        self.AdditionalInformation.setGeometry(QRect(20, 10, 181, 21))
        self.AdditionalInformation.setFont(font)
        self.AdditionalInformation.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.layoutWidget_3 = QWidget(self.frame)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(40, 1120, 421, 411))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.SecondaryEmailLabel = QLabel(self.layoutWidget_3)
        self.SecondaryEmailLabel.setObjectName(u"SecondaryEmailLabel")
        self.SecondaryEmailLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_6.addWidget(self.SecondaryEmailLabel)

        self.SecondaryEmail = QLineEdit(self.layoutWidget_3)
        self.SecondaryEmail.setObjectName(u"SecondaryEmail")
        self.SecondaryEmail.setMinimumSize(QSize(0, 0))
        self.SecondaryEmail.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_6.addWidget(self.SecondaryEmail)

        self.verticalSpacer_11 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_6.addItem(self.verticalSpacer_11)

        self.OtherPhoneNumLabel = QLabel(self.layoutWidget_3)
        self.OtherPhoneNumLabel.setObjectName(u"OtherPhoneNumLabel")
        self.OtherPhoneNumLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_6.addWidget(self.OtherPhoneNumLabel)

        self.OtherPhoneNum = QLineEdit(self.layoutWidget_3)
        self.OtherPhoneNum.setObjectName(u"OtherPhoneNum")
        self.OtherPhoneNum.setMinimumSize(QSize(0, 0))
        self.OtherPhoneNum.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_6.addWidget(self.OtherPhoneNum)

        self.verticalSpacer_12 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_6.addItem(self.verticalSpacer_12)

        self.GenderLabel = QLabel(self.layoutWidget_3)
        self.GenderLabel.setObjectName(u"GenderLabel")
        self.GenderLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_6.addWidget(self.GenderLabel)

        self.Gender = QLineEdit(self.layoutWidget_3)
        self.Gender.setObjectName(u"Gender")
        self.Gender.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_6.addWidget(self.Gender)

        self.verticalSpacer_13 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_6.addItem(self.verticalSpacer_13)

        self.MaritalStatusLabel = QLabel(self.layoutWidget_3)
        self.MaritalStatusLabel.setObjectName(u"MaritalStatusLabel")
        self.MaritalStatusLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_6.addWidget(self.MaritalStatusLabel)

        self.MaritalStatus = QLineEdit(self.layoutWidget_3)
        self.MaritalStatus.setObjectName(u"MaritalStatus")
        self.MaritalStatus.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_6.addWidget(self.MaritalStatus)

        self.layoutWidget_4 = QWidget(self.frame)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(730, 1120, 401, 281))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.CompanyLabel = QLabel(self.layoutWidget_4)
        self.CompanyLabel.setObjectName(u"CompanyLabel")
        self.CompanyLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_7.addWidget(self.CompanyLabel)

        self.Company = QLineEdit(self.layoutWidget_4)
        self.Company.setObjectName(u"Company")
        self.Company.setMinimumSize(QSize(0, 0))
        self.Company.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_7.addWidget(self.Company)

        self.verticalSpacer_14 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_7.addItem(self.verticalSpacer_14)

        self.ReportsToLabel = QLabel(self.layoutWidget_4)
        self.ReportsToLabel.setObjectName(u"ReportsToLabel")
        self.ReportsToLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_7.addWidget(self.ReportsToLabel)

        self.ReportsTo = QLineEdit(self.layoutWidget_4)
        self.ReportsTo.setObjectName(u"ReportsTo")
        self.ReportsTo.setMinimumSize(QSize(0, 0))
        self.ReportsTo.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_7.addWidget(self.ReportsTo)

        self.verticalSpacer_15 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_7.addItem(self.verticalSpacer_15)

        self.FaxLabel = QLabel(self.layoutWidget_4)
        self.FaxLabel.setObjectName(u"FaxLabel")
        self.FaxLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_7.addWidget(self.FaxLabel)

        self.Fax = QLineEdit(self.layoutWidget_4)
        self.Fax.setObjectName(u"Fax")
        self.Fax.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_7.addWidget(self.Fax)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 1610, 1181, 41))
        self.widget_3.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.AdditionalInformation_2 = QLabel(self.widget_3)
        self.AdditionalInformation_2.setObjectName(u"AdditionalInformation_2")
        self.AdditionalInformation_2.setGeometry(QRect(20, 10, 181, 21))
        self.AdditionalInformation_2.setFont(font)
        self.AdditionalInformation_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.layoutWidget_5 = QWidget(self.frame)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(40, 1690, 421, 411))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.AddressLabel = QLabel(self.layoutWidget_5)
        self.AddressLabel.setObjectName(u"AddressLabel")
        self.AddressLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_8.addWidget(self.AddressLabel)

        self.Address = QLineEdit(self.layoutWidget_5)
        self.Address.setObjectName(u"Address")
        self.Address.setMinimumSize(QSize(0, 0))
        self.Address.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_8.addWidget(self.Address)

        self.verticalSpacer_16 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_8.addItem(self.verticalSpacer_16)

        self.CountryLabel = QLabel(self.layoutWidget_5)
        self.CountryLabel.setObjectName(u"CountryLabel")
        self.CountryLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_8.addWidget(self.CountryLabel)

        self.Country = QLineEdit(self.layoutWidget_5)
        self.Country.setObjectName(u"Country")
        self.Country.setMinimumSize(QSize(0, 0))
        self.Country.setMaximumSize(QSize(300, 300))

        self.verticalLayout_8.addWidget(self.Country)

        self.verticalSpacer_17 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_8.addItem(self.verticalSpacer_17)

        self.State_ProvinceLabel = QLabel(self.layoutWidget_5)
        self.State_ProvinceLabel.setObjectName(u"State_ProvinceLabel")
        self.State_ProvinceLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_8.addWidget(self.State_ProvinceLabel)

        self.StateProvince = QLineEdit(self.layoutWidget_5)
        self.StateProvince.setObjectName(u"StateProvince")
        self.StateProvince.setMaximumSize(QSize(300, 300))

        self.verticalLayout_8.addWidget(self.StateProvince)

        self.verticalSpacer_18 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_8.addItem(self.verticalSpacer_18)

        self.ZipPostalCodeLabel = QLabel(self.layoutWidget_5)
        self.ZipPostalCodeLabel.setObjectName(u"ZipPostalCodeLabel")
        self.ZipPostalCodeLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_8.addWidget(self.ZipPostalCodeLabel)

        self.ZipPostalCode = QLineEdit(self.layoutWidget_5)
        self.ZipPostalCode.setObjectName(u"ZipPostalCode")
        self.ZipPostalCode.setMaximumSize(QSize(300, 300))

        self.verticalLayout_8.addWidget(self.ZipPostalCode)

        self.layoutWidget_6 = QWidget(self.frame)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(720, 1770, 421, 411))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.CityLabel = QLabel(self.layoutWidget_6)
        self.CityLabel.setObjectName(u"CityLabel")
        self.CityLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_9.addWidget(self.CityLabel)

        self.City = QLineEdit(self.layoutWidget_6)
        self.City.setObjectName(u"City")
        self.City.setMinimumSize(QSize(0, 0))
        self.City.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_9.addWidget(self.City)

        self.verticalSpacer_19 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_9.addItem(self.verticalSpacer_19)

        self.StreetLabel = QLabel(self.layoutWidget_6)
        self.StreetLabel.setObjectName(u"StreetLabel")
        self.StreetLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_9.addWidget(self.StreetLabel)

        self.Street = QLabel(self.layoutWidget_6)
        self.Street.setObjectName(u"Street")
        self.Street.setMinimumSize(QSize(0, 300))
        self.Street.setStyleSheet(u" QLabel {\n"
"        border-radius: 50px; /* Half of the width/height */\n"
"       background-color: rgb(108, 108, 108);\n"
"    }\n"
"\n"
"")

        self.verticalLayout_9.addWidget(self.Street)

        self.widget_4 = QWidget(self.frame)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 2230, 1181, 41))
        self.widget_4.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.AdditionalInformation_4 = QLabel(self.widget_4)
        self.AdditionalInformation_4.setObjectName(u"AdditionalInformation_4")
        self.AdditionalInformation_4.setGeometry(QRect(20, 10, 181, 21))
        self.AdditionalInformation_4.setFont(font)
        self.AdditionalInformation_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.widget_5 = QWidget(self.frame)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(10, 2310, 1181, 41))
        self.widget_5.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.AdditionalInformation_5 = QLabel(self.widget_5)
        self.AdditionalInformation_5.setObjectName(u"AdditionalInformation_5")
        self.AdditionalInformation_5.setGeometry(QRect(20, 10, 181, 21))
        self.AdditionalInformation_5.setFont(font)
        self.AdditionalInformation_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 2370, 71, 21))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(860, 2370, 81, 21))
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_4.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.contacts_1)
        self.contacts_3 = QWidget()
        self.contacts_3.setObjectName(u"contacts_3")
        self.stackedWidget.addWidget(self.contacts_3)
        self.contacts_4 = QWidget()
        self.contacts_4.setObjectName(u"contacts_4")
        self.stackedWidget.addWidget(self.contacts_4)
        self.contacts_5 = QWidget()
        self.contacts_5.setObjectName(u"contacts_5")
        self.stackedWidget.addWidget(self.contacts_5)
        self.contacts_2 = QWidget()
        self.contacts_2.setObjectName(u"contacts_2")
        self.stackedWidget.addWidget(self.contacts_2)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(contacts)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(contacts)
    # setupUi

    def retranslateUi(self, contacts):
        contacts.setWindowTitle(QCoreApplication.translate("contacts", u"Form", None))
        self.BackToContactsBtn.setText(QCoreApplication.translate("contacts", u"Back to Contacts", None))
        self.NewContacts.setText(QCoreApplication.translate("contacts", u"New Contact", None))
        self.ContactsInformation.setText(QCoreApplication.translate("contacts", u"Contact Infotmation", None))
        self.SearcAccount.setInputMask("")
        self.SearcAccount.setText("")
        self.SearcAccount.setPlaceholderText(QCoreApplication.translate("contacts", u"Search Account's Name", None))
        self.ContactOwner.setText(QCoreApplication.translate("contacts", u"Contact Owner :", None))
        self.ProfilePic.setText("")
        self.ProfileName.setText(QCoreApplication.translate("contacts", u"Jinita", None))
        self.UploadPic.setInputMask("")
        self.UploadPic.setText("")
        self.pushButton.setText(QCoreApplication.translate("contacts", u"See File", None))
        self.Picture.setText(QCoreApplication.translate("contacts", u"Picture :", None))
        self.NameLabel.setText(QCoreApplication.translate("contacts", u"Name ", None))
        self.SalutationLabel.setText(QCoreApplication.translate("contacts", u"Salutation :", None))
        self.Salutation.setItemText(0, QCoreApplication.translate("contacts", u"New Item", None))
        self.Salutation.setItemText(1, QCoreApplication.translate("contacts", u"New Item", None))
        self.Salutation.setItemText(2, QCoreApplication.translate("contacts", u"New Item", None))
        self.Salutation.setItemText(3, QCoreApplication.translate("contacts", u"New Item", None))

        self.FirstNameLabel.setText(QCoreApplication.translate("contacts", u"First Name :", None))
        self.LastNameLabel.setText(QCoreApplication.translate("contacts", u"Last Name :", None))
        self.MiddleNameLabel.setText(QCoreApplication.translate("contacts", u"Middle Name :", None))
        self.SuffixLabel.setText(QCoreApplication.translate("contacts", u"Suffix :", None))
        self.DateOfBirthLabel.setText(QCoreApplication.translate("contacts", u"Date of Birth :", None))
        self.LeadStatusLabel.setText(QCoreApplication.translate("contacts", u"Lead Status :", None))
        self.LeadStatus.setItemText(0, QCoreApplication.translate("contacts", u"New Item", None))
        self.LeadStatus.setItemText(1, QCoreApplication.translate("contacts", u"New Item", None))
        self.LeadStatus.setItemText(2, QCoreApplication.translate("contacts", u"New Item", None))
        self.LeadStatus.setItemText(3, QCoreApplication.translate("contacts", u"New Item", None))

        self.TitleLabel.setText(QCoreApplication.translate("contacts", u"Title :", None))
        self.MiddleNameLabel_2.setText(QCoreApplication.translate("contacts", u"Email :", None))
        self.SuffixLabel_2.setText(QCoreApplication.translate("contacts", u"Phone Number :", None))
        self.AdditionalInformation.setText(QCoreApplication.translate("contacts", u"ADDITIONAL INFORMATION", None))
        self.SecondaryEmailLabel.setText(QCoreApplication.translate("contacts", u"Secondary Email :", None))
        self.OtherPhoneNumLabel.setText(QCoreApplication.translate("contacts", u"Other Phone Number  :", None))
        self.GenderLabel.setText(QCoreApplication.translate("contacts", u"Gender :", None))
        self.MaritalStatusLabel.setText(QCoreApplication.translate("contacts", u"Marital Status :", None))
        self.CompanyLabel.setText(QCoreApplication.translate("contacts", u"Company :", None))
        self.ReportsToLabel.setText(QCoreApplication.translate("contacts", u" Reports To :", None))
        self.FaxLabel.setText(QCoreApplication.translate("contacts", u"Fax :", None))
        self.AdditionalInformation_2.setText(QCoreApplication.translate("contacts", u"ADDRESS INFORMATION", None))
        self.AddressLabel.setText(QCoreApplication.translate("contacts", u"Address :", None))
        self.CountryLabel.setText(QCoreApplication.translate("contacts", u"Country  :", None))
        self.State_ProvinceLabel.setText(QCoreApplication.translate("contacts", u"State/Province :", None))
        self.ZipPostalCodeLabel.setText(QCoreApplication.translate("contacts", u"Zip/Postal Code :", None))
        self.CityLabel.setText(QCoreApplication.translate("contacts", u"City :", None))
        self.StreetLabel.setText(QCoreApplication.translate("contacts", u"Street :", None))
        self.Street.setText("")
        self.AdditionalInformation_4.setText(QCoreApplication.translate("contacts", u"DESCRIPTION INFORMATION", None))
        self.AdditionalInformation_5.setText(QCoreApplication.translate("contacts", u"ADDRESS INFORMATION", None))
        self.label.setText(QCoreApplication.translate("contacts", u"Created By :", None))
        self.label_2.setText(QCoreApplication.translate("contacts", u"Last Modified :", None))
    # retranslateUi

