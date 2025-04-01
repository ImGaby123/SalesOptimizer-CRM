# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QWidget)

class Ui_settings(object):
    def setupUi(self, settings):
        if not settings.objectName():
            settings.setObjectName(u"settings")
        settings.resize(1201, 680)
        settings.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(settings)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.theme_combo = QComboBox(settings)
        self.theme_combo.addItem("")
        self.theme_combo.addItem("")
        self.theme_combo.setObjectName(u"theme_combo")

        self.horizontalLayout.addWidget(self.theme_combo)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.label_ = QLabel(settings)
        self.label_.setObjectName(u"label_")
        font = QFont()
        font.setPointSize(18)
        self.label_.setFont(font)

        self.gridLayout.addWidget(self.label_, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)


        self.retranslateUi(settings)

        QMetaObject.connectSlotsByName(settings)
    # setupUi

    def retranslateUi(self, settings):
        settings.setWindowTitle(QCoreApplication.translate("settings", u"Settings", None))
        self.label.setText(QCoreApplication.translate("settings", u"Theme", None))
        self.theme_combo.setItemText(0, QCoreApplication.translate("settings", u"Light", None))
        self.theme_combo.setItemText(1, QCoreApplication.translate("settings", u"Dark", None))

        self.theme_combo.setPlaceholderText("")
        self.label_.setText(QCoreApplication.translate("settings", u"Settings", None))
    # retranslateUi

