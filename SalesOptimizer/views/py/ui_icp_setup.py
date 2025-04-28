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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTableView, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_icp_setup(object):
    def setupUi(self, icp_setup):
        if not icp_setup.objectName():
            icp_setup.setObjectName(u"icp_setup")
        icp_setup.resize(768, 526)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(icp_setup.sizePolicy().hasHeightForWidth())
        icp_setup.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(icp_setup)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
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
        if (self.attribute_tbl.columnCount() < 2):
            self.attribute_tbl.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.attribute_tbl.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.attribute_tbl.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.attribute_tbl.rowCount() < 6):
            self.attribute_tbl.setRowCount(6)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.attribute_tbl.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.attribute_tbl.setItem(0, 1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.attribute_tbl.setItem(1, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.attribute_tbl.setItem(1, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.attribute_tbl.setItem(2, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.attribute_tbl.setItem(2, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.attribute_tbl.setItem(3, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.attribute_tbl.setItem(3, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.attribute_tbl.setItem(4, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.attribute_tbl.setItem(4, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.attribute_tbl.setItem(5, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.attribute_tbl.setItem(5, 1, __qtablewidgetitem13)
        self.attribute_tbl.setObjectName(u"attribute_tbl")
        self.attribute_tbl.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.attribute_tbl.sizePolicy().hasHeightForWidth())
        self.attribute_tbl.setSizePolicy(sizePolicy2)
        self.attribute_tbl.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.attribute_tbl.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.attribute_tbl.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.attribute_tbl.setGridStyle(Qt.SolidLine)
        self.attribute_tbl.setWordWrap(True)
        self.attribute_tbl.setCornerButtonEnabled(True)
        self.attribute_tbl.setRowCount(6)
        self.attribute_tbl.setColumnCount(2)

        self.verticalLayout_2.addWidget(self.attribute_tbl)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_combo = QComboBox(self.step1_page)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.total_attributes_lbl.sizePolicy().hasHeightForWidth())
        self.total_attributes_lbl.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.total_attributes_lbl)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.total_lbl = QLabel(self.step1_page)
        self.total_lbl.setObjectName(u"total_lbl")
        sizePolicy3.setHeightForWidth(self.total_lbl.sizePolicy().hasHeightForWidth())
        self.total_lbl.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.define_btn.sizePolicy().hasHeightForWidth())
        self.define_btn.setSizePolicy(sizePolicy3)
        self.define_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.define_btn.setStyleSheet(u"background-color: blue;\n"
"color: rgb(255, 255, 255);")

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
        self.attributes_tblview_2 = QTableView(self.step2_page)
        self.attributes_tblview_2.setObjectName(u"attributes_tblview_2")

        self.gridLayout_10.addWidget(self.attributes_tblview_2, 1, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)

        self.stackedWidget_3 = QStackedWidget(self.step2_page)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.city_page_2 = QWidget()
        self.city_page_2.setObjectName(u"city_page_2")
        self.gridLayout_11 = QGridLayout(self.city_page_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.no1_spin_2 = QSpinBox(self.city_page_2)
        self.no1_spin_2.setObjectName(u"no1_spin_2")

        self.gridLayout_11.addWidget(self.no1_spin_2, 0, 4, 1, 1)

        self.city_line_2 = QLineEdit(self.city_page_2)
        self.city_line_2.setObjectName(u"city_line_2")

        self.gridLayout_11.addWidget(self.city_line_2, 0, 2, 1, 1)

        self.city_combo_2 = QComboBox(self.city_page_2)
        self.city_combo_2.addItem("")
        self.city_combo_2.addItem("")
        self.city_combo_2.setObjectName(u"city_combo_2")
        self.city_combo_2.setEditable(True)

        self.gridLayout_11.addWidget(self.city_combo_2, 0, 1, 1, 1)

        self.score_city3_lbl_2 = QLabel(self.city_page_2)
        self.score_city3_lbl_2.setObjectName(u"score_city3_lbl_2")

        self.gridLayout_11.addWidget(self.score_city3_lbl_2, 0, 3, 1, 1)

        self.when_city3_lbl_2 = QLabel(self.city_page_2)
        self.when_city3_lbl_2.setObjectName(u"when_city3_lbl_2")

        self.gridLayout_11.addWidget(self.when_city3_lbl_2, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.city_page_2)
        self.religion_page_2 = QWidget()
        self.religion_page_2.setObjectName(u"religion_page_2")
        self.gridLayout_12 = QGridLayout(self.religion_page_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.religion_line_2 = QLineEdit(self.religion_page_2)
        self.religion_line_2.setObjectName(u"religion_line_2")

        self.gridLayout_12.addWidget(self.religion_line_2, 0, 2, 1, 1)

        self.religion_spin_2 = QSpinBox(self.religion_page_2)
        self.religion_spin_2.setObjectName(u"religion_spin_2")

        self.gridLayout_12.addWidget(self.religion_spin_2, 0, 4, 1, 1)

        self.religion_combo_2 = QComboBox(self.religion_page_2)
        self.religion_combo_2.addItem("")
        self.religion_combo_2.addItem("")
        self.religion_combo_2.setObjectName(u"religion_combo_2")
        self.religion_combo_2.setEditable(True)

        self.gridLayout_12.addWidget(self.religion_combo_2, 0, 1, 1, 1)

        self.score_religion3_lbl_2 = QLabel(self.religion_page_2)
        self.score_religion3_lbl_2.setObjectName(u"score_religion3_lbl_2")

        self.gridLayout_12.addWidget(self.score_religion3_lbl_2, 0, 3, 1, 1)

        self.when_religion3_lbl_3 = QLabel(self.religion_page_2)
        self.when_religion3_lbl_3.setObjectName(u"when_religion3_lbl_3")

        self.gridLayout_12.addWidget(self.when_religion3_lbl_3, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.religion_page_2)
        self.country_page_2 = QWidget()
        self.country_page_2.setObjectName(u"country_page_2")
        self.gridLayout_13 = QGridLayout(self.country_page_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.when_country3_lbl_2 = QLabel(self.country_page_2)
        self.when_country3_lbl_2.setObjectName(u"when_country3_lbl_2")

        self.gridLayout_13.addWidget(self.when_country3_lbl_2, 0, 0, 1, 1)

        self.score_country3_lbl_2 = QLabel(self.country_page_2)
        self.score_country3_lbl_2.setObjectName(u"score_country3_lbl_2")

        self.gridLayout_13.addWidget(self.score_country3_lbl_2, 0, 3, 1, 1)

        self.country_spin_2 = QSpinBox(self.country_page_2)
        self.country_spin_2.setObjectName(u"country_spin_2")

        self.gridLayout_13.addWidget(self.country_spin_2, 0, 4, 1, 1)

        self.country_combo_2 = QComboBox(self.country_page_2)
        self.country_combo_2.addItem("")
        self.country_combo_2.setObjectName(u"country_combo_2")
        self.country_combo_2.setEditable(True)

        self.gridLayout_13.addWidget(self.country_combo_2, 0, 1, 1, 1)

        self.country_line_2 = QLineEdit(self.country_page_2)
        self.country_line_2.setObjectName(u"country_line_2")

        self.gridLayout_13.addWidget(self.country_line_2, 0, 2, 1, 1)

        self.stackedWidget_3.addWidget(self.country_page_2)
        self.profession_page_2 = QWidget()
        self.profession_page_2.setObjectName(u"profession_page_2")
        self.gridLayout_14 = QGridLayout(self.profession_page_2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.profession_spin_2 = QSpinBox(self.profession_page_2)
        self.profession_spin_2.setObjectName(u"profession_spin_2")

        self.gridLayout_14.addWidget(self.profession_spin_2, 0, 4, 1, 1)

        self.when_profession3_lbl_2 = QLabel(self.profession_page_2)
        self.when_profession3_lbl_2.setObjectName(u"when_profession3_lbl_2")

        self.gridLayout_14.addWidget(self.when_profession3_lbl_2, 0, 0, 1, 1)

        self.score_profession3_lbl_2 = QLabel(self.profession_page_2)
        self.score_profession3_lbl_2.setObjectName(u"score_profession3_lbl_2")

        self.gridLayout_14.addWidget(self.score_profession3_lbl_2, 0, 3, 1, 1)

        self.profession_line_2 = QLineEdit(self.profession_page_2)
        self.profession_line_2.setObjectName(u"profession_line_2")

        self.gridLayout_14.addWidget(self.profession_line_2, 0, 2, 1, 1)

        self.profession_combo_2 = QComboBox(self.profession_page_2)
        self.profession_combo_2.addItem("")
        self.profession_combo_2.addItem("")
        self.profession_combo_2.setObjectName(u"profession_combo_2")
        self.profession_combo_2.setEditable(True)

        self.gridLayout_14.addWidget(self.profession_combo_2, 0, 1, 1, 1)

        self.stackedWidget_3.addWidget(self.profession_page_2)
        self.age_page_2 = QWidget()
        self.age_page_2.setObjectName(u"age_page_2")
        self.gridLayout_15 = QGridLayout(self.age_page_2)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.pushButton = QPushButton(self.age_page_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_15.addWidget(self.pushButton, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.age_page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_15.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.label_2 = QLabel(self.age_page_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_15.addWidget(self.label_2, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.age_page_2)
        self.industry_page_2 = QWidget()
        self.industry_page_2.setObjectName(u"industry_page_2")
        self.gridLayout_16 = QGridLayout(self.industry_page_2)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.score_industry3_lbl_2 = QLabel(self.industry_page_2)
        self.score_industry3_lbl_2.setObjectName(u"score_industry3_lbl_2")

        self.gridLayout_16.addWidget(self.score_industry3_lbl_2, 0, 3, 1, 1)

        self.industry_line_2 = QLineEdit(self.industry_page_2)
        self.industry_line_2.setObjectName(u"industry_line_2")

        self.gridLayout_16.addWidget(self.industry_line_2, 0, 2, 1, 1)

        self.when_religion3_lbl_4 = QLabel(self.industry_page_2)
        self.when_religion3_lbl_4.setObjectName(u"when_religion3_lbl_4")

        self.gridLayout_16.addWidget(self.when_religion3_lbl_4, 0, 0, 1, 1)

        self.industry_spin_2 = QSpinBox(self.industry_page_2)
        self.industry_spin_2.setObjectName(u"industry_spin_2")

        self.gridLayout_16.addWidget(self.industry_spin_2, 0, 4, 1, 1)

        self.industry_combo_2 = QComboBox(self.industry_page_2)
        self.industry_combo_2.addItem("")
        self.industry_combo_2.addItem("")
        self.industry_combo_2.setObjectName(u"industry_combo_2")
        self.industry_combo_2.setEditable(True)

        self.gridLayout_16.addWidget(self.industry_combo_2, 0, 1, 1, 1)

        self.stackedWidget_3.addWidget(self.industry_page_2)

        self.gridLayout_10.addWidget(self.stackedWidget_3, 1, 2, 1, 1)

        self.age_set_lbl_2 = QLabel(self.step2_page)
        self.age_set_lbl_2.setObjectName(u"age_set_lbl_2")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.age_set_lbl_2.setFont(font3)

        self.gridLayout_10.addWidget(self.age_set_lbl_2, 0, 2, 1, 1)

        self.label = QLabel(self.step2_page)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.gridLayout_10.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_10)

        self.verticalSpacer_2 = QSpacerItem(729, 136, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.step2_save_btn_2 = QPushButton(self.step2_page)
        self.step2_save_btn_2.setObjectName(u"step2_save_btn_2")

        self.horizontalLayout_4.addWidget(self.step2_save_btn_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.step2_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.retranslateUi(icp_setup)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(icp_setup)
    # setupUi

    def retranslateUi(self, icp_setup):
        icp_setup.setWindowTitle(QCoreApplication.translate("icp_setup", u"ICP Setup", None))
        self.choose_lbl.setText(QCoreApplication.translate("icp_setup", u"Choose Lead Quality Attributes", None))
        self.instruction2_lbl.setText(QCoreApplication.translate("icp_setup", u"attribute and also indicate if it is mandatory for an attribute to have a value to calculate a quality score of a lead.", None))
        self.step1_lbl.setText(QCoreApplication.translate("icp_setup", u"Create Lead Quality Criteria, Step 1 of 2...	", None))
        self.instruction1_lbl.setText(QCoreApplication.translate("icp_setup", u"Choose attributes of lead which can potentially  define the quality of lead. You may choose to provide different weightage of each", None))
        ___qtablewidgetitem = self.attribute_tbl.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("icp_setup", u"Attribute", None));
        ___qtablewidgetitem1 = self.attribute_tbl.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("icp_setup", u"Weightage(%)", None));

        __sortingEnabled = self.attribute_tbl.isSortingEnabled()
        self.attribute_tbl.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.attribute_tbl.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("icp_setup", u"City", None));
        ___qtablewidgetitem3 = self.attribute_tbl.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("icp_setup", u"15", None));
        ___qtablewidgetitem4 = self.attribute_tbl.item(1, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("icp_setup", u"Region", None));
        ___qtablewidgetitem5 = self.attribute_tbl.item(1, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("icp_setup", u"15", None));
        ___qtablewidgetitem6 = self.attribute_tbl.item(2, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("icp_setup", u"Country", None));
        ___qtablewidgetitem7 = self.attribute_tbl.item(2, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("icp_setup", u"15", None));
        ___qtablewidgetitem8 = self.attribute_tbl.item(3, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("icp_setup", u"Profession", None));
        ___qtablewidgetitem9 = self.attribute_tbl.item(3, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("icp_setup", u"20", None));
        ___qtablewidgetitem10 = self.attribute_tbl.item(4, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("icp_setup", u"Age", None));
        ___qtablewidgetitem11 = self.attribute_tbl.item(4, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("icp_setup", u"15", None));
        ___qtablewidgetitem12 = self.attribute_tbl.item(5, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("icp_setup", u"Industry", None));
        ___qtablewidgetitem13 = self.attribute_tbl.item(5, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("icp_setup", u"20", None));
        self.attribute_tbl.setSortingEnabled(__sortingEnabled)

        self.add_combo.setPlaceholderText(QCoreApplication.translate("icp_setup", u"-- Add Lead Attribute --", None))
        self.total_attributes_lbl.setText(QCoreApplication.translate("icp_setup", u"6 Attributes", None))
        self.total_lbl.setText(QCoreApplication.translate("icp_setup", u"100", None))
        self.assign_checkbox.setText(QCoreApplication.translate("icp_setup", u"Assign weightage equally across the attributes", None))
        self.define_btn.setText(QCoreApplication.translate("icp_setup", u"Define Attribute Score>", None))
        self.define_lbl_2.setText(QCoreApplication.translate("icp_setup", u"Define Lead Attribute Rules", None))
        self.step2_lbl_2.setText(QCoreApplication.translate("icp_setup", u"Create Lead Quality Criteria, Step 2 of 2	", None))
        self.guide1_lbl_2.setText(QCoreApplication.translate("icp_setup", u"Provide scores to the relevant attribute values. You may  choose Has other value to assign scores to values out of the attribute's complete", None))
        self.guide2_lbl_2.setText(QCoreApplication.translate("icp_setup", u"list. Also you may choose Rest all to assign score all to remaining attribute values not define in the rule.", None))
        self.city_line_2.setText("")
        self.city_combo_2.setItemText(0, QCoreApplication.translate("icp_setup", u"Contains", None))
        self.city_combo_2.setItemText(1, QCoreApplication.translate("icp_setup", u"Has Other Values", None))

        self.city_combo_2.setCurrentText(QCoreApplication.translate("icp_setup", u"Contains", None))
        self.score_city3_lbl_2.setText(QCoreApplication.translate("icp_setup", u"Score=", None))
        self.when_city3_lbl_2.setText(QCoreApplication.translate("icp_setup", u"When City", None))
        self.religion_line_2.setText("")
        self.religion_combo_2.setItemText(0, QCoreApplication.translate("icp_setup", u"Contains", None))
        self.religion_combo_2.setItemText(1, QCoreApplication.translate("icp_setup", u"Has Other Values", None))

        self.religion_combo_2.setCurrentText(QCoreApplication.translate("icp_setup", u"Contains", None))
        self.score_religion3_lbl_2.setText(QCoreApplication.translate("icp_setup", u"Score=", None))
        self.when_religion3_lbl_3.setText(QCoreApplication.translate("icp_setup", u"When Country", None))
        self.when_country3_lbl_2.setText(QCoreApplication.translate("icp_setup", u"When Religion", None))
        self.score_country3_lbl_2.setText(QCoreApplication.translate("icp_setup", u"Score=", None))
        self.country_combo_2.setItemText(0, QCoreApplication.translate("icp_setup", u"Contains", None))

        self.country_combo_2.setCurrentText(QCoreApplication.translate("icp_setup", u"Contains", None))
        self.country_line_2.setText("")
        self.when_profession3_lbl_2.setText(QCoreApplication.translate("icp_setup", u"When Profession", None))
        self.score_profession3_lbl_2.setText(QCoreApplication.translate("icp_setup", u"Score=", None))
        self.profession_line_2.setText("")
        self.profession_combo_2.setItemText(0, QCoreApplication.translate("icp_setup", u"Contains", None))
        self.profession_combo_2.setItemText(1, QCoreApplication.translate("icp_setup", u"Has Other Value", None))

        self.profession_combo_2.setCurrentText(QCoreApplication.translate("icp_setup", u"Contains", None))
        self.pushButton.setText(QCoreApplication.translate("icp_setup", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("icp_setup", u"PushButton", None))
        self.label_2.setText(QCoreApplication.translate("icp_setup", u"TextLabel", None))
        self.score_industry3_lbl_2.setText(QCoreApplication.translate("icp_setup", u"Score=", None))
        self.industry_line_2.setText("")
        self.when_religion3_lbl_4.setText(QCoreApplication.translate("icp_setup", u"When Industry", None))
        self.industry_combo_2.setItemText(0, QCoreApplication.translate("icp_setup", u"Contains", None))
        self.industry_combo_2.setItemText(1, QCoreApplication.translate("icp_setup", u"Has Other Value", None))

        self.industry_combo_2.setCurrentText(QCoreApplication.translate("icp_setup", u"Contains", None))
        self.age_set_lbl_2.setText(QCoreApplication.translate("icp_setup", u"Set Attribute Scores", None))
        self.label.setText(QCoreApplication.translate("icp_setup", u"Attributes", None))
        self.step2_save_btn_2.setText(QCoreApplication.translate("icp_setup", u"Save", None))
    # retranslateUi

