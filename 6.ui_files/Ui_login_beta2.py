# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\datacode\6.ui_files\login_beta2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(410, 347)
        font = QtGui.QFont()
        font.setPointSize(18)
        Form.setFont(font)
        self.account_label = QtWidgets.QLabel(Form)
        self.account_label.setGeometry(QtCore.QRect(80, 130, 171, 31))
        self.account_label.setObjectName("account_label")
        self.welcome_label = QtWidgets.QLabel(Form)
        self.welcome_label.setGeometry(QtCore.QRect(70, 50, 271, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(25)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        self.account_lineEdit = QtWidgets.QLineEdit(Form)
        self.account_lineEdit.setGeometry(QtCore.QRect(170, 130, 161, 30))
        self.account_lineEdit.setObjectName("account_lineEdit")
        self.passwd_lineEdit = QtWidgets.QLineEdit(Form)
        self.passwd_lineEdit.setGeometry(QtCore.QRect(170, 180, 161, 30))
        self.passwd_lineEdit.setObjectName("passwd_lineEdit")
        self.passwd_label = QtWidgets.QLabel(Form)
        self.passwd_label.setGeometry(QtCore.QRect(80, 180, 171, 31))
        self.passwd_label.setObjectName("passwd_label")
        self.login_btn = QtWidgets.QPushButton(Form)
        self.login_btn.setGeometry(QtCore.QRect(50, 250, 91, 31))
        self.login_btn.setObjectName("login_btn")
        self.register_btn = QtWidgets.QPushButton(Form)
        self.register_btn.setGeometry(QtCore.QRect(160, 250, 91, 31))
        self.register_btn.setObjectName("register_btn")
        self.quit_btn = QtWidgets.QPushButton(Form)
        self.quit_btn.setGeometry(QtCore.QRect(270, 250, 91, 31))
        self.quit_btn.setObjectName("quit_btn")
        self.version_label = QtWidgets.QLabel(Form)
        self.version_label.setGeometry(QtCore.QRect(280, 310, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.version_label.setFont(font)
        self.version_label.setObjectName("version_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.account_lineEdit, self.passwd_lineEdit)
        Form.setTabOrder(self.passwd_lineEdit, self.login_btn)
        Form.setTabOrder(self.login_btn, self.register_btn)
        Form.setTabOrder(self.register_btn, self.quit_btn)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "login_window"))
        self.account_label.setText(_translate("Form", "帐  号："))
        self.welcome_label.setText(_translate("Form", "员工信息管理系统"))
        self.passwd_label.setText(_translate("Form", "密  码："))
        self.login_btn.setText(_translate("Form", "登  陆"))
        self.register_btn.setText(_translate("Form", "注  册"))
        self.quit_btn.setText(_translate("Form", "退  出"))
        self.version_label.setText(_translate("Form", "版本：beta2 20200418"))
