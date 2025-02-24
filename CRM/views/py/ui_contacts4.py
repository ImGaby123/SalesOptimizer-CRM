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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_contacts4(object):
    def setupUi(self, contacts4):
        if not contacts4.objectName():
            contacts4.setObjectName(u"contacts4")
        contacts4.resize(640, 480)
        self.label = QLabel(contacts4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 100, 121, 20))

        self.retranslateUi(contacts4)

        QMetaObject.connectSlotsByName(contacts4)
    # setupUi

    def retranslateUi(self, contacts4):
        contacts4.setWindowTitle(QCoreApplication.translate("contacts4", u"Form", None))
        self.label.setText(QCoreApplication.translate("contacts4", u"awal page 2", None))
    # retranslateUi

