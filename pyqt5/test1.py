import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QWidget
from PyQt5.QtGui import QIcon


class My_ico(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.move(400, 300)
        self.resize(500, 600)
        self.setWindowTitle('第一个作品')
        self.setWindowIcon(QIcon('ljp.ico'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_ico = My_ico()
    sys.exit(app.exec_())

# a = QWidget
# a.setWindowTitle