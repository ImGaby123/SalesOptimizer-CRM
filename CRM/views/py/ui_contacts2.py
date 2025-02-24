# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts2.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_contacts2(object):
    def setupUi(self, contacts2):
        if not contacts2.objectName():
            contacts2.setObjectName(u"contacts2")
        contacts2.resize(640, 480)
        self.label = QLabel(contacts2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 100, 121, 20))

        self.retranslateUi(contacts2)

        QMetaObject.connectSlotsByName(contacts2)
    # setupUi

    def retranslateUi(self, contacts2):
        contacts2.setWindowTitle(QCoreApplication.translate("contacts2", u"Form", None))
        self.label.setText(QCoreApplication.translate("contacts2", u"abuan page 2", None))
    # retranslateUi

