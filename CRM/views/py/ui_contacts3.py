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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_contacts3(object):
    def setupUi(self, contacts3):
        if not contacts3.objectName():
            contacts3.setObjectName(u"contacts3")
        contacts3.resize(640, 480)
        self.label = QLabel(contacts3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 190, 121, 20))

        self.retranslateUi(contacts3)

        QMetaObject.connectSlotsByName(contacts3)
    # setupUi

    def retranslateUi(self, contacts3):
        contacts3.setWindowTitle(QCoreApplication.translate("contacts3", u"Form", None))
        self.label.setText(QCoreApplication.translate("contacts3", u"awal page 1", None))
    # retranslateUi

