# 登录界面和注册界面

from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QWidget,QPushButton,QLabel,QApplication,QMessageBox
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import sys
from Mysql_manager import *
from Re_manager import *

# 登录窗口

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 设置窗口无边框
        self.setWindowFlag(Qt.FramelessWindowHint)

    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(640, 400)
        # login_window.setStyleSheet("#Form{\n"
        #     "background-image: url(:/images/login_bg2.png);\n"
        #     "}")
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap('./images/login_bg2.png')))
        self.setPalette(palette)
        self.user_label = QtWidgets.QLabel(login_window)
        self.user_label.setGeometry(QtCore.QRect(80, 170, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_label.setFont(font)
        self.user_label.setTextFormat(QtCore.Qt.AutoText)
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(login_window)
        self.user_lineEdit.setGeometry(QtCore.QRect(190, 170, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setTabletTracking(True)
        self.user_lineEdit.setStyleSheet("QLineEdit{\n"
            "background-color: rgba(255, 255, 255, 90%)\n"
            "}")
        self.user_lineEdit.setText("")
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.passwd_lineEdit = QtWidgets.QLineEdit(login_window)
        self.passwd_lineEdit.setGeometry(QtCore.QRect(190, 220, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.passwd_lineEdit.setFont(font)
        self.passwd_lineEdit.setTabletTracking(True)
        self.passwd_lineEdit.setText("")
        self.passwd_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd_lineEdit.setObjectName("passwd_lineEdit")
        self.passwd_label = QtWidgets.QLabel(login_window)
        self.passwd_label.setGeometry(QtCore.QRect(80, 220, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.passwd_label.setFont(font)
        self.passwd_label.setTextFormat(QtCore.Qt.AutoText)
        self.passwd_label.setObjectName("passwd_label")
        self.register_btn = QtWidgets.QPushButton(login_window)
        self.register_btn.setGeometry(QtCore.QRect(80, 280, 71, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_btn.setFont(font)
        self.register_btn.setStyleSheet("QPushButton{\n"
            "background-color: rgba(255, 255, 255, 50%)\n"
            "}")
        self.register_btn.setDefault(False)
        self.register_btn.setFlat(False)
        self.register_btn.setObjectName("register_btn")
        self.login_btn = QtWidgets.QPushButton(login_window)
        self.login_btn.setGeometry(QtCore.QRect(180, 280, 71, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("QPushButton{\n"
            "background-color: rgba(255, 255, 255, 50%)\n"
            "}")
        self.login_btn.setDefault(False)
        self.login_btn.setFlat(False)
        self.login_btn.setObjectName("login_btn")
        self.quit_btn = QtWidgets.QPushButton(login_window)
        self.quit_btn.setGeometry(QtCore.QRect(280, 280, 71, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit_btn.setFont(font)
        self.quit_btn.setStyleSheet("QPushButton{\n"
            "background-color: rgba(255, 255, 255, 50%)\n"
            "}")
        self.quit_btn.setDefault(False)
        self.quit_btn.setFlat(False)
        self.quit_btn.setObjectName("quit_btn")
        self.version_label = QtWidgets.QLabel(login_window)
        self.version_label.setGeometry(QtCore.QRect(490, 370, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.version_label.setFont(font)
        self.version_label.setObjectName("version_label")
        self.server_ip_lineEdit = QtWidgets.QLineEdit(login_window)
        self.server_ip_lineEdit.setGeometry(QtCore.QRect(320, 370, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.server_ip_lineEdit.setFont(font)
        self.server_ip_lineEdit.setTabletTracking(True)
        self.server_ip_lineEdit.setStyleSheet("QLineEdit{\n"
            "background-color: rgba(255, 255, 255, 30%)\n"
            "}")
        self.server_ip_lineEdit.setObjectName("server_ip_lineEdit")
        self.server_ip_lineEdit.setVisible(False)

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)
        login_window.setTabOrder(self.user_lineEdit, self.passwd_lineEdit)
        login_window.setTabOrder(self.passwd_lineEdit, self.login_btn)
        login_window.setTabOrder(self.login_btn, self.register_btn)
        login_window.setTabOrder(self.register_btn, self.quit_btn)
        login_window.setTabOrder(self.quit_btn, self.server_ip_lineEdit)

    def retranslateUi(self, login_window):
        _translate = QtCore.QCoreApplication.translate
        login_window.setWindowTitle(_translate("login_window", "Form"))
        self.user_label.setText(_translate("login_window", "账    号："))
        self.passwd_label.setText(_translate("login_window", "密    码："))
        self.register_btn.setText(_translate("login_window", "注   册"))
        self.login_btn.setText(_translate("login_window", "登   录"))
        self.quit_btn.setText(_translate("login_window", "退   出"))
        self.version_label.setText(_translate("login_window", "version:beta4 20200510"))
        self.server_ip_lineEdit.setText(_translate("login_window", "127.0.0.1:12306"))

        # 信号与槽绑定
        self.register_btn.clicked.connect(self.register_clicked)
        self.login_btn.clicked.connect(self.login_clicked)
        self.quit_btn.clicked.connect(self.quit_clicked)


    # 槽函数
    def register_clicked(self):
        # 关闭当前窗口，开启注册窗口
        self.close()
        self.register = Register()
        self.register.show()
    def login_clicked(self):
        user = self.user_lineEdit.text()
        passwd = self.passwd_lineEdit.text()
        if user == '' or passwd == '':
            print('账号密码不能为空')
            reply = QMessageBox.about(self,'注意','账号密码不能为空')
        else:
            # 应该不需要判断格式，直接通过数据库查询
            mm = Mysql_manager()
            with mm:
                sql = 'select * from user_info where user_name = %s and user_passwd = %s'
                mm.exe_db(sql,(user,passwd))
                if mm.cur.rowcount == 0:
                    print('账号密码错误')
                    reply = QMessageBox.about(self,'注意','账号密码错误')
                    # 账号密码错误的情况下也需要重置文本框
                    
                else:
                    print('登录成功')
                    # 准备从这里开始跳转
    def quit_clicked(self):
        self.close()


class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, register_window):
        register_window.setObjectName("register_window")
        register_window.resize(640, 400)
        #设置背景图
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap('./images/register_bg.png')))
        self.setPalette(palette)
        
        self.user_label = QtWidgets.QLabel(register_window)
        self.user_label.setGeometry(QtCore.QRect(80, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_label.setFont(font)
        self.user_label.setTextFormat(QtCore.Qt.AutoText)
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(register_window)
        self.user_lineEdit.setGeometry(QtCore.QRect(190, 130, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setTabletTracking(True)
        self.user_lineEdit.setStyleSheet("QLineEdit{\n"
            "background-color: rgba(255, 255, 255, 90%)\n"
            "}")
        self.user_lineEdit.setText("")
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.passwd_lineEdit = QtWidgets.QLineEdit(register_window)
        self.passwd_lineEdit.setGeometry(QtCore.QRect(190, 180, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.passwd_lineEdit.setFont(font)
        self.passwd_lineEdit.setTabletTracking(True)
        self.passwd_lineEdit.setText("")
        self.passwd_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd_lineEdit.setObjectName("passwd_lineEdit")
        self.passwd_label = QtWidgets.QLabel(register_window)
        self.passwd_label.setGeometry(QtCore.QRect(80, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.passwd_label.setFont(font)
        self.passwd_label.setTextFormat(QtCore.Qt.AutoText)
        self.passwd_label.setObjectName("passwd_label")
        self.goback_btn = QtWidgets.QPushButton(register_window)
        self.goback_btn.setGeometry(QtCore.QRect(80, 280, 71, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.goback_btn.setFont(font)
        self.goback_btn.setStyleSheet("QPushButton{\n"
            "background-color: rgba(255, 255, 255,50%)\n"
            "}")
        self.goback_btn.setDefault(False)
        self.goback_btn.setFlat(False)
        self.goback_btn.setObjectName("goback_btn")
        self.register_btn = QtWidgets.QPushButton(register_window)
        self.register_btn.setGeometry(QtCore.QRect(180, 280, 71, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.register_btn.setFont(font)
        self.register_btn.setStyleSheet("QPushButton{\n"
            "background-color: rgba(255, 255, 255, 50%)\n"
            "}")
        self.register_btn.setDefault(False)
        self.register_btn.setFlat(False)
        self.register_btn.setObjectName("register_btn")
        self.quit_btn = QtWidgets.QPushButton(register_window)
        self.quit_btn.setGeometry(QtCore.QRect(280, 280, 71, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit_btn.setFont(font)
        self.quit_btn.setStyleSheet("QPushButton{\n"
            "background-color: rgba(255, 255, 255, 50%)\n"
            "}")
        self.quit_btn.setDefault(False)
        self.quit_btn.setFlat(False)
        self.quit_btn.setObjectName("quit_btn")
        self.version_label = QtWidgets.QLabel(register_window)
        self.version_label.setGeometry(QtCore.QRect(490, 370, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.version_label.setFont(font)
        self.version_label.setObjectName("version_label")
        self.confirm_label = QtWidgets.QLabel(register_window)
        self.confirm_label.setGeometry(QtCore.QRect(80, 230, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.confirm_label.setFont(font)
        self.confirm_label.setTextFormat(QtCore.Qt.AutoText)
        self.confirm_label.setObjectName("confirm_label")
        self.confirm_lineEdit = QtWidgets.QLineEdit(register_window)
        self.confirm_lineEdit.setGeometry(QtCore.QRect(190, 230, 160, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.confirm_lineEdit.setFont(font)
        self.confirm_lineEdit.setTabletTracking(True)
        self.confirm_lineEdit.setText("")
        self.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_lineEdit.setObjectName("confirm_lineEdit")

        self.retranslateUi(register_window)
        QtCore.QMetaObject.connectSlotsByName(register_window)
        register_window.setTabOrder(self.user_lineEdit, self.passwd_lineEdit)
        register_window.setTabOrder(self.passwd_lineEdit, self.confirm_lineEdit)
        register_window.setTabOrder(self.confirm_lineEdit, self.register_btn)
        register_window.setTabOrder(self.register_btn, self.goback_btn)
        register_window.setTabOrder(self.goback_btn, self.quit_btn)

    def retranslateUi(self, register_window):
        _translate = QtCore.QCoreApplication.translate
        register_window.setWindowTitle(_translate("register_window", "账号注册"))
        self.user_label.setText(_translate("register_window", "账    号："))
        self.passwd_label.setText(_translate("register_window", "密    码："))
        self.goback_btn.setText(_translate("register_window", "返回登录"))
        self.register_btn.setText(_translate("register_window", "注   册"))
        self.quit_btn.setText(_translate("register_window", "退   出"))
        self.version_label.setText(_translate("register_window", "version:beta4 20200510"))
        self.confirm_label.setText(_translate("register_window", "确认密码："))

        # 绑定信号槽
        self.goback_btn.clicked.connect(self.goback_clicked)
        self.register_btn.clicked.connect(self.register_clicked)
        self.quit_btn.clicked.connect(self.quit_clicked)


    # 槽函数
    def goback_clicked(self):
        # 返回前，先重置文本框
        self.user_lineEdit.setText('')
        self.passwd_lineEdit.setText('')
        lo.show()
        self.close()
    def register_clicked(self):
        print('准备注册')
        # 先作空文本判断
        user = self.user_lineEdit.text()
        passwd = self.passwd_lineEdit.text()
        confirm = self.confirm_lineEdit.text()
        if user == '' or passwd == '' or confirm == '':
            print('账号密码不能为空')
            reply = QMessageBox.about(self,'注意','账号密码不能为空')
        elif passwd != confirm:
            print('密码重复输入不一致')
            reply = QMessageBox.about(self,'注意','密码重复输入不一致')
        else:
            rem = Re_manager()
            user = rem.is_user(user)
            passwd = rem.is_passwd(passwd)
            if user == None or passwd == None:
                print('账号或密码不符合要求')
                reply = QMessageBox.about(self,'注意','账号或密码不符合要求')
            else:
                # 所有基本条件符合，将注册信息写入注册表
                mm = Mysql_manager()
                with mm:
                    sql = 'insert into user_info values(%s,%s)'
                    mm.exe_db(sql,(user,passwd))
                    print('账号注册成功')
                    reply = QMessageBox.about(self,'注意','账号注册成功')
    def quit_clicked(self):
        self.close()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    lo = Login()
    lo.show()
    # register = Register()
    # # register.show()
    sys.exit(app.exec_())