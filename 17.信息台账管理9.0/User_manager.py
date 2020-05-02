# 帐号管理类，系统入口，登录界面和注册界面构成
# 方便管理，直接新建两个实例，方便跳转窗口

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox
import sys
from Re_manager import *
from Mysql_manager import *
from Em_manager import *

# 登录窗口
class Login(QWidget):
    def __init__(self):
        super().__init__() # 这句话不加下面会报错
        self.setupUi(self)
        # 禁止最大化和拉伸，注意该语句在setup方法之后，不然他会先禁止拉伸，变成默认窗口了
        self.setFixedSize(self.width(), self.height())


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
        self.config_lineEdit.setVisible(False) # 后期新加功能在此实现

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 绑定信号槽
        self.login_btn.clicked.connect(self.login_clicked)
        self.register_btn.clicked.connect(self.register_clicked)
        self.quit_btn.clicked.connect(self.quit_clicked)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "用户登录"))
        self.title_label.setText(_translate("Form", "员工信息管理系统"))
        self.account_label.setText(_translate("Form", "帐    号："))
        self.passwd_label.setText(_translate("Form", "密    码："))
        self.register_btn.setText(_translate("Form", "注  册"))
        self.login_btn.setText(_translate("Form", "登  录"))
        self.quit_btn.setText(_translate("Form", "退  出"))
        self.version_label.setText(_translate("Form", "version:beta3 20200426"))
        self.config_lineEdit.setText(_translate("Form", "127.0.0.1:12306"))

    # 编写槽函数
    def register_clicked(self):
        # 为了简化语句，好理解，直接就先实例两个类，方便跳转
        # 清空窗口数据
        register.account_lineEdit.setText('')
        register.passwd_lineEdit.setText('')
        register.confirm_lineEdit.setText('')
        register.show()
        login.close()
        
    def login_clicked(self):
        # 首先从文本框获取值，然后交给正则类进行判断
        account = self.account_lineEdit.text()
        passwd = self.passwd_lineEdit.text()
        if account == '' or passwd == '': # 第一层判断是否为空
            print('输入不能为空')
            reply = QMessageBox.about(self,'注意','帐号或密码不能为空')
        else:
            rem = Re_manager()
            account = rem.is_account(account) # 把自己传递进去做判断
            passwd = rem.is_passwd(passwd)
            # 测试
            print('**')
            print(passwd)
            if account == None or passwd == None: # 第二层判断格式问题
                print('帐号或者密码格式错误')
                reply = QMessageBox.about(self,'注意','帐号或者密码格式错误')
            else:
                # 第三层判断帐号或者密码是否正确
                mm = Mysql_manager()
                with mm:
                    sql = 'select * from user_info where user_name = %s and user_passwd = %s'
                    result = mm.db_exe(sql,(account,passwd))
                    if mm.cur.rowcount == 0:
                        print('帐号密码错误')
                        reply = QMessageBox.about(self,'注意','帐号密码错误')
                    else:
                        print(result)
                        print('验证成功，可以登录')  # 这里才是跳转主窗口的语句模块
                        self.em = Em_manager()
                        self.em.show()
                        login.close()




    def quit_clicked(self):
        self.close()

