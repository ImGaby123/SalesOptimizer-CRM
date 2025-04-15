# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'step1.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_icp_step1(object):
    def setupUi(self, icp_step1):
        if not icp_step1.objectName():
            icp_step1.setObjectName(u"icp_step1")
        icp_step1.resize(750, 510)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(icp_step1.sizePolicy().hasHeightForWidth())
        icp_step1.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(icp_step1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.choose_lbl = QLabel(icp_step1)
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

        self.instruction2_lbl = QLabel(icp_step1)
        self.instruction2_lbl.setObjectName(u"instruction2_lbl")
        sizePolicy1.setHeightForWidth(self.instruction2_lbl.sizePolicy().hasHeightForWidth())
        self.instruction2_lbl.setSizePolicy(sizePolicy1)
        self.instruction2_lbl.setWordWrap(True)

        self.gridLayout.addWidget(self.instruction2_lbl, 3, 0, 1, 1)

        self.step1_lbl = QLabel(icp_step1)
        self.step1_lbl.setObjectName(u"step1_lbl")
        sizePolicy1.setHeightForWidth(self.step1_lbl.sizePolicy().hasHeightForWidth())
        self.step1_lbl.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(10)
        self.step1_lbl.setFont(font1)

        self.gridLayout.addWidget(self.step1_lbl, 1, 0, 1, 1)

        self.instruction1_lbl = QLabel(icp_step1)
        self.instruction1_lbl.setObjectName(u"instruction1_lbl")
        sizePolicy1.setHeightForWidth(self.instruction1_lbl.sizePolicy().hasHeightForWidth())
        self.instruction1_lbl.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.instruction1_lbl, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.define_btn = QPushButton(icp_step1)
        self.define_btn.setObjectName(u"define_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.define_btn.sizePolicy().hasHeightForWidth())
        self.define_btn.setSizePolicy(sizePolicy2)
        self.define_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.define_btn.setStyleSheet(u"background-color: blue;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.define_btn)


        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.attribute_tbl = QTableWidget(icp_step1)
        if (self.attribute_tbl.columnCount() < 3):
            self.attribute_tbl.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.attribute_tbl.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.attribute_tbl.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.attribute_tbl.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.attribute_tbl.rowCount() < 6):
            self.attribute_tbl.setRowCount(6)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.attribute_tbl.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.attribute_tbl.setItem(0, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.attribute_tbl.setItem(0, 2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.attribute_tbl.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.attribute_tbl.setItem(1, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.attribute_tbl.setItem(1, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.attribute_tbl.setItem(2, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.attribute_tbl.setItem(2, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.attribute_tbl.setItem(2, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.attribute_tbl.setItem(3, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.attribute_tbl.setItem(3, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.attribute_tbl.setItem(3, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.attribute_tbl.setItem(4, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.attribute_tbl.setItem(4, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.attribute_tbl.setItem(4, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.attribute_tbl.setItem(5, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.attribute_tbl.setItem(5, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.attribute_tbl.setItem(5, 2, __qtablewidgetitem20)
        self.attribute_tbl.setObjectName(u"attribute_tbl")
        self.attribute_tbl.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.attribute_tbl.sizePolicy().hasHeightForWidth())
        self.attribute_tbl.setSizePolicy(sizePolicy3)
        self.attribute_tbl.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.attribute_tbl.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.attribute_tbl.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.attribute_tbl.setGridStyle(Qt.PenStyle.SolidLine)
        self.attribute_tbl.setWordWrap(True)
        self.attribute_tbl.setCornerButtonEnabled(True)
        self.attribute_tbl.setRowCount(6)
        self.attribute_tbl.setColumnCount(3)

        self.verticalLayout.addWidget(self.attribute_tbl)

        self.add_combo = QComboBox(icp_step1)
        self.add_combo.setObjectName(u"add_combo")
        sizePolicy1.setHeightForWidth(self.add_combo.sizePolicy().hasHeightForWidth())
        self.add_combo.setSizePolicy(sizePolicy1)
        self.add_combo.setAutoFillBackground(False)
        self.add_combo.setCurrentText(u"")

        self.verticalLayout.addWidget(self.add_combo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 2, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.assign_checkbox = QCheckBox(icp_step1)
        self.assign_checkbox.setObjectName(u"assign_checkbox")
        sizePolicy1.setHeightForWidth(self.assign_checkbox.sizePolicy().hasHeightForWidth())
        self.assign_checkbox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.assign_checkbox)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 5, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.total_attributes_lbl = QLabel(icp_step1)
        self.total_attributes_lbl.setObjectName(u"total_attributes_lbl")
        sizePolicy2.setHeightForWidth(self.total_attributes_lbl.sizePolicy().hasHeightForWidth())
        self.total_attributes_lbl.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.total_attributes_lbl)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.total_lbl = QLabel(icp_step1)
        self.total_lbl.setObjectName(u"total_lbl")
        sizePolicy2.setHeightForWidth(self.total_lbl.sizePolicy().hasHeightForWidth())
        self.total_lbl.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.total_lbl)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)


        self.retranslateUi(icp_step1)

        QMetaObject.connectSlotsByName(icp_step1)
    # setupUi

    def retranslateUi(self, icp_step1):
        icp_step1.setWindowTitle(QCoreApplication.translate("icp_step1", u"ICP Step 1", None))
        self.choose_lbl.setText(QCoreApplication.translate("icp_step1", u"Choose Lead Quality Attributes", None))
        self.instruction2_lbl.setText(QCoreApplication.translate("icp_step1", u"attribute and also indicate if it is mandatory for an attribute to have a value to calculate a quality score of a lead.", None))
        self.step1_lbl.setText(QCoreApplication.translate("icp_step1", u"Create Lead Quality Criteria, Step 1 of 2...	", None))
        self.instruction1_lbl.setText(QCoreApplication.translate("icp_step1", u"Choose attributes of lead which can potentially  define the quality of lead. You may choose to provide different weightage of each", None))
        self.define_btn.setText(QCoreApplication.translate("icp_step1", u"Define Attribute Score>", None))
        ___qtablewidgetitem = self.attribute_tbl.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("icp_step1", u"Attribute", None));
        ___qtablewidgetitem1 = self.attribute_tbl.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("icp_step1", u"Is Mandatory", None));
        ___qtablewidgetitem2 = self.attribute_tbl.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("icp_step1", u"Weightage(%)", None));

        __sortingEnabled = self.attribute_tbl.isSortingEnabled()
        self.attribute_tbl.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.attribute_tbl.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("icp_step1", u"City", None));
        ___qtablewidgetitem4 = self.attribute_tbl.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("icp_step1", u"Yes", None));
        ___qtablewidgetitem5 = self.attribute_tbl.item(0, 2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("icp_step1", u"15", None));
        ___qtablewidgetitem6 = self.attribute_tbl.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("icp_step1", u"Region", None));
        ___qtablewidgetitem7 = self.attribute_tbl.item(1, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("icp_step1", u"No", None));
        ___qtablewidgetitem8 = self.attribute_tbl.item(1, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("icp_step1", u"15", None));
        ___qtablewidgetitem9 = self.attribute_tbl.item(2, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("icp_step1", u"Country", None));
        ___qtablewidgetitem10 = self.attribute_tbl.item(2, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("icp_step1", u"Yes", None));
        ___qtablewidgetitem11 = self.attribute_tbl.item(2, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("icp_step1", u"15", None));
        ___qtablewidgetitem12 = self.attribute_tbl.item(3, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("icp_step1", u"Profession", None));
        ___qtablewidgetitem13 = self.attribute_tbl.item(3, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("icp_step1", u"Yes", None));
        ___qtablewidgetitem14 = self.attribute_tbl.item(3, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("icp_step1", u"20", None));
        ___qtablewidgetitem15 = self.attribute_tbl.item(4, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("icp_step1", u"Age", None));
        ___qtablewidgetitem16 = self.attribute_tbl.item(4, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("icp_step1", u"No", None));
        ___qtablewidgetitem17 = self.attribute_tbl.item(4, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("icp_step1", u"15", None));
        ___qtablewidgetitem18 = self.attribute_tbl.item(5, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("icp_step1", u"Industry", None));
        ___qtablewidgetitem19 = self.attribute_tbl.item(5, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("icp_step1", u"Yes", None));
        ___qtablewidgetitem20 = self.attribute_tbl.item(5, 2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("icp_step1", u"20", None));
        self.attribute_tbl.setSortingEnabled(__sortingEnabled)

        self.add_combo.setPlaceholderText(QCoreApplication.translate("icp_step1", u"-- Add Lead Attribute --", None))
        self.assign_checkbox.setText(QCoreApplication.translate("icp_step1", u"Assign weightage equally across the attributes", None))
        self.total_attributes_lbl.setText(QCoreApplication.translate("icp_step1", u"6 Attributes", None))
        self.total_lbl.setText(QCoreApplication.translate("icp_step1", u"100", None))
    # retranslateUi

