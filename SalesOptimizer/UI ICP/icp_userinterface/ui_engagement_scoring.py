# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'engagement_scoring.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_engagement_scoring(object):
    def setupUi(self, engagement_scoring):
        if not engagement_scoring.objectName():
            engagement_scoring.setObjectName(u"engagement_scoring")
        engagement_scoring.resize(750, 510)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(engagement_scoring.sizePolicy().hasHeightForWidth())
        engagement_scoring.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(engagement_scoring)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.definition_lbl = QLabel(engagement_scoring)
        self.definition_lbl.setObjectName(u"definition_lbl")
        sizePolicy.setHeightForWidth(self.definition_lbl.sizePolicy().hasHeightForWidth())
        self.definition_lbl.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.definition_lbl.setFont(font)

        self.verticalLayout.addWidget(self.definition_lbl)

        self.caption_lbl = QLabel(engagement_scoring)
        self.caption_lbl.setObjectName(u"caption_lbl")
        sizePolicy.setHeightForWidth(self.caption_lbl.sizePolicy().hasHeightForWidth())
        self.caption_lbl.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(10)
        self.caption_lbl.setFont(font1)

        self.verticalLayout.addWidget(self.caption_lbl)

        self.info1_lbl = QLabel(engagement_scoring)
        self.info1_lbl.setObjectName(u"info1_lbl")
        sizePolicy.setHeightForWidth(self.info1_lbl.sizePolicy().hasHeightForWidth())
        self.info1_lbl.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.info1_lbl)

        self.info2_lbl = QLabel(engagement_scoring)
        self.info2_lbl.setObjectName(u"info2_lbl")
        sizePolicy.setHeightForWidth(self.info2_lbl.sizePolicy().hasHeightForWidth())
        self.info2_lbl.setSizePolicy(sizePolicy)
        self.info2_lbl.setWordWrap(True)

        self.verticalLayout.addWidget(self.info2_lbl)

        self.info3_lbl = QLabel(engagement_scoring)
        self.info3_lbl.setObjectName(u"info3_lbl")

        self.verticalLayout.addWidget(self.info3_lbl)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lead_act_lbl = QLabel(engagement_scoring)
        self.lead_act_lbl.setObjectName(u"lead_act_lbl")
        sizePolicy.setHeightForWidth(self.lead_act_lbl.sizePolicy().hasHeightForWidth())
        self.lead_act_lbl.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.lead_act_lbl)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.act_lbl = QLabel(engagement_scoring)
        self.act_lbl.setObjectName(u"act_lbl")
        sizePolicy.setHeightForWidth(self.act_lbl.sizePolicy().hasHeightForWidth())
        self.act_lbl.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.act_lbl)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lead_stage_lbl = QLabel(engagement_scoring)
        self.lead_stage_lbl.setObjectName(u"lead_stage_lbl")
        sizePolicy.setHeightForWidth(self.lead_stage_lbl.sizePolicy().hasHeightForWidth())
        self.lead_stage_lbl.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.lead_stage_lbl)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.save_btn = QPushButton(engagement_scoring)
        self.save_btn.setObjectName(u"save_btn")
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        self.save_btn.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.save_btn)

        self.horizontalSpacer = QSpacerItem(500, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lead_act_combo = QComboBox(engagement_scoring)
        self.lead_act_combo.addItem("")
        self.lead_act_combo.addItem("")
        self.lead_act_combo.addItem("")
        self.lead_act_combo.addItem("")
        self.lead_act_combo.addItem("")
        self.lead_act_combo.addItem("")
        self.lead_act_combo.addItem("")
        self.lead_act_combo.addItem("")
        self.lead_act_combo.addItem("")
        self.lead_act_combo.addItem("")
        self.lead_act_combo.setObjectName(u"lead_act_combo")
        sizePolicy.setHeightForWidth(self.lead_act_combo.sizePolicy().hasHeightForWidth())
        self.lead_act_combo.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.lead_act_combo)

        self.horizontalSpacer_2 = QSpacerItem(500, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lead_stage_combo = QComboBox(engagement_scoring)
        self.lead_stage_combo.addItem("")
        self.lead_stage_combo.addItem("")
        self.lead_stage_combo.addItem("")
        self.lead_stage_combo.addItem("")
        self.lead_stage_combo.addItem("")
        self.lead_stage_combo.setObjectName(u"lead_stage_combo")
        sizePolicy.setHeightForWidth(self.lead_stage_combo.sizePolicy().hasHeightForWidth())
        self.lead_stage_combo.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.lead_stage_combo)

        self.horizontalSpacer_4 = QSpacerItem(500, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.act_spin = QSpinBox(engagement_scoring)
        self.act_spin.setObjectName(u"act_spin")
        sizePolicy.setHeightForWidth(self.act_spin.sizePolicy().hasHeightForWidth())
        self.act_spin.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.act_spin)

        self.horizontalSpacer_3 = QSpacerItem(500, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.retranslateUi(engagement_scoring)

        QMetaObject.connectSlotsByName(engagement_scoring)
    # setupUi

    def retranslateUi(self, engagement_scoring):
        engagement_scoring.setWindowTitle(QCoreApplication.translate("engagement_scoring", u"Engagement Scoring", None))
        self.definition_lbl.setText(QCoreApplication.translate("engagement_scoring", u"Engagement Scoring", None))
        self.caption_lbl.setText(QCoreApplication.translate("engagement_scoring", u"Manage how engagement score calculated ", None))
        self.info1_lbl.setText(QCoreApplication.translate("engagement_scoring", u"Engagement Score is calculated based on the recent activities of leads. Here, you can configure the number of days in which the activities", None))
        self.info2_lbl.setText(QCoreApplication.translate("engagement_scoring", u"should be considered. You can include/exclude which activities correalate to Engagement of leads. Also, you may want to measure", None))
        self.info3_lbl.setText(QCoreApplication.translate("engagement_scoring", u"engagement of leads which ae in certain lead stages, so that too can figure here.", None))
        self.lead_act_lbl.setText(QCoreApplication.translate("engagement_scoring", u"Lead Activities to include", None))
        self.act_lbl.setText(QCoreApplication.translate("engagement_scoring", u"Activity period (in days)", None))
        self.lead_stage_lbl.setText(QCoreApplication.translate("engagement_scoring", u"Lead Stage to include", None))
        self.save_btn.setText(QCoreApplication.translate("engagement_scoring", u"Save", None))
        self.lead_act_combo.setItemText(0, QCoreApplication.translate("engagement_scoring", u"1 Selected", None))
        self.lead_act_combo.setItemText(1, QCoreApplication.translate("engagement_scoring", u"2 Selected", None))
        self.lead_act_combo.setItemText(2, QCoreApplication.translate("engagement_scoring", u"3 Selected", None))
        self.lead_act_combo.setItemText(3, QCoreApplication.translate("engagement_scoring", u"4 Selected", None))
        self.lead_act_combo.setItemText(4, QCoreApplication.translate("engagement_scoring", u"5 Selected", None))
        self.lead_act_combo.setItemText(5, QCoreApplication.translate("engagement_scoring", u"6 Selected", None))
        self.lead_act_combo.setItemText(6, QCoreApplication.translate("engagement_scoring", u"7 Selected", None))
        self.lead_act_combo.setItemText(7, QCoreApplication.translate("engagement_scoring", u"8 Selected", None))
        self.lead_act_combo.setItemText(8, QCoreApplication.translate("engagement_scoring", u"9 Selected", None))
        self.lead_act_combo.setItemText(9, QCoreApplication.translate("engagement_scoring", u"10 Selected", None))

        self.lead_stage_combo.setItemText(0, QCoreApplication.translate("engagement_scoring", u"1 Selected", None))
        self.lead_stage_combo.setItemText(1, QCoreApplication.translate("engagement_scoring", u"2 Selected", None))
        self.lead_stage_combo.setItemText(2, QCoreApplication.translate("engagement_scoring", u"3 Selected", None))
        self.lead_stage_combo.setItemText(3, QCoreApplication.translate("engagement_scoring", u"4 Selected", None))
        self.lead_stage_combo.setItemText(4, QCoreApplication.translate("engagement_scoring", u"5 Selected", None))

    # retranslateUi

