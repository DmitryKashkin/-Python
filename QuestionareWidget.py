# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QuestionareWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_QuestionareWidget(object):
    def setupUi(self, QuestionareWidget):
        if not QuestionareWidget.objectName():
            QuestionareWidget.setObjectName(u"QuestionareWidget")
        QuestionareWidget.resize(500, 392)
        self.verticalLayout_5 = QVBoxLayout(QuestionareWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.splitter = QSplitter(QuestionareWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label)
        self.label_2 = QLabel(self.splitter)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_2)

        self.verticalLayout_5.addWidget(self.splitter)

        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(QuestionareWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.checkBox = QCheckBox(QuestionareWidget)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        self.checkBox.setFont(font2)
        self.checkBox.setAcceptDrops(False)
        self.checkBox.setIconSize(QSize(16, 16))
        self.checkBox.setTristate(False)

        self.horizontalLayout.addWidget(self.checkBox)

        self.horizontalSpacer_2 = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(QuestionareWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.checkBox_2 = QCheckBox(QuestionareWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setFont(font2)
        self.checkBox_2.setAcceptDrops(False)
        self.checkBox_2.setIconSize(QSize(16, 16))
        self.checkBox_2.setTristate(False)

        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.horizontalSpacer_4 = QSpacerItem(17, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(QuestionareWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(13, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.checkBox_3 = QCheckBox(QuestionareWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        self.checkBox_3.setFont(font2)
        self.checkBox_3.setAcceptDrops(False)
        self.checkBox_3.setIconSize(QSize(16, 16))
        self.checkBox_3.setTristate(False)

        self.horizontalLayout_3.addWidget(self.checkBox_3)

        self.horizontalSpacer_6 = QSpacerItem(13, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(QuestionareWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(13, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.checkBox_4 = QCheckBox(QuestionareWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)
        self.checkBox_4.setFont(font2)
        self.checkBox_4.setAcceptDrops(False)
        self.checkBox_4.setIconSize(QSize(16, 16))
        self.checkBox_4.setTristate(False)

        self.horizontalLayout_4.addWidget(self.checkBox_4)

        self.horizontalSpacer_8 = QSpacerItem(13, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 79, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.label_7 = QLabel(QuestionareWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_7)

        self.pushButton = QPushButton(QuestionareWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)
        self.pushButton.setFlat(False)

        self.verticalLayout_5.addWidget(self.pushButton)


        self.retranslateUi(QuestionareWidget)

        QMetaObject.connectSlotsByName(QuestionareWidget)
    # setupUi

    def retranslateUi(self, QuestionareWidget):
        QuestionareWidget.setWindowTitle(QCoreApplication.translate("QuestionareWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("QuestionareWidget", u"\u0412\u0435\u0447\u0435\u0440\u043d\u0438\u0439 \u043e\u043f\u0440\u043e\u0441", None))
        self.label_2.setText(QCoreApplication.translate("QuestionareWidget", u"\u041d\u0430\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043f\u043b\u043e\u0434\u043e\u0442\u0432\u043e\u0440\u043d\u043e \u043f\u0440\u043e\u0448\u0435\u043b \u0412\u0430\u0448 \u0434\u0435\u043d\u044c?", None))
        self.label_3.setText(QCoreApplication.translate("QuestionareWidget", u"\u0423\u0436\u0430\u0441\u043d\u043e", None))
        self.checkBox.setText(QCoreApplication.translate("QuestionareWidget", u"1", None))
        self.label_4.setText(QCoreApplication.translate("QuestionareWidget", u"\u0422\u0430\u043a \u0441\u0435\u0431\u0435", None))
        self.checkBox_2.setText(QCoreApplication.translate("QuestionareWidget", u"2", None))
        self.label_5.setText(QCoreApplication.translate("QuestionareWidget", u"\u041d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u043e", None))
        self.checkBox_3.setText(QCoreApplication.translate("QuestionareWidget", u"3", None))
        self.label_6.setText(QCoreApplication.translate("QuestionareWidget", u"\u041e\u0442\u043b\u0438\u0447\u043d\u043e", None))
        self.checkBox_4.setText(QCoreApplication.translate("QuestionareWidget", u"4", None))
        self.label_7.setText(QCoreApplication.translate("QuestionareWidget", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043e:", None))
        self.pushButton.setText(QCoreApplication.translate("QuestionareWidget", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

