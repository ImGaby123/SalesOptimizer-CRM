# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
import views.py.icons_rc

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1222, 2522))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1200, 2500))
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
        self.stackedWidget_2 = QStackedWidget(self.contacts_3)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(0, 0, 1201, 681))
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.contacts_6 = QWidget()
        self.contacts_6.setObjectName(u"contacts_6")
        self.label_3 = QLabel(self.contacts_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(530, 50, 101, 20))
        self.stackedWidget_2.addWidget(self.contacts_6)
        self.contacts_7 = QWidget()
        self.contacts_7.setObjectName(u"contacts_7")
        self.tableWidget = QTableWidget(self.contacts_7)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 201, 1161, 451))
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	border: 2px solid black\n"
"}\n"
"")
        self.allContacts = QComboBox(self.contacts_7)
        self.allContacts.setObjectName(u"allContacts")
        self.allContacts.setGeometry(QRect(20, 150, 161, 31))
        self.allContacts.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid black;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.allContacts.setEditable(False)
        self.label_4 = QLabel(self.contacts_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 121, 41))
        self.label_4.setStyleSheet(u"font: 18pt \"Segoe UI\";\n"
"background: transparent;")
        self.search = QLineEdit(self.contacts_7)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(20, 80, 391, 51))
        self.search.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.search.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.search.setClearButtonEnabled(False)
        self.horizontalLayoutWidget_2 = QWidget(self.contacts_7)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(1030, 90, 151, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.add = QPushButton(self.horizontalLayoutWidget_2)
        self.add.setObjectName(u"add")
        self.add.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/new/newPrefix/Resources/plus (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add.setIcon(icon1)
        self.add.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.add)

        self.refresh = QPushButton(self.horizontalLayoutWidget_2)
        self.refresh.setObjectName(u"refresh")
        self.refresh.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	border: transparent;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/new/newPrefix/Resources/refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh.setIcon(icon2)
        self.refresh.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.refresh)

        self.delete_2 = QPushButton(self.horizontalLayoutWidget_2)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/new/newPrefix/Resources/trash-circle-svgrepo-com.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_2.setIcon(icon3)
        self.delete_2.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.delete_2)

        self.horizontalLayoutWidget_3 = QWidget(self.contacts_7)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(1073, 240, 124, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.history = QPushButton(self.horizontalLayoutWidget_3)
        self.history.setObjectName(u"history")
        self.history.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/new/newPrefix/Resources/clock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.history.setIcon(icon4)
        self.history.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.history)

        self.mail = QPushButton(self.horizontalLayoutWidget_3)
        self.mail.setObjectName(u"mail")
        self.mail.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	border: transparent;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/new/newPrefix/Resources/email.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mail.setIcon(icon5)
        self.mail.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.mail)

        self.more = QPushButton(self.horizontalLayoutWidget_3)
        self.more.setObjectName(u"more")
        self.more.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/new/newPrefix/Resources/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.more.setIcon(icon6)
        self.more.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.more)

        self.stackedWidget_2.addWidget(self.contacts_7)
        self.contacts_8 = QWidget()
        self.contacts_8.setObjectName(u"contacts_8")
        self.backToContacts = QPushButton(self.contacts_8)
        self.backToContacts.setObjectName(u"backToContacts")
        self.backToContacts.setGeometry(QRect(10, 10, 141, 41))
        self.backToContacts.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: rgb(0, 0, 0); \n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/new/newPrefix/Resources/left-arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backToContacts.setIcon(icon7)
        self.backToContacts.setIconSize(QSize(15, 15))
        self.sales_pipeline = QFrame(self.contacts_8)
        self.sales_pipeline.setObjectName(u"sales_pipeline")
        self.sales_pipeline.setGeometry(QRect(20, 100, 1151, 101))
        self.sales_pipeline.setStyleSheet(u"QFrame {\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}")
        self.sales_pipeline.setFrameShape(QFrame.Shape.StyledPanel)
        self.sales_pipeline.setFrameShadow(QFrame.Shadow.Raised)
        self.SalesPipeline = QLabel(self.sales_pipeline)
        self.SalesPipeline.setObjectName(u"SalesPipeline")
        self.SalesPipeline.setGeometry(QRect(20, 40, 91, 20))
        self.SalesPipeline.setStyleSheet(u"QLabel{\n"
"	font: 9pt \"Segoe UI\";\n"
"	border: none;\n"
"}")
        self.progressBar = QProgressBar(self.sales_pipeline)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(150, 40, 991, 16))
        self.progressBar.setValue(100)
        self.prospecting = QLabel(self.sales_pipeline)
        self.prospecting.setObjectName(u"prospecting")
        self.prospecting.setGeometry(QRect(120, 60, 71, 20))
        self.prospecting.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.qualifications = QLabel(self.sales_pipeline)
        self.qualifications.setObjectName(u"qualifications")
        self.qualifications.setGeometry(QRect(240, 60, 81, 20))
        self.qualifications.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.contacting = QLabel(self.sales_pipeline)
        self.contacting.setObjectName(u"contacting")
        self.contacting.setGeometry(QRect(360, 60, 61, 20))
        self.contacting.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.building_relationship = QLabel(self.sales_pipeline)
        self.building_relationship.setObjectName(u"building_relationship")
        self.building_relationship.setGeometry(QRect(480, 60, 121, 20))
        self.building_relationship.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.negotiating_with_the_lead = QLabel(self.sales_pipeline)
        self.negotiating_with_the_lead.setObjectName(u"negotiating_with_the_lead")
        self.negotiating_with_the_lead.setGeometry(QRect(660, 60, 141, 20))
        self.negotiating_with_the_lead.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.closed_won = QLabel(self.sales_pipeline)
        self.closed_won.setObjectName(u"closed_won")
        self.closed_won.setGeometry(QRect(950, 60, 71, 20))
        self.closed_won.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.closing = QLabel(self.sales_pipeline)
        self.closing.setObjectName(u"closing")
        self.closing.setGeometry(QRect(850, 60, 41, 20))
        self.closing.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.closed_loss = QLabel(self.sales_pipeline)
        self.closed_loss.setObjectName(u"closed_loss")
        self.closed_loss.setGeometry(QRect(1070, 60, 71, 20))
        self.closed_loss.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.timeline = QFrame(self.contacts_8)
        self.timeline.setObjectName(u"timeline")
        self.timeline.setGeometry(QRect(230, 220, 581, 441))
        self.timeline.setStyleSheet(u"QFrame {\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}")
        self.timeline.setFrameShape(QFrame.Shape.StyledPanel)
        self.timeline.setFrameShadow(QFrame.Shadow.Raised)
        self.Timeline = QLabel(self.timeline)
        self.Timeline.setObjectName(u"Timeline")
        self.Timeline.setGeometry(QRect(250, 10, 71, 20))
        self.Timeline.setStyleSheet(u"QLabel{\n"
"	font: 10pt \"Segoe UI\";\n"
"	border: none;\n"
"}")
        self.search_2 = QLineEdit(self.timeline)
        self.search_2.setObjectName(u"search_2")
        self.search_2.setGeometry(QRect(20, 50, 541, 41))
        self.search_2.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.horizontalLayoutWidget_4 = QWidget(self.timeline)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(440, 10, 124, 32))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pin = QPushButton(self.horizontalLayoutWidget_4)
        self.pin.setObjectName(u"pin")
        self.pin.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/new/newPrefix/Resources/pin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pin.setIcon(icon8)
        self.pin.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.pin)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/new/newPrefix/Resources/bars.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon9)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.label_9 = QLabel(self.timeline)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 410, 541, 21))
        self.label_9.setStyleSheet(u"QLabel{\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	border: none;\n"
"}")
        self.horizontalLayoutWidget_5 = QWidget(self.timeline)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(14, 390, 551, 31))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.edit = QPushButton(self.horizontalLayoutWidget_5)
        self.edit.setObjectName(u"edit")
        self.edit.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/new/newPrefix/Resources/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.edit.setIcon(icon10)

        self.horizontalLayout_5.addWidget(self.edit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.link = QPushButton(self.horizontalLayoutWidget_5)
        self.link.setObjectName(u"link")
        self.link.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/new/newPrefix/Resources/link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.link.setIcon(icon11)

        self.horizontalLayout_5.addWidget(self.link)

        self.attachment = QPushButton(self.horizontalLayoutWidget_5)
        self.attachment.setObjectName(u"attachment")
        self.attachment.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/new/newPrefix/Resources/attach-document.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.attachment.setIcon(icon12)

        self.horizontalLayout_5.addWidget(self.attachment)

        self.contact_information = QFrame(self.contacts_8)
        self.contact_information.setObjectName(u"contact_information")
        self.contact_information.setGeometry(QRect(820, 220, 351, 441))
        self.contact_information.setStyleSheet(u"QFrame {\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}")
        self.contact_information.setFrameShape(QFrame.Shape.StyledPanel)
        self.contact_information.setFrameShadow(QFrame.Shadow.Raised)
        self.ContactInformation = QLabel(self.contact_information)
        self.ContactInformation.setObjectName(u"ContactInformation")
        self.ContactInformation.setGeometry(QRect(110, 10, 161, 20))
        self.ContactInformation.setStyleSheet(u"QLabel{\n"
"	font: 10pt \"Segoe UI\";\n"
"	border: none;\n"
"}")
        self.tableWidget_2 = QTableWidget(self.contacts_8)
        if (self.tableWidget_2.columnCount() < 1):
            self.tableWidget_2.setColumnCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(20, 220, 201, 441))
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"	border: 2px solid black;\n"
"	border-radius: 10px;\n"
"}")
        self.stackedWidget_2.addWidget(self.contacts_8)
        self.contacts_9 = QWidget()
        self.contacts_9.setObjectName(u"contacts_9")
        self.label_5 = QLabel(self.contacts_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(540, 60, 101, 20))
        self.stackedWidget_2.addWidget(self.contacts_9)
        self.contacts_10 = QWidget()
        self.contacts_10.setObjectName(u"contacts_10")
        self.label_6 = QLabel(self.contacts_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(540, 60, 101, 20))
        self.stackedWidget_2.addWidget(self.contacts_10)
        self.stackedWidget.addWidget(self.contacts_3)
        self.contacts_4 = QWidget()
        self.contacts_4.setObjectName(u"contacts_4")
        self.stackedWidget_3 = QStackedWidget(self.contacts_4)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setGeometry(QRect(0, 0, 1201, 681))
        self.stackedWidget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.contacts_11 = QWidget()
        self.contacts_11.setObjectName(u"contacts_11")
        self.label_7 = QLabel(self.contacts_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(530, 50, 101, 20))
        self.stackedWidget_3.addWidget(self.contacts_11)
        self.contacts_12 = QWidget()
        self.contacts_12.setObjectName(u"contacts_12")
        self.tableWidget_3 = QTableWidget(self.contacts_12)
        if (self.tableWidget_3.columnCount() < 4):
            self.tableWidget_3.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(20, 201, 1161, 451))
        self.tableWidget_3.setStyleSheet(u"QTableWidget{\n"
"	border: 2px solid black\n"
"}\n"
"")
        self.allContacts_2 = QComboBox(self.contacts_12)
        self.allContacts_2.setObjectName(u"allContacts_2")
        self.allContacts_2.setGeometry(QRect(20, 150, 161, 31))
        self.allContacts_2.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid black;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.allContacts_2.setEditable(False)
        self.label_8 = QLabel(self.contacts_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 10, 121, 41))
        self.label_8.setStyleSheet(u"font: 18pt \"Segoe UI\";\n"
"background: transparent;")
        self.search_3 = QLineEdit(self.contacts_12)
        self.search_3.setObjectName(u"search_3")
        self.search_3.setGeometry(QRect(20, 80, 391, 51))
        self.search_3.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.search_3.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.search_3.setClearButtonEnabled(False)
        self.horizontalLayoutWidget_6 = QWidget(self.contacts_12)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(1030, 90, 151, 42))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.add_2 = QPushButton(self.horizontalLayoutWidget_6)
        self.add_2.setObjectName(u"add_2")
        self.add_2.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.add_2.setIcon(icon1)
        self.add_2.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.add_2)

        self.refresh_2 = QPushButton(self.horizontalLayoutWidget_6)
        self.refresh_2.setObjectName(u"refresh_2")
        self.refresh_2.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	border: transparent;\n"
