# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_contacts(object):
    def setupUi(self, contacts):
        if not contacts.objectName():
            contacts.setObjectName(u"contacts")
        contacts.resize(1200, 675)
        contacts.setStyleSheet(u"background-color: rgb(64, 65, 66);")
        self.stackedWidget = QStackedWidget(contacts)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1200, 675))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.contacts_1 = QWidget()
        self.contacts_1.setObjectName(u"contacts_1")
        self.label = QLabel(self.contacts_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(530, 50, 101, 20))
        self.stackedWidget.addWidget(self.contacts_1)
        self.contacts_2 = QWidget()
        self.contacts_2.setObjectName(u"contacts_2")
        self.label_2 = QLabel(self.contacts_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(560, 50, 101, 20))
        self.stackedWidget.addWidget(self.contacts_2)
        self.contacts_3 = QWidget()
        self.contacts_3.setObjectName(u"contacts_3")
        self.label_3 = QLabel(self.contacts_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(540, 60, 101, 20))
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

        self.retranslateUi(contacts)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(contacts)
    # setupUi

    def retranslateUi(self, contacts):
        contacts.setWindowTitle(QCoreApplication.translate("contacts", u"Form", None))
        self.label.setText(QCoreApplication.translate("contacts", u"Arcas Page 1", None))
        self.label_2.setText(QCoreApplication.translate("contacts", u"Awal Page 2", None))
        self.label_3.setText(QCoreApplication.translate("contacts", u"Awal Page 3", None))
        self.label_4.setText(QCoreApplication.translate("contacts", u"Abuan Page 4", None))
        self.label_5.setText(QCoreApplication.translate("contacts", u"Abuan Page 5", None))
    # retranslateUi

