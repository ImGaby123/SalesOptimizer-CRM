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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QWidget)

class Ui_contacts2(object):
    def setupUi(self, contacts2):
        if not contacts2.objectName():
            contacts2.setObjectName(u"contacts2")
        contacts2.resize(700, 500)
        contacts2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_2 = QGridLayout(contacts2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.email_txt = QTextEdit(contacts2)
        self.email_txt.setObjectName(u"email_txt")
        self.email_txt.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_33.addWidget(self.email_txt)


        self.gridLayout.addLayout(self.horizontalLayout_33, 6, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.to_label_4 = QLabel(contacts2)
        self.to_label_4.setObjectName(u"to_label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_label_4.sizePolicy().hasHeightForWidth())
        self.to_label_4.setSizePolicy(sizePolicy)
        self.to_label_4.setMaximumSize(QSize(50, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.to_label_4.setFont(font)
        self.to_label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_23.addWidget(self.to_label_4)

        self.to_line = QLineEdit(contacts2)
        self.to_line.setObjectName(u"to_line")

        self.horizontalLayout_23.addWidget(self.to_line)


        self.gridLayout.addLayout(self.horizontalLayout_23, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.from_label_4 = QLabel(contacts2)
        self.from_label_4.setObjectName(u"from_label_4")
        sizePolicy.setHeightForWidth(self.from_label_4.sizePolicy().hasHeightForWidth())
        self.from_label_4.setSizePolicy(sizePolicy)
        self.from_label_4.setMaximumSize(QSize(50, 16777215))
        self.from_label_4.setFont(font)
        self.from_label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_22.addWidget(self.from_label_4)

        self.from_line = QLineEdit(contacts2)
        self.from_line.setObjectName(u"from_line")

        self.horizontalLayout_22.addWidget(self.from_line)


        self.gridLayout.addLayout(self.horizontalLayout_22, 0, 0, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.subject_label_4 = QLabel(contacts2)
        self.subject_label_4.setObjectName(u"subject_label_4")
        sizePolicy.setHeightForWidth(self.subject_label_4.sizePolicy().hasHeightForWidth())
        self.subject_label_4.setSizePolicy(sizePolicy)
        self.subject_label_4.setMaximumSize(QSize(50, 16777215))
        self.subject_label_4.setFont(font)
        self.subject_label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_24.addWidget(self.subject_label_4)

        self.subject_line = QLineEdit(contacts2)
        self.subject_line.setObjectName(u"subject_line")

        self.horizontalLayout_24.addWidget(self.subject_line)


        self.gridLayout.addLayout(self.horizontalLayout_24, 5, 0, 1, 1)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer)

        self.send_btn = QPushButton(contacts2)
        self.send_btn.setObjectName(u"send_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.send_btn.sizePolicy().hasHeightForWidth())
        self.send_btn.setSizePolicy(sizePolicy1)
        self.send_btn.setMinimumSize(QSize(105, 0))
        self.send_btn.setMaximumSize(QSize(16777215, 30))
        self.send_btn.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")

        self.horizontalLayout_35.addWidget(self.send_btn)


        self.gridLayout.addLayout(self.horizontalLayout_35, 8, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(contacts2)

        QMetaObject.connectSlotsByName(contacts2)
    # setupUi

    def retranslateUi(self, contacts2):
        contacts2.setWindowTitle(QCoreApplication.translate("contacts2", u"Form", None))
        self.email_txt.setHtml(QCoreApplication.translate("contacts2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.to_label_4.setText(QCoreApplication.translate("contacts2", u"To:", None))
        self.from_label_4.setText(QCoreApplication.translate("contacts2", u"From:", None))
        self.subject_label_4.setText(QCoreApplication.translate("contacts2", u"Subject:", None))
        self.send_btn.setText(QCoreApplication.translate("contacts2", u"Send", None))
    # retranslateUi

