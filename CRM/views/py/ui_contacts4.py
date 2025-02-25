# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts4.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)
import views.py.icons_rc

class Ui_contacts4(object):
    def setupUi(self, contacts4):
        if not contacts4.objectName():
            contacts4.setObjectName(u"contacts4")
        contacts4.resize(1201, 680)
        self.gridLayoutWidget = QWidget(contacts4)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 1181, 661))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tableWidget_6 = QTableWidget(self.gridLayoutWidget)
        if (self.tableWidget_6.columnCount() < 1):
            self.tableWidget_6.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setMaximumSize(QSize(200, 16777215))
        self.tableWidget_6.setStyleSheet(u"QTableWidget{\n"
"	border: 2px solid black;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_11.addWidget(self.tableWidget_6)

        self.timeline_7 = QFrame(self.gridLayoutWidget)
        self.timeline_7.setObjectName(u"timeline_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeline_7.sizePolicy().hasHeightForWidth())
        self.timeline_7.setSizePolicy(sizePolicy)
        self.timeline_7.setStyleSheet(u"QFrame {\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}")
        self.timeline_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.timeline_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.timeline_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_5 = QSpacerItem(20, 400, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 3, 1, 1, 1)

        self.search_9 = QLineEdit(self.timeline_7)
        self.search_9.setObjectName(u"search_9")
        self.search_9.setMinimumSize(QSize(0, 45))
        self.search_9.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.search_9, 2, 1, 1, 1)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.edit_7 = QPushButton(self.timeline_7)
        self.edit_7.setObjectName(u"edit_7")
        self.edit_7.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Resources/black_edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/Resources/white_edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.edit_7.setIcon(icon)

        self.horizontalLayout_45.addWidget(self.edit_7)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_49)

        self.link_7 = QPushButton(self.timeline_7)
        self.link_7.setObjectName(u"link_7")
        self.link_7.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Resources/black_link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/Resources/white_link.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.link_7.setIcon(icon1)

        self.horizontalLayout_45.addWidget(self.link_7)

        self.attachment_7 = QPushButton(self.timeline_7)
        self.attachment_7.setObjectName(u"attachment_7")
        self.attachment_7.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Resources/black_attach.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/Resources/white_attach.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.attachment_7.setIcon(icon2)

        self.horizontalLayout_45.addWidget(self.attachment_7)


        self.gridLayout_3.addLayout(self.horizontalLayout_45, 4, 1, 1, 1)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalSpacer_47 = QSpacerItem(220, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_47)

        self.Timeline_7 = QLabel(self.timeline_7)
        self.Timeline_7.setObjectName(u"Timeline_7")
        self.Timeline_7.setStyleSheet(u"QLabel{\n"
"	font: 10pt \"Segoe UI\";\n"
"	border: none;\n"
"}")

        self.horizontalLayout_43.addWidget(self.Timeline_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalSpacer_34 = QSpacerItem(120, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_34)

        self.pin_7 = QPushButton(self.timeline_7)
        self.pin_7.setObjectName(u"pin_7")
        self.pin_7.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Resources/black_pin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Resources/white_pin.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pin_7.setIcon(icon3)
        self.pin_7.setIconSize(QSize(30, 30))

        self.horizontalLayout_44.addWidget(self.pin_7)

        self.pushButton_14 = QPushButton(self.timeline_7)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Resources/black_bars.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/Resources/white_bars.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_14.setIcon(icon4)
        self.pushButton_14.setIconSize(QSize(30, 30))

        self.horizontalLayout_44.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.timeline_7)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Resources/black_menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/Resources/white_menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_15.setIcon(icon5)
        self.pushButton_15.setIconSize(QSize(30, 30))

        self.horizontalLayout_44.addWidget(self.pushButton_15)


        self.horizontalLayout_43.addLayout(self.horizontalLayout_44)


        self.gridLayout_3.addLayout(self.horizontalLayout_43, 1, 1, 1, 1)


        self.horizontalLayout_11.addWidget(self.timeline_7)

        self.contact_information_5 = QFrame(self.gridLayoutWidget)
        self.contact_information_5.setObjectName(u"contact_information_5")
        sizePolicy.setHeightForWidth(self.contact_information_5.sizePolicy().hasHeightForWidth())
        self.contact_information_5.setSizePolicy(sizePolicy)
        self.contact_information_5.setMaximumSize(QSize(380, 16777215))
        self.contact_information_5.setStyleSheet(u"QFrame {\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}")
        self.contact_information_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.contact_information_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.contact_information_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ContactInformation_5 = QLabel(self.contact_information_5)
        self.ContactInformation_5.setObjectName(u"ContactInformation_5")
        self.ContactInformation_5.setStyleSheet(u"QLabel{\n"
"	font: 10pt \"Segoe UI\";\n"
"	border: none;\n"
"}")

        self.gridLayout_2.addWidget(self.ContactInformation_5, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.contact_information_5)


        self.gridLayout.addLayout(self.horizontalLayout_11, 9, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 4, 0, 1, 1)

        self.frame = QFrame(self.gridLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame, 8, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_28 = QSpacerItem(130, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_28)

        self.prospecting_4 = QLabel(self.gridLayoutWidget)
        self.prospecting_4.setObjectName(u"prospecting_4")
        self.prospecting_4.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_22.addWidget(self.prospecting_4)

        self.horizontalSpacer_29 = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_29)

        self.qualifications_4 = QLabel(self.gridLayoutWidget)
        self.qualifications_4.setObjectName(u"qualifications_4")
        self.qualifications_4.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_22.addWidget(self.qualifications_4)

        self.horizontalSpacer_30 = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_30)

        self.contacting_4 = QLabel(self.gridLayoutWidget)
        self.contacting_4.setObjectName(u"contacting_4")
        self.contacting_4.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_22.addWidget(self.contacting_4)

        self.horizontalSpacer_31 = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_31)

        self.negotiating_with_the_lead_4 = QLabel(self.gridLayoutWidget)
        self.negotiating_with_the_lead_4.setObjectName(u"negotiating_with_the_lead_4")
        self.negotiating_with_the_lead_4.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_22.addWidget(self.negotiating_with_the_lead_4)

        self.horizontalSpacer_32 = QSpacerItem(120, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_32)

        self.closed_won_4 = QLabel(self.gridLayoutWidget)
        self.closed_won_4.setObjectName(u"closed_won_4")
        self.closed_won_4.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_22.addWidget(self.closed_won_4)

        self.horizontalSpacer_33 = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_33)

        self.closed_loss_4 = QLabel(self.gridLayoutWidget)
        self.closed_loss_4.setObjectName(u"closed_loss_4")
        self.closed_loss_4.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_22.addWidget(self.closed_loss_4)

        self.horizontalSpacer_50 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_50)


        self.gridLayout.addLayout(self.horizontalLayout_22, 6, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.backToContacts_2 = QPushButton(self.gridLayoutWidget)
        self.backToContacts_2.setObjectName(u"backToContacts_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.backToContacts_2.sizePolicy().hasHeightForWidth())
        self.backToContacts_2.setSizePolicy(sizePolicy1)
        self.backToContacts_2.setMinimumSize(QSize(0, 40))
        self.backToContacts_2.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: rgb(0, 0, 0); \n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Resources/black_left-arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/Resources/white_left-arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.backToContacts_2.setIcon(icon6)
        self.backToContacts_2.setIconSize(QSize(15, 15))

        self.horizontalLayout_12.addWidget(self.backToContacts_2, 0, Qt.AlignmentFlag.AlignLeft)


        self.gridLayout.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.gridLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 20))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_2)

        self.SalesPipeline_4 = QLabel(self.gridLayoutWidget)
        self.SalesPipeline_4.setObjectName(u"SalesPipeline_4")
        self.SalesPipeline_4.setStyleSheet(u"QLabel{\n"
"	font: 9pt \"Segoe UI\";\n"
"	border: none;\n"
"}")

        self.horizontalLayout_21.addWidget(self.SalesPipeline_4)

        self.horizontalSpacer_26 = QSpacerItem(20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_26)

        self.progressBar_4 = QProgressBar(self.gridLayoutWidget)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setMinimumSize(QSize(0, 0))
        self.progressBar_4.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.progressBar_4.setStyleSheet(u"border-radius: 10px;")
        self.progressBar_4.setValue(100)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setInvertedAppearance(False)

        self.horizontalLayout_21.addWidget(self.progressBar_4)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_27)


        self.gridLayout.addLayout(self.horizontalLayout_21, 5, 0, 1, 1)


        self.retranslateUi(contacts4)

        QMetaObject.connectSlotsByName(contacts4)
    # setupUi

    def retranslateUi(self, contacts4):
        contacts4.setWindowTitle(QCoreApplication.translate("contacts4", u"Form", None))
        ___qtablewidgetitem = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("contacts4", u"Contacts", None));
        self.search_9.setPlaceholderText(QCoreApplication.translate("contacts4", u"Search", None))
        self.edit_7.setText("")
        self.link_7.setText("")
        self.attachment_7.setText("")
        self.Timeline_7.setText(QCoreApplication.translate("contacts4", u"Timeline", None))
        self.pin_7.setText("")
        self.pushButton_14.setText("")
        self.pushButton_15.setText("")
        self.ContactInformation_5.setText(QCoreApplication.translate("contacts4", u"Contact Information", None))
        self.prospecting_4.setText(QCoreApplication.translate("contacts4", u"Prospecting", None))
        self.qualifications_4.setText(QCoreApplication.translate("contacts4", u"Qualifications", None))
        self.contacting_4.setText(QCoreApplication.translate("contacts4", u"Contacting", None))
        self.negotiating_with_the_lead_4.setText(QCoreApplication.translate("contacts4", u"Negotiating with the Lead", None))
        self.closed_won_4.setText(QCoreApplication.translate("contacts4", u"Closed Won", None))
        self.closed_loss_4.setText(QCoreApplication.translate("contacts4", u"Closed Loss", None))
        self.backToContacts_2.setText(QCoreApplication.translate("contacts4", u"Back To Contacts", None))
        self.SalesPipeline_4.setText(QCoreApplication.translate("contacts4", u"Sales Pipeline", None))
#if QT_CONFIG(tooltip)
        self.progressBar_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.progressBar_4.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.progressBar_4.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.progressBar_4.setFormat("")
    # retranslateUi

