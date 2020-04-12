# 与上一版做大改变，引用GUI模块。采用复制代码方式。而非直接转换。
# 添加登录和注册两个界面。
# 首先用designer生成基本界面，然后添加界面跳转代码和信号槽等的相关设置
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from Mysql_manager import *
from Em_manager_cmd import *

# 注册窗口类
class Register_form(QWidget):

    # def __init__(self):
    #     super().__init__()
    
    # 复制从designer转换生成的Ui_Form类
    # ico 路径手动更改一下
    # 注意每个控件对象名称不要对应错了
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
        
        # 绑定信号槽写在retranslateUi里面也可行
        # 将注册按钮 发射信号 绑定到自定义函数（该函数记录注册数据到数据库并且弹窗提示是否成功）
        self.register_button.clicked.connect(self.regitster_to_DB)
        # 将返回登录界面按钮绑定到自定义函数（跳转到登录界面）
        self.re_login.clicked.connect(self.goto_login)

    def regitster_to_DB(self):
        user = self.user.text() # user对象文本框返回取得的值，文本框内容只要输入，就有返回值。随时调用，随时返回 
        passwd = self.passwd.text()
        confirm = self.confirm.text()
        # 首先进行合法性判断 暂时不做正则判断
        if user == '' or passwd == '' or confirm == '':
            print('输入不能为空')  # 命令行输出
            print(QMessageBox.warning(None,'输入错误','帐号密码不能为空',QMessageBox.Yes,QMessageBox.Yes))
        elif passwd != confirm:
            print('两次密码输入不一致')
            print(QMessageBox.warning(None,'notice','密码输入不一致',QMessageBox.Yes,QMessageBox.Yes))
        else:
            # 确认输入无误后连接数据库并且保存信息
            mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
            with mm:
                # 不需要指定使用数据库？
                sql = 'insert into user_info values(%s,%s,%s)'
                mm.cur.execute(sql,(user,passwd,1)) # 最后一个参数用作其他判断
                # with语句在结束时自动调用exit方法（该方法自动commit和关闭）
                print('注册成功')
                print(QMessageBox.warning(None,'注册成功','账号密码写入到数据库',QMessageBox.Yes,QMessageBox.Yes))

    def goto_login(self):
        # 窗口实例已经运行
        print('跳转到登录界面成功')
        login_form.show() # 一定注意大小写，如果写成大写。那么调用的是类方法。但是类方法没有show方法
        register_form.close()
        







# 登录窗口类
class Login_form(QWidget):
    # def __init__(self):
    #     super().__init__()

    # 复制从designer转换生成的Ui_Form类
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
        self.title.setGeometry(QtCore.QRect(120, 50, 261, 61))
        font = QtGui.QFont()
        font.setFamily("华文新魏")
        font.setPointSize(24)
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "milkbottle"))
        self.title.setText(_translate("Form", "员工信息管理beta1"))
        self.user_label.setText(_translate("Form", "帐    号"))
        self.passwd_label.setText(_translate("Form", "密    码"))
        self.register_button.setText(_translate("Form", "注   册"))
        self.exit_button.setText(_translate("Form", "退   出"))
        self.login_button.setText(_translate("Form", "登   陆"))


        # 绑定信号槽，总共有三个按钮 注册 登录 退出
        self.register_button.clicked.connect(self.goto_register)
        # 退出按钮，直接绑定内置方法qwidget的close()方法
        self.exit_button.clicked.connect(self.close)
        # 登录窗口，登录到主窗口
        self.login_button.clicked.connect(self.goto_primary_window)

    
    def goto_register(self):
        print('跳转到注册页面成功')
        register_form.show()
        login_form.close()

    def goto_primary_window(self):
        # 暂时用来跳转到命令行窗口
        # 主窗口考虑单独建类。因为其本身还有弹出窗口
        # 注意登录窗口要做帐号密码判断检测
        em = Em_manager_cmd()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_form = Login_form()
    login_form.setupUi(login_form) # self也是qwidget，也有show方法 传自己进去
    login_form.show()

    # 测试同时显示两个
    register_form = Register_form()
    register_form.setupUi(register_form)
    # register_form.show()
    sys.exit(app.exec_())
