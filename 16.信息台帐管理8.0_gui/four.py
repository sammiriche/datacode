from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLineEdit
from PyQt5.QtCore import *
import sys

class Four(QWidget):
    mysignal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(550,550,400,400)
        
        self.btn = QPushButton('发送',self)
        self.btn.move(200,200)

        self.edit = QLineEdit(self)
        self.edit.move(200,300)

        self.btn.clicked.connect(self.send)

        self.show()

    def send(self):

        content = self.edit.text()
        self.mysignal.emit(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fo = Four()
    sys.exit(app.exec_())
