# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pythoncode\6.ui_files\register_beta1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(514, 410)
        font = QtGui.QFont()
        font.setPointSize(18)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\pythoncode\\6.ui_files\\../.vscode/ljp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(160, 50, 201, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(22)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.user_label = QtWidgets.QLabel(Form)
        self.user_label.setGeometry(QtCore.QRect(90, 145, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.passwd_label = QtWidgets.QLabel(Form)
        self.passwd_label.setEnabled(True)
        self.passwd_label.setGeometry(QtCore.QRect(90, 205, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.passwd_label.setFont(font)
        self.passwd_label.setObjectName("passwd_label")
        self.confirm_label = QtWidgets.QLabel(Form)
        self.confirm_label.setGeometry(QtCore.QRect(90, 265, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.confirm_label.setFont(font)
        self.confirm_label.setObjectName("confirm_label")
        self.user = QtWidgets.QLineEdit(Form)
        self.user.setGeometry(QtCore.QRect(210, 150, 200, 30))
        self.user.setObjectName("user")
        self.passwd = QtWidgets.QLineEdit(Form)
        self.passwd.setGeometry(QtCore.QRect(210, 210, 200, 30))
        self.passwd.setObjectName("passwd")
        self.confirm = QtWidgets.QLineEdit(Form)
        self.confirm.setGeometry(QtCore.QRect(210, 270, 200, 30))
        self.confirm.setObjectName("confirm")
        self.register_button = QtWidgets.QPushButton(Form)
        self.register_button.setGeometry(QtCore.QRect(90, 325, 101, 31))
        self.register_button.setObjectName("register_button")
        self.re_login = QtWidgets.QPushButton(Form)
        self.re_login.setGeometry(QtCore.QRect(240, 325, 161, 30))
        self.re_login.setObjectName("re_login")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "milkbottle"))
        self.title.setText(_translate("Form", "帐号注册beta1"))
        self.user_label.setText(_translate("Form", "帐    号"))
        self.passwd_label.setText(_translate("Form", "密    码"))
        self.confirm_label.setText(_translate("Form", "确认密码"))
        self.register_button.setText(_translate("Form", "注  册"))
        self.re_login.setText(_translate("Form", "返回登录界面"))
