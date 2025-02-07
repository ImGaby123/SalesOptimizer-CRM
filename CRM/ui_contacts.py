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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -88, 1218, 1218))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1200, 1200))
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
        self.widget1 = QWidget(self.frame)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(40, 380, 471, 561))
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.NameLabel = QLabel(self.widget1)
        self.NameLabel.setObjectName(u"NameLabel")
        self.NameLabel.setFont(font)
        self.NameLabel.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_3.addWidget(self.NameLabel)

        self.verticalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.SalutationLabel = QLabel(self.widget1)
        self.SalutationLabel.setObjectName(u"SalutationLabel")
        self.SalutationLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_3.addWidget(self.SalutationLabel)

        self.comboBox = QComboBox(self.widget1)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout_3.addWidget(self.comboBox)

        self.verticalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.FirstNameLabel = QLabel(self.widget1)
        self.FirstNameLabel.setObjectName(u"FirstNameLabel")
        self.FirstNameLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_3.addWidget(self.FirstNameLabel)

        self.FirstName = QLineEdit(self.widget1)
        self.FirstName.setObjectName(u"FirstName")
        self.FirstName.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_3.addWidget(self.FirstName)

        self.verticalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.LastNameLabel = QLabel(self.widget1)
        self.LastNameLabel.setObjectName(u"LastNameLabel")
        self.LastNameLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_3.addWidget(self.LastNameLabel)

        self.LastName = QLineEdit(self.widget1)
        self.LastName.setObjectName(u"LastName")
        self.LastName.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_3.addWidget(self.LastName)

        self.verticalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.MiddleNameLabel = QLabel(self.widget1)
        self.MiddleNameLabel.setObjectName(u"MiddleNameLabel")
        self.MiddleNameLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_3.addWidget(self.MiddleNameLabel)

        self.MiddleName = QLineEdit(self.widget1)
        self.MiddleName.setObjectName(u"MiddleName")
        self.MiddleName.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_3.addWidget(self.MiddleName)

        self.verticalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.SuffixLabel = QLabel(self.widget1)
        self.SuffixLabel.setObjectName(u"SuffixLabel")
        self.SuffixLabel.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_3.addWidget(self.SuffixLabel)

        self.Suffix = QLineEdit(self.widget1)
        self.Suffix.setObjectName(u"Suffix")
        self.Suffix.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_3.addWidget(self.Suffix)


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
        self.comboBox.setItemText(0, QCoreApplication.translate("contacts", u"New Item", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("contacts", u"New Item", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("contacts", u"New Item", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("contacts", u"New Item", None))

        self.FirstNameLabel.setText(QCoreApplication.translate("contacts", u"First Name :", None))
        self.LastNameLabel.setText(QCoreApplication.translate("contacts", u"Last Name :", None))
        self.MiddleNameLabel.setText(QCoreApplication.translate("contacts", u"Middle Name :", None))
        self.SuffixLabel.setText(QCoreApplication.translate("contacts", u"Suffix :", None))
    # retranslateUi

