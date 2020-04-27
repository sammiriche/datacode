# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pythoncode\6.ui_files\login_beta3.ui'
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
        self.title_label.setGeometry(QtCore.QRect(130, 60, 251, 51))
        font = QtGui.QFont()
        font.setFamily("方正大黑简体")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.account_label = QtWidgets.QLabel(Form)
        self.account_label.setGeometry(QtCore.QRect(100, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.account_label.setFont(font)
        self.account_label.setObjectName("account_label")
        self.account_lineEdit = QtWidgets.QLineEdit(Form)
        self.account_lineEdit.setGeometry(QtCore.QRect(212, 150, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.account_lineEdit.setFont(font)
        self.account_lineEdit.setObjectName("account_lineEdit")
        self.passwd_lineEdit = QtWidgets.QLineEdit(Form)
        self.passwd_lineEdit.setGeometry(QtCore.QRect(210, 200, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.passwd_lineEdit.setFont(font)
        self.passwd_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd_lineEdit.setObjectName("passwd_lineEdit")
        self.passwd_label = QtWidgets.QLabel(Form)
        self.passwd_label.setGeometry(QtCore.QRect(98, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.passwd_label.setFont(font)
        self.passwd_label.setObjectName("passwd_label")
        self.register_btn = QtWidgets.QPushButton(Form)
        self.register_btn.setGeometry(QtCore.QRect(95, 260, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_btn.setFont(font)
        self.register_btn.setObjectName("register_btn")
        self.login_btn = QtWidgets.QPushButton(Form)
        self.login_btn.setGeometry(QtCore.QRect(195, 260, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName("login_btn")
        self.quit_btn = QtWidgets.QPushButton(Form)
        self.quit_btn.setGeometry(QtCore.QRect(295, 260, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        self.version_label = QtWidgets.QLabel(Form)
        self.version_label.setGeometry(QtCore.QRect(280, 320, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.version_label.setFont(font)
        self.version_label.setObjectName("version_label")
        self.config_lineEdit = QtWidgets.QLineEdit(Form)
        self.config_lineEdit.setGeometry(QtCore.QRect(100, 320, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.config_lineEdit.setFont(font)
        self.config_lineEdit.setObjectName("config_lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title_label.setText(_translate("Form", "员工信息管理系统"))
        self.account_label.setText(_translate("Form", "帐    号："))
        self.passwd_label.setText(_translate("Form", "密    码："))
        self.register_btn.setText(_translate("Form", "注  册"))
        self.login_btn.setText(_translate("Form", "登  录"))
        self.quit_btn.setText(_translate("Form", "退  出"))
        self.version_label.setText(_translate("Form", "version:beta3 20200426"))
        self.config_lineEdit.setText(_translate("Form", "192.168.10.1:18080"))
