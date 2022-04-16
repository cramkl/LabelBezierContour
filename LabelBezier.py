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
        MainWindow.resize(1080, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFile.setGeometry(QtCore.QRect(690, 30, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.OpenFile.setFont(font)
        self.OpenFile.setObjectName("OpenFile")
        self.ImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.ImageLabel.setGeometry(QtCore.QRect(10, 30, 640, 480))
        self.ImageLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.ImageLabel.setText("")
        self.ImageLabel.setObjectName("ImageLabel")
        self.LabelButton = QtWidgets.QPushButton(self.centralwidget)
        self.LabelButton.setEnabled(True)
        self.LabelButton.setGeometry(QtCore.QRect(750, 200, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.LabelButton.setFont(font)
        self.LabelButton.setObjectName("LabelButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(False)
        self.groupBox.setGeometry(QtCore.QRect(690, 160, 341, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.OpenFolder = QtWidgets.QPushButton(self.centralwidget)
        self.OpenFolder.setGeometry(QtCore.QRect(870, 30, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.OpenFolder.setFont(font)
        self.OpenFolder.setObjectName("OpenFolder")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(690, 350, 341, 211))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.ControlPointList = QtWidgets.QListWidget(self.groupBox_2)
        self.ControlPointList.setGeometry(QtCore.QRect(10, 30, 321, 161))
        self.ControlPointList.setObjectName("ControlPointList")
        self.LabelDone = QtWidgets.QPushButton(self.centralwidget)
        self.LabelDone.setGeometry(QtCore.QRect(870, 200, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.LabelDone.setFont(font)
        self.LabelDone.setObjectName("LabelDone")
        self.LabelReset = QtWidgets.QPushButton(self.centralwidget)
        self.LabelReset.setGeometry(QtCore.QRect(750, 260, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.LabelReset.setFont(font)
        self.LabelReset.setObjectName("LabelReset")
        self.LabelSave = QtWidgets.QPushButton(self.centralwidget)
        self.LabelSave.setGeometry(QtCore.QRect(870, 260, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.LabelSave.setFont(font)
        self.LabelSave.setObjectName("LabelSave")
        self.OpenNext = QtWidgets.QPushButton(self.centralwidget)
        self.OpenNext.setGeometry(QtCore.QRect(870, 100, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.OpenNext.setFont(font)
        self.OpenNext.setObjectName("OpenNext")
        self.LabelPrevious = QtWidgets.QPushButton(self.centralwidget)
        self.LabelPrevious.setGeometry(QtCore.QRect(690, 100, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.LabelPrevious.setFont(font)
        self.LabelPrevious.setObjectName("LabelPrevious")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 530, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.labelFileName = QtWidgets.QLabel(self.centralwidget)
        self.labelFileName.setGeometry(QtCore.QRect(180, 530, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelFileName.setFont(font)
        self.labelFileName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelFileName.setObjectName("labelFileName")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.OpenFile.raise_()
        self.ImageLabel.raise_()
        self.LabelButton.raise_()
        self.OpenFolder.raise_()
        self.LabelDone.raise_()
        self.LabelReset.raise_()
        self.LabelSave.raise_()
        self.OpenNext.raise_()
        self.LabelPrevious.raise_()
        self.label.raise_()
        self.labelFileName.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 30))
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
        self.LabelButton.setText(_translate("MainWindow", "Start"))
        self.groupBox.setTitle(_translate("MainWindow", "Label Action"))
        self.OpenFolder.setText(_translate("MainWindow", "Open Folder"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Control Points"))
        self.LabelDone.setText(_translate("MainWindow", "Done"))
        self.LabelReset.setText(_translate("MainWindow", "Reset"))
        self.LabelSave.setText(_translate("MainWindow", "Save"))
        self.OpenNext.setText(_translate("MainWindow", "Next"))
        self.LabelPrevious.setText(_translate("MainWindow", "Previous"))
        self.label.setText(_translate("MainWindow", "File Name :"))
        self.labelFileName.setText(_translate("MainWindow", "None"))

