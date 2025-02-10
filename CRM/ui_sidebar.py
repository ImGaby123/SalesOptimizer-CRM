# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(118, 765)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(30, 43, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.Page1Btn = QPushButton(self.frame)
        self.Page1Btn.setObjectName(u"Page1Btn")

        self.verticalLayout.addWidget(self.Page1Btn)

        self.verticalSpacer = QSpacerItem(20, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.Page2Btn = QPushButton(self.frame)
        self.Page2Btn.setObjectName(u"Page2Btn")

        self.verticalLayout.addWidget(self.Page2Btn)

        self.verticalSpacer_4 = QSpacerItem(20, 33, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.Page3Btn = QPushButton(self.frame)
        self.Page3Btn.setObjectName(u"Page3Btn")

        self.verticalLayout.addWidget(self.Page3Btn)

        self.verticalSpacer_6 = QSpacerItem(20, 32, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.Page4Btn = QPushButton(self.frame)
        self.Page4Btn.setObjectName(u"Page4Btn")

        self.verticalLayout.addWidget(self.Page4Btn)

        self.verticalSpacer_7 = QSpacerItem(20, 33, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.Page5Btn = QPushButton(self.frame)
        self.Page5Btn.setObjectName(u"Page5Btn")

        self.verticalLayout.addWidget(self.Page5Btn)

        self.verticalSpacer_8 = QSpacerItem(20, 33, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.Page6Btn = QPushButton(self.frame)
        self.Page6Btn.setObjectName(u"Page6Btn")

        self.verticalLayout.addWidget(self.Page6Btn)

        self.verticalSpacer_3 = QSpacerItem(20, 189, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.LogOutBtn = QPushButton(self.frame)
        self.LogOutBtn.setObjectName(u"LogOutBtn")

        self.verticalLayout.addWidget(self.LogOutBtn)

        self.verticalSpacer_5 = QSpacerItem(13, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignLeft)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 118, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Page1Btn.setText(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.Page2Btn.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.Page3Btn.setText(QCoreApplication.translate("MainWindow", u"Page 3", None))
        self.Page4Btn.setText(QCoreApplication.translate("MainWindow", u"Page 4", None))
        self.Page5Btn.setText(QCoreApplication.translate("MainWindow", u"Page 5", None))
        self.Page6Btn.setText(QCoreApplication.translate("MainWindow", u"Page 6", None))
        self.LogOutBtn.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
    # retranslateUi

