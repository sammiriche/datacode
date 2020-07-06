import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLineEdit
from second import *

class First(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(600,400,500,500)
        self.setWindowTitle('主窗口')
        self.btn = QPushButton('弹出子窗口',self)
        self.btn.move(200,200)

        self.le = QLineEdit(self)
        self.le.move(200,300)
        # self.btn.resize(50,50)
        self.btn.clicked.connect(self.goto_second)
    def goto_second(self):
        self.s = Second()
        self.s.my_signal.connect(self.show_info)
        # self.s.btn2.clicked.connect(self.show_info)
        self.s.show()

    # def rx_info(self):
    #     s = Second()
    #     s.my_signal.connect(self.show_info)
    #     s.exec_()

    def show_info(self,content):
        print('接收信息成功')
        print(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    f = First()
    f.show()
    sys.exit(app.exec_())
        