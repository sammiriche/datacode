# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pythoncode\6.ui_files\add_beta1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui,QtCore,QtSql
from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication,QGridLayout,QDialog
from PyQt5.QtWidgets import QGroupBox,QVBoxLayout,QHBoxLayout,QTableView
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import *

class add_em(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 405)
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setGeometry(QtCore.QRect(40, 95, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 90, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 150, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 210, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 270, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.dept_label = QtWidgets.QLabel(Dialog)
        self.dept_label.setGeometry(QtCore.QRect(40, 155, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dept_label.setFont(font)
        self.dept_label.setObjectName("dept_label")
        self.ip_label = QtWidgets.QLabel(Dialog)
        self.ip_label.setGeometry(QtCore.QRect(40, 215, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName("ip_label")
        self.mac_label = QtWidgets.QLabel(Dialog)
        self.mac_label.setGeometry(QtCore.QRect(40, 275, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mac_label.setFont(font)
        self.mac_label.setObjectName("mac_label")
        self.enter_button = QtWidgets.QPushButton(Dialog)
        self.enter_button.setGeometry(QtCore.QRect(50, 320, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enter_button.setFont(font)
        self.enter_button.setObjectName("enter_button")
        self.cancle_button = QtWidgets.QPushButton(Dialog)
        self.cancle_button.setGeometry(QtCore.QRect(170, 320, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancle_button.setFont(font)
        self.cancle_button.setObjectName("cancle_button")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(80, 30, 181, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.name_label.setText(_translate("Dialog", "姓  名："))
        self.dept_label.setText(_translate("Dialog", "部  门："))
        self.ip_label.setText(_translate("Dialog", "IP地址："))
        self.mac_label.setText(_translate("Dialog", "MAC地址："))
        self.enter_button.setText(_translate("Dialog", "确  认"))
        self.cancle_button.setText(_translate("Dialog", "取  消"))
        self.title.setText(_translate("Dialog", "添加员工信息"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ae = add_em()
    ae.setupUi(ae)
    ae.show()
    sys.exit(app.exec_())