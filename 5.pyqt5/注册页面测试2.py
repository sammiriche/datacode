# 建立大的雏形
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLabel,QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Signup(QWidget):
    # 对这个类的理解，就是封装了一套方法，用来来窗口进行设置（通过传参，这个参数就是实际窗口）
    def __init__(self):
        super().__init__()
        self.resize(800,600) # 设置窗口大小
        self.setup_ui()

    def setup_ui(self):  # 对窗口设置的主方法
        title_font = QFont()   #  实例化字体对象，给标题字体用
        title_font.setPixelSize(22) # 实例化对象的具体属性。
        line_font = QFont()  # 给输入框里面字体用
        line_font.setPixelSize(18)

        self.layout = QVBoxLayout()  #  实例化纵向布局。
        self.setLayout(self.layout)  # 设置总体布局为set.layout

        self.signup_label  = QLabel('员工信息系统管理员注册')  # 注册抬头标签
        self.signup_label.setFixedHeight(150) # 标签高度
        self.signup_label.setAlignment(Qt.AlignCenter) # 设置标签居中显示
        self.signup_label.setFont(title_font)  # 设置标签字体
        self.layout.addWidget(self.signup_label,Qt.AlignHCenter) # 实例化总体布局对象加入一个窗体（标签）,并且H居中（H）


        #  下面几个按钮和文本框有自己的子布局（表单布局）
        self.form_layout = QFormLayout()
        # 总共有三行两列
        # row1
        self.user_label = QLabel('帐  号') # 帐号标签（控件）
        self.user_label.setFont(line_font) #设置该标签字体
        self.user = QLineEdit() # 输入框，对象名字为user
        self.user.setFont(line_font)
        self.user.setFixedWidth(200) # 输入框的大小设置
        self.user.setFixedHeight(32)
        self.form_layout.addRow(self.user_label,self.user) # 将这两个控件加入到子布局

        #下面两行类似设置
        # row2
        self.passwd_label = QLabel('密  码')
        self.passwd_label.setFont(line_font)
        self.passwd = QLineEdit()
        self.passwd.setFont(line_font)
        self.passwd.setFixedWidth(200)
        self.passwd.setFixedHeight(32)
        self.form_layout.addRow(self.passwd_label,self.passwd)

        # row3
        self.confirm_label = QLabel('确认密码')
        self.confirm_label.setFont(line_font)
        self.confirm = QLineEdit()
        self.confirm.setFont(line_font)
        self.confirm.setFixedWidth(200)
        self.confirm.setFixedHeight(32)
        self.form_layout.addRow(self.confirm_label,self.confirm)

        widget = QWidget()  # 整个设置就是一个布局，或者说是控件
        widget.setLayout(self.form_layout)
        widget.setFixedHeight(250)
        widget.setFixedWidth(300)

        self.Hlayout = QHBoxLayout()
        self.Hlayout.addWidget(widget,Qt.AlignCenter)

        wdiget = QWidget()
        widget.setLayout(self.Hlayout)
        
        self.layout.addWidget(widget,Qt.AlignHCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Signup()
    w.show()
    sys.exit(app.exec_())