import sys
from PyQt5.QtWidgets import QWidget,QToolTip,QPushButton,QApplication
from PyQt5.QtGui import QIcon,QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        # 先设置位置，大小，图标和标题
        self.setWindowTitle('中文编程2')
        self.setGeometry(500,500,300,300)
        self.setWindowIcon(QIcon('ljp.ico'))
        #类的静态方法设置提示的字体
        QToolTip.setFont(QFont('SanSerif',10))
        # 这个提示是加载self（qwidget）上面的
        self.setToolTip('这是测试提示一')

        # 添加按钮，并且添加提示
        # 在example类里面再创建一个按钮类，并且把自己作为参数传递给它
        button = QPushButton('按钮',self)
        button.setToolTip('这是测试按钮二')
        button.resize(button.sizeHint()) # 显示默认尺寸
        button.move(50,50) # 这里的坐标是相对于主窗口的，为什么？
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())