"}")
        self.refresh_2.setIcon(icon2)
        self.refresh_2.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.refresh_2)

        self.delete_3 = QPushButton(self.horizontalLayoutWidget_6)
        self.delete_3.setObjectName(u"delete_3")
        self.delete_3.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.delete_3.setIcon(icon3)
        self.delete_3.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.delete_3)

        self.horizontalLayoutWidget_7 = QWidget(self.contacts_12)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(1073, 240, 124, 31))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.history_2 = QPushButton(self.horizontalLayoutWidget_7)
        self.history_2.setObjectName(u"history_2")
        self.history_2.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.history_2.setIcon(icon4)
        self.history_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.history_2)

        self.mail_2 = QPushButton(self.horizontalLayoutWidget_7)
        self.mail_2.setObjectName(u"mail_2")
        self.mail_2.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	border: transparent;\n"
"}")
        self.mail_2.setIcon(icon5)
        self.mail_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.mail_2)

        self.more_2 = QPushButton(self.horizontalLayoutWidget_7)
        self.more_2.setObjectName(u"more_2")
        self.more_2.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.more_2.setIcon(icon6)
        self.more_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.more_2)

        self.stackedWidget_3.addWidget(self.contacts_12)
        self.contacts_13 = QWidget()
        self.contacts_13.setObjectName(u"contacts_13")
        self.backToContacts_2 = QPushButton(self.contacts_13)
        self.backToContacts_2.setObjectName(u"backToContacts_2")
        self.backToContacts_2.setGeometry(QRect(10, 10, 141, 41))
        self.backToContacts_2.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: rgb(0, 0, 0); \n"
