from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import *
from PyQt5 import Qt
from PyQt5.QtCore import *
# import images.pic
import sys

# 登录窗口
class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint) # 设置为无边框
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(640, 400)
        # login_window.setStyleSheet("#Form{\n"
        #         "background-image: url(:/login_bg2.png);\n"
        #         "}")

        palette = QPalette()
        # palette.setBrush(QPalette.Background, QBrush(QPixmap(":/login_bg2.png"))) # 如果导入了qrc相关模块，用冒号，看清楚路径
        palette.setBrush(QPalette.Background,QBrush(QPixmap("./images/login_bg2.png")))  # 不导入冒号。相对路径，.代表当前路径
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    lo = Login()
    lo.show()
    sys.exit(app.exec_())