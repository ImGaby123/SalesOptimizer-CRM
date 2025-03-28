# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lead_list.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1201, 680)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1201, 681))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 1)

        self.list_tbl = QTableWidget(self.layoutWidget)
        self.list_tbl.setObjectName(u"list_tbl")
        self.list_tbl.setMouseTracking(False)
        self.list_tbl.setStyleSheet(u"QTableWidget {\n"
"border: 1px solid black;\n"
"}\n"
"")
        self.list_tbl.horizontalHeader().setCascadingSectionResizes(False)
        self.list_tbl.horizontalHeader().setDefaultSectionSize(200)
        self.list_tbl.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.list_tbl, 7, 0, 1, 1)

        self.verticalSpacer_42 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_42, 1, 0, 1, 1)

        self.list_txt = QLabel(self.layoutWidget)
        self.list_txt.setObjectName(u"list_txt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.list_txt.sizePolicy().hasHeightForWidth())
        self.list_txt.setSizePolicy(sizePolicy1)
        self.list_txt.setMinimumSize(QSize(0, 0))
        self.list_txt.setStyleSheet(u"font: 18pt \"Segoe UI\";\n"
"background: transparent;")

        self.gridLayout.addWidget(self.list_txt, 0, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.search_line = QLineEdit(self.layoutWidget)
        self.search_line.setObjectName(u"search_line")
        sizePolicy1.setHeightForWidth(self.search_line.sizePolicy().hasHeightForWidth())
        self.search_line.setSizePolicy(sizePolicy1)
        self.search_line.setMinimumSize(QSize(0, 30))
        self.search_line.setMaximumSize(QSize(290, 16777215))
        self.search_line.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid black;\n"
"}")
        self.search_line.setFrame(True)
        self.search_line.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.search_line.setClearButtonEnabled(False)

        self.horizontalLayout_22.addWidget(self.search_line)

        self.leadinfo_btn = QPushButton(self.layoutWidget)
        self.leadinfo_btn.setObjectName(u"leadinfo_btn")
        sizePolicy1.setHeightForWidth(self.leadinfo_btn.sizePolicy().hasHeightForWidth())
        self.leadinfo_btn.setSizePolicy(sizePolicy1)

        self.horizontalLayout_22.addWidget(self.leadinfo_btn)

        self.horizontalSpacer = QSpacerItem(850, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.add_btn = QPushButton(self.layoutWidget)
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

        self.delete_btn = QPushButton(self.layoutWidget)
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

        self.sort_combo = QComboBox(self.layoutWidget)
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.addItem("")
        self.sort_combo.setObjectName(u"sort_combo")
        sizePolicy1.setHeightForWidth(self.sort_combo.sizePolicy().hasHeightForWidth())
        self.sort_combo.setSizePolicy(sizePolicy1)
        self.sort_combo.setMinimumSize(QSize(0, 20))
        self.sort_combo.setMaximumSize(QSize(120, 16777215))
        self.sort_combo.setStyleSheet(u"")
        self.sort_combo.setEditable(False)

        self.gridLayout.addWidget(self.sort_combo, 4, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.list_txt.setText(QCoreApplication.translate("Form", u"Lead List", None))
        self.search_line.setPlaceholderText(QCoreApplication.translate("Form", u"Contacts", None))
        self.leadinfo_btn.setText(QCoreApplication.translate("Form", u"Lead Information", None))
#if QT_CONFIG(tooltip)
        self.add_btn.setToolTip(QCoreApplication.translate("Form", u"Add Contact", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.add_btn.setWhatsThis(QCoreApplication.translate("Form", u"add contact", None))
#endif // QT_CONFIG(whatsthis)
        self.add_btn.setText("")
#if QT_CONFIG(tooltip)
        self.delete_btn.setToolTip(QCoreApplication.translate("Form", u"Delete Contacts", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.delete_btn.setWhatsThis(QCoreApplication.translate("Form", u"delete contact", None))
#endif // QT_CONFIG(whatsthis)
        self.delete_btn.setText("")
        self.sort_combo.setItemText(0, QCoreApplication.translate("Form", u"All Contacts", None))
        self.sort_combo.setItemText(1, QCoreApplication.translate("Form", u"Recently Added", None))
        self.sort_combo.setItemText(2, QCoreApplication.translate("Form", u"Oldest", None))
        self.sort_combo.setItemText(3, QCoreApplication.translate("Form", u"Alphabetical", None))

        self.sort_combo.setPlaceholderText(QCoreApplication.translate("Form", u"Sort contacts by:", None))
    # retranslateUi

