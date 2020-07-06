from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLineEdit
from PyQt5.QtCore import *
import sys

class Slave(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(650,550,400,400)

        self.btn = QPushButton('发信到主窗口',self)
        self.btn.move(100,100)

        self.btn2 = QPushButton('发信到主窗口',self)
        self.btn2.move(150,150)

        self.edit1 = QLineEdit(self)
        self.edit1.move(250,100)
        self.edit2 = QLineEdit(self)
        self.edit2.move(250,250)

        self.btn2.clicked.connect(self.get_content)

        self.show()

    def get_content(self):
        content = self.edit1.text()
        self.my_signal.emit(content) # 发射信号，在主窗口接收信号 自定义信号发射是有返回值的
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    sl = Slave()
    sys.exit(app.exec_())
