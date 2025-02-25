# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts3.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_contacts3(object):
    def setupUi(self, contacts3):
        if not contacts3.objectName():
            contacts3.setObjectName(u"contacts3")
        contacts3.resize(1201, 680)
        self.gridLayout_3 = QGridLayout(contacts3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_tbl = QTableWidget(contacts3)
        if (self.tableWidget_tbl.columnCount() < 4):
            self.tableWidget_tbl.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_tbl.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_tbl.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_tbl.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_tbl.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_tbl.setObjectName(u"tableWidget_tbl")
        self.tableWidget_tbl.setStyleSheet(u"QTableWidget{\n"
"	border: 2px solid black\n"
"}\n"
"")

        self.gridLayout.addWidget(self.tableWidget_tbl, 7, 0, 1, 1)

        self.verticalSpacer_41 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_41, 1, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.search_line = QLineEdit(contacts3)
        self.search_line.setObjectName(u"search_line")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_line.sizePolicy().hasHeightForWidth())
        self.search_line.setSizePolicy(sizePolicy)
        self.search_line.setMinimumSize(QSize(0, 40))
        self.search_line.setMaximumSize(QSize(400, 16777215))
        self.search_line.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.search_line.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.search_line.setClearButtonEnabled(False)

        self.horizontalLayout_22.addWidget(self.search_line)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.add_btn = QPushButton(contacts3)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Resources/black_plus .png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/Resources/white_plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.add_btn.setIcon(icon)
        self.add_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.add_btn)

        self.refresh_btn = QPushButton(contacts3)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	border: transparent;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Resources/black_refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/Resources/white_refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.refresh_btn.setIcon(icon1)
        self.refresh_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.refresh_btn)

        self.delete_btn = QPushButton(contacts3)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Resources/black_delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/Resources/white_delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.delete_btn.setIcon(icon2)
        self.delete_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.delete_btn)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_6)


        self.gridLayout.addLayout(self.horizontalLayout_22, 2, 0, 1, 1)

        self.contacts_txt = QLabel(contacts3)
        self.contacts_txt.setObjectName(u"contacts_txt")
        sizePolicy.setHeightForWidth(self.contacts_txt.sizePolicy().hasHeightForWidth())
        self.contacts_txt.setSizePolicy(sizePolicy)
        self.contacts_txt.setMinimumSize(QSize(0, 0))
        self.contacts_txt.setStyleSheet(u"font: 18pt \"Segoe UI\";\n"
"background: transparent;")

        self.gridLayout.addWidget(self.contacts_txt, 0, 0, 1, 1)

        self.verticalSpacer_43 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_43, 5, 0, 1, 1)

        self.verticalSpacer_42 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_42, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.allContacts_combo = QComboBox(contacts3)
        self.allContacts_combo.setObjectName(u"allContacts_combo")
        sizePolicy.setHeightForWidth(self.allContacts_combo.sizePolicy().hasHeightForWidth())
        self.allContacts_combo.setSizePolicy(sizePolicy)
        self.allContacts_combo.setMinimumSize(QSize(0, 30))
        self.allContacts_combo.setMaximumSize(QSize(200, 16777215))
        self.allContacts_combo.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid black;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.allContacts_combo.setEditable(False)

        self.gridLayout_2.addWidget(self.allContacts_combo, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 4, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(contacts3)

        QMetaObject.connectSlotsByName(contacts3)
    # setupUi

    def retranslateUi(self, contacts3):
        contacts3.setWindowTitle(QCoreApplication.translate("contacts3", u"Form", None))
        ___qtablewidgetitem = self.tableWidget_tbl.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("contacts3", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget_tbl.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("contacts3", u"Email", None));
        ___qtablewidgetitem2 = self.tableWidget_tbl.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("contacts3", u"Phone Number", None));
        ___qtablewidgetitem3 = self.tableWidget_tbl.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("contacts3", u"Company", None));
        self.search_line.setPlaceholderText(QCoreApplication.translate("contacts3", u"Search", None))
        self.add_btn.setText("")
        self.refresh_btn.setText("")
        self.delete_btn.setText("")
        self.contacts_txt.setText(QCoreApplication.translate("contacts3", u"Contacts", None))
        self.allContacts_combo.setPlaceholderText(QCoreApplication.translate("contacts3", u"All Contacts", None))
    # retranslateUi

