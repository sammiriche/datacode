import sys
from PyQt5.QtWidgets import QWidget,\
    QPushButton,QApplication
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        btn = QPushButton('按钮退出',self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(50,50)
        btn.move(60,100)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('测试退出按钮')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
