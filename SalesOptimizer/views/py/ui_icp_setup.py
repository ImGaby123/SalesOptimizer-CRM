# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'icp_setup.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_icp_setup(object):
    def setupUi(self, icp_setup):
        if not icp_setup.objectName():
            icp_setup.setObjectName(u"icp_setup")
        icp_setup.resize(949, 467)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(icp_setup.sizePolicy().hasHeightForWidth())
        icp_setup.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(icp_setup)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(icp_setup)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.step1_page = QWidget()
        self.step1_page.setObjectName(u"step1_page")
        self.verticalLayout_2 = QVBoxLayout(self.step1_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.choose_lbl = QLabel(self.step1_page)
        self.choose_lbl.setObjectName(u"choose_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.choose_lbl.sizePolicy().hasHeightForWidth())
        self.choose_lbl.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.choose_lbl.setFont(font)

        self.gridLayout.addWidget(self.choose_lbl, 0, 0, 1, 1)

        self.instruction2_lbl = QLabel(self.step1_page)
        self.instruction2_lbl.setObjectName(u"instruction2_lbl")
        sizePolicy1.setHeightForWidth(self.instruction2_lbl.sizePolicy().hasHeightForWidth())
        self.instruction2_lbl.setSizePolicy(sizePolicy1)
        self.instruction2_lbl.setWordWrap(True)

        self.gridLayout.addWidget(self.instruction2_lbl, 3, 0, 1, 1)

        self.step1_lbl = QLabel(self.step1_page)
        self.step1_lbl.setObjectName(u"step1_lbl")
        sizePolicy1.setHeightForWidth(self.step1_lbl.sizePolicy().hasHeightForWidth())
        self.step1_lbl.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(10)
        self.step1_lbl.setFont(font1)

        self.gridLayout.addWidget(self.step1_lbl, 1, 0, 1, 1)

        self.instruction1_lbl = QLabel(self.step1_page)
        self.instruction1_lbl.setObjectName(u"instruction1_lbl")
        sizePolicy1.setHeightForWidth(self.instruction1_lbl.sizePolicy().hasHeightForWidth())
        self.instruction1_lbl.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.instruction1_lbl, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_8)

        self.attribute_tbl = QTableWidget(self.step1_page)
        self.attribute_tbl.setObjectName(u"attribute_tbl")

        self.verticalLayout_2.addWidget(self.attribute_tbl)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_combo = QComboBox(self.step1_page)
        self.add_combo.addItem("")
        self.add_combo.addItem("")
        self.add_combo.addItem("")
        self.add_combo.addItem("")
        self.add_combo.addItem("")
        self.add_combo.setObjectName(u"add_combo")
        sizePolicy1.setHeightForWidth(self.add_combo.sizePolicy().hasHeightForWidth())
        self.add_combo.setSizePolicy(sizePolicy1)
        self.add_combo.setAutoFillBackground(False)
        self.add_combo.setCurrentText(u"")

        self.verticalLayout.addWidget(self.add_combo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.total_attributes_lbl = QLabel(self.step1_page)
        self.total_attributes_lbl.setObjectName(u"total_attributes_lbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.total_attributes_lbl.sizePolicy().hasHeightForWidth())
        self.total_attributes_lbl.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.total_attributes_lbl)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.total_lbl = QLabel(self.step1_page)
        self.total_lbl.setObjectName(u"total_lbl")
        sizePolicy2.setHeightForWidth(self.total_lbl.sizePolicy().hasHeightForWidth())
        self.total_lbl.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setBold(True)
        self.total_lbl.setFont(font2)

        self.horizontalLayout_2.addWidget(self.total_lbl)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.assign_checkbox = QCheckBox(self.step1_page)
        self.assign_checkbox.setObjectName(u"assign_checkbox")
        sizePolicy1.setHeightForWidth(self.assign_checkbox.sizePolicy().hasHeightForWidth())
        self.assign_checkbox.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.assign_checkbox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.define_btn = QPushButton(self.step1_page)
        self.define_btn.setObjectName(u"define_btn")
        sizePolicy2.setHeightForWidth(self.define_btn.sizePolicy().hasHeightForWidth())
        self.define_btn.setSizePolicy(sizePolicy2)
        self.define_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.define_btn.setStyleSheet(u"QPushButton {\n"
"        background-color: #007BFF;\n"
"        color: white;\n"
"        border-radius: 8px;\n"
"        padding: 8px 16px;\n"
"        font-size: 14px;\n"
"    }\n"
"\n"
"    QPushButton:enabled {\n"
"        background-color: #007BFF;\n"
"        color: white;\n"
"    }\n"
"\n"
"    QPushButton:hover:enabled {\n"
"        background-color: #005FCC;\n"
"    }\n"
"\n"
"    QPushButton:pressed:enabled {\n"
"        background-color: #004B99;\n"
"    }\n"
"\n"
"    QPushButton:disabled {\n"
"        background-color: #cccccc;\n"
"        color: #666666;\n"
"    }")

        self.horizontalLayout.addWidget(self.define_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.step1_page)
        self.step2_page = QWidget()
        self.step2_page.setObjectName(u"step2_page")
        self.verticalLayout_6 = QVBoxLayout(self.step2_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.define_lbl_2 = QLabel(self.step2_page)
        self.define_lbl_2.setObjectName(u"define_lbl_2")
        sizePolicy1.setHeightForWidth(self.define_lbl_2.sizePolicy().hasHeightForWidth())
        self.define_lbl_2.setSizePolicy(sizePolicy1)
        self.define_lbl_2.setFont(font)

        self.verticalLayout_4.addWidget(self.define_lbl_2)

        self.step2_lbl_2 = QLabel(self.step2_page)
        self.step2_lbl_2.setObjectName(u"step2_lbl_2")
        sizePolicy1.setHeightForWidth(self.step2_lbl_2.sizePolicy().hasHeightForWidth())
        self.step2_lbl_2.setSizePolicy(sizePolicy1)
        self.step2_lbl_2.setFont(font1)

        self.verticalLayout_4.addWidget(self.step2_lbl_2)

        self.guide1_lbl_2 = QLabel(self.step2_page)
        self.guide1_lbl_2.setObjectName(u"guide1_lbl_2")
        sizePolicy1.setHeightForWidth(self.guide1_lbl_2.sizePolicy().hasHeightForWidth())
        self.guide1_lbl_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.guide1_lbl_2)

        self.guide2_lbl_2 = QLabel(self.step2_page)
        self.guide2_lbl_2.setObjectName(u"guide2_lbl_2")
        sizePolicy1.setHeightForWidth(self.guide2_lbl_2.sizePolicy().hasHeightForWidth())
        self.guide2_lbl_2.setSizePolicy(sizePolicy1)
        self.guide2_lbl_2.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.guide2_lbl_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.horizontalSpacer_7)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.attribute_tbl_2 = QTableWidget(self.step2_page)
        self.attribute_tbl_2.setObjectName(u"attribute_tbl_2")
        self.attribute_tbl_2.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_10.addWidget(self.attribute_tbl_2, 2, 0, 1, 1)

        self.label = QLabel(self.step2_page)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label.setFont(font3)

        self.gridLayout_10.addWidget(self.label, 0, 0, 1, 1)

        self.age_set_lbl_2 = QLabel(self.step2_page)
        self.age_set_lbl_2.setObjectName(u"age_set_lbl_2")
        self.age_set_lbl_2.setFont(font3)

        self.gridLayout_10.addWidget(self.age_set_lbl_2, 0, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.add_btn = QPushButton(self.step2_page)
        self.add_btn.setObjectName(u"add_btn")

        self.verticalLayout_3.addWidget(self.add_btn)

        self.when_lbl = QLabel(self.step2_page)
        self.when_lbl.setObjectName(u"when_lbl")

        self.verticalLayout_3.addWidget(self.when_lbl)

        self.scroll_area = QScrollArea(self.step2_page)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 448, 170))
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scroll_area)


        self.gridLayout_10.addLayout(self.verticalLayout_3, 2, 2, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_10)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.save_btn = QPushButton(self.step2_page)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout_4.addWidget(self.save_btn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.step2_page)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(icp_setup)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(icp_setup)
    # setupUi

    def retranslateUi(self, icp_setup):
        icp_setup.setWindowTitle(QCoreApplication.translate("icp_setup", u"ICP Setup", None))
        self.choose_lbl.setText(QCoreApplication.translate("icp_setup", u"Choose Lead Quality Attributes", None))
        self.instruction2_lbl.setText(QCoreApplication.translate("icp_setup", u"attribute and also indicate if it is mandatory for an attribute to have a value to calculate a quality score of a lead.", None))
        self.step1_lbl.setText(QCoreApplication.translate("icp_setup", u"Create Lead Quality Criteria, Step 1 of 2...	", None))
        self.instruction1_lbl.setText(QCoreApplication.translate("icp_setup", u"Choose attributes of lead which can potentially  define the quality of lead. You may choose to provide different weightage of each", None))
        self.add_combo.setItemText(0, QCoreApplication.translate("icp_setup", u"Country", None))
        self.add_combo.setItemText(1, QCoreApplication.translate("icp_setup", u"City", None))
        self.add_combo.setItemText(2, QCoreApplication.translate("icp_setup", u"Job Title", None))
        self.add_combo.setItemText(3, QCoreApplication.translate("icp_setup", u"Industry", None))
        self.add_combo.setItemText(4, QCoreApplication.translate("icp_setup", u"Years in Industry", None))

        self.add_combo.setPlaceholderText(QCoreApplication.translate("icp_setup", u"-- Add Lead Attribute --", None))
        self.total_attributes_lbl.setText("")
        self.total_lbl.setText(QCoreApplication.translate("icp_setup", u"Total Weights must be equal to 1.00", None))
        self.assign_checkbox.setText(QCoreApplication.translate("icp_setup", u"Assign weightage equally across the attributes", None))
        self.define_btn.setText(QCoreApplication.translate("icp_setup", u"Define Attribute Score>", None))
        self.define_lbl_2.setText(QCoreApplication.translate("icp_setup", u"Define Lead Attribute Rules", None))
        self.step2_lbl_2.setText(QCoreApplication.translate("icp_setup", u"Create Lead Quality Criteria, Step 2 of 2	", None))
        self.guide1_lbl_2.setText(QCoreApplication.translate("icp_setup", u"Provide scores to the relevant attribute values. You may  choose Has other value to assign scores to values out of the attribute's complete", None))
        self.guide2_lbl_2.setText(QCoreApplication.translate("icp_setup", u"list. Also you may choose Rest all to assign score all to remaining attribute values not define in the rule.", None))
        self.label.setText(QCoreApplication.translate("icp_setup", u"Attributes", None))
        self.age_set_lbl_2.setText(QCoreApplication.translate("icp_setup", u"Set Attribute Scores", None))
        self.add_btn.setText(QCoreApplication.translate("icp_setup", u"Add Category", None))
        self.when_lbl.setText(QCoreApplication.translate("icp_setup", u"When Attribute Contains: ", None))
        self.save_btn.setText(QCoreApplication.translate("icp_setup", u"Save", None))
    # retranslateUi

