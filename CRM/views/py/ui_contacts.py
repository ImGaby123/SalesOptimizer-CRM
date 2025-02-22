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
    QHeaderView, QLabel, QLineEdit, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import views.py.icons_rc

class Ui_contacts(object):
    def setupUi(self, contacts):
        if not contacts.objectName():
            contacts.setObjectName(u"contacts")
        contacts.resize(1201, 681)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(contacts.sizePolicy().hasHeightForWidth())
        contacts.setSizePolicy(sizePolicy)
        self.stackedWidget = QStackedWidget(contacts)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1201, 681))
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.aarcas_page = QWidget()
        self.aarcas_page.setObjectName(u"aarcas_page")
        sizePolicy.setHeightForWidth(self.aarcas_page.sizePolicy().hasHeightForWidth())
        self.aarcas_page.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget_2 = QWidget(self.aarcas_page)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(-10, -10, 1211, 691))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1222, 2522))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(1200, 2500))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.BackToContactsBtn_2 = QPushButton(self.frame_2)
        self.BackToContactsBtn_2.setObjectName(u"BackToContactsBtn_2")
        self.BackToContactsBtn_2.setGeometry(QRect(10, 10, 121, 24))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BackToContactsBtn_2.sizePolicy().hasHeightForWidth())
        self.BackToContactsBtn_2.setSizePolicy(sizePolicy1)
        self.BackToContactsBtn_2.setStyleSheet(u"QPushButton {\n"
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
        self.BackToContactsBtn_2.setIcon(icon)
        self.NewContacts_2 = QLabel(self.frame_2)
        self.NewContacts_2.setObjectName(u"NewContacts_2")
        self.NewContacts_2.setGeometry(QRect(560, 70, 81, 21))
        sizePolicy1.setHeightForWidth(self.NewContacts_2.sizePolicy().hasHeightForWidth())
        self.NewContacts_2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.NewContacts_2.setFont(font)
        self.NewContacts_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.widget_6 = QWidget(self.frame_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(9, 90, 1181, 41))
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.widget_6.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.ContactsInformation_2 = QLabel(self.widget_6)
        self.ContactsInformation_2.setObjectName(u"ContactsInformation_2")
        self.ContactsInformation_2.setGeometry(QRect(20, 10, 131, 21))
        sizePolicy1.setHeightForWidth(self.ContactsInformation_2.sizePolicy().hasHeightForWidth())
        self.ContactsInformation_2.setSizePolicy(sizePolicy1)
        self.ContactsInformation_2.setFont(font)
        self.ContactsInformation_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.SearcAccount_2 = QLineEdit(self.frame_2)
        self.SearcAccount_2.setObjectName(u"SearcAccount_2")
        self.SearcAccount_2.setGeometry(QRect(20, 140, 281, 41))
        self.ContactOwner_2 = QLabel(self.frame_2)
        self.ContactOwner_2.setObjectName(u"ContactOwner_2")
        self.ContactOwner_2.setGeometry(QRect(20, 210, 91, 16))
        self.ContactOwner_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.horizontalLayoutWidget_2 = QWidget(self.frame_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(30, 230, 1121, 101))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ProfilePic_2 = QLabel(self.horizontalLayoutWidget_2)
        self.ProfilePic_2.setObjectName(u"ProfilePic_2")
        self.ProfilePic_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ProfilePic_2.sizePolicy().hasHeightForWidth())
        self.ProfilePic_2.setSizePolicy(sizePolicy1)
        self.ProfilePic_2.setMaximumSize(QSize(50, 50))
        self.ProfilePic_2.setStyleSheet(u"QLabel#ProfilePic {\n"
"    width: 50px; /* Palitan ayon sa gusto mong laki */\n"
"    height: 50px;\n"
"    border-radius: 25px; /* Kalahati ng width/height para maging bilog */\n"
"    background-color: #E5DAFB; /* Light purple background */\n"
"    border: 1px solid #D0C4F0; /* Optional: Light border */\n"
"}\n"
"")
        self.ProfilePic_2.setPixmap(QPixmap(u":/new/newPrefix/Resources/user.png"))
        self.ProfilePic_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.ProfilePic_2)

        self.horizontalSpacer_3 = QSpacerItem(5, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.ProfileName_2 = QLabel(self.horizontalLayoutWidget_2)
        self.ProfileName_2.setObjectName(u"ProfileName_2")
        sizePolicy1.setHeightForWidth(self.ProfileName_2.sizePolicy().hasHeightForWidth())
        self.ProfileName_2.setSizePolicy(sizePolicy1)
        self.ProfileName_2.setFont(font)
        self.ProfileName_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.ProfileName_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.ProfileName_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.UploadPic_2 = QLineEdit(self.horizontalLayoutWidget_2)
        self.UploadPic_2.setObjectName(u"UploadPic_2")
        self.UploadPic_2.setMinimumSize(QSize(0, 50))
        self.UploadPic_2.setStyleSheet(u"")
        self.UploadPic_2.setCursorPosition(0)

        self.horizontalLayout_2.addWidget(self.UploadPic_2)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1100, 320, 61, 24))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
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
        self.Picture_2 = QLabel(self.frame_2)
        self.Picture_2.setObjectName(u"Picture_2")
        self.Picture_2.setGeometry(QRect(640, 210, 49, 16))
        self.Picture_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.layoutWidget_7 = QWidget(self.frame_2)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(40, 380, 471, 561))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.NameLabel_2 = QLabel(self.layoutWidget_7)
        self.NameLabel_2.setObjectName(u"NameLabel_2")
        sizePolicy1.setHeightForWidth(self.NameLabel_2.sizePolicy().hasHeightForWidth())
        self.NameLabel_2.setSizePolicy(sizePolicy1)
        self.NameLabel_2.setFont(font)
        self.NameLabel_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_12.addWidget(self.NameLabel_2)

        self.verticalSpacer_6 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_6)

        self.SalutationLabel_2 = QLabel(self.layoutWidget_7)
        self.SalutationLabel_2.setObjectName(u"SalutationLabel_2")
        sizePolicy1.setHeightForWidth(self.SalutationLabel_2.sizePolicy().hasHeightForWidth())
        self.SalutationLabel_2.setSizePolicy(sizePolicy1)
        self.SalutationLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_12.addWidget(self.SalutationLabel_2)

        self.Salutation_2 = QComboBox(self.layoutWidget_7)
        self.Salutation_2.addItem("")
        self.Salutation_2.addItem("")
        self.Salutation_2.addItem("")
        self.Salutation_2.addItem("")
        self.Salutation_2.setObjectName(u"Salutation_2")
        sizePolicy1.setHeightForWidth(self.Salutation_2.sizePolicy().hasHeightForWidth())
        self.Salutation_2.setSizePolicy(sizePolicy1)
        self.Salutation_2.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout_12.addWidget(self.Salutation_2)

        self.verticalSpacer_20 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_20)

        self.FirstNameLabel_2 = QLabel(self.layoutWidget_7)
        self.FirstNameLabel_2.setObjectName(u"FirstNameLabel_2")
        sizePolicy1.setHeightForWidth(self.FirstNameLabel_2.sizePolicy().hasHeightForWidth())
        self.FirstNameLabel_2.setSizePolicy(sizePolicy1)
        self.FirstNameLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_12.addWidget(self.FirstNameLabel_2)

        self.FirstName_2 = QLineEdit(self.layoutWidget_7)
        self.FirstName_2.setObjectName(u"FirstName_2")
        self.FirstName_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_12.addWidget(self.FirstName_2)

        self.verticalSpacer_21 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_21)

        self.LastNameLabel_2 = QLabel(self.layoutWidget_7)
        self.LastNameLabel_2.setObjectName(u"LastNameLabel_2")
        sizePolicy1.setHeightForWidth(self.LastNameLabel_2.sizePolicy().hasHeightForWidth())
        self.LastNameLabel_2.setSizePolicy(sizePolicy1)
        self.LastNameLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_12.addWidget(self.LastNameLabel_2)

        self.LastName_2 = QLineEdit(self.layoutWidget_7)
        self.LastName_2.setObjectName(u"LastName_2")
        self.LastName_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_12.addWidget(self.LastName_2)

        self.verticalSpacer_22 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_22)

        self.MiddleNameLabel_3 = QLabel(self.layoutWidget_7)
        self.MiddleNameLabel_3.setObjectName(u"MiddleNameLabel_3")
        sizePolicy1.setHeightForWidth(self.MiddleNameLabel_3.sizePolicy().hasHeightForWidth())
        self.MiddleNameLabel_3.setSizePolicy(sizePolicy1)
        self.MiddleNameLabel_3.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_12.addWidget(self.MiddleNameLabel_3)

        self.MiddleName_2 = QLineEdit(self.layoutWidget_7)
        self.MiddleName_2.setObjectName(u"MiddleName_2")
        self.MiddleName_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_12.addWidget(self.MiddleName_2)

        self.verticalSpacer_23 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_23)

        self.SuffixLabel_3 = QLabel(self.layoutWidget_7)
        self.SuffixLabel_3.setObjectName(u"SuffixLabel_3")
        sizePolicy1.setHeightForWidth(self.SuffixLabel_3.sizePolicy().hasHeightForWidth())
        self.SuffixLabel_3.setSizePolicy(sizePolicy1)
        self.SuffixLabel_3.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_12.addWidget(self.SuffixLabel_3)

        self.Suffix_3 = QLineEdit(self.layoutWidget_7)
        self.Suffix_3.setObjectName(u"Suffix_3")
        self.Suffix_3.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_12.addWidget(self.Suffix_3)

        self.layoutWidget_8 = QWidget(self.frame_2)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(670, 370, 481, 571))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.DateOfBirthLabel_2 = QLabel(self.layoutWidget_8)
        self.DateOfBirthLabel_2.setObjectName(u"DateOfBirthLabel_2")
        sizePolicy1.setHeightForWidth(self.DateOfBirthLabel_2.sizePolicy().hasHeightForWidth())
        self.DateOfBirthLabel_2.setSizePolicy(sizePolicy1)
        self.DateOfBirthLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_13.addWidget(self.DateOfBirthLabel_2)

        self.DateOfBIrth_2 = QLineEdit(self.layoutWidget_8)
        self.DateOfBIrth_2.setObjectName(u"DateOfBIrth_2")
        self.DateOfBIrth_2.setMinimumSize(QSize(0, 0))
        self.DateOfBIrth_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_13.addWidget(self.DateOfBIrth_2)

        self.verticalSpacer_24 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_24)

        self.LeadStatusLabel_2 = QLabel(self.layoutWidget_8)
        self.LeadStatusLabel_2.setObjectName(u"LeadStatusLabel_2")
        sizePolicy1.setHeightForWidth(self.LeadStatusLabel_2.sizePolicy().hasHeightForWidth())
        self.LeadStatusLabel_2.setSizePolicy(sizePolicy1)
        self.LeadStatusLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_13.addWidget(self.LeadStatusLabel_2)

        self.LeadStatus_2 = QComboBox(self.layoutWidget_8)
        self.LeadStatus_2.addItem("")
        self.LeadStatus_2.addItem("")
        self.LeadStatus_2.addItem("")
        self.LeadStatus_2.addItem("")
        self.LeadStatus_2.setObjectName(u"LeadStatus_2")
        sizePolicy1.setHeightForWidth(self.LeadStatus_2.sizePolicy().hasHeightForWidth())
        self.LeadStatus_2.setSizePolicy(sizePolicy1)
        self.LeadStatus_2.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout_13.addWidget(self.LeadStatus_2)

        self.verticalSpacer_25 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_25)

        self.TitleLabel_2 = QLabel(self.layoutWidget_8)
        self.TitleLabel_2.setObjectName(u"TitleLabel_2")
        sizePolicy1.setHeightForWidth(self.TitleLabel_2.sizePolicy().hasHeightForWidth())
        self.TitleLabel_2.setSizePolicy(sizePolicy1)
        self.TitleLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_13.addWidget(self.TitleLabel_2)

        self.Title_2 = QLineEdit(self.layoutWidget_8)
        self.Title_2.setObjectName(u"Title_2")
        self.Title_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_13.addWidget(self.Title_2)

        self.verticalSpacer_26 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_26)

        self.MiddleNameLabel_4 = QLabel(self.layoutWidget_8)
        self.MiddleNameLabel_4.setObjectName(u"MiddleNameLabel_4")
        sizePolicy1.setHeightForWidth(self.MiddleNameLabel_4.sizePolicy().hasHeightForWidth())
        self.MiddleNameLabel_4.setSizePolicy(sizePolicy1)
        self.MiddleNameLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_13.addWidget(self.MiddleNameLabel_4)

        self.Email_2 = QLineEdit(self.layoutWidget_8)
        self.Email_2.setObjectName(u"Email_2")
        self.Email_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_13.addWidget(self.Email_2)

        self.verticalSpacer_27 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_27)

        self.SuffixLabel_4 = QLabel(self.layoutWidget_8)
        self.SuffixLabel_4.setObjectName(u"SuffixLabel_4")
        sizePolicy1.setHeightForWidth(self.SuffixLabel_4.sizePolicy().hasHeightForWidth())
        self.SuffixLabel_4.setSizePolicy(sizePolicy1)
        self.SuffixLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_13.addWidget(self.SuffixLabel_4)

        self.Suffix_4 = QLineEdit(self.layoutWidget_8)
        self.Suffix_4.setObjectName(u"Suffix_4")
        self.Suffix_4.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_13.addWidget(self.Suffix_4)

        self.widget_7 = QWidget(self.frame_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(10, 1040, 1181, 41))
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.widget_7.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.AdditionalInformation_3 = QLabel(self.widget_7)
        self.AdditionalInformation_3.setObjectName(u"AdditionalInformation_3")
        self.AdditionalInformation_3.setGeometry(QRect(20, 10, 181, 21))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.AdditionalInformation_3.sizePolicy().hasHeightForWidth())
        self.AdditionalInformation_3.setSizePolicy(sizePolicy2)
        self.AdditionalInformation_3.setFont(font)
        self.AdditionalInformation_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.layoutWidget_9 = QWidget(self.frame_2)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(40, 1120, 421, 411))
        self.verticalLayout_14 = QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.SecondaryEmailLabel_2 = QLabel(self.layoutWidget_9)
        self.SecondaryEmailLabel_2.setObjectName(u"SecondaryEmailLabel_2")
        sizePolicy1.setHeightForWidth(self.SecondaryEmailLabel_2.sizePolicy().hasHeightForWidth())
        self.SecondaryEmailLabel_2.setSizePolicy(sizePolicy1)
        self.SecondaryEmailLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_14.addWidget(self.SecondaryEmailLabel_2)

        self.SecondaryEmail_2 = QLineEdit(self.layoutWidget_9)
        self.SecondaryEmail_2.setObjectName(u"SecondaryEmail_2")
        self.SecondaryEmail_2.setMinimumSize(QSize(0, 0))
        self.SecondaryEmail_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_14.addWidget(self.SecondaryEmail_2)

        self.verticalSpacer_28 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_28)

        self.OtherPhoneNumLabel_2 = QLabel(self.layoutWidget_9)
        self.OtherPhoneNumLabel_2.setObjectName(u"OtherPhoneNumLabel_2")
        sizePolicy1.setHeightForWidth(self.OtherPhoneNumLabel_2.sizePolicy().hasHeightForWidth())
        self.OtherPhoneNumLabel_2.setSizePolicy(sizePolicy1)
        self.OtherPhoneNumLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_14.addWidget(self.OtherPhoneNumLabel_2)

        self.OtherPhoneNum_2 = QLineEdit(self.layoutWidget_9)
        self.OtherPhoneNum_2.setObjectName(u"OtherPhoneNum_2")
        self.OtherPhoneNum_2.setMinimumSize(QSize(0, 0))
        self.OtherPhoneNum_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_14.addWidget(self.OtherPhoneNum_2)

        self.verticalSpacer_29 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_29)

        self.GenderLabel_2 = QLabel(self.layoutWidget_9)
        self.GenderLabel_2.setObjectName(u"GenderLabel_2")
        sizePolicy1.setHeightForWidth(self.GenderLabel_2.sizePolicy().hasHeightForWidth())
        self.GenderLabel_2.setSizePolicy(sizePolicy1)
        self.GenderLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_14.addWidget(self.GenderLabel_2)

        self.Gender_2 = QLineEdit(self.layoutWidget_9)
        self.Gender_2.setObjectName(u"Gender_2")
        self.Gender_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_14.addWidget(self.Gender_2)

        self.verticalSpacer_30 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_30)

        self.MaritalStatusLabel_2 = QLabel(self.layoutWidget_9)
        self.MaritalStatusLabel_2.setObjectName(u"MaritalStatusLabel_2")
        sizePolicy1.setHeightForWidth(self.MaritalStatusLabel_2.sizePolicy().hasHeightForWidth())
        self.MaritalStatusLabel_2.setSizePolicy(sizePolicy1)
        self.MaritalStatusLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_14.addWidget(self.MaritalStatusLabel_2)

        self.MaritalStatus_2 = QLineEdit(self.layoutWidget_9)
        self.MaritalStatus_2.setObjectName(u"MaritalStatus_2")
        self.MaritalStatus_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_14.addWidget(self.MaritalStatus_2)

        self.layoutWidget_10 = QWidget(self.frame_2)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(730, 1120, 401, 281))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget_10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.CompanyLabel_2 = QLabel(self.layoutWidget_10)
        self.CompanyLabel_2.setObjectName(u"CompanyLabel_2")
        sizePolicy1.setHeightForWidth(self.CompanyLabel_2.sizePolicy().hasHeightForWidth())
        self.CompanyLabel_2.setSizePolicy(sizePolicy1)
        self.CompanyLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_15.addWidget(self.CompanyLabel_2)

        self.Company_2 = QLineEdit(self.layoutWidget_10)
        self.Company_2.setObjectName(u"Company_2")
        self.Company_2.setMinimumSize(QSize(0, 0))
        self.Company_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_15.addWidget(self.Company_2)

        self.verticalSpacer_31 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_31)

        self.ReportsToLabel_2 = QLabel(self.layoutWidget_10)
        self.ReportsToLabel_2.setObjectName(u"ReportsToLabel_2")
        sizePolicy1.setHeightForWidth(self.ReportsToLabel_2.sizePolicy().hasHeightForWidth())
        self.ReportsToLabel_2.setSizePolicy(sizePolicy1)
        self.ReportsToLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_15.addWidget(self.ReportsToLabel_2)

        self.ReportsTo_2 = QLineEdit(self.layoutWidget_10)
        self.ReportsTo_2.setObjectName(u"ReportsTo_2")
        self.ReportsTo_2.setMinimumSize(QSize(0, 0))
        self.ReportsTo_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_15.addWidget(self.ReportsTo_2)

        self.verticalSpacer_32 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_32)

        self.FaxLabel_2 = QLabel(self.layoutWidget_10)
        self.FaxLabel_2.setObjectName(u"FaxLabel_2")
        sizePolicy1.setHeightForWidth(self.FaxLabel_2.sizePolicy().hasHeightForWidth())
        self.FaxLabel_2.setSizePolicy(sizePolicy1)
        self.FaxLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_15.addWidget(self.FaxLabel_2)

        self.Fax_2 = QLineEdit(self.layoutWidget_10)
        self.Fax_2.setObjectName(u"Fax_2")
        self.Fax_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_15.addWidget(self.Fax_2)

        self.widget_8 = QWidget(self.frame_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(10, 1610, 1181, 41))
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.widget_8.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.AdditionalInformation_6 = QLabel(self.widget_8)
        self.AdditionalInformation_6.setObjectName(u"AdditionalInformation_6")
        self.AdditionalInformation_6.setGeometry(QRect(20, 10, 181, 21))
        sizePolicy1.setHeightForWidth(self.AdditionalInformation_6.sizePolicy().hasHeightForWidth())
        self.AdditionalInformation_6.setSizePolicy(sizePolicy1)
        self.AdditionalInformation_6.setFont(font)
        self.AdditionalInformation_6.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.layoutWidget_11 = QWidget(self.frame_2)
        self.layoutWidget_11.setObjectName(u"layoutWidget_11")
        self.layoutWidget_11.setGeometry(QRect(40, 1690, 421, 411))
        self.verticalLayout_16 = QVBoxLayout(self.layoutWidget_11)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.AddressLabel_2 = QLabel(self.layoutWidget_11)
        self.AddressLabel_2.setObjectName(u"AddressLabel_2")
        sizePolicy1.setHeightForWidth(self.AddressLabel_2.sizePolicy().hasHeightForWidth())
        self.AddressLabel_2.setSizePolicy(sizePolicy1)
        self.AddressLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_16.addWidget(self.AddressLabel_2)

        self.Address_2 = QLineEdit(self.layoutWidget_11)
        self.Address_2.setObjectName(u"Address_2")
        self.Address_2.setMinimumSize(QSize(0, 0))
        self.Address_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_16.addWidget(self.Address_2)

        self.verticalSpacer_33 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_33)

        self.CountryLabel_2 = QLabel(self.layoutWidget_11)
        self.CountryLabel_2.setObjectName(u"CountryLabel_2")
        sizePolicy1.setHeightForWidth(self.CountryLabel_2.sizePolicy().hasHeightForWidth())
        self.CountryLabel_2.setSizePolicy(sizePolicy1)
        self.CountryLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_16.addWidget(self.CountryLabel_2)

        self.Country_2 = QLineEdit(self.layoutWidget_11)
        self.Country_2.setObjectName(u"Country_2")
        self.Country_2.setMinimumSize(QSize(0, 0))
        self.Country_2.setMaximumSize(QSize(300, 300))

        self.verticalLayout_16.addWidget(self.Country_2)

        self.verticalSpacer_34 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_34)

        self.State_ProvinceLabel_2 = QLabel(self.layoutWidget_11)
        self.State_ProvinceLabel_2.setObjectName(u"State_ProvinceLabel_2")
        sizePolicy1.setHeightForWidth(self.State_ProvinceLabel_2.sizePolicy().hasHeightForWidth())
        self.State_ProvinceLabel_2.setSizePolicy(sizePolicy1)
        self.State_ProvinceLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_16.addWidget(self.State_ProvinceLabel_2)

        self.StateProvince_2 = QLineEdit(self.layoutWidget_11)
        self.StateProvince_2.setObjectName(u"StateProvince_2")
        self.StateProvince_2.setMaximumSize(QSize(300, 300))

        self.verticalLayout_16.addWidget(self.StateProvince_2)

        self.verticalSpacer_35 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_35)

        self.ZipPostalCodeLabel_2 = QLabel(self.layoutWidget_11)
        self.ZipPostalCodeLabel_2.setObjectName(u"ZipPostalCodeLabel_2")
        sizePolicy1.setHeightForWidth(self.ZipPostalCodeLabel_2.sizePolicy().hasHeightForWidth())
        self.ZipPostalCodeLabel_2.setSizePolicy(sizePolicy1)
        self.ZipPostalCodeLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_16.addWidget(self.ZipPostalCodeLabel_2)

        self.ZipPostalCode_2 = QLineEdit(self.layoutWidget_11)
        self.ZipPostalCode_2.setObjectName(u"ZipPostalCode_2")
        self.ZipPostalCode_2.setMaximumSize(QSize(300, 300))

        self.verticalLayout_16.addWidget(self.ZipPostalCode_2)

        self.layoutWidget_12 = QWidget(self.frame_2)
        self.layoutWidget_12.setObjectName(u"layoutWidget_12")
        self.layoutWidget_12.setGeometry(QRect(720, 1770, 421, 411))
        self.verticalLayout_17 = QVBoxLayout(self.layoutWidget_12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.CityLabel_2 = QLabel(self.layoutWidget_12)
        self.CityLabel_2.setObjectName(u"CityLabel_2")
        sizePolicy1.setHeightForWidth(self.CityLabel_2.sizePolicy().hasHeightForWidth())
        self.CityLabel_2.setSizePolicy(sizePolicy1)
        self.CityLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_17.addWidget(self.CityLabel_2)

        self.City_2 = QLineEdit(self.layoutWidget_12)
        self.City_2.setObjectName(u"City_2")
        self.City_2.setMinimumSize(QSize(0, 0))
        self.City_2.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_17.addWidget(self.City_2)

        self.verticalSpacer_36 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_36)

        self.StreetLabel_2 = QLabel(self.layoutWidget_12)
        self.StreetLabel_2.setObjectName(u"StreetLabel_2")
        sizePolicy1.setHeightForWidth(self.StreetLabel_2.sizePolicy().hasHeightForWidth())
        self.StreetLabel_2.setSizePolicy(sizePolicy1)
        self.StreetLabel_2.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_17.addWidget(self.StreetLabel_2)

        self.Street_2 = QLabel(self.layoutWidget_12)
        self.Street_2.setObjectName(u"Street_2")
        sizePolicy1.setHeightForWidth(self.Street_2.sizePolicy().hasHeightForWidth())
        self.Street_2.setSizePolicy(sizePolicy1)
        self.Street_2.setMinimumSize(QSize(0, 300))
        self.Street_2.setStyleSheet(u" QLabel {\n"
"        border-radius: 50px; /* Half of the width/height */\n"
"       background-color: rgb(108, 108, 108);\n"
"    }\n"
"\n"
"")

        self.verticalLayout_17.addWidget(self.Street_2)

        self.widget_9 = QWidget(self.frame_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(10, 2230, 1181, 41))
        sizePolicy1.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy1)
        self.widget_9.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.AdditionalInformation_7 = QLabel(self.widget_9)
        self.AdditionalInformation_7.setObjectName(u"AdditionalInformation_7")
        self.AdditionalInformation_7.setGeometry(QRect(20, 10, 181, 21))
        sizePolicy1.setHeightForWidth(self.AdditionalInformation_7.sizePolicy().hasHeightForWidth())
        self.AdditionalInformation_7.setSizePolicy(sizePolicy1)
        self.AdditionalInformation_7.setFont(font)
        self.AdditionalInformation_7.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.widget_10 = QWidget(self.frame_2)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(10, 2310, 1181, 41))
        sizePolicy1.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy1)
        self.widget_10.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.AdditionalInformation_8 = QLabel(self.widget_10)
        self.AdditionalInformation_8.setObjectName(u"AdditionalInformation_8")
        self.AdditionalInformation_8.setGeometry(QRect(20, 10, 181, 21))
        sizePolicy1.setHeightForWidth(self.AdditionalInformation_8.sizePolicy().hasHeightForWidth())
        self.AdditionalInformation_8.setSizePolicy(sizePolicy1)
        self.AdditionalInformation_8.setFont(font)
        self.AdditionalInformation_8.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 2370, 71, 21))
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(860, 2370, 81, 21))
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_11.addWidget(self.frame_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_10.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.aarcas_page)
        self.awal_page1 = QWidget()
        self.awal_page1.setObjectName(u"awal_page1")
        sizePolicy.setHeightForWidth(self.awal_page1.sizePolicy().hasHeightForWidth())
        self.awal_page1.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget_8 = QWidget(self.awal_page1)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(0, 0, 1201, 681))
        self.verticalLayout_23 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_23.setSpacing(7)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.verticalLayoutWidget_8)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMinimumSize(QSize(0, 0))
        self.label_8.setStyleSheet(u"font: 18pt \"Segoe UI\";\n"
"background: transparent;")

        self.verticalLayout_23.addWidget(self.label_8)

        self.verticalSpacer_41 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_23.addItem(self.verticalSpacer_41)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.search_3 = QLineEdit(self.verticalLayoutWidget_8)
        self.search_3.setObjectName(u"search_3")
        sizePolicy1.setHeightForWidth(self.search_3.sizePolicy().hasHeightForWidth())
        self.search_3.setSizePolicy(sizePolicy1)
        self.search_3.setMinimumSize(QSize(0, 60))
        self.search_3.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.search_3.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.search_3.setClearButtonEnabled(False)

        self.horizontalLayout_22.addWidget(self.search_3)

        self.horizontalSpacer_21 = QSpacerItem(625, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_21)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.add_2 = QPushButton(self.verticalLayoutWidget_8)
        self.add_2.setObjectName(u"add_2")
        self.add_2.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Resources/black_plus .png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/Resources/white_plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.add_2.setIcon(icon1)
        self.add_2.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.add_2)

        self.refresh_2 = QPushButton(self.verticalLayoutWidget_8)
        self.refresh_2.setObjectName(u"refresh_2")
        self.refresh_2.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	border: transparent;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Resources/black_refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/Resources/white_refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.refresh_2.setIcon(icon2)
        self.refresh_2.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.refresh_2)

        self.delete_3 = QPushButton(self.verticalLayoutWidget_8)
        self.delete_3.setObjectName(u"delete_3")
        self.delete_3.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Resources/black_delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Resources/white_delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.delete_3.setIcon(icon3)
        self.delete_3.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.delete_3)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_6)


        self.verticalLayout_23.addLayout(self.horizontalLayout_22)

        self.verticalSpacer_42 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_23.addItem(self.verticalSpacer_42)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.allContacts_2 = QComboBox(self.verticalLayoutWidget_8)
        self.allContacts_2.setObjectName(u"allContacts_2")
        sizePolicy1.setHeightForWidth(self.allContacts_2.sizePolicy().hasHeightForWidth())
        self.allContacts_2.setSizePolicy(sizePolicy1)
        self.allContacts_2.setMinimumSize(QSize(0, 30))
        self.allContacts_2.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid black;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.allContacts_2.setEditable(False)

        self.horizontalLayout_23.addWidget(self.allContacts_2)

        self.horizontalSpacer_22 = QSpacerItem(975, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_22)


        self.verticalLayout_23.addLayout(self.horizontalLayout_23)

        self.verticalSpacer_43 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_23.addItem(self.verticalSpacer_43)

        self.tableWidget_3 = QTableWidget(self.verticalLayoutWidget_8)
        if (self.tableWidget_3.columnCount() < 4):
            self.tableWidget_3.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setStyleSheet(u"QTableWidget{\n"
"	border: 2px solid black\n"
"}\n"
"")

        self.verticalLayout_23.addWidget(self.tableWidget_3)

        self.stackedWidget.addWidget(self.awal_page1)
        self.awal_page2 = QWidget()
        self.awal_page2.setObjectName(u"awal_page2")
        sizePolicy.setHeightForWidth(self.awal_page2.sizePolicy().hasHeightForWidth())
        self.awal_page2.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget_3 = QWidget(self.awal_page2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 1181, 661))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(40, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.backToContacts = QPushButton(self.verticalLayoutWidget_3)
        self.backToContacts.setObjectName(u"backToContacts")
        sizePolicy1.setHeightForWidth(self.backToContacts.sizePolicy().hasHeightForWidth())
        self.backToContacts.setSizePolicy(sizePolicy1)
        self.backToContacts.setMinimumSize(QSize(0, 40))
        self.backToContacts.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: rgb(0, 0, 0); \n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Resources/black_left-arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/Resources/white_left-arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.backToContacts.setIcon(icon4)
        self.backToContacts.setIconSize(QSize(15, 15))

        self.horizontalLayout_3.addWidget(self.backToContacts)

        self.horizontalSpacer_5 = QSpacerItem(1050, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sales_pipeline = QFrame(self.verticalLayoutWidget_3)
        self.sales_pipeline.setObjectName(u"sales_pipeline")
        sizePolicy1.setHeightForWidth(self.sales_pipeline.sizePolicy().hasHeightForWidth())
        self.sales_pipeline.setSizePolicy(sizePolicy1)
        self.sales_pipeline.setMinimumSize(QSize(0, 100))
        self.sales_pipeline.setStyleSheet(u"QFrame {\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}")
        self.sales_pipeline.setFrameShape(QFrame.Shape.StyledPanel)
        self.sales_pipeline.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_7 = QWidget(self.sales_pipeline)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(10, 20, 1161, 61))
        self.verticalLayout_22 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.SalesPipeline = QLabel(self.verticalLayoutWidget_7)
        self.SalesPipeline.setObjectName(u"SalesPipeline")
        self.SalesPipeline.setStyleSheet(u"QLabel{\n"
"	font: 9pt \"Segoe UI\";\n"
"	border: none;\n"
"}")

        self.horizontalLayout_19.addWidget(self.SalesPipeline)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_11)

        self.progressBar = QProgressBar(self.verticalLayoutWidget_7)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 0))
        self.progressBar.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.progressBar.setStyleSheet(u"border-radius: 10px;")
        self.progressBar.setValue(100)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_19.addWidget(self.progressBar)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_20)


        self.verticalLayout_22.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_19 = QSpacerItem(90, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_19)

        self.prospecting = QLabel(self.verticalLayoutWidget_7)
        self.prospecting.setObjectName(u"prospecting")
        self.prospecting.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_20.addWidget(self.prospecting)

        self.horizontalSpacer_12 = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_12)

        self.qualifications = QLabel(self.verticalLayoutWidget_7)
        self.qualifications.setObjectName(u"qualifications")
        self.qualifications.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_20.addWidget(self.qualifications)

        self.horizontalSpacer_13 = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_13)

        self.contacting = QLabel(self.verticalLayoutWidget_7)
        self.contacting.setObjectName(u"contacting")
        self.contacting.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_20.addWidget(self.contacting)

        self.horizontalSpacer_14 = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_14)

        self.negotiating_with_the_lead = QLabel(self.verticalLayoutWidget_7)
        self.negotiating_with_the_lead.setObjectName(u"negotiating_with_the_lead")
        self.negotiating_with_the_lead.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_20.addWidget(self.negotiating_with_the_lead)

        self.horizontalSpacer_15 = QSpacerItem(120, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_15)

        self.closed_won = QLabel(self.verticalLayoutWidget_7)
        self.closed_won.setObjectName(u"closed_won")
        self.closed_won.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_20.addWidget(self.closed_won)

        self.horizontalSpacer_16 = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_16)

        self.closed_loss = QLabel(self.verticalLayoutWidget_7)
        self.closed_loss.setObjectName(u"closed_loss")
        self.closed_loss.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_20.addWidget(self.closed_loss)


        self.verticalLayout_22.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_4.addWidget(self.sales_pipeline)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tableWidget_2 = QTableWidget(self.verticalLayoutWidget_3)
        if (self.tableWidget_2.columnCount() < 1):
            self.tableWidget_2.setColumnCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMaximumSize(QSize(200, 16777215))
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"	border: 2px solid black;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.tableWidget_2)

        self.timeline_3 = QFrame(self.verticalLayoutWidget_3)
        self.timeline_3.setObjectName(u"timeline_3")
        sizePolicy.setHeightForWidth(self.timeline_3.sizePolicy().hasHeightForWidth())
        self.timeline_3.setSizePolicy(sizePolicy)
        self.timeline_3.setStyleSheet(u"QFrame {\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}")
        self.timeline_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.timeline_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_11 = QWidget(self.timeline_3)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(10, 10, 561, 401))
        self.verticalLayout_27 = QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_35 = QSpacerItem(230, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_35)

        self.Timeline_3 = QLabel(self.verticalLayoutWidget_11)
        self.Timeline_3.setObjectName(u"Timeline_3")
        self.Timeline_3.setStyleSheet(u"QLabel{\n"
"	font: 10pt \"Segoe UI\";\n"
"	border: none;\n"
"}")

        self.horizontalLayout_31.addWidget(self.Timeline_3)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_36)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.pin_3 = QPushButton(self.verticalLayoutWidget_11)
        self.pin_3.setObjectName(u"pin_3")
        self.pin_3.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Resources/black_pin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/Resources/white_pin.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pin_3.setIcon(icon5)
        self.pin_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_32.addWidget(self.pin_3)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget_11)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Resources/black_bars.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/Resources/white_bars.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QSize(30, 30))

        self.horizontalLayout_32.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.verticalLayoutWidget_11)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/Resources/black_menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/Resources/white_menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setIconSize(QSize(30, 30))

        self.horizontalLayout_32.addWidget(self.pushButton_7)


        self.horizontalLayout_31.addLayout(self.horizontalLayout_32)


        self.verticalLayout_27.addLayout(self.horizontalLayout_31)

        self.search_5 = QLineEdit(self.verticalLayoutWidget_11)
        self.search_5.setObjectName(u"search_5")
        self.search_5.setMinimumSize(QSize(0, 45))
        self.search_5.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"")

        self.verticalLayout_27.addWidget(self.search_5)

        self.verticalSpacer_45 = QSpacerItem(20, 999, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_27.addItem(self.verticalSpacer_45)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.edit_3 = QPushButton(self.verticalLayoutWidget_11)
        self.edit_3.setObjectName(u"edit_3")
        self.edit_3.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/Resources/black_edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/Resources/white_edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.edit_3.setIcon(icon8)

        self.horizontalLayout_33.addWidget(self.edit_3)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_37)

        self.link_3 = QPushButton(self.verticalLayoutWidget_11)
        self.link_3.setObjectName(u"link_3")
        self.link_3.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/Resources/black_link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/Resources/white_link.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.link_3.setIcon(icon9)

        self.horizontalLayout_33.addWidget(self.link_3)

        self.attachment_3 = QPushButton(self.verticalLayoutWidget_11)
        self.attachment_3.setObjectName(u"attachment_3")
        self.attachment_3.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/Resources/black_attach.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/Resources/white_attach.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.attachment_3.setIcon(icon10)

        self.horizontalLayout_33.addWidget(self.attachment_3)


        self.verticalLayout_28.addLayout(self.horizontalLayout_33)


        self.verticalLayout_27.addLayout(self.verticalLayout_28)


        self.horizontalLayout_7.addWidget(self.timeline_3)

        self.contact_information = QFrame(self.verticalLayoutWidget_3)
        self.contact_information.setObjectName(u"contact_information")
        sizePolicy.setHeightForWidth(self.contact_information.sizePolicy().hasHeightForWidth())
        self.contact_information.setSizePolicy(sizePolicy)
        self.contact_information.setMaximumSize(QSize(380, 16777215))
        self.contact_information.setStyleSheet(u"QFrame {\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}")
        self.contact_information.setFrameShape(QFrame.Shape.StyledPanel)
        self.contact_information.setFrameShadow(QFrame.Shadow.Raised)
        self.ContactInformation = QLabel(self.contact_information)
        self.ContactInformation.setObjectName(u"ContactInformation")
        self.ContactInformation.setGeometry(QRect(120, 10, 161, 20))
        self.ContactInformation.setStyleSheet(u"QLabel{\n"
"	font: 10pt \"Segoe UI\";\n"
"	border: none;\n"
"}")

        self.horizontalLayout_7.addWidget(self.contact_information)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.stackedWidget.addWidget(self.awal_page2)
        self.abuan_page1 = QWidget()
        self.abuan_page1.setObjectName(u"abuan_page1")
        sizePolicy.setHeightForWidth(self.abuan_page1.sizePolicy().hasHeightForWidth())
        self.abuan_page1.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(self.abuan_page1)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1201, 681))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.back_to_contacts_2 = QPushButton(self.verticalLayoutWidget)
        self.back_to_contacts_2.setObjectName(u"back_to_contacts_2")
        font1 = QFont()
        font1.setPointSize(14)
        self.back_to_contacts_2.setFont(font1)
        self.back_to_contacts_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")

        self.horizontalLayout_24.addWidget(self.back_to_contacts_2)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_17)


        self.verticalLayout.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.logo_user_2 = QLabel(self.verticalLayoutWidget)
        self.logo_user_2.setObjectName(u"logo_user_2")
        self.logo_user_2.setMinimumSize(QSize(30, 0))
        self.logo_user_2.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.logo_user_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.logo_user_2)

        self.company_ni_gab_2 = QLabel(self.verticalLayoutWidget)
        self.company_ni_gab_2.setObjectName(u"company_ni_gab_2")
        self.company_ni_gab_2.setFont(font1)
        self.company_ni_gab_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_21.addWidget(self.company_ni_gab_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.frame_8 = QFrame(self.verticalLayoutWidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 90))
        self.frame_8.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.sales_pipeline_4 = QLabel(self.frame_8)
        self.sales_pipeline_4.setObjectName(u"sales_pipeline_4")
        self.sales_pipeline_4.setGeometry(QRect(10, 10, 101, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.sales_pipeline_4.setFont(font2)
        self.sales_pipeline_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;\n"
"")
        self.sales_pipeline_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sales_pipeline_4.setWordWrap(False)
        self.closed_won_4 = QLabel(self.frame_8)
        self.closed_won_4.setObjectName(u"closed_won_4")
        self.closed_won_4.setGeometry(QRect(970, 50, 81, 16))
        self.closed_won_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")
        self.prospecting_4 = QLabel(self.frame_8)
        self.prospecting_4.setObjectName(u"prospecting_4")
        self.prospecting_4.setGeometry(QRect(120, 50, 71, 16))
        self.prospecting_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")
        self.negotiating_2 = QLabel(self.frame_8)
        self.negotiating_2.setObjectName(u"negotiating_2")
        self.negotiating_2.setGeometry(QRect(680, 50, 141, 16))
        self.negotiating_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")
        self.closing_4 = QLabel(self.frame_8)
        self.closing_4.setObjectName(u"closing_4")
        self.closing_4.setGeometry(QRect(870, 50, 51, 16))
        self.closing_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")
        self.closed_loss_4 = QLabel(self.frame_8)
        self.closed_loss_4.setObjectName(u"closed_loss_4")
        self.closed_loss_4.setGeometry(QRect(1090, 50, 81, 16))
        self.closed_loss_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")
        self.contacting_4 = QLabel(self.frame_8)
        self.contacting_4.setObjectName(u"contacting_4")
        self.contacting_4.setGeometry(QRect(370, 50, 81, 16))
        self.contacting_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")
        self.progressBar_4 = QProgressBar(self.frame_8)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setGeometry(QRect(120, 20, 1041, 23))
        self.progressBar_4.setStyleSheet(u"")
        self.progressBar_4.setValue(24)
        self.building_relationship_4 = QLabel(self.frame_8)
        self.building_relationship_4.setObjectName(u"building_relationship_4")
        self.building_relationship_4.setGeometry(QRect(510, 50, 121, 16))
        self.building_relationship_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")
        self.qualifications_4 = QLabel(self.frame_8)
        self.qualifications_4.setObjectName(u"qualifications_4")
        self.qualifications_4.setGeometry(QRect(240, 50, 81, 16))
        self.qualifications_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")

        self.horizontalLayout_26.addWidget(self.frame_8)


        self.verticalLayout.addLayout(self.horizontalLayout_26)

        self.verticalSpacer_7 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.tableWidget_4 = QTableWidget(self.verticalLayoutWidget)
        if (self.tableWidget_4.columnCount() < 1):
            self.tableWidget_4.setColumnCount(1)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font3 = QFont()
        font3.setBold(False)
        font3.setKerning(True)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        __qtablewidgetitem5.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem5.setForeground(brush);
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setMaximumSize(QSize(200, 16777215))
        self.tableWidget_4.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 10px;")

        self.horizontalLayout_25.addWidget(self.tableWidget_4)

        self.frame_6 = QFrame(self.verticalLayoutWidget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 10px;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.contact_info_2 = QLabel(self.frame_6)
        self.contact_info_2.setObjectName(u"contact_info_2")
        self.contact_info_2.setGeometry(QRect(200, 10, 201, 51))
        font4 = QFont()
        font4.setPointSize(16)
        self.contact_info_2.setFont(font4)
        self.contact_info_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")
        self.contact_info_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.verticalLayoutWidget)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMaximumSize(QSize(380, 16777215))
        self.frame_7.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 10px;")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.sales_funnel_label_2 = QLabel(self.frame_7)
        self.sales_funnel_label_2.setObjectName(u"sales_funnel_label_2")
        self.sales_funnel_label_2.setGeometry(QRect(90, 10, 211, 31))
        self.sales_funnel_label_2.setFont(font4)
        self.sales_funnel_label_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")
        self.sales_funnel_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.frame_7)


        self.verticalLayout.addLayout(self.horizontalLayout_25)

        self.stackedWidget.addWidget(self.abuan_page1)
        self.abuan_page2 = QWidget()
        self.abuan_page2.setObjectName(u"abuan_page2")
        sizePolicy.setHeightForWidth(self.abuan_page2.sizePolicy().hasHeightForWidth())
        self.abuan_page2.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget_5 = QWidget(self.abuan_page2)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(0, 0, 1201, 681))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.from_label_2 = QLabel(self.verticalLayoutWidget_5)
        self.from_label_2.setObjectName(u"from_label_2")
        sizePolicy1.setHeightForWidth(self.from_label_2.sizePolicy().hasHeightForWidth())
        self.from_label_2.setSizePolicy(sizePolicy1)
        self.from_label_2.setMaximumSize(QSize(110, 16777215))
        self.from_label_2.setFont(font4)
        self.from_label_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_17.addWidget(self.from_label_2)

        self.from_line_2 = QLineEdit(self.verticalLayoutWidget_5)
        self.from_line_2.setObjectName(u"from_line_2")
        self.from_line_2.setMinimumSize(QSize(0, 50))
        self.from_line_2.setMaximumSize(QSize(1060, 16777215))
        self.from_line_2.setStyleSheet(u"border: 2px solid #C0C0C0; /* Gray border */\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 4px; /* Smooth edges */\n"
"    padding: 6px; /* Space inside the field */\n"
"    font-size: 14px;")

        self.horizontalLayout_17.addWidget(self.from_line_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.to_label_2 = QLabel(self.verticalLayoutWidget_5)
        self.to_label_2.setObjectName(u"to_label_2")
        sizePolicy1.setHeightForWidth(self.to_label_2.sizePolicy().hasHeightForWidth())
        self.to_label_2.setSizePolicy(sizePolicy1)
        self.to_label_2.setMaximumSize(QSize(110, 16777215))
        self.to_label_2.setFont(font4)
        self.to_label_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_16.addWidget(self.to_label_2)

        self.to_line_2 = QLineEdit(self.verticalLayoutWidget_5)
        self.to_line_2.setObjectName(u"to_line_2")
        self.to_line_2.setMinimumSize(QSize(0, 50))
        self.to_line_2.setMaximumSize(QSize(1060, 16777215))
        self.to_line_2.setStyleSheet(u"border: 2px solid #C0C0C0; /* Gray border */\n"
"    border-radius: 4px; /* Smooth edges */\n"
"    padding: 6px; /* Space inside the field */\n"
"    font-size: 14px;\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_16.addWidget(self.to_line_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.subject_label_2 = QLabel(self.verticalLayoutWidget_5)
        self.subject_label_2.setObjectName(u"subject_label_2")
        sizePolicy1.setHeightForWidth(self.subject_label_2.sizePolicy().hasHeightForWidth())
        self.subject_label_2.setSizePolicy(sizePolicy1)
        self.subject_label_2.setMaximumSize(QSize(110, 16777215))
        self.subject_label_2.setFont(font4)
        self.subject_label_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_18.addWidget(self.subject_label_2)

        self.subject_line_2 = QLineEdit(self.verticalLayoutWidget_5)
        self.subject_line_2.setObjectName(u"subject_line_2")
        self.subject_line_2.setMinimumSize(QSize(0, 50))
        self.subject_line_2.setMaximumSize(QSize(1060, 16777215))
        self.subject_line_2.setStyleSheet(u"border: 2px solid #C0C0C0; /* Gray border */\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 4px; /* Smooth edges */\n"
"    padding: 6px; /* Space inside the field */\n"
"    font-size: 14px;")

        self.horizontalLayout_18.addWidget(self.subject_line_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.email_body_2 = QTextEdit(self.verticalLayoutWidget_5)
        self.email_body_2.setObjectName(u"email_body_2")
        self.email_body_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_27.addWidget(self.email_body_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_27)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.bold_button_2 = QPushButton(self.verticalLayoutWidget_5)
        self.bold_button_2.setObjectName(u"bold_button_2")
        sizePolicy1.setHeightForWidth(self.bold_button_2.sizePolicy().hasHeightForWidth())
        self.bold_button_2.setSizePolicy(sizePolicy1)
        self.bold_button_2.setMaximumSize(QSize(30, 30))
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        self.bold_button_2.setFont(font5)
        self.bold_button_2.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_28.addWidget(self.bold_button_2)

        self.italic_button_2 = QPushButton(self.verticalLayoutWidget_5)
        self.italic_button_2.setObjectName(u"italic_button_2")
        sizePolicy1.setHeightForWidth(self.italic_button_2.sizePolicy().hasHeightForWidth())
        self.italic_button_2.setSizePolicy(sizePolicy1)
        self.italic_button_2.setMaximumSize(QSize(30, 30))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(16)
        font6.setBold(False)
        font6.setItalic(True)
        self.italic_button_2.setFont(font6)
        self.italic_button_2.setStyleSheet(u"\n"
"\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_28.addWidget(self.italic_button_2)

        self.underline_button_2 = QPushButton(self.verticalLayoutWidget_5)
        self.underline_button_2.setObjectName(u"underline_button_2")
        sizePolicy1.setHeightForWidth(self.underline_button_2.sizePolicy().hasHeightForWidth())
        self.underline_button_2.setSizePolicy(sizePolicy1)
        self.underline_button_2.setMaximumSize(QSize(30, 30))
        font7 = QFont()
        font7.setPointSize(16)
        font7.setBold(False)
        font7.setUnderline(True)
        self.underline_button_2.setFont(font7)
        self.underline_button_2.setStyleSheet(u"\n"
"\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_28.addWidget(self.underline_button_2)

        self.horizontalSpacer_9 = QSpacerItem(120, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_9)

        self.insert_combo_2 = QComboBox(self.verticalLayoutWidget_5)
        self.insert_combo_2.addItem("")
        self.insert_combo_2.setObjectName(u"insert_combo_2")
        sizePolicy1.setHeightForWidth(self.insert_combo_2.sizePolicy().hasHeightForWidth())
        self.insert_combo_2.setSizePolicy(sizePolicy1)
        self.insert_combo_2.setMinimumSize(QSize(70, 0))
        self.insert_combo_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.insert_combo_2.setEditable(False)

        self.horizontalLayout_28.addWidget(self.insert_combo_2)

        self.horizontalSpacer_10 = QSpacerItem(130, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_10)

        self.more_combo_2 = QComboBox(self.verticalLayoutWidget_5)
        self.more_combo_2.addItem("")
        self.more_combo_2.setObjectName(u"more_combo_2")
        sizePolicy1.setHeightForWidth(self.more_combo_2.sizePolicy().hasHeightForWidth())
        self.more_combo_2.setSizePolicy(sizePolicy1)
        self.more_combo_2.setMinimumSize(QSize(70, 0))
        self.more_combo_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.more_combo_2.setEditable(False)

        self.horizontalLayout_28.addWidget(self.more_combo_2)

        self.horizontalSpacer_23 = QSpacerItem(930, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_23)


        self.verticalLayout_4.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.send_button_2 = QPushButton(self.verticalLayoutWidget_5)
        self.send_button_2.setObjectName(u"send_button_2")
        sizePolicy1.setHeightForWidth(self.send_button_2.sizePolicy().hasHeightForWidth())
        self.send_button_2.setSizePolicy(sizePolicy1)
        self.send_button_2.setMinimumSize(QSize(105, 0))
        self.send_button_2.setMaximumSize(QSize(16777215, 30))
        self.send_button_2.setFont(font2)
        self.send_button_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")

        self.horizontalLayout_30.addWidget(self.send_button_2)

        self.horizontalSpacer_34 = QSpacerItem(330, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_34)

        self.text_combo_2 = QComboBox(self.verticalLayoutWidget_5)
        self.text_combo_2.addItem("")
        self.text_combo_2.setObjectName(u"text_combo_2")
        sizePolicy1.setHeightForWidth(self.text_combo_2.sizePolicy().hasHeightForWidth())
        self.text_combo_2.setSizePolicy(sizePolicy1)
        self.text_combo_2.setMinimumSize(QSize(70, 0))
        self.text_combo_2.setMaximumSize(QSize(16777215, 16777215))
        self.text_combo_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.text_combo_2.setEditable(False)

        self.horizontalLayout_30.addWidget(self.text_combo_2)

        self.size_combo_2 = QComboBox(self.verticalLayoutWidget_5)
        self.size_combo_2.addItem("")
        self.size_combo_2.setObjectName(u"size_combo_2")
        sizePolicy1.setHeightForWidth(self.size_combo_2.sizePolicy().hasHeightForWidth())
        self.size_combo_2.setSizePolicy(sizePolicy1)
        self.size_combo_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.size_combo_2.setEditable(False)

        self.horizontalLayout_30.addWidget(self.size_combo_2)

        self.letter_combo_2 = QComboBox(self.verticalLayoutWidget_5)
        self.letter_combo_2.addItem("")
        self.letter_combo_2.setObjectName(u"letter_combo_2")
        sizePolicy1.setHeightForWidth(self.letter_combo_2.sizePolicy().hasHeightForWidth())
        self.letter_combo_2.setSizePolicy(sizePolicy1)
        self.letter_combo_2.setMinimumSize(QSize(40, 0))
        self.letter_combo_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.letter_combo_2.setEditable(False)

        self.horizontalLayout_30.addWidget(self.letter_combo_2)

        self.horizontalSpacer_33 = QSpacerItem(925, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_33)


        self.verticalLayout_4.addLayout(self.horizontalLayout_30)

        self.stackedWidget.addWidget(self.abuan_page2)

        self.retranslateUi(contacts)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(contacts)
    # setupUi

    def retranslateUi(self, contacts):
        contacts.setWindowTitle(QCoreApplication.translate("contacts", u"Form", None))
        self.BackToContactsBtn_2.setText(QCoreApplication.translate("contacts", u"Back to Contacts", None))
        self.NewContacts_2.setText(QCoreApplication.translate("contacts", u"New Contact", None))
        self.ContactsInformation_2.setText(QCoreApplication.translate("contacts", u"Contact Infotmation", None))
        self.SearcAccount_2.setInputMask("")
        self.SearcAccount_2.setText("")
        self.SearcAccount_2.setPlaceholderText(QCoreApplication.translate("contacts", u"Search Account's Name", None))
        self.ContactOwner_2.setText(QCoreApplication.translate("contacts", u"Contact Owner :", None))
        self.ProfilePic_2.setText("")
        self.ProfileName_2.setText(QCoreApplication.translate("contacts", u"Jinita", None))
        self.UploadPic_2.setInputMask("")
        self.UploadPic_2.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("contacts", u"See File", None))
        self.Picture_2.setText(QCoreApplication.translate("contacts", u"Picture :", None))
        self.NameLabel_2.setText(QCoreApplication.translate("contacts", u"Name ", None))
        self.SalutationLabel_2.setText(QCoreApplication.translate("contacts", u"Salutation :", None))
        self.Salutation_2.setItemText(0, QCoreApplication.translate("contacts", u"New Item", None))
        self.Salutation_2.setItemText(1, QCoreApplication.translate("contacts", u"New Item", None))
        self.Salutation_2.setItemText(2, QCoreApplication.translate("contacts", u"New Item", None))
        self.Salutation_2.setItemText(3, QCoreApplication.translate("contacts", u"New Item", None))

        self.FirstNameLabel_2.setText(QCoreApplication.translate("contacts", u"First Name :", None))
        self.LastNameLabel_2.setText(QCoreApplication.translate("contacts", u"Last Name :", None))
        self.MiddleNameLabel_3.setText(QCoreApplication.translate("contacts", u"Middle Name :", None))
        self.SuffixLabel_3.setText(QCoreApplication.translate("contacts", u"Suffix :", None))
        self.DateOfBirthLabel_2.setText(QCoreApplication.translate("contacts", u"Date of Birth :", None))
        self.LeadStatusLabel_2.setText(QCoreApplication.translate("contacts", u"Lead Status :", None))
        self.LeadStatus_2.setItemText(0, QCoreApplication.translate("contacts", u"New Item", None))
        self.LeadStatus_2.setItemText(1, QCoreApplication.translate("contacts", u"New Item", None))
        self.LeadStatus_2.setItemText(2, QCoreApplication.translate("contacts", u"New Item", None))
        self.LeadStatus_2.setItemText(3, QCoreApplication.translate("contacts", u"New Item", None))

        self.TitleLabel_2.setText(QCoreApplication.translate("contacts", u"Title :", None))
        self.MiddleNameLabel_4.setText(QCoreApplication.translate("contacts", u"Email :", None))
        self.SuffixLabel_4.setText(QCoreApplication.translate("contacts", u"Phone Number :", None))
        self.AdditionalInformation_3.setText(QCoreApplication.translate("contacts", u"ADDITIONAL INFORMATION", None))
        self.SecondaryEmailLabel_2.setText(QCoreApplication.translate("contacts", u"Secondary Email :", None))
        self.OtherPhoneNumLabel_2.setText(QCoreApplication.translate("contacts", u"Other Phone Number  :", None))
        self.GenderLabel_2.setText(QCoreApplication.translate("contacts", u"Gender :", None))
        self.MaritalStatusLabel_2.setText(QCoreApplication.translate("contacts", u"Marital Status :", None))
        self.CompanyLabel_2.setText(QCoreApplication.translate("contacts", u"Company :", None))
        self.ReportsToLabel_2.setText(QCoreApplication.translate("contacts", u" Reports To :", None))
        self.FaxLabel_2.setText(QCoreApplication.translate("contacts", u"Fax :", None))
        self.AdditionalInformation_6.setText(QCoreApplication.translate("contacts", u"ADDRESS INFORMATION", None))
        self.AddressLabel_2.setText(QCoreApplication.translate("contacts", u"Address :", None))
        self.CountryLabel_2.setText(QCoreApplication.translate("contacts", u"Country  :", None))
        self.State_ProvinceLabel_2.setText(QCoreApplication.translate("contacts", u"State/Province :", None))
        self.ZipPostalCodeLabel_2.setText(QCoreApplication.translate("contacts", u"Zip/Postal Code :", None))
        self.CityLabel_2.setText(QCoreApplication.translate("contacts", u"City :", None))
        self.StreetLabel_2.setText(QCoreApplication.translate("contacts", u"Street :", None))
        self.Street_2.setText("")
        self.AdditionalInformation_7.setText(QCoreApplication.translate("contacts", u"DESCRIPTION INFORMATION", None))
        self.AdditionalInformation_8.setText(QCoreApplication.translate("contacts", u"ADDRESS INFORMATION", None))
        self.label_3.setText(QCoreApplication.translate("contacts", u"Created By :", None))
        self.label_4.setText(QCoreApplication.translate("contacts", u"Last Modified :", None))
        self.label_8.setText(QCoreApplication.translate("contacts", u"Contacts", None))
        self.search_3.setPlaceholderText(QCoreApplication.translate("contacts", u"Search", None))
        self.add_2.setText("")
        self.refresh_2.setText("")
        self.delete_3.setText("")
        self.allContacts_2.setPlaceholderText(QCoreApplication.translate("contacts", u"All Contacts", None))
        ___qtablewidgetitem = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("contacts", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("contacts", u"Email", None));
        ___qtablewidgetitem2 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("contacts", u"Phone Number", None));
        ___qtablewidgetitem3 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("contacts", u"Company", None));
        self.backToContacts.setText(QCoreApplication.translate("contacts", u"Back To Contacts", None))
        self.SalesPipeline.setText(QCoreApplication.translate("contacts", u"Sales Pipeline", None))
#if QT_CONFIG(tooltip)
        self.progressBar.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.progressBar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.progressBar.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.progressBar.setFormat("")
        self.prospecting.setText(QCoreApplication.translate("contacts", u"Prospecting", None))
        self.qualifications.setText(QCoreApplication.translate("contacts", u"Qualifications", None))
        self.contacting.setText(QCoreApplication.translate("contacts", u"Contacting", None))
        self.negotiating_with_the_lead.setText(QCoreApplication.translate("contacts", u"Negotiating with the Lead", None))
        self.closed_won.setText(QCoreApplication.translate("contacts", u"Closed Won", None))
        self.closed_loss.setText(QCoreApplication.translate("contacts", u"Closed Loss", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("contacts", u"Contacts", None));
        self.Timeline_3.setText(QCoreApplication.translate("contacts", u"Timeline", None))
        self.pin_3.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.search_5.setPlaceholderText(QCoreApplication.translate("contacts", u"Search", None))
        self.edit_3.setText("")
        self.link_3.setText("")
        self.attachment_3.setText("")
        self.ContactInformation.setText(QCoreApplication.translate("contacts", u"Contact Information", None))
        self.back_to_contacts_2.setText(QCoreApplication.translate("contacts", u"< Back to Contacts", None))
        self.logo_user_2.setText(QCoreApplication.translate("contacts", u"G", None))
        self.company_ni_gab_2.setText(QCoreApplication.translate("contacts", u"Company ni Gab", None))
        self.sales_pipeline_4.setText(QCoreApplication.translate("contacts", u"Sales Pipeline", None))
        self.closed_won_4.setText(QCoreApplication.translate("contacts", u"Closed Won", None))
        self.prospecting_4.setText(QCoreApplication.translate("contacts", u"Prospecting", None))
        self.negotiating_2.setText(QCoreApplication.translate("contacts", u"Negotiating with the lead", None))
        self.closing_4.setText(QCoreApplication.translate("contacts", u"Closing", None))
        self.closed_loss_4.setText(QCoreApplication.translate("contacts", u"Closed Loss", None))
        self.contacting_4.setText(QCoreApplication.translate("contacts", u"Contacting", None))
        self.building_relationship_4.setText(QCoreApplication.translate("contacts", u"Building Relationship", None))
        self.qualifications_4.setText(QCoreApplication.translate("contacts", u"Qualifications", None))
        ___qtablewidgetitem5 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("contacts", u"Contacts", None));
        self.contact_info_2.setText(QCoreApplication.translate("contacts", u"Contact Information", None))
        self.sales_funnel_label_2.setText(QCoreApplication.translate("contacts", u"Sales Funnel", None))
        self.from_label_2.setText(QCoreApplication.translate("contacts", u"From:", None))
        self.to_label_2.setText(QCoreApplication.translate("contacts", u"To:", None))
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
        self.insert_combo_2.setItemText(0, QCoreApplication.translate("contacts", u"Insert", None))

        self.insert_combo_2.setCurrentText(QCoreApplication.translate("contacts", u"Insert", None))
        self.more_combo_2.setItemText(0, QCoreApplication.translate("contacts", u"More", None))

        self.more_combo_2.setCurrentText(QCoreApplication.translate("contacts", u"More", None))
        self.send_button_2.setText(QCoreApplication.translate("contacts", u"Send", None))
        self.text_combo_2.setItemText(0, QCoreApplication.translate("contacts", u"Arial", None))

#if QT_CONFIG(accessibility)
        self.text_combo_2.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.text_combo_2.setCurrentText(QCoreApplication.translate("contacts", u"Arial", None))
        self.size_combo_2.setItemText(0, QCoreApplication.translate("contacts", u"11", None))

        self.size_combo_2.setCurrentText(QCoreApplication.translate("contacts", u"11", None))
        self.letter_combo_2.setItemText(0, QCoreApplication.translate("contacts", u"A", None))

        self.letter_combo_2.setCurrentText(QCoreApplication.translate("contacts", u"A", None))
    # retranslateUi

