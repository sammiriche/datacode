# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\datacode\ui_files\a.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dd = QtWidgets.QPushButton(self.centralwidget)
        self.dd.setGeometry(QtCore.QRect(100, 200, 75, 23))
        self.dd.setObjectName("dd")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dd.setText(_translate("MainWindow", "PushButton"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Ui_MainWindow()
    w.setupUi(QMainWindow())
    w.show()
    sys.exit(app.exec_())