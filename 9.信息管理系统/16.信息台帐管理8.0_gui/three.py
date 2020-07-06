# 测试自定义信号发送

from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLineEdit
from PyQt5.QtCore import *
import sys
from four import *

class Three(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(500,400,500,500)
        self.btn = QPushButton('跳转子窗口',self)
        self.btn.move(200,200)

        self.edit = QLineEdit(self)
        self.edit.move(300,250)
        self.btn.clicked.connect(self.goto_four)

        self.show()
    def goto_four(self):
        self.fo = Four()
        self.fo.mysignal.connect(self.edit.setText)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    th = Three()
    sys.exit(app.exec_())
