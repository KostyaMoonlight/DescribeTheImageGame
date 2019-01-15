# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/game_design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GameWindow(object):
    def setupUi(self, GameWindow):
        GameWindow.setObjectName("GameWindow")
        GameWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(GameWindow)
        self.centralwidget.setObjectName("centralwidget")
        GameWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GameWindow)
        self.statusbar.setObjectName("statusbar")
        GameWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GameWindow)
        QtCore.QMetaObject.connectSlotsByName(GameWindow)

    def retranslateUi(self, GameWindow):
        _translate = QtCore.QCoreApplication.translate
        GameWindow.setWindowTitle(_translate("GameWindow", "Game"))

