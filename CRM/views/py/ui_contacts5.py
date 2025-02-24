# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts5.ui'
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
import views.py.icons_rc

class Ui_contacts5(object):
    def setupUi(self, contacts5):
        if not contacts5.objectName():
            contacts5.setObjectName(u"contacts5")
        contacts5.resize(1201, 681)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(contacts5.sizePolicy().hasHeightForWidth())
        contacts5.setSizePolicy(sizePolicy)
        self.gridLayout_22 = QGridLayout(contacts5)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.scrollArea_4 = QScrollArea(contacts5)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1222, 2522))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_4.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_4 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(1200, 2500))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.BackToContactsBtn_4 = QPushButton(self.frame_4)
        self.BackToContactsBtn_4.setObjectName(u"BackToContactsBtn_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BackToContactsBtn_4.sizePolicy().hasHeightForWidth())
        self.BackToContactsBtn_4.setSizePolicy(sizePolicy1)
        self.BackToContactsBtn_4.setStyleSheet(u"QPushButton {\n"
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
        self.BackToContactsBtn_4.setIcon(icon)

        self.gridLayout.addWidget(self.BackToContactsBtn_4, 0, 0, 1, 1)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.horizontalSpacer_142 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_142, 0, 0, 1, 1)

        self.NewContacts_4 = QLabel(self.frame_4)
        self.NewContacts_4.setObjectName(u"NewContacts_4")
        sizePolicy1.setHeightForWidth(self.NewContacts_4.sizePolicy().hasHeightForWidth())
        self.NewContacts_4.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.NewContacts_4.setFont(font)
        self.NewContacts_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_21.addWidget(self.NewContacts_4, 0, 1, 1, 1)

        self.horizontalSpacer_143 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_143, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_21, 1, 0, 1, 1)

        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_161 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_161, 0, 0, 1, 1)

        self.SearcAccount_4 = QLineEdit(self.frame_4)
        self.SearcAccount_4.setObjectName(u"SearcAccount_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.SearcAccount_4.sizePolicy().hasHeightForWidth())
        self.SearcAccount_4.setSizePolicy(sizePolicy2)
        self.SearcAccount_4.setMinimumSize(QSize(0, 30))

        self.gridLayout_3.addWidget(self.SearcAccount_4, 0, 1, 1, 1)

        self.horizontalSpacer_162 = QSpacerItem(900, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_162, 0, 2, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_3, 2, 0, 1, 1)

        self.widget_19 = QWidget(self.frame_4)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy2.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy2)
        self.widget_19.setMinimumSize(QSize(0, 25))
        self.widget_19.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.gridLayout_12 = QGridLayout(self.widget_19)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.ContactsInformation_4 = QLabel(self.widget_19)
        self.ContactsInformation_4.setObjectName(u"ContactsInformation_4")
        sizePolicy2.setHeightForWidth(self.ContactsInformation_4.sizePolicy().hasHeightForWidth())
        self.ContactsInformation_4.setSizePolicy(sizePolicy2)
        self.ContactsInformation_4.setMinimumSize(QSize(0, 30))
        self.ContactsInformation_4.setFont(font)
        self.ContactsInformation_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_12.addWidget(self.ContactsInformation_4, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.widget_19, 0, 0, 1, 1)

        self.verticalSpacer_95 = QSpacerItem(13, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_13.addItem(self.verticalSpacer_95, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_13, 2, 0, 1, 2)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.horizontalSpacer_149 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_149, 0, 0, 1, 1)

        self.ContactOwner_4 = QLabel(self.frame_4)
        self.ContactOwner_4.setObjectName(u"ContactOwner_4")
        sizePolicy2.setHeightForWidth(self.ContactOwner_4.sizePolicy().hasHeightForWidth())
        self.ContactOwner_4.setSizePolicy(sizePolicy2)
        self.ContactOwner_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_20.addWidget(self.ContactOwner_4, 0, 1, 1, 1)

        self.horizontalSpacer_150 = QSpacerItem(450, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_150, 0, 2, 1, 1)

        self.Picture_4 = QLabel(self.frame_4)
        self.Picture_4.setObjectName(u"Picture_4")
        sizePolicy2.setHeightForWidth(self.Picture_4.sizePolicy().hasHeightForWidth())
        self.Picture_4.setSizePolicy(sizePolicy2)
        self.Picture_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_20.addWidget(self.Picture_4, 0, 3, 1, 1)

        self.horizontalSpacer_151 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_151, 0, 4, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_20, 3, 0, 1, 2)

        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.widget_18 = QWidget(self.frame_4)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy2.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy2)
        self.widget_18.setMinimumSize(QSize(0, 40))
        self.widget_18.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.gridLayout_7 = QGridLayout(self.widget_18)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.AdditionalInformation_5 = QLabel(self.widget_18)
        self.AdditionalInformation_5.setObjectName(u"AdditionalInformation_5")
        sizePolicy2.setHeightForWidth(self.AdditionalInformation_5.sizePolicy().hasHeightForWidth())
        self.AdditionalInformation_5.setSizePolicy(sizePolicy2)
        self.AdditionalInformation_5.setFont(font)
        self.AdditionalInformation_5.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_7.addWidget(self.AdditionalInformation_5, 0, 0, 1, 1)


        self.gridLayout_27.addWidget(self.widget_18, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_27, 6, 0, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.widget_20 = QWidget(self.frame_4)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy2.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy2)
        self.widget_20.setMinimumSize(QSize(0, 40))
        self.widget_20.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.gridLayout_4 = QGridLayout(self.widget_20)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.AdditionalInformation_14 = QLabel(self.widget_20)
        self.AdditionalInformation_14.setObjectName(u"AdditionalInformation_14")
        sizePolicy2.setHeightForWidth(self.AdditionalInformation_14.sizePolicy().hasHeightForWidth())
        self.AdditionalInformation_14.setSizePolicy(sizePolicy2)
        self.AdditionalInformation_14.setFont(font)
        self.AdditionalInformation_14.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_4.addWidget(self.AdditionalInformation_14, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.widget_20, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_14, 8, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 9, 1, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.verticalSpacer_94 = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_15.addItem(self.verticalSpacer_94, 1, 0, 1, 1)

        self.widget_17 = QWidget(self.frame_4)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy2.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy2)
        self.widget_17.setMinimumSize(QSize(0, 40))
        self.widget_17.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.gridLayout_6 = QGridLayout(self.widget_17)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.AdditionalInformation_13 = QLabel(self.widget_17)
        self.AdditionalInformation_13.setObjectName(u"AdditionalInformation_13")
        sizePolicy2.setHeightForWidth(self.AdditionalInformation_13.sizePolicy().hasHeightForWidth())
        self.AdditionalInformation_13.setSizePolicy(sizePolicy2)
        self.AdditionalInformation_13.setFont(font)
        self.AdditionalInformation_13.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_6.addWidget(self.AdditionalInformation_13, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.widget_17, 2, 0, 1, 1)

        self.widget_16 = QWidget(self.frame_4)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy2.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy2)
        self.widget_16.setMinimumSize(QSize(0, 40))
        self.widget_16.setStyleSheet(u"background-color: rgb(149, 149, 149);")
        self.gridLayout_5 = QGridLayout(self.widget_16)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.AdditionalInformation_12 = QLabel(self.widget_16)
        self.AdditionalInformation_12.setObjectName(u"AdditionalInformation_12")
        sizePolicy2.setHeightForWidth(self.AdditionalInformation_12.sizePolicy().hasHeightForWidth())
        self.AdditionalInformation_12.setSizePolicy(sizePolicy2)
        self.AdditionalInformation_12.setFont(font)
        self.AdditionalInformation_12.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_5.addWidget(self.AdditionalInformation_12, 2, 0, 1, 1)


        self.gridLayout_15.addWidget(self.widget_16, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_15, 12, 0, 1, 1)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.LastModifiedLabel_3 = QLabel(self.frame_4)
        self.LastModifiedLabel_3.setObjectName(u"LastModifiedLabel_3")
        sizePolicy1.setHeightForWidth(self.LastModifiedLabel_3.sizePolicy().hasHeightForWidth())
        self.LastModifiedLabel_3.setSizePolicy(sizePolicy1)
        self.LastModifiedLabel_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_19.addWidget(self.LastModifiedLabel_3, 0, 0, 1, 1)

        self.horizontalSpacer_158 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_158, 0, 1, 1, 1)

        self.LastModified_Label_3 = QLabel(self.frame_4)
        self.LastModified_Label_3.setObjectName(u"LastModified_Label_3")
        sizePolicy2.setHeightForWidth(self.LastModified_Label_3.sizePolicy().hasHeightForWidth())
        self.LastModified_Label_3.setSizePolicy(sizePolicy2)

        self.gridLayout_19.addWidget(self.LastModified_Label_3, 0, 2, 1, 1)

        self.horizontalSpacer_159 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_159, 0, 3, 1, 1)

        self.CreatedByLabel_3 = QLabel(self.frame_4)
        self.CreatedByLabel_3.setObjectName(u"CreatedByLabel_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.CreatedByLabel_3.sizePolicy().hasHeightForWidth())
        self.CreatedByLabel_3.setSizePolicy(sizePolicy3)
        self.CreatedByLabel_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_19.addWidget(self.CreatedByLabel_3, 0, 4, 1, 1)

        self.horizontalSpacer_160 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_160, 0, 5, 1, 1)

        self.CreatedBy_Label_3 = QLabel(self.frame_4)
        self.CreatedBy_Label_3.setObjectName(u"CreatedBy_Label_3")
        sizePolicy2.setHeightForWidth(self.CreatedBy_Label_3.sizePolicy().hasHeightForWidth())
        self.CreatedBy_Label_3.setSizePolicy(sizePolicy2)

        self.gridLayout_19.addWidget(self.CreatedBy_Label_3, 0, 6, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_19, 13, 0, 1, 1)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.ProfilePic_4 = QLabel(self.frame_4)
        self.ProfilePic_4.setObjectName(u"ProfilePic_4")
        self.ProfilePic_4.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.ProfilePic_4.sizePolicy().hasHeightForWidth())
        self.ProfilePic_4.setSizePolicy(sizePolicy2)
        self.ProfilePic_4.setMaximumSize(QSize(50, 50))
        self.ProfilePic_4.setStyleSheet(u"QLabel#ProfilePic {\n"
"    width: 50px; /* Palitan ayon sa gusto mong laki */\n"
"    height: 50px;\n"
"    border-radius: 25px; /* Kalahati ng width/height para maging bilog */\n"
"    background-color: #E5DAFB; /* Light purple background */\n"
"    border: 1px solid #D0C4F0; /* Optional: Light border */\n"
"}\n"
"")
        self.ProfilePic_4.setPixmap(QPixmap(u":/new/newPrefix/Resources/user.png"))
        self.ProfilePic_4.setScaledContents(True)

        self.gridLayout_26.addWidget(self.ProfilePic_4, 0, 0, 2, 1)

        self.horizontalSpacer_148 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_148, 0, 2, 2, 1)

        self.UploadPic_4 = QLineEdit(self.frame_4)
        self.UploadPic_4.setObjectName(u"UploadPic_4")
        sizePolicy2.setHeightForWidth(self.UploadPic_4.sizePolicy().hasHeightForWidth())
        self.UploadPic_4.setSizePolicy(sizePolicy2)
        self.UploadPic_4.setMinimumSize(QSize(0, 30))
        self.UploadPic_4.setStyleSheet(u"")
        self.UploadPic_4.setCursorPosition(0)

        self.gridLayout_26.addWidget(self.UploadPic_4, 0, 3, 2, 1)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_26.addWidget(self.pushButton_4, 2, 3, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.ProfileName_4 = QLabel(self.frame_4)
        self.ProfileName_4.setObjectName(u"ProfileName_4")
        sizePolicy2.setHeightForWidth(self.ProfileName_4.sizePolicy().hasHeightForWidth())
        self.ProfileName_4.setSizePolicy(sizePolicy2)
        self.ProfileName_4.setFont(font)
        self.ProfileName_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.ProfileName_4.setScaledContents(True)

        self.gridLayout_26.addWidget(self.ProfileName_4, 1, 1, 1, 1)


        self.gridLayout_25.addLayout(self.gridLayout_26, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_25, 4, 0, 1, 2)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_145 = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_145, 0, 2, 1, 1)

        self.horizontalSpacer_144 = QSpacerItem(10, 10, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_144, 0, 0, 1, 1)

        self.horizontalSpacer_146 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_146, 0, 4, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalSpacer_83 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_83, 10, 0, 1, 1)

        self.MiddleNameLabel_8 = QLabel(self.frame_4)
        self.MiddleNameLabel_8.setObjectName(u"MiddleNameLabel_8")
        sizePolicy2.setHeightForWidth(self.MiddleNameLabel_8.sizePolicy().hasHeightForWidth())
        self.MiddleNameLabel_8.setSizePolicy(sizePolicy2)
        self.MiddleNameLabel_8.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.MiddleNameLabel_8, 12, 0, 1, 1)

        self.TitleLabel_4 = QLabel(self.frame_4)
        self.TitleLabel_4.setObjectName(u"TitleLabel_4")
        sizePolicy2.setHeightForWidth(self.TitleLabel_4.sizePolicy().hasHeightForWidth())
        self.TitleLabel_4.setSizePolicy(sizePolicy2)
        self.TitleLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.TitleLabel_4, 8, 0, 1, 1)

        self.SuffixLabel_8 = QLabel(self.frame_4)
        self.SuffixLabel_8.setObjectName(u"SuffixLabel_8")
        sizePolicy2.setHeightForWidth(self.SuffixLabel_8.sizePolicy().hasHeightForWidth())
        self.SuffixLabel_8.setSizePolicy(sizePolicy2)
        self.SuffixLabel_8.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.SuffixLabel_8, 16, 0, 1, 1)

        self.verticalSpacer_82 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_82, 6, 0, 1, 1)

        self.Suffix_8 = QLineEdit(self.frame_4)
        self.Suffix_8.setObjectName(u"Suffix_8")
        sizePolicy.setHeightForWidth(self.Suffix_8.sizePolicy().hasHeightForWidth())
        self.Suffix_8.setSizePolicy(sizePolicy)
        self.Suffix_8.setMaximumSize(QSize(16777215, 150))

        self.gridLayout_10.addWidget(self.Suffix_8, 17, 0, 1, 1)

        self.LeadStatusLabel_4 = QLabel(self.frame_4)
        self.LeadStatusLabel_4.setObjectName(u"LeadStatusLabel_4")
        sizePolicy2.setHeightForWidth(self.LeadStatusLabel_4.sizePolicy().hasHeightForWidth())
        self.LeadStatusLabel_4.setSizePolicy(sizePolicy2)
        self.LeadStatusLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.LeadStatusLabel_4, 4, 0, 1, 1)

        self.LeadStatus_4 = QComboBox(self.frame_4)
        self.LeadStatus_4.addItem("")
        self.LeadStatus_4.addItem("")
        self.LeadStatus_4.addItem("")
        self.LeadStatus_4.addItem("")
        self.LeadStatus_4.setObjectName(u"LeadStatus_4")
        sizePolicy.setHeightForWidth(self.LeadStatus_4.sizePolicy().hasHeightForWidth())
        self.LeadStatus_4.setSizePolicy(sizePolicy)
        self.LeadStatus_4.setMaximumSize(QSize(16777215, 150))

        self.gridLayout_10.addWidget(self.LeadStatus_4, 5, 0, 1, 1)

        self.Email_4 = QLineEdit(self.frame_4)
        self.Email_4.setObjectName(u"Email_4")
        sizePolicy.setHeightForWidth(self.Email_4.sizePolicy().hasHeightForWidth())
        self.Email_4.setSizePolicy(sizePolicy)
        self.Email_4.setMaximumSize(QSize(16777215, 150))

        self.gridLayout_10.addWidget(self.Email_4, 13, 0, 1, 1)

        self.DateOfBIrth_4 = QLineEdit(self.frame_4)
        self.DateOfBIrth_4.setObjectName(u"DateOfBIrth_4")
        sizePolicy.setHeightForWidth(self.DateOfBIrth_4.sizePolicy().hasHeightForWidth())
        self.DateOfBIrth_4.setSizePolicy(sizePolicy)
        self.DateOfBIrth_4.setMinimumSize(QSize(0, 0))
        self.DateOfBIrth_4.setMaximumSize(QSize(16777215, 150))

        self.gridLayout_10.addWidget(self.DateOfBIrth_4, 1, 0, 1, 1)

        self.verticalSpacer_84 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_84, 14, 0, 1, 1)

        self.DateOfBirthLabel_4 = QLabel(self.frame_4)
        self.DateOfBirthLabel_4.setObjectName(u"DateOfBirthLabel_4")
        sizePolicy2.setHeightForWidth(self.DateOfBirthLabel_4.sizePolicy().hasHeightForWidth())
        self.DateOfBirthLabel_4.setSizePolicy(sizePolicy2)
        self.DateOfBirthLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_10.addWidget(self.DateOfBirthLabel_4, 0, 0, 1, 1)

        self.Title_4 = QLineEdit(self.frame_4)
        self.Title_4.setObjectName(u"Title_4")
        sizePolicy.setHeightForWidth(self.Title_4.sizePolicy().hasHeightForWidth())
        self.Title_4.setSizePolicy(sizePolicy)
        self.Title_4.setMaximumSize(QSize(16777215, 150))

        self.gridLayout_10.addWidget(self.Title_4, 9, 0, 1, 1)

        self.verticalSpacer_81 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_81, 2, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_10, 0, 3, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.LastNameLabel_4 = QLabel(self.frame_4)
        self.LastNameLabel_4.setObjectName(u"LastNameLabel_4")
        sizePolicy2.setHeightForWidth(self.LastNameLabel_4.sizePolicy().hasHeightForWidth())
        self.LastNameLabel_4.setSizePolicy(sizePolicy2)
        self.LastNameLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.LastNameLabel_4, 11, 0, 1, 1)

        self.FirstName_4 = QLineEdit(self.frame_4)
        self.FirstName_4.setObjectName(u"FirstName_4")
        sizePolicy.setHeightForWidth(self.FirstName_4.sizePolicy().hasHeightForWidth())
        self.FirstName_4.setSizePolicy(sizePolicy)
        self.FirstName_4.setMaximumSize(QSize(16777215, 300))

        self.gridLayout_9.addWidget(self.FirstName_4, 8, 0, 1, 1)

        self.verticalSpacer_77 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_77, 5, 0, 1, 1)

        self.LastName_4 = QLineEdit(self.frame_4)
        self.LastName_4.setObjectName(u"LastName_4")
        sizePolicy.setHeightForWidth(self.LastName_4.sizePolicy().hasHeightForWidth())
        self.LastName_4.setSizePolicy(sizePolicy)
        self.LastName_4.setMaximumSize(QSize(16777215, 300))

        self.gridLayout_9.addWidget(self.LastName_4, 12, 0, 1, 1)

        self.FirstNameLabel_4 = QLabel(self.frame_4)
        self.FirstNameLabel_4.setObjectName(u"FirstNameLabel_4")
        sizePolicy2.setHeightForWidth(self.FirstNameLabel_4.sizePolicy().hasHeightForWidth())
        self.FirstNameLabel_4.setSizePolicy(sizePolicy2)
        self.FirstNameLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.FirstNameLabel_4, 7, 0, 1, 1)

        self.SalutationLabel_4 = QLabel(self.frame_4)
        self.SalutationLabel_4.setObjectName(u"SalutationLabel_4")
        sizePolicy2.setHeightForWidth(self.SalutationLabel_4.sizePolicy().hasHeightForWidth())
        self.SalutationLabel_4.setSizePolicy(sizePolicy2)
        self.SalutationLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.SalutationLabel_4, 3, 0, 1, 1)

        self.NameLabel_4 = QLabel(self.frame_4)
        self.NameLabel_4.setObjectName(u"NameLabel_4")
        sizePolicy2.setHeightForWidth(self.NameLabel_4.sizePolicy().hasHeightForWidth())
        self.NameLabel_4.setSizePolicy(sizePolicy2)
        self.NameLabel_4.setFont(font)
        self.NameLabel_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.gridLayout_9.addWidget(self.NameLabel_4, 0, 0, 1, 1)

        self.SuffixLabel_7 = QLabel(self.frame_4)
        self.SuffixLabel_7.setObjectName(u"SuffixLabel_7")
        sizePolicy2.setHeightForWidth(self.SuffixLabel_7.sizePolicy().hasHeightForWidth())
        self.SuffixLabel_7.setSizePolicy(sizePolicy2)
        self.SuffixLabel_7.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.SuffixLabel_7, 19, 0, 1, 1)

        self.verticalSpacer_79 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_79, 13, 0, 1, 1)

        self.verticalSpacer_76 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_76, 1, 0, 1, 1)

        self.MiddleName_4 = QLineEdit(self.frame_4)
        self.MiddleName_4.setObjectName(u"MiddleName_4")
        sizePolicy.setHeightForWidth(self.MiddleName_4.sizePolicy().hasHeightForWidth())
        self.MiddleName_4.setSizePolicy(sizePolicy)
        self.MiddleName_4.setMaximumSize(QSize(16777215, 300))

        self.gridLayout_9.addWidget(self.MiddleName_4, 16, 0, 1, 1)

        self.Salutation_4 = QComboBox(self.frame_4)
        self.Salutation_4.addItem("")
        self.Salutation_4.addItem("")
        self.Salutation_4.addItem("")
        self.Salutation_4.addItem("")
        self.Salutation_4.setObjectName(u"Salutation_4")
        sizePolicy.setHeightForWidth(self.Salutation_4.sizePolicy().hasHeightForWidth())
        self.Salutation_4.setSizePolicy(sizePolicy)
        self.Salutation_4.setMaximumSize(QSize(16777215, 150))

        self.gridLayout_9.addWidget(self.Salutation_4, 4, 0, 1, 1)

        self.Suffix_7 = QLineEdit(self.frame_4)
        self.Suffix_7.setObjectName(u"Suffix_7")
        sizePolicy.setHeightForWidth(self.Suffix_7.sizePolicy().hasHeightForWidth())
        self.Suffix_7.setSizePolicy(sizePolicy)
        self.Suffix_7.setMaximumSize(QSize(16777215, 300))

        self.gridLayout_9.addWidget(self.Suffix_7, 20, 0, 1, 1)

        self.verticalSpacer_78 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_78, 9, 0, 1, 1)

        self.MiddleNameLabel_7 = QLabel(self.frame_4)
        self.MiddleNameLabel_7.setObjectName(u"MiddleNameLabel_7")
        sizePolicy2.setHeightForWidth(self.MiddleNameLabel_7.sizePolicy().hasHeightForWidth())
        self.MiddleNameLabel_7.setSizePolicy(sizePolicy2)
        self.MiddleNameLabel_7.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_9.addWidget(self.MiddleNameLabel_7, 15, 0, 1, 1)

        self.verticalSpacer_80 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_80, 17, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_8, 5, 0, 1, 2)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalSpacer_152 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_152, 0, 0, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.SecondaryEmail_4 = QLineEdit(self.frame_4)
        self.SecondaryEmail_4.setObjectName(u"SecondaryEmail_4")
        sizePolicy2.setHeightForWidth(self.SecondaryEmail_4.sizePolicy().hasHeightForWidth())
        self.SecondaryEmail_4.setSizePolicy(sizePolicy2)
        self.SecondaryEmail_4.setMinimumSize(QSize(0, 40))
        self.SecondaryEmail_4.setMaximumSize(QSize(16777215, 300))

        self.gridLayout_16.addWidget(self.SecondaryEmail_4, 1, 0, 1, 1)

        self.verticalSpacer_85 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_85, 2, 0, 1, 1)

        self.verticalSpacer_86 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_86, 6, 0, 1, 1)

        self.OtherPhoneNumLabel_4 = QLabel(self.frame_4)
        self.OtherPhoneNumLabel_4.setObjectName(u"OtherPhoneNumLabel_4")
        sizePolicy2.setHeightForWidth(self.OtherPhoneNumLabel_4.sizePolicy().hasHeightForWidth())
        self.OtherPhoneNumLabel_4.setSizePolicy(sizePolicy2)
        self.OtherPhoneNumLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_16.addWidget(self.OtherPhoneNumLabel_4, 4, 0, 1, 1)

        self.GenderLabel_4 = QLabel(self.frame_4)
        self.GenderLabel_4.setObjectName(u"GenderLabel_4")
        sizePolicy2.setHeightForWidth(self.GenderLabel_4.sizePolicy().hasHeightForWidth())
        self.GenderLabel_4.setSizePolicy(sizePolicy2)
        self.GenderLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_16.addWidget(self.GenderLabel_4, 8, 0, 1, 1)

        self.SecondaryEmailLabel_4 = QLabel(self.frame_4)
        self.SecondaryEmailLabel_4.setObjectName(u"SecondaryEmailLabel_4")
        sizePolicy2.setHeightForWidth(self.SecondaryEmailLabel_4.sizePolicy().hasHeightForWidth())
        self.SecondaryEmailLabel_4.setSizePolicy(sizePolicy2)
        self.SecondaryEmailLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_16.addWidget(self.SecondaryEmailLabel_4, 0, 0, 1, 1)

        self.Gender_4 = QLineEdit(self.frame_4)
        self.Gender_4.setObjectName(u"Gender_4")
        sizePolicy2.setHeightForWidth(self.Gender_4.sizePolicy().hasHeightForWidth())
        self.Gender_4.setSizePolicy(sizePolicy2)
        self.Gender_4.setMinimumSize(QSize(0, 40))
        self.Gender_4.setMaximumSize(QSize(16777215, 300))

        self.gridLayout_16.addWidget(self.Gender_4, 9, 0, 1, 1)

        self.MaritalStatus_4 = QLineEdit(self.frame_4)
        self.MaritalStatus_4.setObjectName(u"MaritalStatus_4")
        sizePolicy2.setHeightForWidth(self.MaritalStatus_4.sizePolicy().hasHeightForWidth())
        self.MaritalStatus_4.setSizePolicy(sizePolicy2)
        self.MaritalStatus_4.setMinimumSize(QSize(0, 40))
        self.MaritalStatus_4.setMaximumSize(QSize(16777215, 150))

        self.gridLayout_16.addWidget(self.MaritalStatus_4, 13, 0, 1, 1)

        self.OtherPhoneNum_4 = QLineEdit(self.frame_4)
        self.OtherPhoneNum_4.setObjectName(u"OtherPhoneNum_4")
        sizePolicy2.setHeightForWidth(self.OtherPhoneNum_4.sizePolicy().hasHeightForWidth())
        self.OtherPhoneNum_4.setSizePolicy(sizePolicy2)
        self.OtherPhoneNum_4.setMinimumSize(QSize(0, 40))
        self.OtherPhoneNum_4.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_16.addWidget(self.OtherPhoneNum_4, 5, 0, 1, 1)

        self.MaritalStatusLabel_4 = QLabel(self.frame_4)
        self.MaritalStatusLabel_4.setObjectName(u"MaritalStatusLabel_4")
        sizePolicy2.setHeightForWidth(self.MaritalStatusLabel_4.sizePolicy().hasHeightForWidth())
        self.MaritalStatusLabel_4.setSizePolicy(sizePolicy2)
        self.MaritalStatusLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_16.addWidget(self.MaritalStatusLabel_4, 12, 0, 1, 1)

        self.verticalSpacer_87 = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_87, 10, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_16, 0, 1, 1, 1)

        self.horizontalSpacer_153 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_153, 0, 2, 1, 1)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.verticalSpacer_89 = QSpacerItem(30, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_17.addItem(self.verticalSpacer_89, 6, 0, 1, 1)

        self.verticalSpacer_102 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_17.addItem(self.verticalSpacer_102, 10, 0, 1, 1)

        self.ReportsTo_4 = QLineEdit(self.frame_4)
        self.ReportsTo_4.setObjectName(u"ReportsTo_4")
        sizePolicy2.setHeightForWidth(self.ReportsTo_4.sizePolicy().hasHeightForWidth())
        self.ReportsTo_4.setSizePolicy(sizePolicy2)
        self.ReportsTo_4.setMinimumSize(QSize(0, 10))
        self.ReportsTo_4.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_17.addWidget(self.ReportsTo_4, 5, 0, 1, 1)

        self.ReportsToLabel_4 = QLabel(self.frame_4)
        self.ReportsToLabel_4.setObjectName(u"ReportsToLabel_4")
        sizePolicy2.setHeightForWidth(self.ReportsToLabel_4.sizePolicy().hasHeightForWidth())
        self.ReportsToLabel_4.setSizePolicy(sizePolicy2)
        self.ReportsToLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_17.addWidget(self.ReportsToLabel_4, 4, 0, 1, 1)

        self.Fax_4 = QLineEdit(self.frame_4)
        self.Fax_4.setObjectName(u"Fax_4")
        sizePolicy2.setHeightForWidth(self.Fax_4.sizePolicy().hasHeightForWidth())
        self.Fax_4.setSizePolicy(sizePolicy2)
        self.Fax_4.setMinimumSize(QSize(0, 30))
        self.Fax_4.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_17.addWidget(self.Fax_4, 9, 0, 1, 1)

        self.CompanyLabel_4 = QLabel(self.frame_4)
        self.CompanyLabel_4.setObjectName(u"CompanyLabel_4")
        sizePolicy2.setHeightForWidth(self.CompanyLabel_4.sizePolicy().hasHeightForWidth())
        self.CompanyLabel_4.setSizePolicy(sizePolicy2)
        self.CompanyLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_17.addWidget(self.CompanyLabel_4, 0, 0, 1, 1)

        self.FaxLabel_4 = QLabel(self.frame_4)
        self.FaxLabel_4.setObjectName(u"FaxLabel_4")
        sizePolicy2.setHeightForWidth(self.FaxLabel_4.sizePolicy().hasHeightForWidth())
        self.FaxLabel_4.setSizePolicy(sizePolicy2)
        self.FaxLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_17.addWidget(self.FaxLabel_4, 8, 0, 1, 1)

        self.Company_4 = QLineEdit(self.frame_4)
        self.Company_4.setObjectName(u"Company_4")
        sizePolicy2.setHeightForWidth(self.Company_4.sizePolicy().hasHeightForWidth())
        self.Company_4.setSizePolicy(sizePolicy2)
        self.Company_4.setMinimumSize(QSize(0, 0))
        self.Company_4.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_17.addWidget(self.Company_4, 1, 0, 1, 1)

        self.verticalSpacer_88 = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_17.addItem(self.verticalSpacer_88, 2, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_17, 0, 3, 1, 1)

        self.horizontalSpacer_154 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_154, 0, 4, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_11, 7, 0, 1, 2)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.CityLabel_4 = QLabel(self.frame_4)
        self.CityLabel_4.setObjectName(u"CityLabel_4")
        sizePolicy2.setHeightForWidth(self.CityLabel_4.sizePolicy().hasHeightForWidth())
        self.CityLabel_4.setSizePolicy(sizePolicy2)
        self.CityLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_23.addWidget(self.CityLabel_4, 0, 0, 1, 1)

        self.City_4 = QLineEdit(self.frame_4)
        self.City_4.setObjectName(u"City_4")
        self.City_4.setMinimumSize(QSize(0, 31))
        self.City_4.setMaximumSize(QSize(16777215, 300))

        self.gridLayout_23.addWidget(self.City_4, 1, 0, 1, 1)

        self.verticalSpacer_93 = QSpacerItem(10, 90, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_93, 2, 1, 1, 1)

        self.StreetLabel_4 = QLabel(self.frame_4)
        self.StreetLabel_4.setObjectName(u"StreetLabel_4")
        sizePolicy2.setHeightForWidth(self.StreetLabel_4.sizePolicy().hasHeightForWidth())
        self.StreetLabel_4.setSizePolicy(sizePolicy2)
        self.StreetLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.gridLayout_23.addWidget(self.StreetLabel_4, 3, 0, 1, 1)

        self.Street_4 = QLabel(self.frame_4)
        self.Street_4.setObjectName(u"Street_4")
        sizePolicy2.setHeightForWidth(self.Street_4.sizePolicy().hasHeightForWidth())
        self.Street_4.setSizePolicy(sizePolicy2)
        self.Street_4.setMinimumSize(QSize(0, 300))
        self.Street_4.setStyleSheet(u" QLabel {\n"
"        border-radius: 50px; /* Half of the width/height */\n"
"       background-color: rgb(108, 108, 108);\n"
"    }\n"
"\n"
"")

        self.gridLayout_23.addWidget(self.Street_4, 4, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_23, 0, 3, 1, 1)

        self.horizontalSpacer_156 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_156, 0, 2, 1, 1)

        self.horizontalSpacer_157 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_157, 0, 4, 1, 1)

        self.horizontalSpacer_155 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_155, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.AddressLabel_4 = QLabel(self.frame_4)
        self.AddressLabel_4.setObjectName(u"AddressLabel_4")
        sizePolicy2.setHeightForWidth(self.AddressLabel_4.sizePolicy().hasHeightForWidth())
        self.AddressLabel_4.setSizePolicy(sizePolicy2)
        self.AddressLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_3.addWidget(self.AddressLabel_4)

        self.Address_4 = QLineEdit(self.frame_4)
        self.Address_4.setObjectName(u"Address_4")
        self.Address_4.setMinimumSize(QSize(0, 0))
        self.Address_4.setMaximumSize(QSize(16777215, 300))

        self.verticalLayout_3.addWidget(self.Address_4)

        self.verticalSpacer_90 = QSpacerItem(10, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_90)

        self.CountryLabel_4 = QLabel(self.frame_4)
        self.CountryLabel_4.setObjectName(u"CountryLabel_4")
        sizePolicy2.setHeightForWidth(self.CountryLabel_4.sizePolicy().hasHeightForWidth())
        self.CountryLabel_4.setSizePolicy(sizePolicy2)
        self.CountryLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_3.addWidget(self.CountryLabel_4)

        self.Country_4 = QLineEdit(self.frame_4)
        self.Country_4.setObjectName(u"Country_4")
        self.Country_4.setMinimumSize(QSize(0, 0))
        self.Country_4.setMaximumSize(QSize(300, 300))

        self.verticalLayout_3.addWidget(self.Country_4)

        self.verticalSpacer_91 = QSpacerItem(10, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_91)

        self.State_ProvinceLabel_4 = QLabel(self.frame_4)
        self.State_ProvinceLabel_4.setObjectName(u"State_ProvinceLabel_4")
        sizePolicy2.setHeightForWidth(self.State_ProvinceLabel_4.sizePolicy().hasHeightForWidth())
        self.State_ProvinceLabel_4.setSizePolicy(sizePolicy2)
        self.State_ProvinceLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_3.addWidget(self.State_ProvinceLabel_4)

        self.StateProvince_4 = QLineEdit(self.frame_4)
        self.StateProvince_4.setObjectName(u"StateProvince_4")
        self.StateProvince_4.setMaximumSize(QSize(300, 300))

        self.verticalLayout_3.addWidget(self.StateProvince_4)

        self.verticalSpacer_92 = QSpacerItem(10, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_92)

        self.ZipPostalCodeLabel_4 = QLabel(self.frame_4)
        self.ZipPostalCodeLabel_4.setObjectName(u"ZipPostalCodeLabel_4")
        sizePolicy2.setHeightForWidth(self.ZipPostalCodeLabel_4.sizePolicy().hasHeightForWidth())
        self.ZipPostalCodeLabel_4.setSizePolicy(sizePolicy2)
        self.ZipPostalCodeLabel_4.setStyleSheet(u"color: rgb(98, 98, 98);")

        self.verticalLayout_3.addWidget(self.ZipPostalCodeLabel_4)

        self.ZipPostalCode_4 = QLineEdit(self.frame_4)
        self.ZipPostalCode_4.setObjectName(u"ZipPostalCode_4")
        self.ZipPostalCode_4.setMaximumSize(QSize(300, 300))

        self.verticalLayout_3.addWidget(self.ZipPostalCode_4)


        self.gridLayout_18.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_2, 1, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_18, 10, 0, 1, 2)


        self.gridLayout_2.addWidget(self.frame_4, 0, 1, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_22.addWidget(self.scrollArea_4, 0, 0, 1, 1)


        self.retranslateUi(contacts5)

        QMetaObject.connectSlotsByName(contacts5)
    # setupUi

    def retranslateUi(self, contacts5):
        contacts5.setWindowTitle(QCoreApplication.translate("contacts5", u"Form", None))
        self.BackToContactsBtn_4.setText(QCoreApplication.translate("contacts5", u"Back to Contacts", None))
        self.NewContacts_4.setText(QCoreApplication.translate("contacts5", u"New Contact", None))
        self.SearcAccount_4.setInputMask("")
        self.SearcAccount_4.setText("")
        self.SearcAccount_4.setPlaceholderText(QCoreApplication.translate("contacts5", u"Search Account's Name", None))
        self.ContactsInformation_4.setText(QCoreApplication.translate("contacts5", u"Contact Infotmation", None))
        self.ContactOwner_4.setText(QCoreApplication.translate("contacts5", u"Contact Owner :", None))
        self.Picture_4.setText(QCoreApplication.translate("contacts5", u"Picture :", None))
        self.AdditionalInformation_5.setText(QCoreApplication.translate("contacts5", u"ADDITIONAL INFORMATION", None))
        self.AdditionalInformation_14.setText(QCoreApplication.translate("contacts5", u"ADDRESS INFORMATION", None))
        self.AdditionalInformation_13.setText(QCoreApplication.translate("contacts5", u"ADDRESS INFORMATION", None))
        self.AdditionalInformation_12.setText(QCoreApplication.translate("contacts5", u"DESCRIPTION INFORMATION", None))
        self.LastModifiedLabel_3.setText(QCoreApplication.translate("contacts5", u"Last Modified :", None))
        self.LastModified_Label_3.setText(QCoreApplication.translate("contacts5", u"--------------------", None))
        self.CreatedByLabel_3.setText(QCoreApplication.translate("contacts5", u"Created By :", None))
        self.CreatedBy_Label_3.setText(QCoreApplication.translate("contacts5", u"--------------------", None))
        self.ProfilePic_4.setText("")
        self.UploadPic_4.setInputMask("")
        self.UploadPic_4.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("contacts5", u"See File", None))
        self.ProfileName_4.setText(QCoreApplication.translate("contacts5", u"Jinita", None))
        self.MiddleNameLabel_8.setText(QCoreApplication.translate("contacts5", u"Email :", None))
        self.TitleLabel_4.setText(QCoreApplication.translate("contacts5", u"Title :", None))
        self.SuffixLabel_8.setText(QCoreApplication.translate("contacts5", u"Phone Number :", None))
        self.LeadStatusLabel_4.setText(QCoreApplication.translate("contacts5", u"Lead Status :", None))
        self.LeadStatus_4.setItemText(0, QCoreApplication.translate("contacts5", u"New Item", None))
        self.LeadStatus_4.setItemText(1, QCoreApplication.translate("contacts5", u"New Item", None))
        self.LeadStatus_4.setItemText(2, QCoreApplication.translate("contacts5", u"New Item", None))
        self.LeadStatus_4.setItemText(3, QCoreApplication.translate("contacts5", u"New Item", None))

        self.DateOfBirthLabel_4.setText(QCoreApplication.translate("contacts5", u"Date of Birth :", None))
        self.LastNameLabel_4.setText(QCoreApplication.translate("contacts5", u"Last Name :", None))
        self.FirstNameLabel_4.setText(QCoreApplication.translate("contacts5", u"First Name :", None))
        self.SalutationLabel_4.setText(QCoreApplication.translate("contacts5", u"Salutation :", None))
        self.NameLabel_4.setText(QCoreApplication.translate("contacts5", u"Name ", None))
        self.SuffixLabel_7.setText(QCoreApplication.translate("contacts5", u"Suffix :", None))
        self.Salutation_4.setItemText(0, QCoreApplication.translate("contacts5", u"New Item", None))
        self.Salutation_4.setItemText(1, QCoreApplication.translate("contacts5", u"New Item", None))
        self.Salutation_4.setItemText(2, QCoreApplication.translate("contacts5", u"New Item", None))
        self.Salutation_4.setItemText(3, QCoreApplication.translate("contacts5", u"New Item", None))

        self.MiddleNameLabel_7.setText(QCoreApplication.translate("contacts5", u"Middle Name :", None))
        self.OtherPhoneNumLabel_4.setText(QCoreApplication.translate("contacts5", u"Other Phone Number  :", None))
        self.GenderLabel_4.setText(QCoreApplication.translate("contacts5", u"Gender :", None))
        self.SecondaryEmailLabel_4.setText(QCoreApplication.translate("contacts5", u"Secondary Email :", None))
        self.MaritalStatusLabel_4.setText(QCoreApplication.translate("contacts5", u"Marital Status :", None))
        self.ReportsToLabel_4.setText(QCoreApplication.translate("contacts5", u" Reports To :", None))
        self.CompanyLabel_4.setText(QCoreApplication.translate("contacts5", u"Company :", None))
        self.FaxLabel_4.setText(QCoreApplication.translate("contacts5", u"Fax :", None))
        self.CityLabel_4.setText(QCoreApplication.translate("contacts5", u"City :", None))
        self.StreetLabel_4.setText(QCoreApplication.translate("contacts5", u"Street :", None))
        self.Street_4.setText("")
        self.AddressLabel_4.setText(QCoreApplication.translate("contacts5", u"Address :", None))
        self.CountryLabel_4.setText(QCoreApplication.translate("contacts5", u"Country  :", None))
        self.State_ProvinceLabel_4.setText(QCoreApplication.translate("contacts5", u"State/Province :", None))
        self.ZipPostalCodeLabel_4.setText(QCoreApplication.translate("contacts5", u"Zip/Postal Code :", None))
    # retranslateUi

