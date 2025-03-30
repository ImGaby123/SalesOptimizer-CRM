# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts4.ui'
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
        self.gridLayout_4 = QGridLayout(contacts4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tableWidget_tbl = QTableWidget(contacts4)
        if (self.tableWidget_tbl.columnCount() < 1):
            self.tableWidget_tbl.setColumnCount(1)
        font = QFont()
        font.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget_tbl.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget_tbl.setObjectName(u"tableWidget_tbl")
        self.tableWidget_tbl.setMaximumSize(QSize(200, 16777215))
        self.tableWidget_tbl.setStyleSheet(u"QTableWidget{\n"
"	border: 2px solid black;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_11.addWidget(self.tableWidget_tbl)

        self.timeline_7 = QFrame(contacts4)
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
        self.edit_btn = QPushButton(self.timeline_7)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Resources/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.edit_btn.setIcon(icon)

        self.horizontalLayout_45.addWidget(self.edit_btn)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_49)

        self.link_btn = QPushButton(self.timeline_7)
        self.link_btn.setObjectName(u"link_btn")
        self.link_btn.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Resources/link.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.link_btn.setIcon(icon1)

        self.horizontalLayout_45.addWidget(self.link_btn)

        self.attach_btn = QPushButton(self.timeline_7)
        self.attach_btn.setObjectName(u"attach_btn")
        self.attach_btn.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Resources/attach.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.attach_btn.setIcon(icon2)

        self.horizontalLayout_45.addWidget(self.attach_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout_45, 4, 1, 1, 1)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalSpacer_47 = QSpacerItem(220, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_47)

        self.timeline_txt = QLabel(self.timeline_7)
        self.timeline_txt.setObjectName(u"timeline_txt")
        self.timeline_txt.setStyleSheet(u"QLabel{\n"
"	font: 10pt \"Segoe UI\";\n"
"	border: none;\n"
"}")

        self.horizontalLayout_43.addWidget(self.timeline_txt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalSpacer_34 = QSpacerItem(120, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_34)

        self.pin_btn = QPushButton(self.timeline_7)
        self.pin_btn.setObjectName(u"pin_btn")
        self.pin_btn.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Resources/pin.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pin_btn.setIcon(icon3)
        self.pin_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_44.addWidget(self.pin_btn)

        self.bars_btn = QPushButton(self.timeline_7)
        self.bars_btn.setObjectName(u"bars_btn")
        self.bars_btn.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Resources/bars.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bars_btn.setIcon(icon4)
        self.bars_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_44.addWidget(self.bars_btn)

        self.menu_btn = QPushButton(self.timeline_7)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Resources/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_btn.setIcon(icon5)
        self.menu_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_44.addWidget(self.menu_btn)


        self.horizontalLayout_43.addLayout(self.horizontalLayout_44)


        self.gridLayout_3.addLayout(self.horizontalLayout_43, 1, 1, 1, 1)


        self.horizontalLayout_11.addWidget(self.timeline_7)

        self.contact_information_5 = QFrame(contacts4)
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
        self.contactinfo_txt = QLabel(self.contact_information_5)
        self.contactinfo_txt.setObjectName(u"contactinfo_txt")
        self.contactinfo_txt.setStyleSheet(u"QLabel{\n"
"	font: 10pt \"Segoe UI\";\n"
"	border: none;\n"
"}")

        self.gridLayout_2.addWidget(self.contactinfo_txt, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.contact_information_5)


        self.gridLayout.addLayout(self.horizontalLayout_11, 9, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 4, 0, 1, 1)

        self.frame = QFrame(contacts4)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame, 8, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_28 = QSpacerItem(130, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_28)

        self.prospecting_txt = QLabel(contacts4)
        self.prospecting_txt.setObjectName(u"prospecting_txt")
        self.prospecting_txt.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_22.addWidget(self.prospecting_txt)

        self.horizontalSpacer_29 = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_29)

        self.qualifications_txt = QLabel(contacts4)
        self.qualifications_txt.setObjectName(u"qualifications_txt")
        self.qualifications_txt.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_22.addWidget(self.qualifications_txt)

        self.horizontalSpacer_30 = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_30)

        self.contacting_txt = QLabel(contacts4)
        self.contacting_txt.setObjectName(u"contacting_txt")
        self.contacting_txt.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_22.addWidget(self.contacting_txt)

        self.horizontalSpacer_31 = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_31)

        self.nwtl_txt = QLabel(contacts4)
        self.nwtl_txt.setObjectName(u"nwtl_txt")
        self.nwtl_txt.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_22.addWidget(self.nwtl_txt)

        self.horizontalSpacer_32 = QSpacerItem(120, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_32)

        self.closed_won_txt = QLabel(contacts4)
        self.closed_won_txt.setObjectName(u"closed_won_txt")
        self.closed_won_txt.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_22.addWidget(self.closed_won_txt)

        self.horizontalSpacer_33 = QSpacerItem(80, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_33)

        self.closed_loss_txt = QLabel(contacts4)
        self.closed_loss_txt.setObjectName(u"closed_loss_txt")
        self.closed_loss_txt.setStyleSheet(u"QLabel{\n"
"	font: 7pt \"Segoe UI\";\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}")

        self.horizontalLayout_22.addWidget(self.closed_loss_txt)

        self.horizontalSpacer_50 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_50)


        self.gridLayout.addLayout(self.horizontalLayout_22, 6, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.backToContacts_btn = QPushButton(contacts4)
        self.backToContacts_btn.setObjectName(u"backToContacts_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.backToContacts_btn.sizePolicy().hasHeightForWidth())
        self.backToContacts_btn.setSizePolicy(sizePolicy1)
        self.backToContacts_btn.setMinimumSize(QSize(0, 40))
        self.backToContacts_btn.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: rgb(0, 0, 0); \n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Resources/leftarrow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backToContacts_btn.setIcon(icon6)
        self.backToContacts_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_12.addWidget(self.backToContacts_btn, 0, Qt.AlignmentFlag.AlignLeft)


        self.gridLayout.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)

        self.frame_2 = QFrame(contacts4)
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

        self.salespipeline_txt = QLabel(contacts4)
        self.salespipeline_txt.setObjectName(u"salespipeline_txt")
        self.salespipeline_txt.setStyleSheet(u"QLabel{\n"
"	font: 9pt \"Segoe UI\";\n"
"	border: none;\n"
"}")

        self.horizontalLayout_21.addWidget(self.salespipeline_txt)

        self.horizontalSpacer_26 = QSpacerItem(20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_26)

        self.sales_bar = QProgressBar(contacts4)
        self.sales_bar.setObjectName(u"sales_bar")
        self.sales_bar.setMinimumSize(QSize(0, 0))
        self.sales_bar.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.sales_bar.setStyleSheet(u"border-radius: 10px;")
        self.sales_bar.setValue(100)
        self.sales_bar.setTextVisible(False)
        self.sales_bar.setInvertedAppearance(False)

        self.horizontalLayout_21.addWidget(self.sales_bar)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_27)


        self.gridLayout.addLayout(self.horizontalLayout_21, 5, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(contacts4)

        QMetaObject.connectSlotsByName(contacts4)
    # setupUi

    def retranslateUi(self, contacts4):
        contacts4.setWindowTitle(QCoreApplication.translate("contacts4", u"Form", None))
        ___qtablewidgetitem = self.tableWidget_tbl.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("contacts4", u"Contacts", None));
        self.search_9.setPlaceholderText(QCoreApplication.translate("contacts4", u"Search", None))
        self.edit_btn.setText("")
        self.link_btn.setText("")
        self.attach_btn.setText("")
        self.timeline_txt.setText(QCoreApplication.translate("contacts4", u"Timeline", None))
        self.pin_btn.setText("")
        self.bars_btn.setText("")
        self.menu_btn.setText("")
        self.contactinfo_txt.setText(QCoreApplication.translate("contacts4", u"Contact Information", None))
        self.prospecting_txt.setText(QCoreApplication.translate("contacts4", u"Prospecting", None))
        self.qualifications_txt.setText(QCoreApplication.translate("contacts4", u"Qualifications", None))
        self.contacting_txt.setText(QCoreApplication.translate("contacts4", u"Contacting", None))
        self.nwtl_txt.setText(QCoreApplication.translate("contacts4", u"Negotiating with the Lead", None))
        self.closed_won_txt.setText(QCoreApplication.translate("contacts4", u"Closed Won", None))
        self.closed_loss_txt.setText(QCoreApplication.translate("contacts4", u"Closed Loss", None))
        self.backToContacts_btn.setText(QCoreApplication.translate("contacts4", u"Back To Contacts", None))
        self.salespipeline_txt.setText(QCoreApplication.translate("contacts4", u"Sales Pipeline", None))
#if QT_CONFIG(tooltip)
        self.sales_bar.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.sales_bar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.sales_bar.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.sales_bar.setFormat("")
    # retranslateUi

