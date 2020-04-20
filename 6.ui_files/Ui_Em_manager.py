# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\datacode\6.ui_files\Em_manager.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 682)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.show_tableview = QtWidgets.QTableView(self.centralwidget)
        self.show_tableview.setGeometry(QtCore.QRect(190, 0, 681, 651))
        self.show_tableview.setObjectName("show_tableview")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(20, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.del_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_btn.setGeometry(QtCore.QRect(20, 200, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.del_btn.setFont(font)
        self.del_btn.setObjectName("del_btn")
        self.modify_btn = QtWidgets.QPushButton(self.centralwidget)
        self.modify_btn.setGeometry(QtCore.QRect(20, 280, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.modify_btn.setFont(font)
        self.modify_btn.setObjectName("modify_btn")
        self.query_btn = QtWidgets.QPushButton(self.centralwidget)
        self.query_btn.setGeometry(QtCore.QRect(20, 360, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.query_btn.setFont(font)
        self.query_btn.setObjectName("query_btn")
        self.quit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.quit_btn.setGeometry(QtCore.QRect(20, 440, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 23))
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
        self.add_btn.setText(_translate("MainWindow", "添加员工信息"))
        self.del_btn.setText(_translate("MainWindow", "删除员工信息"))
        self.modify_btn.setText(_translate("MainWindow", "修改员工信息"))
        self.query_btn.setText(_translate("MainWindow", "查询员工信息"))
        self.quit_btn.setText(_translate("MainWindow", "退 出系 统"))
