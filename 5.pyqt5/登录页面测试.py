# 窗体的加载
# 用户名和密码的登录框
# 获取用户名和密码属性值
# from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLabel,QMessageBox,QLineEdit
# from PyQt5.QtWidgets import QVBoxLayout
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import *

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Signup(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        title_font = QFont()  #  字体对象实例，准备给标题抬头用
        title_font.setPixelSize(22) #  该对象的属性值（字体大小）
        self.layout = QVBoxLayout() # 实例纵向布局给类变量
        self.setLayout(self.layout) # 设置类实例的布局类型
        self.signup_label = QLabel('欢迎使用员工管理系统') # 实例一个label给self （注册按钮）
        self.signup_label.setFixedHeight(100) # 设置标签高度
        self.signup_label.setAlignment(Qt.AlignCenter)  #标签居中显示
        self.signup_label.setFont(title_font)
        self.layout.addWidget(self.signup_label,Qt.AlignCenter) #注册标签加入到纵向布局

        # 设置表单对象，包括用户名，密码，确认密码
        self.formlayout = QFormLayout()
        # row 1
        self.user_label = QLabel('用户名：')
        self.user_edit = QLineEdit() # 注册标签右边单行文本框，用于输入
        self.user_edit.setFixedWidth(180)  # 输入文本框的宽度
        self.user_edit.setFixedHeight(32)  # 输入文本框的高度
        self.formlayout.addRow(self.user_label,self.user_edit) # 将标签和文本框加入表单布局

        # row 2
        self.passwd_label = QLabel('密码：')
        self.passwd_edit = QLineEdit() # 注册标签右边单行文本框，用于输入
        self.passwd_edit.setFixedWidth(180)  # 输入文本框的宽度
        self.passwd_edit.setFixedHeight(32)  # 输入文本框的高度
        self.formlayout.addRow(self.passwd_label,self.passwd_edit) # 将标签和文本框加入表单布局

        # row 3
        self.confirm_label = QLabel('确认密码：')
        self.confirm_edit = QLineEdit() # 注册标签右边单行文本框，用于输入
        self.confirm_edit.setFixedWidth(180)  # 输入文本框的宽度
        self.confirm_edit.setFixedHeight(32)  # 输入文本框的高度
        self.formlayout.addRow(self.confirm_label,self.confirm_edit) # 将标签和文本框加入表单布局

        # 单独的注册按钮
        self.signup_button = QPushButton('点击注册')
        self.signup_button.setFixedHeight(30)
        self.signup_button.setFixedWidth(180)
        self.formlayout.addRow('***',self.signup_button)  # 将空格和按钮加入表单布局row？和widget区别？

        widget = QWidget()
        widget.setLayout(self.formlayout)
        widget.setFixedWidth(300)
        widget.setFixedHeight(250)

        self.Hlayout = QHBoxLayout()
        self.Hlayout.addWidget(widget,Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(self.Hlayout)

        self.layout.addWidget(widget,Qt.AlignCenter)


        # 这里将信号与槽做绑定，（自定义槽函数）
        self.user_edit.returnPressed.connect(self.record)
        self.passwd_edit.returnPressed.connect(self.record)
        self.confirm_edit.returnPressed.connect(self.record)
        self.signup_button.clicked.connect(self.record)
    # 界面和数据库联动，获取输入内容
    def record(self):
        self.user = self.user_edit.text() # 保存单行文本框的文本内容
        self.passwd = self.passwd_edit.text()
        self.confirm = self.confirm_edit.text()
        print(f'获取信息成功,{self.user}{self.passwd}{self.confirm}')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Signup()
    w.show()
    sys.exit(app.exec_())