# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuLibrary = QMenu(self.menubar)
        self.menuLibrary.setObjectName(u"menuLibrary")
        self.menuLanguage_Base = QMenu(self.menubar)
        self.menuLanguage_Base.setObjectName(u"menuLanguage_Base")
        self.menuOutput_Settings = QMenu(self.menubar)
        self.menuOutput_Settings.setObjectName(u"menuOutput_Settings")
        self.menuCreate = QMenu(self.menubar)
        self.menuCreate.setObjectName(u"menuCreate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLibrary.menuAction())
        self.menubar.addAction(self.menuLanguage_Base.menuAction())
        self.menubar.addAction(self.menuOutput_Settings.menuAction())
        self.menubar.addAction(self.menuCreate.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuLibrary.setTitle(QCoreApplication.translate("MainWindow", u"Library", None))
        self.menuLanguage_Base.setTitle(QCoreApplication.translate("MainWindow", u"Language Base", None))
        self.menuOutput_Settings.setTitle(QCoreApplication.translate("MainWindow", u"Output Settings", None))
        self.menuCreate.setTitle(QCoreApplication.translate("MainWindow", u"Create", None))
    # retranslateUi

