import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLineEdit
from PyQt5.QtCore import *

class Second(QWidget):

    # 自定义信号
    my_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(300,300,300,200)
        self.btn = QPushButton('子按钮',self)
        self.btn.move(100,60)

        self.btn2 = QPushButton('子按钮',self)
        self.btn2.move(200,60)

        self.le = QLineEdit(self)
        self.le.move(100,160)

        self.btn.clicked.connect(self.get_content)
    
    def get_content(self):
        print('测试绑定')
        content = self.le.text()
        self.my_signal.emit(content)  # 发出信号


if __name__ == "__main__":
    app = QApplication(sys.argv)
    s = Second()
    s.show()
    sys.exit(app.exec_())