# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\datacode\6.ui_files\del_beta3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(456, 347)
        self.title_label = QtWidgets.QLabel(Form)
        self.title_label.setGeometry(QtCore.QRect(150, 60, 251, 51))
        font = QtGui.QFont()
        font.setFamily("方正大黑简体")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.user_label = QtWidgets.QLabel(Form)
        self.user_label.setGeometry(QtCore.QRect(100, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(Form)
        self.user_lineEdit.setGeometry(QtCore.QRect(212, 150, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.ip_lineEdit = QtWidgets.QLineEdit(Form)
        self.ip_lineEdit.setGeometry(QtCore.QRect(210, 200, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_lineEdit.setFont(font)
        self.ip_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ip_lineEdit.setObjectName("ip_lineEdit")
        self.ip_label = QtWidgets.QLabel(Form)
        self.ip_label.setGeometry(QtCore.QRect(98, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName("ip_label")
        self.del_btn = QtWidgets.QPushButton(Form)
        self.del_btn.setGeometry(QtCore.QRect(95, 260, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.del_btn.setFont(font)
        self.del_btn.setObjectName("del_btn")
        self.reset_btn = QtWidgets.QPushButton(Form)
        self.reset_btn.setGeometry(QtCore.QRect(195, 260, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("reset_btn")
        self.quit_btn = QtWidgets.QPushButton(Form)
        self.quit_btn.setGeometry(QtCore.QRect(295, 260, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        self.tip_label = QtWidgets.QLabel(Form)
        self.tip_label.setGeometry(QtCore.QRect(170, 110, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tip_label.setFont(font)
        self.tip_label.setObjectName("tip_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title_label.setText(_translate("Form", "删除员工信息"))
        self.user_label.setText(_translate("Form", "姓    名："))
        self.ip_label.setText(_translate("Form", "IP 地 址："))
        self.del_btn.setText(_translate("Form", "删  除"))
        self.reset_btn.setText(_translate("Form", "重  置"))
        self.quit_btn.setText(_translate("Form", "退  出"))
        self.tip_label.setText(_translate("Form", "通过使用人或者IP删除信息"))
