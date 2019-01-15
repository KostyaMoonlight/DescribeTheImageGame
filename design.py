# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 582)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.OpenImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenImageButton.setMinimumSize(QtCore.QSize(0, 200))
        self.OpenImageButton.setIconSize(QtCore.QSize(40, 40))
        self.OpenImageButton.setObjectName("OpenImageButton")
        self.verticalLayout.addWidget(self.OpenImageButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_w = QtWidgets.QLabel(self.centralwidget)
        self.label_w.setObjectName("label_w")
        self.horizontalLayout.addWidget(self.label_w)
        self.spinBox_w = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_w.setProperty("value", 4)
        self.spinBox_w.setObjectName("spinBox_w")
        self.horizontalLayout.addWidget(self.spinBox_w)
        self.label_h = QtWidgets.QLabel(self.centralwidget)
        self.label_h.setObjectName("label_h")
        self.horizontalLayout.addWidget(self.label_h)
        self.spinBox_h = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_h.setProperty("value", 5)
        self.spinBox_h.setObjectName("spinBox_h")
        self.horizontalLayout.addWidget(self.spinBox_h)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_size = QtWidgets.QLabel(self.centralwidget)
        self.label_size.setObjectName("label_size")
        self.horizontalLayout_2.addWidget(self.label_size)
        self.newSize = QtWidgets.QLineEdit(self.centralwidget)
        self.newSize.setObjectName("newSize")
        self.horizontalLayout_2.addWidget(self.newSize)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.StartGameButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartGameButton.setMinimumSize(QtCore.QSize(0, 200))
        self.StartGameButton.setObjectName("StartGameButton")
        self.verticalLayout.addWidget(self.StartGameButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Solve Image"))
        self.OpenImageButton.setText(_translate("MainWindow", "Open image"))
        self.label_w.setText(_translate("MainWindow", "W:"))
        self.label_h.setText(_translate("MainWindow", "H:"))
        self.label_size.setText(_translate("MainWindow", "Size:"))
        self.StartGameButton.setText(_translate("MainWindow", "Start game"))

