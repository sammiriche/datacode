# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pythoncode\6.ui_files\d.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import login


class Ui_Form(QWidget):
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
        icon.addPixmap(QtGui.QPixmap("d:\\pythoncode\\.vscode\\ljp.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(180, 40, 161, 61))
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



        # 关联注册按钮和相关获取信息的函数
        # self.user.returnPressed.connect(self.record)
        # self.passwd.returnPressed.connect(self.record)
        # self.confirm.returnPressed.connect(self.record)
        self.register_button.clicked.connect(self.record)

        # 实现跳转界面 关联
        self.re_login.clicked.connect(self.goto_login)


    def record(self): # 实例化后里面的函数的变量也是可以保存属性值
        self.user_content = self.user.text()
        self.passwd_content = self.passwd.text()
        self.confirm_content = self.confirm.text()

        # 对获取到的内容进行保存处理(输出显示和保存等)
        if self.user_content == '' or self.passwd_content =='' or self.confirm_content == '':
            print(QMessageBox.warning(None,'输入错误','帐号密码不能为空',QMessageBox.Yes,QMessageBox.Yes))
            print('帐号密码不能为空')

        elif self.passwd_content != self.confirm_content:
            print(QMessageBox.warning(None,'警告','两次密码输入不一致',QMessageBox.Yes,QMessageBox.Yes))
        else:
            # 这里假设符合正则了。准备录入到数据库了
            print(f'注册成功{self.user_content} {self.passwd_content} {self.confirm_content}')


    def goto_login(self):
        print('跳转成功')
        self.ui2 = login.Ui_Form2()
        self.ui2.setupUi(self.ui2)
        self.ui2.show()
        self.hide()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "milkbottle"))
        self.title.setText(_translate("Form", "管理员注册"))
        self.user_label.setText(_translate("Form", "帐    号"))
        self.passwd_label.setText(_translate("Form", "密    码"))
        self.confirm_label.setText(_translate("Form", "确认密码"))
        self.register_button.setText(_translate("Form", "注  册"))
        self.re_login.setText(_translate("Form", "返回登录界面"))


if __name__ =='__main__':
    app = QApplication(sys.argv)
    # my_window = QWidget()
    ui = Ui_Form()
    ui.setupUi(ui)
    ui.show()
    # my_window.show()
    sys.exit(app.exec_())