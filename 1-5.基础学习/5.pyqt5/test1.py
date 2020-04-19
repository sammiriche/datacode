import sys
from PyQt5.QtWidgets import QWidget,QToolTip,QPushButton,QApplication
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        QToolTip.setFont(QFont('SansSerif',10)) # 注意这里是静态方法
        self.setToolTip('this is a <b>QWidget</b> widget')

        btn = QPushButton('按钮1',self) # 把按钮加在self上面，self是qwidget
        btn.setToolTip('this is a 按钮')
        btn.resize(60,60)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('tooltips')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
