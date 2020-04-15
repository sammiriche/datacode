# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pythoncode\6.ui_files\first_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys

class First_view(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 722) # 主窗口尺寸
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.my_view = QtWidgets.QTableView(self.centralwidget)
        self.my_view.setGeometry(QtCore.QRect(225, 71, 681, 611))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.my_view.setFont(font)
        self.my_view.setShowGrid(True)
        self.my_view.setSortingEnabled(False)
        self.my_view.setObjectName("my_view")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 130, 111, 291))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.show_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.show_button.setFont(font)
        self.show_button.setObjectName("show_button")
        self.verticalLayout.addWidget(self.show_button)
        self.add_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.verticalLayout.addWidget(self.add_button)
        self.del_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.del_button.setFont(font)
        self.del_button.setObjectName("del_button")
        self.verticalLayout.addWidget(self.del_button)
        self.modify_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modify_button.setFont(font)
        self.modify_button.setObjectName("modify_button")
        self.verticalLayout.addWidget(self.modify_button)
        self.query_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.query_button.setFont(font)
        self.query_button.setObjectName("query_button")
        self.verticalLayout.addWidget(self.query_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 23))
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
        self.show_button.setText(_translate("MainWindow", "显示所有员工"))
        self.add_button.setText(_translate("MainWindow", "添加员工信息"))
        self.del_button.setText(_translate("MainWindow", "删除员工信息"))
        self.modify_button.setText(_translate("MainWindow", "修改员工信息"))
        self.query_button.setText(_translate("MainWindow", "查询员工信息"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fv = First_view()
    fv.setupUi(fv)
    fv.show()
    sys.exit(app.exec_())