from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('event')
        self.show()

    def keyPressEvent(self,a):
        if a.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

    