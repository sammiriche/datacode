import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
from PyQt5.QtCore import pyqtSignal,QObject

class Signal(QObject):
    showmouse = pyqtSignal()  # 创建一个自定义的信号

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('自定义信号')
        self.s = Signal()
        self.s.showmouse.connect(self.about) # 自定义信号连接到about函数

        self.show()

    def about(self):
        QMessageBox.about(self,'鼠标','你点击了鼠标了啊')
    
    def mousePressEvent(self,e):  # 重写方法
        self.s.showmouse.emit()  #  自定义信号在按下鼠标时发出信号

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
