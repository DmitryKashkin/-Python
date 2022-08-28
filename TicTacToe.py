# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TicTacToe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(201, 243)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionNew_Game = QAction(MainWindow)
        self.actionNew_Game.setObjectName(u"actionNew_Game")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_00 = QPushButton(self.centralwidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.pushButton_00)
        self.pushButton_00.setObjectName(u"pushButton_00")
        self.pushButton_00.setGeometry(QRect(20, 20, 51, 51))
        font = QFont()
        font.setPointSize(18)
        self.pushButton_00.setFont(font)
        self.pushButton_01 = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.pushButton_01)
        self.pushButton_01.setObjectName(u"pushButton_01")
        self.pushButton_01.setGeometry(QRect(70, 20, 51, 51))
        self.pushButton_01.setFont(font)
        self.pushButton_02 = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.pushButton_02)
        self.pushButton_02.setObjectName(u"pushButton_02")
        self.pushButton_02.setGeometry(QRect(120, 20, 51, 51))
        self.pushButton_02.setFont(font)
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.pushButton_10)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(20, 70, 51, 51))
        self.pushButton_10.setFont(font)
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.pushButton_11)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(70, 70, 51, 51))
        self.pushButton_11.setFont(font)
        self.pushButton_12 = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.pushButton_12)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(120, 70, 51, 51))
        self.pushButton_12.setFont(font)
        self.pushButton_22 = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.pushButton_22)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(120, 120, 51, 51))
        self.pushButton_22.setFont(font)
        self.pushButton_20 = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.pushButton_20)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(20, 120, 51, 51))
        self.pushButton_20.setFont(font)
        self.pushButton_21 = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.pushButton_21)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(70, 120, 51, 51))
        self.pushButton_21.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 201, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionNew_Game)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionNew_Game.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.pushButton_00.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_01.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_02.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

