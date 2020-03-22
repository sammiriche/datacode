import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Ico(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # self.setGeometry(300, 200, 400, 500)
        self.move(400,500)
        self.resize(500,600)
        self.setWindowTitle('我的第二个作品')
        self.setWindowIcon(QIcon('ljp.ico'))
        button = QPushButton('测试按钮', self)
        button.clicked.connect(QCoreApplication.instance().quit)
        button.resize(70, 30)
        button.move(300, 100)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ico = Ico()
    sys.exit(app.exec_())
