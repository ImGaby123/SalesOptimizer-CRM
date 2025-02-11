# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'awal.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QWidget)
import icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1201, 682)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1201, 681))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.contacts_1 = QWidget()
        self.contacts_1.setObjectName(u"contacts_1")
        self.label = QLabel(self.contacts_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(530, 50, 101, 20))
        self.stackedWidget.addWidget(self.contacts_1)
        self.contacts_2 = QWidget()
        self.contacts_2.setObjectName(u"contacts_2")
        self.tableWidget = QTableWidget(self.contacts_2)
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
        self.allContacts = QComboBox(self.contacts_2)
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
        self.label_2 = QLabel(self.contacts_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 121, 41))
        self.label_2.setStyleSheet(u"font: 18pt \"Segoe UI\";\n"
"background: transparent;")
        self.search = QLineEdit(self.contacts_2)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(20, 80, 391, 51))
        self.search.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.search.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.search.setClearButtonEnabled(False)
        self.horizontalLayoutWidget = QWidget(self.contacts_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(1030, 90, 151, 42))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.add = QPushButton(self.horizontalLayoutWidget)
        self.add.setObjectName(u"add")
        self.add.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/new/newPrefix/Resources/plus (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add.setIcon(icon)
        self.add.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.add)

        self.refresh = QPushButton(self.horizontalLayoutWidget)
        self.refresh.setObjectName(u"refresh")
        self.refresh.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	border: transparent;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/new/newPrefix/Resources/refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh.setIcon(icon1)
        self.refresh.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.refresh)

        self.delete_2 = QPushButton(self.horizontalLayoutWidget)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/new/newPrefix/Resources/trash-circle-svgrepo-com.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_2.setIcon(icon2)
        self.delete_2.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.delete_2)

        self.horizontalLayoutWidget_3 = QWidget(self.contacts_2)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(1073, 240, 91, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.history = QPushButton(self.horizontalLayoutWidget_3)
        self.history.setObjectName(u"history")
        self.history.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/new/newPrefix/Resources/clock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.history.setIcon(icon3)
        self.history.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.history)

        self.mail = QPushButton(self.horizontalLayoutWidget_3)
        self.mail.setObjectName(u"mail")
        self.mail.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	border: transparent;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/new/newPrefix/Resources/email.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mail.setIcon(icon4)
        self.mail.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.mail)

        self.more = QPushButton(self.horizontalLayoutWidget_3)
        self.more.setObjectName(u"more")
        self.more.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/new/newPrefix/Resources/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.more.setIcon(icon5)
        self.more.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.more)

        self.stackedWidget.addWidget(self.contacts_2)
        self.contacts_3 = QWidget()
        self.contacts_3.setObjectName(u"contacts_3")
        self.backToContacts = QPushButton(self.contacts_3)
        self.backToContacts.setObjectName(u"backToContacts")
        self.backToContacts.setGeometry(QRect(10, 10, 141, 41))
        self.backToContacts.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: rgb(0, 0, 0); \n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/new/newPrefix/Resources/left-arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backToContacts.setIcon(icon6)
        self.backToContacts.setIconSize(QSize(15, 15))
        self.sales_pipeline = QFrame(self.contacts_3)
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
        self.timeline = QFrame(self.contacts_3)
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
        self.horizontalLayoutWidget_2 = QWidget(self.timeline)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(440, 10, 124, 32))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pin = QPushButton(self.horizontalLayoutWidget_2)
        self.pin.setObjectName(u"pin")
        self.pin.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/new/newPrefix/Resources/pin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pin.setIcon(icon7)
        self.pin.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pin)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/new/newPrefix/Resources/bars.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon8)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.label_9 = QLabel(self.timeline)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 410, 541, 21))
        self.label_9.setStyleSheet(u"QLabel{\n"
"	font: 700 10pt \"Segoe UI\";\n"
"	border: none;\n"
"}")
        self.horizontalLayoutWidget_4 = QWidget(self.timeline)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(14, 390, 551, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.edit = QPushButton(self.horizontalLayoutWidget_4)
        self.edit.setObjectName(u"edit")
        self.edit.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/new/newPrefix/Resources/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.edit.setIcon(icon9)

        self.horizontalLayout_4.addWidget(self.edit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.link = QPushButton(self.horizontalLayoutWidget_4)
        self.link.setObjectName(u"link")
        self.link.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/new/newPrefix/Resources/link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.link.setIcon(icon10)

        self.horizontalLayout_4.addWidget(self.link)

        self.attachment = QPushButton(self.horizontalLayoutWidget_4)
        self.attachment.setObjectName(u"attachment")
        self.attachment.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/new/newPrefix/Resources/attach-document.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.attachment.setIcon(icon11)

        self.horizontalLayout_4.addWidget(self.attachment)

        self.contact_information = QFrame(self.contacts_3)
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
        self.tableWidget_2 = QTableWidget(self.contacts_3)
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
        self.stackedWidget.addWidget(self.contacts_3)
        self.contacts_4 = QWidget()
        self.contacts_4.setObjectName(u"contacts_4")
        self.label_4 = QLabel(self.contacts_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(540, 60, 101, 20))
        self.stackedWidget.addWidget(self.contacts_4)
        self.contacts_5 = QWidget()
        self.contacts_5.setObjectName(u"contacts_5")
        self.label_5 = QLabel(self.contacts_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(540, 60, 101, 20))
        self.stackedWidget.addWidget(self.contacts_5)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Arcas Page 1", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Email", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Phone Number", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Company", None));
        self.allContacts.setPlaceholderText(QCoreApplication.translate("Form", u"All Contacts", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Contacts", None))
        self.search.setPlaceholderText(QCoreApplication.translate("Form", u"Search", None))
        self.add.setText("")
        self.refresh.setText("")
        self.delete_2.setText("")
        self.history.setText("")
        self.mail.setText("")
        self.more.setText("")
        self.backToContacts.setText(QCoreApplication.translate("Form", u"Back To Contacts", None))
        self.SalesPipeline.setText(QCoreApplication.translate("Form", u"Sales Pipeline", None))
        self.progressBar.setFormat("")
        self.prospecting.setText(QCoreApplication.translate("Form", u"Prospecting", None))
        self.qualifications.setText(QCoreApplication.translate("Form", u"Qualifications", None))
        self.contacting.setText(QCoreApplication.translate("Form", u"Contacting", None))
        self.building_relationship.setText(QCoreApplication.translate("Form", u"Building Relationship", None))
        self.negotiating_with_the_lead.setText(QCoreApplication.translate("Form", u"Negotiating with the Lead", None))
        self.closed_won.setText(QCoreApplication.translate("Form", u"Closed Won", None))
        self.closing.setText(QCoreApplication.translate("Form", u"Closing", None))
        self.closed_loss.setText(QCoreApplication.translate("Form", u"Closed Loss", None))
        self.Timeline.setText(QCoreApplication.translate("Form", u"Timeline", None))
        self.search_2.setPlaceholderText(QCoreApplication.translate("Form", u"Search", None))
        self.pin.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"______________________________________________________________________________________________________________", None))
        self.edit.setText("")
        self.link.setText("")
        self.attachment.setText("")
        self.ContactInformation.setText(QCoreApplication.translate("Form", u"Contact Information", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Contacts", None));
        self.label_4.setText(QCoreApplication.translate("Form", u"Abuan Page 4", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Abuan Page 5", None))
    # retranslateUi

