# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\datacode\6.ui_files\del_em_beta2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 452)
        self.welcome_label = QtWidgets.QLabel(Dialog)
        self.welcome_label.setGeometry(QtCore.QRect(120, 60, 141, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(22)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        self.user_label = QtWidgets.QLabel(Dialog)
        self.user_label.setGeometry(QtCore.QRect(50, 203, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.user_lineEdit.setGeometry(QtCore.QRect(170, 210, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setText("")
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.ip_label = QtWidgets.QLabel(Dialog)
        self.ip_label.setGeometry(QtCore.QRect(50, 273, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName("ip_label")
        self.ip_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.ip_lineEdit.setGeometry(QtCore.QRect(170, 280, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_lineEdit.setFont(font)
        self.ip_lineEdit.setText("")
        self.ip_lineEdit.setObjectName("ip_lineEdit")
        self.confirm_label = QtWidgets.QPushButton(Dialog)
        self.confirm_label.setGeometry(QtCore.QRect(40, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.confirm_label.setFont(font)
        self.confirm_label.setObjectName("confirm_label")
        self.cancel_label = QtWidgets.QPushButton(Dialog)
        self.cancel_label.setGeometry(QtCore.QRect(150, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cancel_label.setFont(font)
        self.cancel_label.setObjectName("cancel_label")
        self.quit_label = QtWidgets.QPushButton(Dialog)
        self.quit_label.setGeometry(QtCore.QRect(260, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.quit_label.setFont(font)
        self.quit_label.setObjectName("quit_label")
        self.notice_label = QtWidgets.QLabel(Dialog)
        self.notice_label.setGeometry(QtCore.QRect(90, 150, 231, 16))
        self.notice_label.setObjectName("notice_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.welcome_label.setText(_translate("Dialog", "删 除 员 工"))
        self.user_label.setText(_translate("Dialog", "用户名称："))
        self.ip_label.setText(_translate("Dialog", "IP地址："))
        self.confirm_label.setText(_translate("Dialog", "确 认"))
        self.cancel_label.setText(_translate("Dialog", "取 消"))
        self.quit_label.setText(_translate("Dialog", "退 出"))
        self.notice_label.setText(_translate("Dialog", "提示：通过名称或者IP来删除用户信息"))
