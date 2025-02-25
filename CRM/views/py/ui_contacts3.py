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
import views.py.icons_rc

class Ui_contacts3(object):
    def setupUi(self, contacts3):
        if not contacts3.objectName():
            contacts3.setObjectName(u"contacts3")
        contacts3.resize(1201, 680)
        self.gridLayoutWidget = QWidget(contacts3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 1201, 681))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_3 = QTableWidget(self.gridLayoutWidget)
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

        self.gridLayout.addWidget(self.tableWidget_3, 7, 0, 1, 1)

        self.verticalSpacer_41 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_41, 1, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.search_3 = QLineEdit(self.gridLayoutWidget)
        self.search_3.setObjectName(u"search_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_3.sizePolicy().hasHeightForWidth())
        self.search_3.setSizePolicy(sizePolicy)
        self.search_3.setMinimumSize(QSize(0, 40))
        self.search_3.setMaximumSize(QSize(400, 16777215))
        self.search_3.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.search_3.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.search_3.setClearButtonEnabled(False)

        self.horizontalLayout_22.addWidget(self.search_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.add_2 = QPushButton(self.gridLayoutWidget)
        self.add_2.setObjectName(u"add_2")
        self.add_2.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Resources/black_plus .png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/Resources/white_plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.add_2.setIcon(icon)
        self.add_2.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.add_2)

        self.refresh_2 = QPushButton(self.gridLayoutWidget)
        self.refresh_2.setObjectName(u"refresh_2")
        self.refresh_2.setStyleSheet(u"QPushButton {\n"
"	background: transparent;\n"
"	border: transparent;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Resources/black_refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/Resources/white_refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.refresh_2.setIcon(icon1)
        self.refresh_2.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.refresh_2)

        self.delete_3 = QPushButton(self.gridLayoutWidget)
        self.delete_3.setObjectName(u"delete_3")
        self.delete_3.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Resources/black_delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/Resources/white_delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.delete_3.setIcon(icon2)
        self.delete_3.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.delete_3)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_6)


        self.gridLayout.addLayout(self.horizontalLayout_22, 2, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(0, 0))
        self.label_8.setStyleSheet(u"font: 18pt \"Segoe UI\";\n"
"background: transparent;")

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.verticalSpacer_43 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_43, 5, 0, 1, 1)

        self.verticalSpacer_42 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_42, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.allContacts_2 = QComboBox(self.gridLayoutWidget)
        self.allContacts_2.setObjectName(u"allContacts_2")
        sizePolicy.setHeightForWidth(self.allContacts_2.sizePolicy().hasHeightForWidth())
        self.allContacts_2.setSizePolicy(sizePolicy)
        self.allContacts_2.setMinimumSize(QSize(0, 30))
        self.allContacts_2.setMaximumSize(QSize(200, 16777215))
        self.allContacts_2.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid black;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.allContacts_2.setEditable(False)

        self.gridLayout_2.addWidget(self.allContacts_2, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 4, 0, 1, 1)


        self.retranslateUi(contacts3)

        QMetaObject.connectSlotsByName(contacts3)
    # setupUi

    def retranslateUi(self, contacts3):
        contacts3.setWindowTitle(QCoreApplication.translate("contacts3", u"Form", None))
        ___qtablewidgetitem = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("contacts3", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("contacts3", u"Email", None));
        ___qtablewidgetitem2 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("contacts3", u"Phone Number", None));
        ___qtablewidgetitem3 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("contacts3", u"Company", None));
        self.search_3.setPlaceholderText(QCoreApplication.translate("contacts3", u"Search", None))
        self.add_2.setText("")
        self.refresh_2.setText("")
        self.delete_3.setText("")
        self.label_8.setText(QCoreApplication.translate("contacts3", u"Contacts", None))
        self.allContacts_2.setPlaceholderText(QCoreApplication.translate("contacts3", u"All Contacts", None))
    # retranslateUi

