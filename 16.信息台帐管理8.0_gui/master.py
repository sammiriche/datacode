# 两个不同的办法在主次窗口传值
# 自定义信号方法的使用
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLineEdit,QLabel
import sys
from slave import *

class Master(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    
    def setupUi(self):
        self.setGeometry(400,400,500,500)
        self.btn = QPushButton('连接到子窗口',self)
        self.btn.move(100,200)

        self.btn2 = QPushButton('发送',self)
        self.btn2.move(200,200)
        self.edit = QLineEdit(self)
        self.edit.move(300,200)
        self.edit2 = QLineEdit(self)
        self.edit2.move(300,300)

        self.btn.clicked.connect(self.goto_slave)
        
        self

        self.show()

    def goto_slave(self):
        print('连接到子窗口')
        self.sl = Slave()
        self.sl.btn.clicked.connect(self.show_content)
        self.sl.edit2.setText(self.edit2.text())


    # 接收子窗口内容
    def show_content(self,content):
        content1 = self.sl.edit1.text()
        self.edit.setText(content1)
        # self.edit2.setText(content)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ma = Master()
    sys.exit(app.exec_())


