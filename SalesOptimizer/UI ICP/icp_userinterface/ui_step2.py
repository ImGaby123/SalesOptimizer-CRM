# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'step2.ui'
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
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_icp_step2(object):
    def setupUi(self, icp_step2):
        if not icp_step2.objectName():
            icp_step2.setObjectName(u"icp_step2")
        icp_step2.resize(750, 510)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(icp_step2.sizePolicy().hasHeightForWidth())
        icp_step2.setSizePolicy(sizePolicy)
        self.gridLayout_9 = QGridLayout(icp_step2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.define_lbl = QLabel(icp_step2)
        self.define_lbl.setObjectName(u"define_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.define_lbl.sizePolicy().hasHeightForWidth())
        self.define_lbl.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.define_lbl.setFont(font)

        self.verticalLayout.addWidget(self.define_lbl)

        self.step2_lbl = QLabel(icp_step2)
        self.step2_lbl.setObjectName(u"step2_lbl")
        sizePolicy1.setHeightForWidth(self.step2_lbl.sizePolicy().hasHeightForWidth())
        self.step2_lbl.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(10)
        self.step2_lbl.setFont(font1)

        self.verticalLayout.addWidget(self.step2_lbl)

        self.guide1_lbl = QLabel(icp_step2)
        self.guide1_lbl.setObjectName(u"guide1_lbl")
        sizePolicy1.setHeightForWidth(self.guide1_lbl.sizePolicy().hasHeightForWidth())
        self.guide1_lbl.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.guide1_lbl)

        self.guide2_lbl = QLabel(icp_step2)
        self.guide2_lbl.setObjectName(u"guide2_lbl")
        sizePolicy1.setHeightForWidth(self.guide2_lbl.sizePolicy().hasHeightForWidth())
        self.guide2_lbl.setSizePolicy(sizePolicy1)
        self.guide2_lbl.setWordWrap(True)

        self.verticalLayout.addWidget(self.guide2_lbl)


        self.gridLayout_9.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.attributes_tblview = QTableView(icp_step2)
        self.attributes_tblview.setObjectName(u"attributes_tblview")

        self.gridLayout_2.addWidget(self.attributes_tblview, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(icp_step2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.city1_page = QWidget()
        self.city1_page.setObjectName(u"city1_page")
        self.gridLayout_3 = QGridLayout(self.city1_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.city_line = QLineEdit(self.city1_page)
        self.city_line.setObjectName(u"city_line")

        self.gridLayout_3.addWidget(self.city_line, 5, 2, 1, 1)

        self.no1_spin = QSpinBox(self.city1_page)
        self.no1_spin.setObjectName(u"no1_spin")

        self.gridLayout_3.addWidget(self.no1_spin, 5, 4, 1, 1)

        self.when_city1_lbl = QLabel(self.city1_page)
        self.when_city1_lbl.setObjectName(u"when_city1_lbl")

        self.gridLayout_3.addWidget(self.when_city1_lbl, 1, 0, 1, 1)

        self.othervalue_lbl = QLabel(self.city1_page)
        self.othervalue_lbl.setObjectName(u"othervalue_lbl")

        self.gridLayout_3.addWidget(self.othervalue_lbl, 3, 1, 1, 1)

        self.when_city3_lbl = QLabel(self.city1_page)
        self.when_city3_lbl.setObjectName(u"when_city3_lbl")

        self.gridLayout_3.addWidget(self.when_city3_lbl, 5, 0, 1, 1)

        self.set_attribute_lbl = QLabel(self.city1_page)
        self.set_attribute_lbl.setObjectName(u"set_attribute_lbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.set_attribute_lbl.sizePolicy().hasHeightForWidth())
        self.set_attribute_lbl.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.set_attribute_lbl.setFont(font2)

        self.gridLayout_3.addWidget(self.set_attribute_lbl, 0, 0, 1, 1)

        self.score_city3_lbl = QLabel(self.city1_page)
        self.score_city3_lbl.setObjectName(u"score_city3_lbl")

        self.gridLayout_3.addWidget(self.score_city3_lbl, 5, 3, 1, 1)

        self.contains_lbl = QLabel(self.city1_page)
        self.contains_lbl.setObjectName(u"contains_lbl")

        self.gridLayout_3.addWidget(self.contains_lbl, 1, 1, 1, 1)

        self.label_4 = QLabel(self.city1_page)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 2, 1, 1)

        self.score_city1_lbl = QLabel(self.city1_page)
        self.score_city1_lbl.setObjectName(u"score_city1_lbl")

        self.gridLayout_3.addWidget(self.score_city1_lbl, 1, 3, 1, 1)

        self.when_city2_lbl = QLabel(self.city1_page)
        self.when_city2_lbl.setObjectName(u"when_city2_lbl")

        self.gridLayout_3.addWidget(self.when_city2_lbl, 3, 0, 1, 1)

        self.city_combo = QComboBox(self.city1_page)
        self.city_combo.addItem("")
        self.city_combo.addItem("")
        self.city_combo.setObjectName(u"city_combo")
        self.city_combo.setEditable(True)

        self.gridLayout_3.addWidget(self.city_combo, 5, 1, 1, 1)

        self.city1_lbl = QLabel(self.city1_page)
        self.city1_lbl.setObjectName(u"city1_lbl")

        self.gridLayout_3.addWidget(self.city1_lbl, 1, 4, 1, 1)

        self.score_city2_lbl = QLabel(self.city1_page)
        self.score_city2_lbl.setObjectName(u"score_city2_lbl")

        self.gridLayout_3.addWidget(self.score_city2_lbl, 3, 3, 1, 1)

        self.city2_lbl = QLabel(self.city1_page)
        self.city2_lbl.setObjectName(u"city2_lbl")

        self.gridLayout_3.addWidget(self.city2_lbl, 3, 4, 1, 1)

        self.stackedWidget.addWidget(self.city1_page)
        self.religion2_page = QWidget()
        self.religion2_page.setObjectName(u"religion2_page")
        self.gridLayout_4 = QGridLayout(self.religion2_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.religion_set_attribute_lbl = QLabel(self.religion2_page)
        self.religion_set_attribute_lbl.setObjectName(u"religion_set_attribute_lbl")
        sizePolicy2.setHeightForWidth(self.religion_set_attribute_lbl.sizePolicy().hasHeightForWidth())
        self.religion_set_attribute_lbl.setSizePolicy(sizePolicy2)
        self.religion_set_attribute_lbl.setFont(font2)

        self.gridLayout_4.addWidget(self.religion_set_attribute_lbl, 0, 0, 1, 1)

        self.when_religion1_lbl = QLabel(self.religion2_page)
        self.when_religion1_lbl.setObjectName(u"when_religion1_lbl")

        self.gridLayout_4.addWidget(self.when_religion1_lbl, 1, 0, 1, 1)

        self.religion_contains_lbl = QLabel(self.religion2_page)
        self.religion_contains_lbl.setObjectName(u"religion_contains_lbl")

        self.gridLayout_4.addWidget(self.religion_contains_lbl, 1, 1, 1, 1)

        self.religion_random_lbl = QLabel(self.religion2_page)
        self.religion_random_lbl.setObjectName(u"religion_random_lbl")

        self.gridLayout_4.addWidget(self.religion_random_lbl, 1, 2, 1, 1)

        self.score_religion1_lbl = QLabel(self.religion2_page)
        self.score_religion1_lbl.setObjectName(u"score_religion1_lbl")

        self.gridLayout_4.addWidget(self.score_religion1_lbl, 1, 3, 1, 1)

        self.religion1_lbl = QLabel(self.religion2_page)
        self.religion1_lbl.setObjectName(u"religion1_lbl")

        self.gridLayout_4.addWidget(self.religion1_lbl, 1, 4, 1, 1)

        self.when_religion2_lbl = QLabel(self.religion2_page)
        self.when_religion2_lbl.setObjectName(u"when_religion2_lbl")

        self.gridLayout_4.addWidget(self.when_religion2_lbl, 2, 0, 1, 1)

        self.religion_other_lbl = QLabel(self.religion2_page)
        self.religion_other_lbl.setObjectName(u"religion_other_lbl")

        self.gridLayout_4.addWidget(self.religion_other_lbl, 2, 1, 1, 1)

        self.score_religion2_lbl = QLabel(self.religion2_page)
        self.score_religion2_lbl.setObjectName(u"score_religion2_lbl")

        self.gridLayout_4.addWidget(self.score_religion2_lbl, 2, 3, 1, 1)

        self.religion2_lbl = QLabel(self.religion2_page)
        self.religion2_lbl.setObjectName(u"religion2_lbl")

        self.gridLayout_4.addWidget(self.religion2_lbl, 2, 4, 1, 1)

        self.when_religion3_lbl = QLabel(self.religion2_page)
        self.when_religion3_lbl.setObjectName(u"when_religion3_lbl")

        self.gridLayout_4.addWidget(self.when_religion3_lbl, 3, 0, 1, 1)

        self.religion_combo = QComboBox(self.religion2_page)
        self.religion_combo.addItem("")
        self.religion_combo.addItem("")
        self.religion_combo.setObjectName(u"religion_combo")
        self.religion_combo.setEditable(True)

        self.gridLayout_4.addWidget(self.religion_combo, 3, 1, 1, 1)

        self.religion_line = QLineEdit(self.religion2_page)
        self.religion_line.setObjectName(u"religion_line")

        self.gridLayout_4.addWidget(self.religion_line, 3, 2, 1, 1)

        self.score_religion3_lbl = QLabel(self.religion2_page)
        self.score_religion3_lbl.setObjectName(u"score_religion3_lbl")

        self.gridLayout_4.addWidget(self.score_religion3_lbl, 3, 3, 1, 1)

        self.religion_spin = QSpinBox(self.religion2_page)
        self.religion_spin.setObjectName(u"religion_spin")

        self.gridLayout_4.addWidget(self.religion_spin, 3, 4, 1, 1)

        self.stackedWidget.addWidget(self.religion2_page)
        self.country3_page = QWidget()
        self.country3_page.setObjectName(u"country3_page")
        self.gridLayout_5 = QGridLayout(self.country3_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.country_set_attribute_lbl = QLabel(self.country3_page)
        self.country_set_attribute_lbl.setObjectName(u"country_set_attribute_lbl")
        sizePolicy2.setHeightForWidth(self.country_set_attribute_lbl.sizePolicy().hasHeightForWidth())
        self.country_set_attribute_lbl.setSizePolicy(sizePolicy2)
        self.country_set_attribute_lbl.setFont(font2)

        self.gridLayout_5.addWidget(self.country_set_attribute_lbl, 0, 0, 1, 1)

        self.when_country1_lbl = QLabel(self.country3_page)
        self.when_country1_lbl.setObjectName(u"when_country1_lbl")

        self.gridLayout_5.addWidget(self.when_country1_lbl, 1, 0, 1, 1)

        self.country_contains_lbl = QLabel(self.country3_page)
        self.country_contains_lbl.setObjectName(u"country_contains_lbl")

        self.gridLayout_5.addWidget(self.country_contains_lbl, 1, 1, 1, 1)

        self.country_random_lbl = QLabel(self.country3_page)
        self.country_random_lbl.setObjectName(u"country_random_lbl")

        self.gridLayout_5.addWidget(self.country_random_lbl, 1, 2, 1, 1)

        self.score_country1_lbl = QLabel(self.country3_page)
        self.score_country1_lbl.setObjectName(u"score_country1_lbl")

        self.gridLayout_5.addWidget(self.score_country1_lbl, 1, 3, 1, 1)

        self.country1_lbl = QLabel(self.country3_page)
        self.country1_lbl.setObjectName(u"country1_lbl")

        self.gridLayout_5.addWidget(self.country1_lbl, 1, 4, 1, 1)

        self.when_country2_lbl = QLabel(self.country3_page)
        self.when_country2_lbl.setObjectName(u"when_country2_lbl")

        self.gridLayout_5.addWidget(self.when_country2_lbl, 2, 0, 1, 1)

        self.country_other_lbl = QLabel(self.country3_page)
        self.country_other_lbl.setObjectName(u"country_other_lbl")

        self.gridLayout_5.addWidget(self.country_other_lbl, 2, 1, 1, 1)

        self.score_country2_lbl = QLabel(self.country3_page)
        self.score_country2_lbl.setObjectName(u"score_country2_lbl")

        self.gridLayout_5.addWidget(self.score_country2_lbl, 2, 3, 1, 1)

        self.country2_lbl = QLabel(self.country3_page)
        self.country2_lbl.setObjectName(u"country2_lbl")

        self.gridLayout_5.addWidget(self.country2_lbl, 2, 4, 1, 1)

        self.when_country3_lbl = QLabel(self.country3_page)
        self.when_country3_lbl.setObjectName(u"when_country3_lbl")

        self.gridLayout_5.addWidget(self.when_country3_lbl, 3, 0, 1, 1)

        self.country_combo = QComboBox(self.country3_page)
        self.country_combo.addItem("")
        self.country_combo.setObjectName(u"country_combo")
        self.country_combo.setEditable(True)

        self.gridLayout_5.addWidget(self.country_combo, 3, 1, 1, 1)

        self.country_line = QLineEdit(self.country3_page)
        self.country_line.setObjectName(u"country_line")

        self.gridLayout_5.addWidget(self.country_line, 3, 2, 1, 1)

        self.score_country3_lbl = QLabel(self.country3_page)
        self.score_country3_lbl.setObjectName(u"score_country3_lbl")

        self.gridLayout_5.addWidget(self.score_country3_lbl, 3, 3, 1, 1)

        self.country_spin = QSpinBox(self.country3_page)
        self.country_spin.setObjectName(u"country_spin")

        self.gridLayout_5.addWidget(self.country_spin, 3, 4, 1, 1)

        self.stackedWidget.addWidget(self.country3_page)
        self.profession4_page = QWidget()
        self.profession4_page.setObjectName(u"profession4_page")
        self.gridLayout_6 = QGridLayout(self.profession4_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.profession_set_attribute_lbl = QLabel(self.profession4_page)
        self.profession_set_attribute_lbl.setObjectName(u"profession_set_attribute_lbl")
        sizePolicy2.setHeightForWidth(self.profession_set_attribute_lbl.sizePolicy().hasHeightForWidth())
        self.profession_set_attribute_lbl.setSizePolicy(sizePolicy2)
        self.profession_set_attribute_lbl.setFont(font2)

        self.gridLayout_6.addWidget(self.profession_set_attribute_lbl, 0, 0, 1, 1)

        self.when_profession1_lbl = QLabel(self.profession4_page)
        self.when_profession1_lbl.setObjectName(u"when_profession1_lbl")

        self.gridLayout_6.addWidget(self.when_profession1_lbl, 1, 0, 1, 1)

        self.profession_contains_lbl = QLabel(self.profession4_page)
        self.profession_contains_lbl.setObjectName(u"profession_contains_lbl")

        self.gridLayout_6.addWidget(self.profession_contains_lbl, 1, 1, 1, 1)

        self.profession_random_lbl = QLabel(self.profession4_page)
        self.profession_random_lbl.setObjectName(u"profession_random_lbl")

        self.gridLayout_6.addWidget(self.profession_random_lbl, 1, 2, 1, 1)

        self.score_profession1_lbl = QLabel(self.profession4_page)
        self.score_profession1_lbl.setObjectName(u"score_profession1_lbl")

        self.gridLayout_6.addWidget(self.score_profession1_lbl, 1, 3, 1, 1)

        self.profession1_lbl = QLabel(self.profession4_page)
        self.profession1_lbl.setObjectName(u"profession1_lbl")

        self.gridLayout_6.addWidget(self.profession1_lbl, 1, 4, 1, 1)

        self.when_profession2_lbl = QLabel(self.profession4_page)
        self.when_profession2_lbl.setObjectName(u"when_profession2_lbl")

        self.gridLayout_6.addWidget(self.when_profession2_lbl, 2, 0, 1, 1)

        self.profession_other_lbl = QLabel(self.profession4_page)
        self.profession_other_lbl.setObjectName(u"profession_other_lbl")

        self.gridLayout_6.addWidget(self.profession_other_lbl, 2, 1, 1, 1)

        self.score_profession2_lbl = QLabel(self.profession4_page)
        self.score_profession2_lbl.setObjectName(u"score_profession2_lbl")

        self.gridLayout_6.addWidget(self.score_profession2_lbl, 2, 3, 1, 1)

        self.profession2_lbl = QLabel(self.profession4_page)
        self.profession2_lbl.setObjectName(u"profession2_lbl")

        self.gridLayout_6.addWidget(self.profession2_lbl, 2, 4, 1, 1)

        self.when_profession3_lbl = QLabel(self.profession4_page)
        self.when_profession3_lbl.setObjectName(u"when_profession3_lbl")

        self.gridLayout_6.addWidget(self.when_profession3_lbl, 3, 0, 1, 1)

        self.profession_combo = QComboBox(self.profession4_page)
        self.profession_combo.addItem("")
        self.profession_combo.addItem("")
        self.profession_combo.setObjectName(u"profession_combo")
        self.profession_combo.setEditable(True)

        self.gridLayout_6.addWidget(self.profession_combo, 3, 1, 1, 1)

        self.profession_line = QLineEdit(self.profession4_page)
        self.profession_line.setObjectName(u"profession_line")

        self.gridLayout_6.addWidget(self.profession_line, 3, 2, 1, 1)

        self.score_profession3_lbl = QLabel(self.profession4_page)
        self.score_profession3_lbl.setObjectName(u"score_profession3_lbl")

        self.gridLayout_6.addWidget(self.score_profession3_lbl, 3, 3, 1, 1)

        self.profession_spin = QSpinBox(self.profession4_page)
        self.profession_spin.setObjectName(u"profession_spin")

        self.gridLayout_6.addWidget(self.profession_spin, 3, 4, 1, 1)

        self.stackedWidget.addWidget(self.profession4_page)
        self.age5_page = QWidget()
        self.age5_page.setObjectName(u"age5_page")
        self.gridLayout = QGridLayout(self.age5_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.age3_lbl = QLabel(self.age5_page)
        self.age3_lbl.setObjectName(u"age3_lbl")

        self.gridLayout.addWidget(self.age3_lbl, 3, 4, 1, 1)

        self.age2_lbl = QLabel(self.age5_page)
        self.age2_lbl.setObjectName(u"age2_lbl")

        self.gridLayout.addWidget(self.age2_lbl, 2, 4, 1, 1)

        self.between_lbl = QLabel(self.age5_page)
        self.between_lbl.setObjectName(u"between_lbl")

        self.gridLayout.addWidget(self.between_lbl, 1, 1, 1, 1)

        self.when_age4_lbl = QLabel(self.age5_page)
        self.when_age4_lbl.setObjectName(u"when_age4_lbl")

        self.gridLayout.addWidget(self.when_age4_lbl, 4, 0, 1, 1)

        self.age_set_lbl = QLabel(self.age5_page)
        self.age_set_lbl.setObjectName(u"age_set_lbl")
        self.age_set_lbl.setFont(font2)

        self.gridLayout.addWidget(self.age_set_lbl, 0, 0, 1, 1)

        self.score_age4_lbl = QLabel(self.age5_page)
        self.score_age4_lbl.setObjectName(u"score_age4_lbl")

        self.gridLayout.addWidget(self.score_age4_lbl, 4, 3, 1, 1)

        self.age_spin = QSpinBox(self.age5_page)
        self.age_spin.setObjectName(u"age_spin")

        self.gridLayout.addWidget(self.age_spin, 4, 4, 1, 1)

        self.age_combo = QComboBox(self.age5_page)
        self.age_combo.addItem("")
        self.age_combo.addItem("")
        self.age_combo.addItem("")
        self.age_combo.setObjectName(u"age_combo")
        self.age_combo.setEditable(True)

        self.gridLayout.addWidget(self.age_combo, 4, 1, 1, 1)

        self.less_lbl = QLabel(self.age5_page)
        self.less_lbl.setObjectName(u"less_lbl")

        self.gridLayout.addWidget(self.less_lbl, 3, 1, 1, 1)

        self.when_age2_lbl = QLabel(self.age5_page)
        self.when_age2_lbl.setObjectName(u"when_age2_lbl")

        self.gridLayout.addWidget(self.when_age2_lbl, 2, 0, 1, 1)

        self.age_line = QLineEdit(self.age5_page)
        self.age_line.setObjectName(u"age_line")

        self.gridLayout.addWidget(self.age_line, 4, 2, 1, 1)

        self.score_age1_lbl = QLabel(self.age5_page)
        self.score_age1_lbl.setObjectName(u"score_age1_lbl")

        self.gridLayout.addWidget(self.score_age1_lbl, 1, 3, 1, 1)

        self.when_age3_lbl = QLabel(self.age5_page)
        self.when_age3_lbl.setObjectName(u"when_age3_lbl")

        self.gridLayout.addWidget(self.when_age3_lbl, 3, 0, 1, 1)

        self.second_lbl = QLabel(self.age5_page)
        self.second_lbl.setObjectName(u"second_lbl")

        self.gridLayout.addWidget(self.second_lbl, 2, 2, 1, 1)

        self.greater_lbl = QLabel(self.age5_page)
        self.greater_lbl.setObjectName(u"greater_lbl")

        self.gridLayout.addWidget(self.greater_lbl, 2, 1, 1, 1)

        self.age1_lbl = QLabel(self.age5_page)
        self.age1_lbl.setObjectName(u"age1_lbl")

        self.gridLayout.addWidget(self.age1_lbl, 1, 4, 1, 1)

        self.when_age1_lbl = QLabel(self.age5_page)
        self.when_age1_lbl.setObjectName(u"when_age1_lbl")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.when_age1_lbl.sizePolicy().hasHeightForWidth())
        self.when_age1_lbl.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.when_age1_lbl, 1, 0, 1, 1)

        self.score_age2_lbl = QLabel(self.age5_page)
        self.score_age2_lbl.setObjectName(u"score_age2_lbl")

        self.gridLayout.addWidget(self.score_age2_lbl, 2, 3, 1, 1)

        self.third_lbl = QLabel(self.age5_page)
        self.third_lbl.setObjectName(u"third_lbl")

        self.gridLayout.addWidget(self.third_lbl, 3, 2, 1, 1)

        self.score_age3_lbl = QLabel(self.age5_page)
        self.score_age3_lbl.setObjectName(u"score_age3_lbl")

        self.gridLayout.addWidget(self.score_age3_lbl, 3, 3, 1, 1)

        self.first_lbl = QLabel(self.age5_page)
        self.first_lbl.setObjectName(u"first_lbl")

        self.gridLayout.addWidget(self.first_lbl, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.age5_page)
        self.industry6_page = QWidget()
        self.industry6_page.setObjectName(u"industry6_page")
        self.gridLayout_7 = QGridLayout(self.industry6_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.industry_set_attribute_lbl = QLabel(self.industry6_page)
        self.industry_set_attribute_lbl.setObjectName(u"industry_set_attribute_lbl")
        sizePolicy2.setHeightForWidth(self.industry_set_attribute_lbl.sizePolicy().hasHeightForWidth())
        self.industry_set_attribute_lbl.setSizePolicy(sizePolicy2)
        self.industry_set_attribute_lbl.setFont(font2)

        self.gridLayout_7.addWidget(self.industry_set_attribute_lbl, 0, 0, 1, 1)

        self.when_industry1_lbl = QLabel(self.industry6_page)
        self.when_industry1_lbl.setObjectName(u"when_industry1_lbl")

        self.gridLayout_7.addWidget(self.when_industry1_lbl, 1, 0, 1, 1)

        self.industry_contains_lbl = QLabel(self.industry6_page)
        self.industry_contains_lbl.setObjectName(u"industry_contains_lbl")

        self.gridLayout_7.addWidget(self.industry_contains_lbl, 1, 1, 1, 1)

        self.industry_random_lbl = QLabel(self.industry6_page)
        self.industry_random_lbl.setObjectName(u"industry_random_lbl")

        self.gridLayout_7.addWidget(self.industry_random_lbl, 1, 2, 1, 1)

        self.score_industry1_lbl = QLabel(self.industry6_page)
        self.score_industry1_lbl.setObjectName(u"score_industry1_lbl")

        self.gridLayout_7.addWidget(self.score_industry1_lbl, 1, 3, 1, 1)

        self.industry1_lbl = QLabel(self.industry6_page)
        self.industry1_lbl.setObjectName(u"industry1_lbl")

        self.gridLayout_7.addWidget(self.industry1_lbl, 1, 4, 1, 1)

        self.when_industry2_lbl = QLabel(self.industry6_page)
        self.when_industry2_lbl.setObjectName(u"when_industry2_lbl")

        self.gridLayout_7.addWidget(self.when_industry2_lbl, 2, 0, 1, 1)

        self.industry_other_lbl = QLabel(self.industry6_page)
        self.industry_other_lbl.setObjectName(u"industry_other_lbl")

        self.gridLayout_7.addWidget(self.industry_other_lbl, 2, 1, 1, 1)

        self.score_industry2_lbl = QLabel(self.industry6_page)
        self.score_industry2_lbl.setObjectName(u"score_industry2_lbl")

        self.gridLayout_7.addWidget(self.score_industry2_lbl, 2, 3, 1, 1)

        self.industry2_lbl = QLabel(self.industry6_page)
        self.industry2_lbl.setObjectName(u"industry2_lbl")

        self.gridLayout_7.addWidget(self.industry2_lbl, 2, 4, 1, 1)

        self.when_religion3_lbl_2 = QLabel(self.industry6_page)
        self.when_religion3_lbl_2.setObjectName(u"when_religion3_lbl_2")

        self.gridLayout_7.addWidget(self.when_religion3_lbl_2, 3, 0, 1, 1)

        self.industry_combo = QComboBox(self.industry6_page)
        self.industry_combo.addItem("")
        self.industry_combo.addItem("")
        self.industry_combo.setObjectName(u"industry_combo")
        self.industry_combo.setEditable(True)

        self.gridLayout_7.addWidget(self.industry_combo, 3, 1, 1, 1)

        self.industry_line = QLineEdit(self.industry6_page)
        self.industry_line.setObjectName(u"industry_line")

        self.gridLayout_7.addWidget(self.industry_line, 3, 2, 1, 1)

        self.score_industry3_lbl = QLabel(self.industry6_page)
        self.score_industry3_lbl.setObjectName(u"score_industry3_lbl")

        self.gridLayout_7.addWidget(self.score_industry3_lbl, 3, 3, 1, 1)

        self.industry_spin = QSpinBox(self.industry6_page)
        self.industry_spin.setObjectName(u"industry_spin")

        self.gridLayout_7.addWidget(self.industry_spin, 3, 4, 1, 1)

        self.stackedWidget.addWidget(self.industry6_page)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.step2_save_btn = QPushButton(icp_step2)
        self.step2_save_btn.setObjectName(u"step2_save_btn")

        self.horizontalLayout.addWidget(self.step2_save_btn)


        self.gridLayout_9.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        QWidget.setTabOrder(self.city_combo, self.city_line)
        QWidget.setTabOrder(self.city_line, self.no1_spin)
        QWidget.setTabOrder(self.no1_spin, self.country_combo)
        QWidget.setTabOrder(self.country_combo, self.country_line)
        QWidget.setTabOrder(self.country_line, self.country_spin)
        QWidget.setTabOrder(self.country_spin, self.religion_combo)
        QWidget.setTabOrder(self.religion_combo, self.religion_line)
        QWidget.setTabOrder(self.religion_line, self.religion_spin)
        QWidget.setTabOrder(self.religion_spin, self.profession_combo)
        QWidget.setTabOrder(self.profession_combo, self.profession_line)
        QWidget.setTabOrder(self.profession_line, self.profession_spin)
        QWidget.setTabOrder(self.profession_spin, self.age_combo)
        QWidget.setTabOrder(self.age_combo, self.age_line)
        QWidget.setTabOrder(self.age_line, self.age_spin)
        QWidget.setTabOrder(self.age_spin, self.industry_combo)
        QWidget.setTabOrder(self.industry_combo, self.industry_line)
        QWidget.setTabOrder(self.industry_line, self.industry_spin)

        self.retranslateUi(icp_step2)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(icp_step2)
    # setupUi

    def retranslateUi(self, icp_step2):
        icp_step2.setWindowTitle(QCoreApplication.translate("icp_step2", u"ICP Step 2", None))
        self.define_lbl.setText(QCoreApplication.translate("icp_step2", u"Define Lead Attribute Rules", None))
        self.step2_lbl.setText(QCoreApplication.translate("icp_step2", u"Create Lead Quality Criteria, Step 2 of 2	", None))
        self.guide1_lbl.setText(QCoreApplication.translate("icp_step2", u"Provide scores to the relevant attribute values. You may  choose Has other value to assign scores to values out of the attribute's complete", None))
        self.guide2_lbl.setText(QCoreApplication.translate("icp_step2", u"list. Also you may choose Rest all to assign score all to remaining attribute values not define in the rule.", None))
        self.city_line.setText("")
        self.when_city1_lbl.setText(QCoreApplication.translate("icp_step2", u"When City", None))
        self.othervalue_lbl.setText(QCoreApplication.translate("icp_step2", u"Has Other Value", None))
        self.when_city3_lbl.setText(QCoreApplication.translate("icp_step2", u"When City", None))
        self.set_attribute_lbl.setText(QCoreApplication.translate("icp_step2", u"Set Attribute Scores", None))
        self.score_city3_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.contains_lbl.setText(QCoreApplication.translate("icp_step2", u"Contains", None))
        self.label_4.setText(QCoreApplication.translate("icp_step2", u"Quezon City", None))
        self.score_city1_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.when_city2_lbl.setText(QCoreApplication.translate("icp_step2", u"When City", None))
        self.city_combo.setItemText(0, QCoreApplication.translate("icp_step2", u"Contains", None))
        self.city_combo.setItemText(1, QCoreApplication.translate("icp_step2", u"Has Other Values", None))

        self.city_combo.setCurrentText(QCoreApplication.translate("icp_step2", u"Contains", None))
        self.city1_lbl.setText(QCoreApplication.translate("icp_step2", u"10", None))
        self.score_city2_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.city2_lbl.setText(QCoreApplication.translate("icp_step2", u"5", None))
        self.religion_set_attribute_lbl.setText(QCoreApplication.translate("icp_step2", u"Set Attribute Scores", None))
        self.when_religion1_lbl.setText(QCoreApplication.translate("icp_step2", u"When Country", None))
        self.religion_contains_lbl.setText(QCoreApplication.translate("icp_step2", u"Contains", None))
        self.religion_random_lbl.setText(QCoreApplication.translate("icp_step2", u"Philippines", None))
        self.score_religion1_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.religion1_lbl.setText(QCoreApplication.translate("icp_step2", u"10", None))
        self.when_religion2_lbl.setText(QCoreApplication.translate("icp_step2", u"When Country", None))
        self.religion_other_lbl.setText(QCoreApplication.translate("icp_step2", u"Has Oher Values", None))
        self.score_religion2_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.religion2_lbl.setText(QCoreApplication.translate("icp_step2", u"8", None))
        self.when_religion3_lbl.setText(QCoreApplication.translate("icp_step2", u"When Country", None))
        self.religion_combo.setItemText(0, QCoreApplication.translate("icp_step2", u"Contains", None))
        self.religion_combo.setItemText(1, QCoreApplication.translate("icp_step2", u"Has Other Values", None))

        self.religion_combo.setCurrentText(QCoreApplication.translate("icp_step2", u"Contains", None))
        self.religion_line.setText("")
        self.score_religion3_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.country_set_attribute_lbl.setText(QCoreApplication.translate("icp_step2", u"Set Attribute Scores", None))
        self.when_country1_lbl.setText(QCoreApplication.translate("icp_step2", u"When Religion", None))
        self.country_contains_lbl.setText(QCoreApplication.translate("icp_step2", u"Contains", None))
        self.country_random_lbl.setText(QCoreApplication.translate("icp_step2", u"Have religion", None))
        self.score_country1_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.country1_lbl.setText(QCoreApplication.translate("icp_step2", u"10", None))
        self.when_country2_lbl.setText(QCoreApplication.translate("icp_step2", u"When Religion", None))
        self.country_other_lbl.setText(QCoreApplication.translate("icp_step2", u"None", None))
        self.score_country2_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.country2_lbl.setText(QCoreApplication.translate("icp_step2", u"5", None))
        self.when_country3_lbl.setText(QCoreApplication.translate("icp_step2", u"When Religion", None))
        self.country_combo.setItemText(0, QCoreApplication.translate("icp_step2", u"Contains", None))

        self.country_combo.setCurrentText(QCoreApplication.translate("icp_step2", u"Contains", None))
        self.country_line.setText("")
        self.score_country3_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.profession_set_attribute_lbl.setText(QCoreApplication.translate("icp_step2", u"Set Attribute Scores", None))
        self.when_profession1_lbl.setText(QCoreApplication.translate("icp_step2", u"When Profession", None))
        self.profession_contains_lbl.setText(QCoreApplication.translate("icp_step2", u"Contains", None))
        self.profession_random_lbl.setText(QCoreApplication.translate("icp_step2", u"Computer Related", None))
        self.score_profession1_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.profession1_lbl.setText(QCoreApplication.translate("icp_step2", u"20", None))
        self.when_profession2_lbl.setText(QCoreApplication.translate("icp_step2", u"When Profession", None))
        self.profession_other_lbl.setText(QCoreApplication.translate("icp_step2", u"Has Other Value", None))
        self.score_profession2_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.profession2_lbl.setText(QCoreApplication.translate("icp_step2", u"15", None))
        self.when_profession3_lbl.setText(QCoreApplication.translate("icp_step2", u"When Profession", None))
        self.profession_combo.setItemText(0, QCoreApplication.translate("icp_step2", u"Contains", None))
        self.profession_combo.setItemText(1, QCoreApplication.translate("icp_step2", u"Has Other Value", None))

        self.profession_combo.setCurrentText(QCoreApplication.translate("icp_step2", u"Contains", None))
        self.profession_line.setText("")
        self.score_profession3_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.age3_lbl.setText(QCoreApplication.translate("icp_step2", u"6", None))
        self.age2_lbl.setText(QCoreApplication.translate("icp_step2", u"8", None))
        self.between_lbl.setText(QCoreApplication.translate("icp_step2", u"Between", None))
        self.when_age4_lbl.setText(QCoreApplication.translate("icp_step2", u"When Age", None))
        self.age_set_lbl.setText(QCoreApplication.translate("icp_step2", u"Set Attribute Scores", None))
        self.score_age4_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.age_combo.setItemText(0, QCoreApplication.translate("icp_step2", u"Between", None))
        self.age_combo.setItemText(1, QCoreApplication.translate("icp_step2", u"Is Greater Than", None))
        self.age_combo.setItemText(2, QCoreApplication.translate("icp_step2", u"Is Less Than", None))

        self.age_combo.setCurrentText(QCoreApplication.translate("icp_step2", u"Between", None))
        self.less_lbl.setText(QCoreApplication.translate("icp_step2", u"Less Than", None))
        self.when_age2_lbl.setText(QCoreApplication.translate("icp_step2", u"When Age", None))
        self.score_age1_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.when_age3_lbl.setText(QCoreApplication.translate("icp_step2", u"When Age", None))
        self.second_lbl.setText(QCoreApplication.translate("icp_step2", u"45", None))
        self.greater_lbl.setText(QCoreApplication.translate("icp_step2", u"Greater Than", None))
        self.age1_lbl.setText(QCoreApplication.translate("icp_step2", u"10", None))
        self.when_age1_lbl.setText(QCoreApplication.translate("icp_step2", u"When Age", None))
        self.score_age2_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.third_lbl.setText(QCoreApplication.translate("icp_step2", u"20", None))
        self.score_age3_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.first_lbl.setText(QCoreApplication.translate("icp_step2", u"20 & 45", None))
        self.industry_set_attribute_lbl.setText(QCoreApplication.translate("icp_step2", u"Set Attribute Scores", None))
        self.when_industry1_lbl.setText(QCoreApplication.translate("icp_step2", u"When Industry", None))
        self.industry_contains_lbl.setText(QCoreApplication.translate("icp_step2", u"Contains", None))
        self.industry_random_lbl.setText(QCoreApplication.translate("icp_step2", u"IT Field", None))
        self.score_industry1_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.industry1_lbl.setText(QCoreApplication.translate("icp_step2", u"15", None))
        self.when_industry2_lbl.setText(QCoreApplication.translate("icp_step2", u"When Industry", None))
        self.industry_other_lbl.setText(QCoreApplication.translate("icp_step2", u"Has Other Value", None))
        self.score_industry2_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.industry2_lbl.setText(QCoreApplication.translate("icp_step2", u"12", None))
        self.when_religion3_lbl_2.setText(QCoreApplication.translate("icp_step2", u"When Industry", None))
        self.industry_combo.setItemText(0, QCoreApplication.translate("icp_step2", u"Contains", None))
        self.industry_combo.setItemText(1, QCoreApplication.translate("icp_step2", u"Has Other Value", None))

        self.industry_combo.setCurrentText(QCoreApplication.translate("icp_step2", u"Contains", None))
        self.industry_line.setText("")
        self.score_industry3_lbl.setText(QCoreApplication.translate("icp_step2", u"Score=", None))
        self.step2_save_btn.setText(QCoreApplication.translate("icp_step2", u"Save", None))
    # retranslateUi

