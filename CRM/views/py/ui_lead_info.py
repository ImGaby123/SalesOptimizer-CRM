# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lead_info.ui'
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
    QProgressBar, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1201, 680)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 1201, 671))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.prospecting_txt = QLabel(self.gridLayoutWidget)
        self.prospecting_txt.setObjectName(u"prospecting_txt")
        sizePolicy.setHeightForWidth(self.prospecting_txt.sizePolicy().hasHeightForWidth())
        self.prospecting_txt.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.prospecting_txt)

        self.qualifications_txt = QLabel(self.gridLayoutWidget)
        self.qualifications_txt.setObjectName(u"qualifications_txt")
        sizePolicy.setHeightForWidth(self.qualifications_txt.sizePolicy().hasHeightForWidth())
        self.qualifications_txt.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.qualifications_txt)

        self.contacting_txt = QLabel(self.gridLayoutWidget)
        self.contacting_txt.setObjectName(u"contacting_txt")
        sizePolicy.setHeightForWidth(self.contacting_txt.sizePolicy().hasHeightForWidth())
        self.contacting_txt.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.contacting_txt)

        self.negotiating_txt = QLabel(self.gridLayoutWidget)
        self.negotiating_txt.setObjectName(u"negotiating_txt")
        sizePolicy.setHeightForWidth(self.negotiating_txt.sizePolicy().hasHeightForWidth())
        self.negotiating_txt.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.negotiating_txt)

        self.loss_txt = QLabel(self.gridLayoutWidget)
        self.loss_txt.setObjectName(u"loss_txt")
        sizePolicy.setHeightForWidth(self.loss_txt.sizePolicy().hasHeightForWidth())
        self.loss_txt.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.loss_txt)

        self.won_txt = QLabel(self.gridLayoutWidget)
        self.won_txt.setObjectName(u"won_txt")
        sizePolicy.setHeightForWidth(self.won_txt.sizePolicy().hasHeightForWidth())
        self.won_txt.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.won_txt)


        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.info_bar = QProgressBar(self.gridLayoutWidget)
        self.info_bar.setObjectName(u"info_bar")
        self.info_bar.setValue(15)

        self.horizontalLayout_6.addWidget(self.info_bar)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Lead ", None))
        self.label.setText(QCoreApplication.translate("Form", u"Leads", None))
        self.prospecting_txt.setText(QCoreApplication.translate("Form", u"Prospecting", None))
        self.qualifications_txt.setText(QCoreApplication.translate("Form", u"Qualifications", None))
        self.contacting_txt.setText(QCoreApplication.translate("Form", u"Contacting", None))
        self.negotiating_txt.setText(QCoreApplication.translate("Form", u"Negotiating", None))
        self.loss_txt.setText(QCoreApplication.translate("Form", u"Closed Loss", None))
        self.won_txt.setText(QCoreApplication.translate("Form", u"Closed Won", None))
    # retranslateUi