"}")
        self.backToContacts_2.setIcon(icon7)
        self.backToContacts_2.setIconSize(QSize(15, 15))
        self.sales_pipeline_2 = QFrame(self.contacts_13)
        self.sales_pipeline_2.setObjectName(u"sales_pipeline_2")
        self.sales_pipeline_2.setGeometry(QRect(20, 100, 1151, 101))
        self.sales_pipeline_2.setStyleSheet(u"QFrame {\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}")
        self.sales_pipeline_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.sales_pipeline_2.setFrameShadow(QFrame.Shadow.Raised)
        self.SalesPipeline_2 = QLabel(self.sales_pipeline_2)
        self.SalesPipeline_2.setObjectName(u"SalesPipeline_2")
        self.SalesPipeline_2.setGeometry(QRect(20, 40, 91, 20))
        self.SalesPipeline_2.setStyleSheet(u"QLabel{\n"
"	font: 9pt \"Segoe UI\";\n"
"	border: none;\n"
"}")
        self.progressBar_2 = QProgressBar(self.sales_pipeline_2)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(150, 40, 991, 16))
        self.progressBar_2.setValue(100)
        self.prospecting_2 = QLabel(self.sales_pipeline_2)
        self.prospecting_2.setObjectName(u"prospecting_2")
        self.prospecting_2.setGeometry(QRect(120, 60, 71, 20))
        self.prospecting_2.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.qualifications_2 = QLabel(self.sales_pipeline_2)
        self.qualifications_2.setObjectName(u"qualifications_2")
        self.qualifications_2.setGeometry(QRect(240, 60, 81, 20))
        self.qualifications_2.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.contacting_2 = QLabel(self.sales_pipeline_2)
        self.contacting_2.setObjectName(u"contacting_2")
        self.contacting_2.setGeometry(QRect(360, 60, 61, 20))
        self.contacting_2.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.building_relationship_2 = QLabel(self.sales_pipeline_2)
        self.building_relationship_2.setObjectName(u"building_relationship_2")
        self.building_relationship_2.setGeometry(QRect(480, 60, 121, 20))
        self.building_relationship_2.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.negotiating_with_the_lead_2 = QLabel(self.sales_pipeline_2)
        self.negotiating_with_the_lead_2.setObjectName(u"negotiating_with_the_lead_2")
        self.negotiating_with_the_lead_2.setGeometry(QRect(660, 60, 141, 20))
        self.negotiating_with_the_lead_2.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.closed_won_2 = QLabel(self.sales_pipeline_2)
        self.closed_won_2.setObjectName(u"closed_won_2")
        self.closed_won_2.setGeometry(QRect(950, 60, 71, 20))
        self.closed_won_2.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.closing_2 = QLabel(self.sales_pipeline_2)
        self.closing_2.setObjectName(u"closing_2")
        self.closing_2.setGeometry(QRect(850, 60, 41, 20))
        self.closing_2.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.closed_loss_2 = QLabel(self.sales_pipeline_2)
        self.closed_loss_2.setObjectName(u"closed_loss_2")
        self.closed_loss_2.setGeometry(QRect(1070, 60, 71, 20))
        self.closed_loss_2.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")
        self.timeline_2 = QFrame(self.contacts_13)
        self.timeline_2.setObjectName(u"timeline_2")
        self.timeline_2.setGeometry(QRect(230, 220, 581, 441))
        self.timeline_2.setStyleSheet(u"QFrame {\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}")
        self.timeline_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.timeline_2.setFrameShadow(QFrame.Shadow.Raised)
        self.Timeline_2 = QLabel(self.timeline_2)
        self.Timeline_2.setObjectName(u"Timeline_2")
        self.Timeline_2.setGeometry(QRect(250, 10, 71, 20))
        self.Timeline_2.setStyleSheet(u"QLabel{\n"
"	font: 10pt \"Segoe UI\";\n"
"	border: none;\n"
"}")
        self.search_4 = QLineEdit(self.timeline_2)
        self.search_4.setObjectName(u"search_4")
        self.search_4.setGeometry(QRect(20, 50, 541, 41))
        self.search_4.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.horizontalLayoutWidget_8 = QWidget(self.timeline_2)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(440, 10, 124, 32))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pin_2 = QPushButton(self.horizontalLayoutWidget_8)
        self.pin_2.setObjectName(u"pin_2")
        self.pin_2.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.pin_2.setIcon(icon8)
        self.pin_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.pin_2)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.pushButton_4.setIcon(icon9)
        self.pushButton_4.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.horizontalLayoutWidget_8)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.pushButton_5)

        self.label_10 = QLabel(self.timeline_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 410, 541, 21))
        self.label_10.setStyleSheet(u"QLabel{\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	border: none;\n"
"}")
        self.horizontalLayoutWidget_9 = QWidget(self.timeline_2)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(14, 390, 551, 31))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.edit_2 = QPushButton(self.horizontalLayoutWidget_9)
        self.edit_2.setObjectName(u"edit_2")
        self.edit_2.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.edit_2.setIcon(icon10)

        self.horizontalLayout_9.addWidget(self.edit_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.link_2 = QPushButton(self.horizontalLayoutWidget_9)
        self.link_2.setObjectName(u"link_2")
        self.link_2.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.link_2.setIcon(icon11)

        self.horizontalLayout_9.addWidget(self.link_2)

        self.attachment_2 = QPushButton(self.horizontalLayoutWidget_9)
        self.attachment_2.setObjectName(u"attachment_2")
        self.attachment_2.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.attachment_2.setIcon(icon12)

        self.horizontalLayout_9.addWidget(self.attachment_2)

        self.contact_information_2 = QFrame(self.contacts_13)
        self.contact_information_2.setObjectName(u"contact_information_2")
        self.contact_information_2.setGeometry(QRect(820, 220, 351, 441))
        self.contact_information_2.setStyleSheet(u"QFrame {\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}")
        self.contact_information_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.contact_information_2.setFrameShadow(QFrame.Shadow.Raised)
        self.ContactInformation_2 = QLabel(self.contact_information_2)
        self.ContactInformation_2.setObjectName(u"ContactInformation_2")
        self.ContactInformation_2.setGeometry(QRect(110, 10, 161, 20))
        self.ContactInformation_2.setStyleSheet(u"QLabel{\n"
"	font: 10pt \"Segoe UI\";\n"
"	border: none;\n"
"}")
        self.tableWidget_4 = QTableWidget(self.contacts_13)
        if (self.tableWidget_4.columnCount() < 1):
            self.tableWidget_4.setColumnCount(1)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(20, 220, 201, 441))
        self.tableWidget_4.setStyleSheet(u"QTableWidget{\n"
"	border: 2px solid black;\n"
"	border-radius: 10px;\n"
"}")
        self.stackedWidget_3.addWidget(self.contacts_13)
        self.contacts_14 = QWidget()
        self.contacts_14.setObjectName(u"contacts_14")
        self.label_11 = QLabel(self.contacts_14)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(540, 60, 101, 20))
        self.stackedWidget_3.addWidget(self.contacts_14)
        self.contacts_15 = QWidget()
        self.contacts_15.setObjectName(u"contacts_15")
        self.label_12 = QLabel(self.contacts_15)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(540, 60, 101, 20))
        self.stackedWidget_3.addWidget(self.contacts_15)
        self.stackedWidget.addWidget(self.contacts_4)
        self.contacts_5 = QWidget()
        self.contacts_5.setObjectName(u"contacts_5")
        self.stackedWidget_4 = QStackedWidget(self.contacts_5)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.stackedWidget_4.setGeometry(QRect(0, 0, 1200, 675))
        self.stackedWidget_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.contacts_16 = QWidget()
        self.contacts_16.setObjectName(u"contacts_16")
        self.label_13 = QLabel(self.contacts_16)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(530, 50, 101, 20))
        self.stackedWidget_4.addWidget(self.contacts_16)
        self.contacts_17 = QWidget()
        self.contacts_17.setObjectName(u"contacts_17")
        self.label_14 = QLabel(self.contacts_17)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(560, 50, 101, 20))
        self.stackedWidget_4.addWidget(self.contacts_17)
        self.contacts_18 = QWidget()
        self.contacts_18.setObjectName(u"contacts_18")
        self.label_15 = QLabel(self.contacts_18)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(540, 60, 101, 20))
        self.stackedWidget_4.addWidget(self.contacts_18)
        self.contact_details = QWidget()
        self.contact_details.setObjectName(u"contact_details")
        self.contact_details.setStyleSheet(u"")
        self.back_to_contacts = QPushButton(self.contact_details)
        self.back_to_contacts.setObjectName(u"back_to_contacts")
        self.back_to_contacts.setGeometry(QRect(0, 0, 171, 41))
        font1 = QFont()
        font1.setPointSize(14)
        self.back_to_contacts.setFont(font1)
        self.back_to_contacts.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.logo_user = QLabel(self.contact_details)
        self.logo_user.setObjectName(u"logo_user")
        self.logo_user.setGeometry(QRect(10, 70, 21, 31))
        self.logo_user.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.logo_user.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.company_ni_gab = QLabel(self.contact_details)
        self.company_ni_gab.setObjectName(u"company_ni_gab")
        self.company_ni_gab.setGeometry(QRect(40, 70, 151, 31))
        self.company_ni_gab.setFont(font1)
        self.company_ni_gab.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.contact_information_3 = QListView(self.contact_details)
        self.contact_information_3.setObjectName(u"contact_information_3")
        self.contact_information_3.setGeometry(QRect(250, 230, 611, 431))
        self.sales_pipeline_3 = QLabel(self.contact_details)
        self.sales_pipeline_3.setObjectName(u"sales_pipeline_3")
        self.sales_pipeline_3.setGeometry(QRect(20, 130, 101, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.sales_pipeline_3.setFont(font2)
        self.sales_pipeline_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.sales_pipeline_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sales_pipeline_3.setWordWrap(False)
        self.prospecting_3 = QLabel(self.contact_details)
        self.prospecting_3.setObjectName(u"prospecting_3")
        self.prospecting_3.setGeometry(QRect(130, 170, 71, 16))
        self.prospecting_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.qualifications_3 = QLabel(self.contact_details)
        self.qualifications_3.setObjectName(u"qualifications_3")
        self.qualifications_3.setGeometry(QRect(250, 170, 81, 16))
        self.qualifications_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.contacting_3 = QLabel(self.contact_details)
        self.contacting_3.setObjectName(u"contacting_3")
        self.contacting_3.setGeometry(QRect(380, 170, 81, 16))
        self.contacting_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.building_relationship_3 = QLabel(self.contact_details)
        self.building_relationship_3.setObjectName(u"building_relationship_3")
        self.building_relationship_3.setGeometry(QRect(520, 170, 121, 16))
        self.building_relationship_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.negotiating = QLabel(self.contact_details)
        self.negotiating.setObjectName(u"negotiating")
        self.negotiating.setGeometry(QRect(690, 170, 141, 16))
        self.negotiating.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.closing_3 = QLabel(self.contact_details)
        self.closing_3.setObjectName(u"closing_3")
        self.closing_3.setGeometry(QRect(880, 170, 51, 16))
        self.closing_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.closed_won_3 = QLabel(self.contact_details)
        self.closed_won_3.setObjectName(u"closed_won_3")
        self.closed_won_3.setGeometry(QRect(980, 170, 81, 16))
        self.closed_won_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.closed_loss_3 = QLabel(self.contact_details)
        self.closed_loss_3.setObjectName(u"closed_loss_3")
        self.closed_loss_3.setGeometry(QRect(1100, 170, 81, 16))
        self.closed_loss_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.contact_info = QLabel(self.contact_details)
        self.contact_info.setObjectName(u"contact_info")
        self.contact_info.setGeometry(QRect(470, 250, 211, 31))
        font3 = QFont()
        font3.setPointSize(16)
        self.contact_info.setFont(font3)
        self.contact_info.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.contact_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar_3 = QProgressBar(self.contact_details)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setGeometry(QRect(150, 140, 1031, 23))
        self.progressBar_3.setValue(24)
        self.contact = QListView(self.contact_details)
        self.contact.setObjectName(u"contact")
        self.contact.setGeometry(QRect(10, 230, 211, 431))
        self.sales_funnel = QListView(self.contact_details)
        self.sales_funnel.setObjectName(u"sales_funnel")
        self.sales_funnel.setGeometry(QRect(890, 230, 291, 431))
        self.sales_funnel_label = QLabel(self.contact_details)
        self.sales_funnel_label.setObjectName(u"sales_funnel_label")
        self.sales_funnel_label.setGeometry(QRect(940, 240, 211, 31))
        self.sales_funnel_label.setFont(font3)
        self.sales_funnel_label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.sales_funnel_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.contacts_label = QLabel(self.contact_details)
        self.contacts_label.setObjectName(u"contacts_label")
        self.contacts_label.setGeometry(QRect(60, 240, 101, 31))
        self.contacts_label.setFont(font3)
        self.contacts_label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.contacts_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_2 = QFrame(self.contact_details)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 120, 1181, 91))
        self.frame_2.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget_4.addWidget(self.contact_details)
        self.contact_information_3.raise_()
        self.sales_pipeline_3.raise_()
        self.prospecting_3.raise_()
        self.qualifications_3.raise_()
        self.contacting_3.raise_()
        self.building_relationship_3.raise_()
        self.closing_3.raise_()
        self.closed_won_3.raise_()
        self.closed_loss_3.raise_()
        self.progressBar_3.raise_()
        self.frame_2.raise_()
        self.back_to_contacts.raise_()
        self.company_ni_gab.raise_()
        self.logo_user.raise_()
        self.negotiating.raise_()
        self.contact_info.raise_()
        self.contact.raise_()
        self.sales_funnel.raise_()
        self.sales_funnel_label.raise_()
        self.contacts_label.raise_()
        self.email_page = QWidget()
        self.email_page.setObjectName(u"email_page")
        self.to_label = QLabel(self.email_page)
        self.to_label.setObjectName(u"to_label")
        self.to_label.setGeometry(QRect(20, 20, 91, 31))
        self.to_label.setFont(font3)
        self.to_label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.from_label = QLabel(self.email_page)
        self.from_label.setObjectName(u"from_label")
        self.from_label.setGeometry(QRect(20, 70, 91, 31))
        self.from_label.setFont(font3)
        self.from_label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.subject_label = QLabel(self.email_page)
        self.subject_label.setObjectName(u"subject_label")
        self.subject_label.setGeometry(QRect(20, 140, 91, 31))
        self.subject_label.setFont(font3)
        self.subject_label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.to_line = QLineEdit(self.email_page)
        self.to_line.setObjectName(u"to_line")
        self.to_line.setGeometry(QRect(130, 10, 1041, 51))
        self.to_line.setStyleSheet(u"border: 2px solid #C0C0C0; /* Gray border */\n"
"    border-radius: 4px; /* Smooth edges */\n"
"    padding: 6px; /* Space inside the field */\n"
"    font-size: 14px;\n"
"color: rgb(0, 0, 0);")
        self.from_line = QLineEdit(self.email_page)
        self.from_line.setObjectName(u"from_line")
        self.from_line.setGeometry(QRect(130, 60, 1041, 51))
        self.from_line.setStyleSheet(u"border: 2px solid #C0C0C0; /* Gray border */\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 4px; /* Smooth edges */\n"
"    padding: 6px; /* Space inside the field */\n"
"    font-size: 14px;")
        self.subject_line = QLineEdit(self.email_page)
        self.subject_line.setObjectName(u"subject_line")
        self.subject_line.setGeometry(QRect(130, 130, 1041, 51))
        self.subject_line.setStyleSheet(u"border: 2px solid #C0C0C0; /* Gray border */\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 4px; /* Smooth edges */\n"
"    padding: 6px; /* Space inside the field */\n"
"    font-size: 14px;")
        self.email_body = QTextEdit(self.email_page)
        self.email_body.setObjectName(u"email_body")
        self.email_body.setGeometry(QRect(10, 200, 1171, 401))
        self.email_body.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.bold_button = QPushButton(self.email_page)
        self.bold_button.setObjectName(u"bold_button")
        self.bold_button.setGeometry(QRect(10, 610, 31, 31))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.bold_button.setFont(font4)
        self.bold_button.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.italic_button = QPushButton(self.email_page)
        self.italic_button.setObjectName(u"italic_button")
        self.italic_button.setGeometry(QRect(40, 610, 31, 31))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(16)
        font5.setBold(False)
        font5.setItalic(True)
        self.italic_button.setFont(font5)
        self.italic_button.setStyleSheet(u"\n"
"\n"
"color: rgb(0, 0, 0);")
        self.underline_button = QPushButton(self.email_page)
        self.underline_button.setObjectName(u"underline_button")
        self.underline_button.setGeometry(QRect(70, 610, 31, 31))
        font6 = QFont()
        font6.setPointSize(16)
        font6.setBold(False)
        font6.setUnderline(True)
        self.underline_button.setFont(font6)
        self.underline_button.setStyleSheet(u"\n"
"\n"
"color: rgb(0, 0, 0);")
        self.send_button = QPushButton(self.email_page)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setGeometry(QRect(10, 640, 91, 31))
        self.send_button.setFont(font2)
        self.send_button.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.text_combo = QComboBox(self.email_page)
        self.text_combo.addItem("")
        self.text_combo.setObjectName(u"text_combo")
        self.text_combo.setGeometry(QRect(280, 650, 51, 22))
        self.text_combo.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.text_combo.setEditable(False)
        self.size_combo = QComboBox(self.email_page)
        self.size_combo.addItem("")
        self.size_combo.setObjectName(u"size_combo")
        self.size_combo.setGeometry(QRect(330, 650, 41, 22))
        self.size_combo.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.size_combo.setEditable(False)
        self.more_combo = QComboBox(self.email_page)
        self.more_combo.addItem("")
        self.more_combo.setObjectName(u"more_combo")
        self.more_combo.setGeometry(QRect(280, 610, 71, 31))
        self.more_combo.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.more_combo.setEditable(False)
        self.insert_combo = QComboBox(self.email_page)
        self.insert_combo.addItem("")
        self.insert_combo.setObjectName(u"insert_combo")
        self.insert_combo.setGeometry(QRect(130, 610, 71, 31))
        self.insert_combo.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.insert_combo.setEditable(False)
        self.letter_combo = QComboBox(self.email_page)
        self.letter_combo.addItem("")
        self.letter_combo.setObjectName(u"letter_combo")
        self.letter_combo.setGeometry(QRect(370, 650, 41, 22))
        self.letter_combo.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.letter_combo.setEditable(False)
        self.cc_button = QPushButton(self.email_page)
        self.cc_button.setObjectName(u"cc_button")
        self.cc_button.setGeometry(QRect(1080, 30, 41, 31))
        font7 = QFont()
        font7.setUnderline(True)
        self.cc_button.setFont(font7)
        self.cc_button.setStyleSheet(u"\n"
"    color: #007bff;  /* Bootstrap-like blue color */\n"
"    background: transparent;\n"
"    border: none;\n"
"    text-decoration: underline;\n"
"    font-size: 20px;\n"
"")
        self.bcc_button = QPushButton(self.email_page)
        self.bcc_button.setObjectName(u"bcc_button")
        self.bcc_button.setGeometry(QRect(1130, 30, 41, 31))
        self.bcc_button.setFont(font7)
        self.bcc_button.setStyleSheet(u"\n"
"    color: #007bff;  /* Bootstrap-like blue color */\n"
"    background: transparent;\n"
"    border: none;\n"
"    text-decoration: underline;\n"
"    font-size: 20px;\n"
"")
        self.stackedWidget_4.addWidget(self.email_page)
        self.stackedWidget.addWidget(self.contacts_5)
        self.contacts_2 = QWidget()
        self.contacts_2.setObjectName(u"contacts_2")
        self.stackedWidget_5 = QStackedWidget(self.contacts_2)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.stackedWidget_5.setGeometry(QRect(0, 0, 1200, 675))
        self.stackedWidget_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.contacts_19 = QWidget()
        self.contacts_19.setObjectName(u"contacts_19")
        self.label_16 = QLabel(self.contacts_19)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(530, 50, 101, 20))
        self.stackedWidget_5.addWidget(self.contacts_19)
        self.contacts_20 = QWidget()
        self.contacts_20.setObjectName(u"contacts_20")
        self.label_17 = QLabel(self.contacts_20)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(560, 50, 101, 20))
        self.stackedWidget_5.addWidget(self.contacts_20)
        self.contacts_21 = QWidget()
        self.contacts_21.setObjectName(u"contacts_21")
        self.label_18 = QLabel(self.contacts_21)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(540, 60, 101, 20))
        self.stackedWidget_5.addWidget(self.contacts_21)
        self.contact_details_2 = QWidget()
        self.contact_details_2.setObjectName(u"contact_details_2")
        self.contact_details_2.setStyleSheet(u"")
        self.back_to_contacts_2 = QPushButton(self.contact_details_2)
        self.back_to_contacts_2.setObjectName(u"back_to_contacts_2")
        self.back_to_contacts_2.setGeometry(QRect(0, 0, 171, 41))
        self.back_to_contacts_2.setFont(font1)
        self.back_to_contacts_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.logo_user_2 = QLabel(self.contact_details_2)
        self.logo_user_2.setObjectName(u"logo_user_2")
        self.logo_user_2.setGeometry(QRect(10, 70, 21, 31))
        self.logo_user_2.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.logo_user_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.company_ni_gab_2 = QLabel(self.contact_details_2)
        self.company_ni_gab_2.setObjectName(u"company_ni_gab_2")
        self.company_ni_gab_2.setGeometry(QRect(40, 70, 151, 31))
        self.company_ni_gab_2.setFont(font1)
        self.company_ni_gab_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.contact_information_4 = QListView(self.contact_details_2)
        self.contact_information_4.setObjectName(u"contact_information_4")
        self.contact_information_4.setGeometry(QRect(250, 230, 611, 431))
        self.sales_pipeline_4 = QLabel(self.contact_details_2)
        self.sales_pipeline_4.setObjectName(u"sales_pipeline_4")
        self.sales_pipeline_4.setGeometry(QRect(20, 130, 101, 41))
        self.sales_pipeline_4.setFont(font2)
        self.sales_pipeline_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.sales_pipeline_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sales_pipeline_4.setWordWrap(False)
        self.prospecting_4 = QLabel(self.contact_details_2)
        self.prospecting_4.setObjectName(u"prospecting_4")
        self.prospecting_4.setGeometry(QRect(130, 170, 71, 16))
        self.prospecting_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.qualifications_4 = QLabel(self.contact_details_2)
        self.qualifications_4.setObjectName(u"qualifications_4")
        self.qualifications_4.setGeometry(QRect(250, 170, 81, 16))
        self.qualifications_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.contacting_4 = QLabel(self.contact_details_2)
        self.contacting_4.setObjectName(u"contacting_4")
        self.contacting_4.setGeometry(QRect(380, 170, 81, 16))
        self.contacting_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.building_relationship_4 = QLabel(self.contact_details_2)
        self.building_relationship_4.setObjectName(u"building_relationship_4")
        self.building_relationship_4.setGeometry(QRect(520, 170, 121, 16))
        self.building_relationship_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.negotiating_2 = QLabel(self.contact_details_2)
        self.negotiating_2.setObjectName(u"negotiating_2")
        self.negotiating_2.setGeometry(QRect(690, 170, 141, 16))
        self.negotiating_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.closing_4 = QLabel(self.contact_details_2)
        self.closing_4.setObjectName(u"closing_4")
        self.closing_4.setGeometry(QRect(880, 170, 51, 16))
        self.closing_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.closed_won_4 = QLabel(self.contact_details_2)
        self.closed_won_4.setObjectName(u"closed_won_4")
        self.closed_won_4.setGeometry(QRect(980, 170, 81, 16))
        self.closed_won_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.closed_loss_4 = QLabel(self.contact_details_2)
        self.closed_loss_4.setObjectName(u"closed_loss_4")
        self.closed_loss_4.setGeometry(QRect(1100, 170, 81, 16))
        self.closed_loss_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.contact_info_2 = QLabel(self.contact_details_2)
        self.contact_info_2.setObjectName(u"contact_info_2")
        self.contact_info_2.setGeometry(QRect(470, 250, 211, 31))
        self.contact_info_2.setFont(font3)
        self.contact_info_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.contact_info_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar_4 = QProgressBar(self.contact_details_2)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setGeometry(QRect(150, 140, 1031, 23))
        self.progressBar_4.setValue(24)
        self.contact_2 = QListView(self.contact_details_2)
        self.contact_2.setObjectName(u"contact_2")
        self.contact_2.setGeometry(QRect(10, 230, 211, 431))
        self.sales_funnel_2 = QListView(self.contact_details_2)
        self.sales_funnel_2.setObjectName(u"sales_funnel_2")
        self.sales_funnel_2.setGeometry(QRect(890, 230, 291, 431))
        self.sales_funnel_label_2 = QLabel(self.contact_details_2)
        self.sales_funnel_label_2.setObjectName(u"sales_funnel_label_2")
        self.sales_funnel_label_2.setGeometry(QRect(940, 240, 211, 31))
        self.sales_funnel_label_2.setFont(font3)
        self.sales_funnel_label_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.sales_funnel_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.contacts_label_2 = QLabel(self.contact_details_2)
        self.contacts_label_2.setObjectName(u"contacts_label_2")
        self.contacts_label_2.setGeometry(QRect(60, 240, 101, 31))
        self.contacts_label_2.setFont(font3)
        self.contacts_label_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.contacts_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_3 = QFrame(self.contact_details_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 120, 1181, 91))
        self.frame_3.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget_5.addWidget(self.contact_details_2)
        self.email_page_2 = QWidget()
        self.email_page_2.setObjectName(u"email_page_2")
        self.to_label_2 = QLabel(self.email_page_2)
        self.to_label_2.setObjectName(u"to_label_2")
        self.to_label_2.setGeometry(QRect(20, 20, 91, 31))
        self.to_label_2.setFont(font3)
        self.to_label_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.from_label_2 = QLabel(self.email_page_2)
        self.from_label_2.setObjectName(u"from_label_2")
        self.from_label_2.setGeometry(QRect(20, 70, 91, 31))
        self.from_label_2.setFont(font3)
        self.from_label_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.subject_label_2 = QLabel(self.email_page_2)
        self.subject_label_2.setObjectName(u"subject_label_2")
        self.subject_label_2.setGeometry(QRect(20, 140, 91, 31))
        self.subject_label_2.setFont(font3)
        self.subject_label_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.to_line_2 = QLineEdit(self.email_page_2)
        self.to_line_2.setObjectName(u"to_line_2")
        self.to_line_2.setGeometry(QRect(130, 10, 1041, 51))
        self.to_line_2.setStyleSheet(u"border: 2px solid #C0C0C0; /* Gray border */\n"
"    border-radius: 4px; /* Smooth edges */\n"
"    padding: 6px; /* Space inside the field */\n"
"    font-size: 14px;\n"
"color: rgb(0, 0, 0);")
        self.from_line_2 = QLineEdit(self.email_page_2)
        self.from_line_2.setObjectName(u"from_line_2")
        self.from_line_2.setGeometry(QRect(130, 60, 1041, 51))
        self.from_line_2.setStyleSheet(u"border: 2px solid #C0C0C0; /* Gray border */\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 4px; /* Smooth edges */\n"
"    padding: 6px; /* Space inside the field */\n"
"    font-size: 14px;")
        self.subject_line_2 = QLineEdit(self.email_page_2)
        self.subject_line_2.setObjectName(u"subject_line_2")
        self.subject_line_2.setGeometry(QRect(130, 130, 1041, 51))
        self.subject_line_2.setStyleSheet(u"border: 2px solid #C0C0C0; /* Gray border */\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 4px; /* Smooth edges */\n"
"    padding: 6px; /* Space inside the field */\n"
"    font-size: 14px;")
        self.email_body_2 = QTextEdit(self.email_page_2)
        self.email_body_2.setObjectName(u"email_body_2")
        self.email_body_2.setGeometry(QRect(10, 200, 1171, 401))
        self.email_body_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.bold_button_2 = QPushButton(self.email_page_2)
        self.bold_button_2.setObjectName(u"bold_button_2")
        self.bold_button_2.setGeometry(QRect(10, 610, 31, 31))
        self.bold_button_2.setFont(font4)
        self.bold_button_2.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")
        self.italic_button_2 = QPushButton(self.email_page_2)
        self.italic_button_2.setObjectName(u"italic_button_2")
        self.italic_button_2.setGeometry(QRect(40, 610, 31, 31))
        self.italic_button_2.setFont(font5)
        self.italic_button_2.setStyleSheet(u"\n"
"\n"
"color: rgb(0, 0, 0);")
        self.underline_button_2 = QPushButton(self.email_page_2)
        self.underline_button_2.setObjectName(u"underline_button_2")
        self.underline_button_2.setGeometry(QRect(70, 610, 31, 31))
        self.underline_button_2.setFont(font6)
        self.underline_button_2.setStyleSheet(u"\n"
"\n"
"color: rgb(0, 0, 0);")
        self.send_button_2 = QPushButton(self.email_page_2)
        self.send_button_2.setObjectName(u"send_button_2")
        self.send_button_2.setGeometry(QRect(10, 640, 91, 31))
        self.send_button_2.setFont(font2)
        self.send_button_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.text_combo_2 = QComboBox(self.email_page_2)
        self.text_combo_2.addItem("")
        self.text_combo_2.setObjectName(u"text_combo_2")
        self.text_combo_2.setGeometry(QRect(280, 650, 51, 22))
        self.text_combo_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.text_combo_2.setEditable(False)
        self.size_combo_2 = QComboBox(self.email_page_2)
        self.size_combo_2.addItem("")
        self.size_combo_2.setObjectName(u"size_combo_2")
        self.size_combo_2.setGeometry(QRect(330, 650, 41, 22))
        self.size_combo_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.size_combo_2.setEditable(False)
        self.more_combo_2 = QComboBox(self.email_page_2)
        self.more_combo_2.addItem("")
        self.more_combo_2.setObjectName(u"more_combo_2")
        self.more_combo_2.setGeometry(QRect(280, 610, 71, 31))
        self.more_combo_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.more_combo_2.setEditable(False)
        self.insert_combo_2 = QComboBox(self.email_page_2)
        self.insert_combo_2.addItem("")
        self.insert_combo_2.setObjectName(u"insert_combo_2")
        self.insert_combo_2.setGeometry(QRect(130, 610, 71, 31))
        self.insert_combo_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.insert_combo_2.setEditable(False)
        self.letter_combo_2 = QComboBox(self.email_page_2)
        self.letter_combo_2.addItem("")
        self.letter_combo_2.setObjectName(u"letter_combo_2")
        self.letter_combo_2.setGeometry(QRect(370, 650, 41, 22))
        self.letter_combo_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.letter_combo_2.setEditable(False)
        self.cc_button_2 = QPushButton(self.email_page_2)
        self.cc_button_2.setObjectName(u"cc_button_2")
        self.cc_button_2.setGeometry(QRect(1080, 30, 41, 31))
        self.cc_button_2.setFont(font7)
        self.cc_button_2.setStyleSheet(u"\n"
"    color: #007bff;  /* Bootstrap-like blue color */\n"
"    background: transparent;\n"
"    border: none;\n"
"    text-decoration: underline;\n"
"    font-size: 20px;\n"
"")
        self.bcc_button_2 = QPushButton(self.email_page_2)
        self.bcc_button_2.setObjectName(u"bcc_button_2")
        self.bcc_button_2.setGeometry(QRect(1130, 30, 41, 31))
        self.bcc_button_2.setFont(font7)
        self.bcc_button_2.setStyleSheet(u"\n"
"    color: #007bff;  /* Bootstrap-like blue color */\n"
"    background: transparent;\n"
"    border: none;\n"
"    text-decoration: underline;\n"
"    font-size: 20px;\n"
"")
        self.stackedWidget_5.addWidget(self.email_page_2)
        self.stackedWidget.addWidget(self.contacts_2)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(contacts)

        self.stackedWidget.setCurrentIndex(4)
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(2)
        self.stackedWidget_4.setCurrentIndex(4)
        self.stackedWidget_5.setCurrentIndex(3)


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
        self.label_3.setText(QCoreApplication.translate("contacts", u"Arcas Page 1", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("contacts", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("contacts", u"Email", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("contacts", u"Phone Number", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("contacts", u"Company", None));
        self.allContacts.setPlaceholderText(QCoreApplication.translate("contacts", u"All Contacts", None))
        self.label_4.setText(QCoreApplication.translate("contacts", u"Contacts", None))
        self.search.setPlaceholderText(QCoreApplication.translate("contacts", u"Search", None))
        self.add.setText("")
        self.refresh.setText("")
        self.delete_2.setText("")
        self.history.setText("")
        self.mail.setText("")
        self.more.setText("")
        self.backToContacts.setText(QCoreApplication.translate("contacts", u"Back To Contacts", None))
        self.SalesPipeline.setText(QCoreApplication.translate("contacts", u"Sales Pipeline", None))
        self.progressBar.setFormat("")
        self.prospecting.setText(QCoreApplication.translate("contacts", u"Prospecting", None))
        self.qualifications.setText(QCoreApplication.translate("contacts", u"Qualifications", None))
        self.contacting.setText(QCoreApplication.translate("contacts", u"Contacting", None))
        self.building_relationship.setText(QCoreApplication.translate("contacts", u"Building Relationship", None))
        self.negotiating_with_the_lead.setText(QCoreApplication.translate("contacts", u"Negotiating with the Lead", None))
        self.closed_won.setText(QCoreApplication.translate("contacts", u"Closed Won", None))
        self.closing.setText(QCoreApplication.translate("contacts", u"Closing", None))
        self.closed_loss.setText(QCoreApplication.translate("contacts", u"Closed Loss", None))
        self.Timeline.setText(QCoreApplication.translate("contacts", u"Timeline", None))
        self.search_2.setPlaceholderText(QCoreApplication.translate("contacts", u"Search", None))
        self.pin.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label_9.setText(QCoreApplication.translate("contacts", u"______________________________________________________________________________________________________________", None))
        self.edit.setText("")
        self.link.setText("")
        self.attachment.setText("")
        self.ContactInformation.setText(QCoreApplication.translate("contacts", u"Contact Information", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("contacts", u"Contacts", None));
        self.label_5.setText(QCoreApplication.translate("contacts", u"Abuan Page 4", None))
        self.label_6.setText(QCoreApplication.translate("contacts", u"Abuan Page 5", None))
        self.label_7.setText(QCoreApplication.translate("contacts", u"Arcas Page 1", None))
        ___qtablewidgetitem5 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("contacts", u"Name", None));
        ___qtablewidgetitem6 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("contacts", u"Email", None));
        ___qtablewidgetitem7 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("contacts", u"Phone Number", None));
        ___qtablewidgetitem8 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("contacts", u"Company", None));
        self.allContacts_2.setPlaceholderText(QCoreApplication.translate("contacts", u"All Contacts", None))
        self.label_8.setText(QCoreApplication.translate("contacts", u"Contacts", None))
        self.search_3.setPlaceholderText(QCoreApplication.translate("contacts", u"Search", None))
        self.add_2.setText("")
        self.refresh_2.setText("")
        self.delete_3.setText("")
        self.history_2.setText("")
        self.mail_2.setText("")
        self.more_2.setText("")
        self.backToContacts_2.setText(QCoreApplication.translate("contacts", u"Back To Contacts", None))
        self.SalesPipeline_2.setText(QCoreApplication.translate("contacts", u"Sales Pipeline", None))
        self.progressBar_2.setFormat("")
        self.prospecting_2.setText(QCoreApplication.translate("contacts", u"Prospecting", None))
        self.qualifications_2.setText(QCoreApplication.translate("contacts", u"Qualifications", None))
        self.contacting_2.setText(QCoreApplication.translate("contacts", u"Contacting", None))
        self.building_relationship_2.setText(QCoreApplication.translate("contacts", u"Building Relationship", None))
        self.negotiating_with_the_lead_2.setText(QCoreApplication.translate("contacts", u"Negotiating with the Lead", None))
        self.closed_won_2.setText(QCoreApplication.translate("contacts", u"Closed Won", None))
        self.closing_2.setText(QCoreApplication.translate("contacts", u"Closing", None))
        self.closed_loss_2.setText(QCoreApplication.translate("contacts", u"Closed Loss", None))
        self.Timeline_2.setText(QCoreApplication.translate("contacts", u"Timeline", None))
        self.search_4.setPlaceholderText(QCoreApplication.translate("contacts", u"Search", None))
        self.pin_2.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.label_10.setText(QCoreApplication.translate("contacts", u"______________________________________________________________________________________________________________", None))
        self.edit_2.setText("")
        self.link_2.setText("")
        self.attachment_2.setText("")
        self.ContactInformation_2.setText(QCoreApplication.translate("contacts", u"Contact Information", None))
        ___qtablewidgetitem9 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("contacts", u"Contacts", None));
        self.label_11.setText(QCoreApplication.translate("contacts", u"Abuan Page 4", None))
        self.label_12.setText(QCoreApplication.translate("contacts", u"Abuan Page 5", None))
        self.label_13.setText(QCoreApplication.translate("contacts", u"Arcas Page 1", None))
        self.label_14.setText(QCoreApplication.translate("contacts", u"Awal Page 2", None))
        self.label_15.setText(QCoreApplication.translate("contacts", u"Awal Page 3", None))
        self.back_to_contacts.setText(QCoreApplication.translate("contacts", u"< Back to Contacts", None))
        self.logo_user.setText(QCoreApplication.translate("contacts", u"G", None))
        self.company_ni_gab.setText(QCoreApplication.translate("contacts", u"Company ni Gab", None))
        self.sales_pipeline_3.setText(QCoreApplication.translate("contacts", u"Sales Pipeline", None))
        self.prospecting_3.setText(QCoreApplication.translate("contacts", u"Prospecting", None))
        self.qualifications_3.setText(QCoreApplication.translate("contacts", u"Qualifications", None))
        self.contacting_3.setText(QCoreApplication.translate("contacts", u"Contacting", None))
        self.building_relationship_3.setText(QCoreApplication.translate("contacts", u"Building Relationship", None))
        self.negotiating.setText(QCoreApplication.translate("contacts", u"Negotiating with the lead", None))
        self.closing_3.setText(QCoreApplication.translate("contacts", u"Closing", None))
        self.closed_won_3.setText(QCoreApplication.translate("contacts", u"Closed Won", None))
        self.closed_loss_3.setText(QCoreApplication.translate("contacts", u"Closed Loss", None))
        self.contact_info.setText(QCoreApplication.translate("contacts", u"Contact Information", None))
        self.sales_funnel_label.setText(QCoreApplication.translate("contacts", u"Sales Funnel", None))
        self.contacts_label.setText(QCoreApplication.translate("contacts", u"Contacts", None))
        self.to_label.setText(QCoreApplication.translate("contacts", u"To:", None))
        self.from_label.setText(QCoreApplication.translate("contacts", u"From:", None))
        self.subject_label.setText(QCoreApplication.translate("contacts", u"Subject:", None))
        self.email_body.setHtml(QCoreApplication.translate("contacts", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bold_button.setText(QCoreApplication.translate("contacts", u"B", None))
        self.italic_button.setText(QCoreApplication.translate("contacts", u"I", None))
        self.underline_button.setText(QCoreApplication.translate("contacts", u"U", None))
        self.send_button.setText(QCoreApplication.translate("contacts", u"Send", None))
        self.text_combo.setItemText(0, QCoreApplication.translate("contacts", u"Arial", None))

#if QT_CONFIG(accessibility)
        self.text_combo.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.text_combo.setCurrentText(QCoreApplication.translate("contacts", u"Arial", None))
        self.size_combo.setItemText(0, QCoreApplication.translate("contacts", u"11", None))

        self.size_combo.setCurrentText(QCoreApplication.translate("contacts", u"11", None))
        self.more_combo.setItemText(0, QCoreApplication.translate("contacts", u"More", None))

        self.more_combo.setCurrentText(QCoreApplication.translate("contacts", u"More", None))
        self.insert_combo.setItemText(0, QCoreApplication.translate("contacts", u"Insert", None))

        self.insert_combo.setCurrentText(QCoreApplication.translate("contacts", u"Insert", None))
        self.letter_combo.setItemText(0, QCoreApplication.translate("contacts", u"A", None))

        self.letter_combo.setCurrentText(QCoreApplication.translate("contacts", u"A", None))
        self.cc_button.setText(QCoreApplication.translate("contacts", u"Cc", None))
        self.bcc_button.setText(QCoreApplication.translate("contacts", u"Bcc", None))
        self.label_16.setText(QCoreApplication.translate("contacts", u"Arcas Page 1", None))
        self.label_17.setText(QCoreApplication.translate("contacts", u"Awal Page 2", None))
        self.label_18.setText(QCoreApplication.translate("contacts", u"Awal Page 3", None))
        self.back_to_contacts_2.setText(QCoreApplication.translate("contacts", u"< Back to Contacts", None))
        self.logo_user_2.setText(QCoreApplication.translate("contacts", u"G", None))
        self.company_ni_gab_2.setText(QCoreApplication.translate("contacts", u"Company ni Gab", None))
        self.sales_pipeline_4.setText(QCoreApplication.translate("contacts", u"Sales Pipeline", None))
        self.prospecting_4.setText(QCoreApplication.translate("contacts", u"Prospecting", None))
        self.qualifications_4.setText(QCoreApplication.translate("contacts", u"Qualifications", None))
        self.contacting_4.setText(QCoreApplication.translate("contacts", u"Contacting", None))
        self.building_relationship_4.setText(QCoreApplication.translate("contacts", u"Building Relationship", None))
        self.negotiating_2.setText(QCoreApplication.translate("contacts", u"Negotiating with the lead", None))
        self.closing_4.setText(QCoreApplication.translate("contacts", u"Closing", None))
        self.closed_won_4.setText(QCoreApplication.translate("contacts", u"Closed Won", None))
        self.closed_loss_4.setText(QCoreApplication.translate("contacts", u"Closed Loss", None))
        self.contact_info_2.setText(QCoreApplication.translate("contacts", u"Contact Information", None))
        self.sales_funnel_label_2.setText(QCoreApplication.translate("contacts", u"Sales Funnel", None))
        self.contacts_label_2.setText(QCoreApplication.translate("contacts", u"Contacts", None))
        self.to_label_2.setText(QCoreApplication.translate("contacts", u"To:", None))
        self.from_label_2.setText(QCoreApplication.translate("contacts", u"From:", None))
        self.subject_label_2.setText(QCoreApplication.translate("contacts", u"Subject:", None))
        self.email_body_2.setHtml(QCoreApplication.translate("contacts", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bold_button_2.setText(QCoreApplication.translate("contacts", u"B", None))
        self.italic_button_2.setText(QCoreApplication.translate("contacts", u"I", None))
        self.underline_button_2.setText(QCoreApplication.translate("contacts", u"U", None))
        self.send_button_2.setText(QCoreApplication.translate("contacts", u"Send", None))
        self.text_combo_2.setItemText(0, QCoreApplication.translate("contacts", u"Arial", None))

#if QT_CONFIG(accessibility)
        self.text_combo_2.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.text_combo_2.setCurrentText(QCoreApplication.translate("contacts", u"Arial", None))
        self.size_combo_2.setItemText(0, QCoreApplication.translate("contacts", u"11", None))

        self.size_combo_2.setCurrentText(QCoreApplication.translate("contacts", u"11", None))
        self.more_combo_2.setItemText(0, QCoreApplication.translate("contacts", u"More", None))

        self.more_combo_2.setCurrentText(QCoreApplication.translate("contacts", u"More", None))
        self.insert_combo_2.setItemText(0, QCoreApplication.translate("contacts", u"Insert", None))

        self.insert_combo_2.setCurrentText(QCoreApplication.translate("contacts", u"Insert", None))
        self.letter_combo_2.setItemText(0, QCoreApplication.translate("contacts", u"A", None))

        self.letter_combo_2.setCurrentText(QCoreApplication.translate("contacts", u"A", None))
        self.cc_button_2.setText(QCoreApplication.translate("contacts", u"Cc", None))
        self.bcc_button_2.setText(QCoreApplication.translate("contacts", u"Bcc", None))
    # retranslateUi

