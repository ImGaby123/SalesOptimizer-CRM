# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts1.ui'
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
    QHeaderView, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)
import views.py.icons_rc

class Ui_contacts1(object):
    def setupUi(self, contacts1):
        if not contacts1.objectName():
            contacts1.setObjectName(u"contacts1")
        contacts1.resize(1201, 680)
        self.gridLayout_4 = QGridLayout(contacts1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.back_to_contacts_2 = QPushButton(contacts1)
        self.back_to_contacts_2.setObjectName(u"back_to_contacts_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_to_contacts_2.sizePolicy().hasHeightForWidth())
        self.back_to_contacts_2.setSizePolicy(sizePolicy)
        self.back_to_contacts_2.setMinimumSize(QSize(0, 20))
        self.back_to_contacts_2.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(11)
        self.back_to_contacts_2.setFont(font)
        self.back_to_contacts_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")

        self.horizontalLayout_24.addWidget(self.back_to_contacts_2)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_17)


        self.gridLayout_3.addLayout(self.horizontalLayout_24, 0, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.logo_user_2 = QLabel(contacts1)
        self.logo_user_2.setObjectName(u"logo_user_2")
        self.logo_user_2.setMinimumSize(QSize(30, 0))
        self.logo_user_2.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.logo_user_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.logo_user_2)

        self.company_ni_gab_2 = QLabel(contacts1)
        self.company_ni_gab_2.setObjectName(u"company_ni_gab_2")
        self.company_ni_gab_2.setFont(font)
        self.company_ni_gab_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_21.addWidget(self.company_ni_gab_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_8)


        self.gridLayout_3.addLayout(self.horizontalLayout_21, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.sales_pipeline_4 = QLabel(contacts1)
        self.sales_pipeline_4.setObjectName(u"sales_pipeline_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sales_pipeline_4.sizePolicy().hasHeightForWidth())
        self.sales_pipeline_4.setSizePolicy(sizePolicy1)
        self.sales_pipeline_4.setMinimumSize(QSize(100, 0))
        self.sales_pipeline_4.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.sales_pipeline_4.setFont(font1)
        self.sales_pipeline_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;\n"
"")
        self.sales_pipeline_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sales_pipeline_4.setWordWrap(False)

        self.horizontalLayout.addWidget(self.sales_pipeline_4)

        self.progressBar_4 = QProgressBar(contacts1)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setStyleSheet(u"")
        self.progressBar_4.setValue(24)

        self.horizontalLayout.addWidget(self.progressBar_4)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(100, 0, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.prospecting_4 = QLabel(contacts1)
        self.prospecting_4.setObjectName(u"prospecting_4")
        self.prospecting_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.prospecting_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.qualifications_4 = QLabel(contacts1)
        self.qualifications_4.setObjectName(u"qualifications_4")
        self.qualifications_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.qualifications_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.contacting_4 = QLabel(contacts1)
        self.contacting_4.setObjectName(u"contacting_4")
        self.contacting_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.contacting_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.building_relationship_4 = QLabel(contacts1)
        self.building_relationship_4.setObjectName(u"building_relationship_4")
        self.building_relationship_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.building_relationship_4)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.negotiating_2 = QLabel(contacts1)
        self.negotiating_2.setObjectName(u"negotiating_2")
        self.negotiating_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.negotiating_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.closing_4 = QLabel(contacts1)
        self.closing_4.setObjectName(u"closing_4")
        self.closing_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.closing_4)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.closed_won_4 = QLabel(contacts1)
        self.closed_won_4.setObjectName(u"closed_won_4")
        self.closed_won_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.closed_won_4)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.closed_loss_4 = QLabel(contacts1)
        self.closed_loss_4.setObjectName(u"closed_loss_4")
        self.closed_loss_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.closed_loss_4)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.tableWidget_4 = QTableWidget(contacts1)
        if (self.tableWidget_4.columnCount() < 1):
            self.tableWidget_4.setColumnCount(1)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font2 = QFont()
        font2.setBold(False)
        font2.setKerning(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setMaximumSize(QSize(200, 16777215))
        self.tableWidget_4.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 10px;")

        self.horizontalLayout_25.addWidget(self.tableWidget_4)

        self.frame_6 = QFrame(contacts1)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 10px;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.contact_info_2 = QLabel(self.frame_6)
        self.contact_info_2.setObjectName(u"contact_info_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.contact_info_2.sizePolicy().hasHeightForWidth())
        self.contact_info_2.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(16)
        self.contact_info_2.setFont(font3)
        self.contact_info_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")
        self.contact_info_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.contact_info_2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.contact_info_2.raise_()

        self.horizontalLayout_25.addWidget(self.frame_6)

        self.frame_7 = QFrame(contacts1)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setMaximumSize(QSize(380, 16777215))
        self.frame_7.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 10px;")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sales_funnel_label_2 = QLabel(self.frame_7)
        self.sales_funnel_label_2.setObjectName(u"sales_funnel_label_2")
        sizePolicy3.setHeightForWidth(self.sales_funnel_label_2.sizePolicy().hasHeightForWidth())
        self.sales_funnel_label_2.setSizePolicy(sizePolicy3)
        self.sales_funnel_label_2.setFont(font3)
        self.sales_funnel_label_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: none;")
        self.sales_funnel_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.sales_funnel_label_2, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.sales_funnel_label_2.raise_()

        self.horizontalLayout_25.addWidget(self.frame_7)


        self.gridLayout_3.addLayout(self.horizontalLayout_25, 4, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.retranslateUi(contacts1)

        QMetaObject.connectSlotsByName(contacts1)
    # setupUi

    def retranslateUi(self, contacts1):
        contacts1.setWindowTitle(QCoreApplication.translate("contacts1", u"Form", None))
        self.back_to_contacts_2.setText(QCoreApplication.translate("contacts1", u"< Back to Contacts", None))
        self.logo_user_2.setText(QCoreApplication.translate("contacts1", u"G", None))
        self.company_ni_gab_2.setText(QCoreApplication.translate("contacts1", u"Company ni Gab", None))
        self.sales_pipeline_4.setText(QCoreApplication.translate("contacts1", u"Sales Pipeline", None))
        self.prospecting_4.setText(QCoreApplication.translate("contacts1", u"Prospecting", None))
        self.qualifications_4.setText(QCoreApplication.translate("contacts1", u"Qualifications", None))
        self.contacting_4.setText(QCoreApplication.translate("contacts1", u"Contacting", None))
        self.building_relationship_4.setText(QCoreApplication.translate("contacts1", u"Building Relationship", None))
        self.negotiating_2.setText(QCoreApplication.translate("contacts1", u"Negotiating with the lead", None))
        self.closing_4.setText(QCoreApplication.translate("contacts1", u"Closing", None))
        self.closed_won_4.setText(QCoreApplication.translate("contacts1", u"Closed Won", None))
        self.closed_loss_4.setText(QCoreApplication.translate("contacts1", u"Closed Loss", None))
        ___qtablewidgetitem = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("contacts1", u"Contacts", None));
        self.contact_info_2.setText(QCoreApplication.translate("contacts1", u"Contact Information", None))
        self.sales_funnel_label_2.setText(QCoreApplication.translate("contacts1", u"Sales Funnel", None))
    # retranslateUi

