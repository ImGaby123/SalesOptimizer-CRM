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
        settings.setStyleSheet(u"")
        self.gridLayout = QGridLayout(settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(settings)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: transparent;\n"
"color: White")

        self.horizontalLayout.addWidget(self.label)

        self.theme_combo = QComboBox(settings)
        self.theme_combo.addItem("")
        self.theme_combo.setObjectName(u"theme_combo")
        self.theme_combo.setStyleSheet(u"QComboBox {\n"
"    background-color: #262626;\n"
"    border: 1px solid #737373;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #262626;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* Down Arrow (Icon) */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/Resources/dropdown_white.svg);\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    margin-right: 15px; /* Space from the left */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.theme_combo)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.label_ = QLabel(settings)
        self.label_.setObjectName(u"label_")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_.setFont(font1)
        self.label_.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: transparent;")

        self.gridLayout.addWidget(self.label_, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 5, 1, 1, 1)


        self.retranslateUi(settings)

        QMetaObject.connectSlotsByName(settings)
    # setupUi

    def retranslateUi(self, settings):
        settings.setWindowTitle(QCoreApplication.translate("settings", u"Settings", None))
        self.label.setText(QCoreApplication.translate("settings", u"Theme", None))
        self.theme_combo.setItemText(0, QCoreApplication.translate("settings", u"Dark", None))

        self.theme_combo.setPlaceholderText("")
        self.label_.setText(QCoreApplication.translate("settings", u"Settings", None))
    # retranslateUi