# 注册窗口
class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(456, 347)
        self.title_label = QtWidgets.QLabel(Form)
        self.title_label.setGeometry(QtCore.QRect(140, 30, 201, 51))
        font = QtGui.QFont()
        font.setFamily("方正大黑简体")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.passwd_label = QtWidgets.QLabel(Form)
        self.passwd_label.setGeometry(QtCore.QRect(100, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.passwd_label.setFont(font)
        self.passwd_label.setObjectName("passwd_label")
        self.passwd_lineEdit = QtWidgets.QLineEdit(Form)
        self.passwd_lineEdit.setGeometry(QtCore.QRect(212, 150, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.passwd_lineEdit.setFont(font)
        self.passwd_lineEdit.setText("")
        self.passwd_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd_lineEdit.setObjectName("passwd_lineEdit")
        self.confirm_lineEdit = QtWidgets.QLineEdit(Form)
        self.confirm_lineEdit.setGeometry(QtCore.QRect(212, 200, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.confirm_lineEdit.setFont(font)
        self.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_lineEdit.setObjectName("confirm_lineEdit")
        self.confirm_label = QtWidgets.QLabel(Form)
        self.confirm_label.setGeometry(QtCore.QRect(100, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.confirm_label.setFont(font)
        self.confirm_label.setObjectName("confirm_label")
        self.goback_btn = QtWidgets.QPushButton(Form)
        self.goback_btn.setGeometry(QtCore.QRect(95, 260, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.goback_btn.setFont(font)
        self.goback_btn.setObjectName("goback_btn")
        self.register_btn = QtWidgets.QPushButton(Form)
        self.register_btn.setGeometry(QtCore.QRect(195, 260, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_btn.setFont(font)
        self.register_btn.setObjectName("register_btn")
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
        self.account_lineEdit = QtWidgets.QLineEdit(Form)
        self.account_lineEdit.setGeometry(QtCore.QRect(212, 100, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.account_lineEdit.setFont(font)
        self.account_lineEdit.setText("")
        self.account_lineEdit.setObjectName("account_lineEdit")
        self.account_label = QtWidgets.QLabel(Form)
        self.account_label.setGeometry(QtCore.QRect(100, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.account_label.setFont(font)
        self.account_label.setObjectName("account_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 绑定信号槽，在setup语句里面
        self.goback_btn.clicked.connect(self.goback_clicked)
        self.register_btn.clicked.connect(self.register_clicked)
        self.quit_btn.clicked.connect(self.quit_clicked)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员注册"))
        self.title_label.setText(_translate("Form", "系统管理员注册"))
        self.passwd_label.setText(_translate("Form", "密    码："))
        self.confirm_label.setText(_translate("Form", "确认密码："))
        self.goback_btn.setText(_translate("Form", "返回登录"))
        self.register_btn.setText(_translate("Form", "注  册"))
        self.quit_btn.setText(_translate("Form", "退  出"))
        self.version_label.setText(_translate("Form", "version:beta3 20200426"))
        self.account_label.setText(_translate("Form", "帐    号："))

    # 槽函数
    def goback_clicked(self):
        # 首先重置窗口清空数据
        login.account_lineEdit.setText('')
        login.passwd_lineEdit.setText('')
        login.show()
        self.close()
    def register_clicked(self): # 两个类的同名函数,测试同名函数的影响
        # 获取文本框值，先做正则判断，再写入数据库
        account = self.account_lineEdit.text()
        passwd = self.passwd_lineEdit.text()
        confirm = self.confirm_lineEdit.text()
        # 先判断输入不能为空 测试不配对else
        if account == '' or passwd == '' or confirm == '':
            print('输入不能为空')
            reply = QMessageBox.about(self,'提示','输入不能为空')
        # 判断两次密码是否一致
        elif passwd != confirm:
            print('密码输入不一致')
            reply = QMessageBox.about(self,'提示','密码输入不一致')
            # 判断是否符合正则,这里必须在else下面了。防止不必要的执行
        else:
            # 然后进行正则判断
            rem = Re_manager()
            account = rem.is_account(account)
            passwd = rem.is_passwd(passwd)
            if account == None or passwd == None:
                print('帐号或者密码不符合要求')
                reply = QMessageBox.about(self,'提示','帐号或者密码不符合要求')
            else:
                mm = Mysql_manager()
                with mm:
                    sql = 'insert into user_info values(%s,%s,%s)'
                    mm.db_exe(sql,(account,passwd,1))
                    print('帐号注册成功')
                    reply = QMessageBox.about(self,'提示','帐号注册成功')
        

    def quit_clicked(self):
        self.close() 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.show()

    register = Register()
    # register.show()
    sys.exit(app.exec_())
