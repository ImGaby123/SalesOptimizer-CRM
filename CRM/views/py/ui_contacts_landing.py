# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts_landing.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)
import views.py.icons_rc

class Ui_contacts_landing(object):
    def setupUi(self, contacts_landing):
        if not contacts_landing.objectName():
            contacts_landing.setObjectName(u"contacts_landing")
        contacts_landing.resize(1201, 680)
        self.gridLayout_3 = QGridLayout(contacts_landing)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.sort_combo = QComboBox(contacts_landing)
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.setObjectName(u"sort_combo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sort_combo.sizePolicy().hasHeightForWidth())
        self.sort_combo.setSizePolicy(sizePolicy)
        self.sort_combo.setMinimumSize(QSize(0, 30))
        self.sort_combo.setMaximumSize(QSize(200, 16777215))
        self.sort_combo.setStyleSheet(u"")
        self.sort_combo.setEditable(False)

        self.horizontalLayout_22.addWidget(self.sort_combo)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_2)

        self.selecteditems_lbl = QLabel(contacts_landing)
        self.selecteditems_lbl.setObjectName(u"selecteditems_lbl")
        self.selecteditems_lbl.setEnabled(True)
        self.selecteditems_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_22.addWidget(self.selecteditems_lbl)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer)

        self.search_line = QLineEdit(contacts_landing)
        self.search_line.setObjectName(u"search_line")
        sizePolicy.setHeightForWidth(self.search_line.sizePolicy().hasHeightForWidth())
        self.search_line.setSizePolicy(sizePolicy)
        self.search_line.setMinimumSize(QSize(0, 30))
        self.search_line.setMaximumSize(QSize(290, 16777215))
        self.search_line.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid black;\n"
"}")
        self.search_line.setFrame(True)
        self.search_line.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.search_line.setClearButtonEnabled(False)

        self.horizontalLayout_22.addWidget(self.search_line)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.add_btn = QPushButton(contacts_landing)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_btn.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgba(100, 100, 100, 0.2); /* Light gray with transparency */\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Resources/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_btn.setIcon(icon)
        self.add_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.add_btn)

        self.delete_btn = QPushButton(contacts_landing)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_btn.setStyleSheet(u"QPushButton{\n"
"	background: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgba(100, 100, 100, 0.2); /* Light gray with transparency */\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Resources/delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_btn.setIcon(icon1)
        self.delete_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.delete_btn)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_6)


        self.gridLayout.addLayout(self.horizontalLayout_22, 2, 0, 1, 1)

        self.contacts_tbl = QTableWidget(contacts_landing)
        self.contacts_tbl.setObjectName(u"contacts_tbl")
        self.contacts_tbl.setMouseTracking(False)
        self.contacts_tbl.setStyleSheet(u"QTableWidget {\n"
"border: 1px solid black;\n"
"}\n"
"")
        self.contacts_tbl.horizontalHeader().setCascadingSectionResizes(False)
        self.contacts_tbl.horizontalHeader().setDefaultSectionSize(200)
        self.contacts_tbl.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.contacts_tbl, 7, 0, 1, 1)

        self.verticalSpacer_43 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_43, 4, 0, 1, 1)

        self.contacts_txt = QLabel(contacts_landing)
        self.contacts_txt.setObjectName(u"contacts_txt")
        sizePolicy.setHeightForWidth(self.contacts_txt.sizePolicy().hasHeightForWidth())
        self.contacts_txt.setSizePolicy(sizePolicy)
        self.contacts_txt.setMinimumSize(QSize(0, 0))
        self.contacts_txt.setStyleSheet(u"font: 18pt \"Segoe UI\";\n"
"background: transparent;")

        self.gridLayout.addWidget(self.contacts_txt, 0, 0, 1, 1)

        self.verticalSpacer_41 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_41, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(contacts_landing)

        QMetaObject.connectSlotsByName(contacts_landing)
    # setupUi

    def retranslateUi(self, contacts_landing):
        contacts_landing.setWindowTitle(QCoreApplication.translate("contacts_landing", u"Contacts", None))
        self.sort_combo.setItemText(0, QCoreApplication.translate("contacts_landing", u"Recently Added", None))
        self.sort_combo.setItemText(1, QCoreApplication.translate("contacts_landing", u"Oldest", None))
        self.sort_combo.setItemText(2, QCoreApplication.translate("contacts_landing", u"Alphabetical", None))

        self.sort_combo.setPlaceholderText(QCoreApplication.translate("contacts_landing", u"Sort contacts by:", None))
        self.selecteditems_lbl.setText(QCoreApplication.translate("contacts_landing", u"TextLabel", None))
        self.search_line.setPlaceholderText(QCoreApplication.translate("contacts_landing", u"Search contacts by name, email, or company", None))
#if QT_CONFIG(tooltip)
        self.add_btn.setToolTip(QCoreApplication.translate("contacts_landing", u"Add Contact", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.add_btn.setWhatsThis(QCoreApplication.translate("contacts_landing", u"add contact", None))
#endif // QT_CONFIG(whatsthis)
        self.add_btn.setText("")
#if QT_CONFIG(tooltip)
        self.delete_btn.setToolTip(QCoreApplication.translate("contacts_landing", u"Delete Contacts", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.delete_btn.setWhatsThis(QCoreApplication.translate("contacts_landing", u"delete contact", None))
#endif // QT_CONFIG(whatsthis)
        self.delete_btn.setText("")
        self.contacts_txt.setText(QCoreApplication.translate("contacts_landing", u"Contacts", None))
    # retranslateUi

