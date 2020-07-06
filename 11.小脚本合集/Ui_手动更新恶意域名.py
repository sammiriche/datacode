# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pythoncode\20.利用python更新恶意域名\手动更新恶意域名.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(257, 493)
        self.add_list = QtWidgets.QPlainTextEdit(Dialog)
        self.add_list.setGeometry(QtCore.QRect(20, 70, 211, 351))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_list.setFont(font)
        self.add_list.setPlainText("")
        self.add_list.setObjectName("add_list")
        self.titel_label = QtWidgets.QLabel(Dialog)
        self.titel_label.setGeometry(QtCore.QRect(50, 30, 141, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.titel_label.setFont(font)
        self.titel_label.setObjectName("titel_label")
        self.import_btn = QtWidgets.QPushButton(Dialog)
        self.import_btn.setGeometry(QtCore.QRect(20, 430, 101, 23))
        self.import_btn.setObjectName("import_btn")
        self.update_btn = QtWidgets.QPushButton(Dialog)
        self.update_btn.setGeometry(QtCore.QRect(128, 430, 101, 23))
        self.update_btn.setObjectName("update_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.titel_label.setText(_translate("Dialog", "更新HOST文件"))
        self.import_btn.setText(_translate("Dialog", "从表格导入域名"))
        self.update_btn.setText(_translate("Dialog", "更新域名到hosts"))

