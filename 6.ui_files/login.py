# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pythoncode\6.ui_files\e.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import register


class Ui_Form2(QWidget):
    def __init__(self):
        super().__init__()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(514, 410)
        font = QtGui.QFont()
        font.setPointSize(18)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\pythoncode\\.vscode/ljp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(130, 50, 261, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(30)
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
        self.passwd_label.setGeometry(QtCore.QRect(90, 235, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.passwd_label.setFont(font)
        self.passwd_label.setObjectName("passwd_label")
        self.user = QtWidgets.QLineEdit(Form)
        self.user.setGeometry(QtCore.QRect(210, 150, 200, 30))
        self.user.setObjectName("user")
        self.passwd = QtWidgets.QLineEdit(Form)
        self.passwd.setGeometry(QtCore.QRect(210, 240, 200, 30))
        self.passwd.setObjectName("passwd")
        self.register_button = QtWidgets.QPushButton(Form)
        self.register_button.setGeometry(QtCore.QRect(90, 325, 101, 31))
        self.register_button.setObjectName("register_button")
        self.exit_button = QtWidgets.QPushButton(Form)
        self.exit_button.setGeometry(QtCore.QRect(310, 325, 101, 31))
        self.exit_button.setObjectName("exit_button")
        self.login_button = QtWidgets.QPushButton(Form)
        self.login_button.setGeometry(QtCore.QRect(200, 325, 101, 31))
        self.login_button.setObjectName("login_button")

        # 信号槽的建立
        self.user.returnPressed.connect(self.record)
        self.passwd.returnPressed.connect(self.record)
        self.login_button.clicked.connect(self.record)

        # 转向注册页面
        self.register_button.clicked.connect(self.goto_register)




        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def record(self):
        pass
    def goto_register(self):
        print('从登陆跳转到注册页面')
        
        self.ui = register.Ui_Form()
        self.ui.setupUi(self.ui)
        self.ui.show()
        self.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "milkbottle"))
        self.title.setText(_translate("Form", "员工信息管理"))
        self.user_label.setText(_translate("Form", "帐    号"))
        self.passwd_label.setText(_translate("Form", "密    码"))
        self.register_button.setText(_translate("Form", "注   册"))
        self.exit_button.setText(_translate("Form", "退   出"))
        self.login_button.setText(_translate("Form", "登   陆"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui2 = Ui_Form2()
    ui2.setupUi(ui2)
    # my_window.show()
    ui2.show()
    sys.exit(app.exec_())