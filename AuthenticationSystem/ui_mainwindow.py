# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMdiArea, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 617)
        self.actioncenter = QAction(MainWindow)
        self.actioncenter.setObjectName(u"actioncenter")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")
        self.mdiArea.setGeometry(QRect(0, 0, 801, 561))
        self.left_subwindow = QWidget()
        self.left_subwindow.setObjectName(u"left_subwindow")
        self.mdiArea.addSubWindow(self.left_subwindow)
        self.center_subwindow = QWidget()
        self.center_subwindow.setObjectName(u"center_subwindow")
        self.mdiArea.addSubWindow(self.center_subwindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 797, 21))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        self.menuleft = QMenu(self.menufile)
        self.menuleft.setObjectName(u"menuleft")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menufile.menuAction())
        self.menufile.addAction(self.menuleft.menuAction())
        self.menuleft.addAction(self.actioncenter)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actioncenter.setText(QCoreApplication.translate("MainWindow", u"center", None))
        self.left_subwindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Subwindow", None))
        self.center_subwindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Subwindow", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file", None))
        self.menuleft.setTitle(QCoreApplication.translate("MainWindow", u"left", None))
    # retranslateUi

