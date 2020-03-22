from PyQt5.QtWidgets import QMainWindow,QApplication
import sys

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        self.statusBar().showMessage('这里是状态栏')
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('这里是标题')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
