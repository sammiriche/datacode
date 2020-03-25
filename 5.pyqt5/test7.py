# 测试信号槽
import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        self.setGeometry(500,600,400,300)
        self.setWindowIcon(QIcon('ljp.ico'))        
        self.setWindowTitle('中文编程三')

        btn = QPushButton('退出',self)
        btn.move(50,50)
        btn.resize(btn.sizeHint())
        # 信号与槽的对接
        btn.clicked.connect(QCoreApplication.instance().exit)

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())