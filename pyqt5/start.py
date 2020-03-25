import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QLabel

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('second')
        self.lab = QLabel('方向',self)
        self.lab.setGeometry(150,150,100,100)

        self.show()
    
    def key_press(self,e):
        if e.key() == Qt.key_8:
            self.lab.setText('↑')
        elif e.key() == Qt.key_2:
            self.lab.setWindowTitle('down')
        elif e.key() == Qt.key_6:
            self.lab.setWindowTitle('right')
        elif e.key() == Qt.key_4:
            self.lab.setWindowTitle('left')
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

