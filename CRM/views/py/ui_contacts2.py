# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts2.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QWidget)
import views.py.icons_rc

class Ui_contacts2(object):
    def setupUi(self, contacts2):
        if not contacts2.objectName():
            contacts2.setObjectName(u"contacts2")
        contacts2.resize(1201, 681)
        self.gridLayout_2 = QGridLayout(contacts2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.from_label_4 = QLabel(contacts2)
        self.from_label_4.setObjectName(u"from_label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.from_label_4.sizePolicy().hasHeightForWidth())
        self.from_label_4.setSizePolicy(sizePolicy)
        self.from_label_4.setMaximumSize(QSize(110, 16777215))
        font = QFont()
        font.setPointSize(16)
        self.from_label_4.setFont(font)
        self.from_label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_22.addWidget(self.from_label_4)

        self.from_line_4 = QLineEdit(contacts2)
        self.from_line_4.setObjectName(u"from_line_4")
        self.from_line_4.setMinimumSize(QSize(0, 50))
        self.from_line_4.setMaximumSize(QSize(1060, 16777215))
        self.from_line_4.setStyleSheet(u"border: 2px solid #C0C0C0; /* Gray border */\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 4px; /* Smooth edges */\n"
"    padding: 6px; /* Space inside the field */\n"
"    font-size: 14px;")

        self.horizontalLayout_22.addWidget(self.from_line_4)


        self.gridLayout.addLayout(self.horizontalLayout_22, 0, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.to_label_4 = QLabel(contacts2)
        self.to_label_4.setObjectName(u"to_label_4")
        sizePolicy.setHeightForWidth(self.to_label_4.sizePolicy().hasHeightForWidth())
        self.to_label_4.setSizePolicy(sizePolicy)
        self.to_label_4.setMaximumSize(QSize(110, 16777215))
        self.to_label_4.setFont(font)
        self.to_label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_23.addWidget(self.to_label_4)

        self.to_line_4 = QLineEdit(contacts2)
        self.to_line_4.setObjectName(u"to_line_4")
        self.to_line_4.setMinimumSize(QSize(0, 50))
        self.to_line_4.setMaximumSize(QSize(1060, 16777215))
        self.to_line_4.setStyleSheet(u"border: 2px solid #C0C0C0; /* Gray border */\n"
"    border-radius: 4px; /* Smooth edges */\n"
"    padding: 6px; /* Space inside the field */\n"
"    font-size: 14px;\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_23.addWidget(self.to_line_4)


        self.gridLayout.addLayout(self.horizontalLayout_23, 1, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_8, 2, 0, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.subject_label_4 = QLabel(contacts2)
        self.subject_label_4.setObjectName(u"subject_label_4")
        sizePolicy.setHeightForWidth(self.subject_label_4.sizePolicy().hasHeightForWidth())
        self.subject_label_4.setSizePolicy(sizePolicy)
        self.subject_label_4.setMaximumSize(QSize(110, 16777215))
        self.subject_label_4.setFont(font)
        self.subject_label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_24.addWidget(self.subject_label_4)

        self.subject_line_4 = QLineEdit(contacts2)
        self.subject_line_4.setObjectName(u"subject_line_4")
        self.subject_line_4.setMinimumSize(QSize(0, 50))
        self.subject_line_4.setMaximumSize(QSize(1060, 16777215))
        self.subject_line_4.setStyleSheet(u"border: 2px solid #C0C0C0; /* Gray border */\n"
"color: rgb(0, 0, 0);\n"
"    border-radius: 4px; /* Smooth edges */\n"
"    padding: 6px; /* Space inside the field */\n"
"    font-size: 14px;")

        self.horizontalLayout_24.addWidget(self.subject_line_4)


        self.gridLayout.addLayout(self.horizontalLayout_24, 3, 0, 1, 1)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.email_body_4 = QTextEdit(contacts2)
        self.email_body_4.setObjectName(u"email_body_4")
        self.email_body_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_33.addWidget(self.email_body_4)


        self.gridLayout.addLayout(self.horizontalLayout_33, 4, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_9, 5, 0, 1, 1)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.bold_button_4 = QPushButton(contacts2)
        self.bold_button_4.setObjectName(u"bold_button_4")
        sizePolicy.setHeightForWidth(self.bold_button_4.sizePolicy().hasHeightForWidth())
        self.bold_button_4.setSizePolicy(sizePolicy)
        self.bold_button_4.setMaximumSize(QSize(30, 30))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.bold_button_4.setFont(font1)
        self.bold_button_4.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_34.addWidget(self.bold_button_4)

        self.italic_button_4 = QPushButton(contacts2)
        self.italic_button_4.setObjectName(u"italic_button_4")
        sizePolicy.setHeightForWidth(self.italic_button_4.sizePolicy().hasHeightForWidth())
        self.italic_button_4.setSizePolicy(sizePolicy)
        self.italic_button_4.setMaximumSize(QSize(30, 30))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(True)
        self.italic_button_4.setFont(font2)
        self.italic_button_4.setStyleSheet(u"\n"
"\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_34.addWidget(self.italic_button_4)

        self.underline_button_4 = QPushButton(contacts2)
        self.underline_button_4.setObjectName(u"underline_button_4")
        sizePolicy.setHeightForWidth(self.underline_button_4.sizePolicy().hasHeightForWidth())
        self.underline_button_4.setSizePolicy(sizePolicy)
        self.underline_button_4.setMaximumSize(QSize(30, 30))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setUnderline(True)
        self.underline_button_4.setFont(font3)
        self.underline_button_4.setStyleSheet(u"\n"
"\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_34.addWidget(self.underline_button_4)

        self.horizontalSpacer_13 = QSpacerItem(120, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_13)

        self.insert_combo_4 = QComboBox(contacts2)
        self.insert_combo_4.addItem("")
        self.insert_combo_4.setObjectName(u"insert_combo_4")
        sizePolicy.setHeightForWidth(self.insert_combo_4.sizePolicy().hasHeightForWidth())
        self.insert_combo_4.setSizePolicy(sizePolicy)
        self.insert_combo_4.setMinimumSize(QSize(70, 0))
        self.insert_combo_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.insert_combo_4.setEditable(False)

        self.horizontalLayout_34.addWidget(self.insert_combo_4)

        self.horizontalSpacer_14 = QSpacerItem(130, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_14)

        self.more_combo_4 = QComboBox(contacts2)
        self.more_combo_4.addItem("")
        self.more_combo_4.setObjectName(u"more_combo_4")
        sizePolicy.setHeightForWidth(self.more_combo_4.sizePolicy().hasHeightForWidth())
        self.more_combo_4.setSizePolicy(sizePolicy)
        self.more_combo_4.setMinimumSize(QSize(70, 0))
        self.more_combo_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.more_combo_4.setEditable(False)

        self.horizontalLayout_34.addWidget(self.more_combo_4)

        self.horizontalSpacer_25 = QSpacerItem(930, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_25)


        self.gridLayout.addLayout(self.horizontalLayout_34, 6, 0, 1, 1)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.send_button_4 = QPushButton(contacts2)
        self.send_button_4.setObjectName(u"send_button_4")
        sizePolicy.setHeightForWidth(self.send_button_4.sizePolicy().hasHeightForWidth())
        self.send_button_4.setSizePolicy(sizePolicy)
        self.send_button_4.setMinimumSize(QSize(105, 0))
        self.send_button_4.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setPointSize(12)
        self.send_button_4.setFont(font4)
        self.send_button_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")

        self.horizontalLayout_35.addWidget(self.send_button_4)

        self.horizontalSpacer_37 = QSpacerItem(330, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_37)

        self.text_combo_4 = QComboBox(contacts2)
        self.text_combo_4.addItem("")
        self.text_combo_4.setObjectName(u"text_combo_4")
        sizePolicy.setHeightForWidth(self.text_combo_4.sizePolicy().hasHeightForWidth())
        self.text_combo_4.setSizePolicy(sizePolicy)
        self.text_combo_4.setMinimumSize(QSize(70, 0))
        self.text_combo_4.setMaximumSize(QSize(16777215, 16777215))
        self.text_combo_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.text_combo_4.setEditable(False)

        self.horizontalLayout_35.addWidget(self.text_combo_4)

        self.size_combo_4 = QComboBox(contacts2)
        self.size_combo_4.addItem("")
        self.size_combo_4.setObjectName(u"size_combo_4")
        sizePolicy.setHeightForWidth(self.size_combo_4.sizePolicy().hasHeightForWidth())
        self.size_combo_4.setSizePolicy(sizePolicy)
        self.size_combo_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.size_combo_4.setEditable(False)

        self.horizontalLayout_35.addWidget(self.size_combo_4)

        self.letter_combo_4 = QComboBox(contacts2)
        self.letter_combo_4.addItem("")
        self.letter_combo_4.setObjectName(u"letter_combo_4")
        sizePolicy.setHeightForWidth(self.letter_combo_4.sizePolicy().hasHeightForWidth())
        self.letter_combo_4.setSizePolicy(sizePolicy)
        self.letter_combo_4.setMinimumSize(QSize(40, 0))
        self.letter_combo_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.letter_combo_4.setEditable(False)

        self.horizontalLayout_35.addWidget(self.letter_combo_4)

        self.horizontalSpacer_38 = QSpacerItem(925, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_38)


        self.gridLayout.addLayout(self.horizontalLayout_35, 7, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(contacts2)

        QMetaObject.connectSlotsByName(contacts2)
    # setupUi

    def retranslateUi(self, contacts2):
        contacts2.setWindowTitle(QCoreApplication.translate("contacts2", u"Form", None))
        self.from_label_4.setText(QCoreApplication.translate("contacts2", u"From:", None))
        self.to_label_4.setText(QCoreApplication.translate("contacts2", u"To:", None))
        self.subject_label_4.setText(QCoreApplication.translate("contacts2", u"Subject:", None))
        self.email_body_4.setHtml(QCoreApplication.translate("contacts2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.bold_button_4.setText(QCoreApplication.translate("contacts2", u"B", None))
        self.italic_button_4.setText(QCoreApplication.translate("contacts2", u"I", None))
        self.underline_button_4.setText(QCoreApplication.translate("contacts2", u"U", None))
        self.insert_combo_4.setItemText(0, QCoreApplication.translate("contacts2", u"Insert", None))

        self.insert_combo_4.setCurrentText(QCoreApplication.translate("contacts2", u"Insert", None))
        self.more_combo_4.setItemText(0, QCoreApplication.translate("contacts2", u"More", None))

        self.more_combo_4.setCurrentText(QCoreApplication.translate("contacts2", u"More", None))
        self.send_button_4.setText(QCoreApplication.translate("contacts2", u"Send", None))
        self.text_combo_4.setItemText(0, QCoreApplication.translate("contacts2", u"Arial", None))

#if QT_CONFIG(accessibility)
        self.text_combo_4.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.text_combo_4.setCurrentText(QCoreApplication.translate("contacts2", u"Arial", None))
        self.size_combo_4.setItemText(0, QCoreApplication.translate("contacts2", u"11", None))

        self.size_combo_4.setCurrentText(QCoreApplication.translate("contacts2", u"11", None))
        self.letter_combo_4.setItemText(0, QCoreApplication.translate("contacts2", u"A", None))

        self.letter_combo_4.setCurrentText(QCoreApplication.translate("contacts2", u"A", None))
    # retranslateUi

