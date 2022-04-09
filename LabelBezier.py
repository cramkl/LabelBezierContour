# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LabelBezier.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(988, 738)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFile.setGeometry(QtCore.QRect(710, 30, 112, 34))
        self.OpenFile.setObjectName("OpenFile")
        self.ImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.ImageLabel.setGeometry(QtCore.QRect(10, 20, 640, 480))
        self.ImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.ImageLabel.setText("")
        self.ImageLabel.setObjectName("ImageLabel")
        self.LabelButton = QtWidgets.QPushButton(self.centralwidget)
        self.LabelButton.setGeometry(QtCore.QRect(710, 110, 111, 41))
        self.LabelButton.setObjectName("LabelButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 988, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LabelBezier"))
        self.OpenFile.setText(_translate("MainWindow", "Open File"))
        self.LabelButton.setText(_translate("MainWindow", "Label"))

