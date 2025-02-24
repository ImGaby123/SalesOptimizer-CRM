# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts1.ui'
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

class Ui_contacts1(object):
    def setupUi(self, contacts1):
        if not contacts1.objectName():
            contacts1.setObjectName(u"contacts1")
        contacts1.resize(640, 480)
        self.label = QLabel(contacts1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 180, 121, 20))

        self.retranslateUi(contacts1)

        QMetaObject.connectSlotsByName(contacts1)
    # setupUi

    def retranslateUi(self, contacts1):
        contacts1.setWindowTitle(QCoreApplication.translate("contacts1", u"Form", None))
        self.label.setText(QCoreApplication.translate("contacts1", u"abuan page 1", None))
    # retranslateUi

