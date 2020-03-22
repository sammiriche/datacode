# 面向对象编程风格
"""
1导入包，2 创建类，重写构造函数（添加调用另外一个主函数）
3 实例类
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon
# 创建类，继承qtwidget(普通窗口，对话窗口，方便调用父类方法)
class Example(QWidget):
    def __init__(self):
        # 重写父类构造方法，多加一行调用其他函数，这样实例类时直接创建类就好
        super().__init__()
        self.run()  #该方法就是用来显示窗口，设置窗口

    def run(self):
        # 设置位置和大小标题，和左上角ico
        self.setGeometry(0,0,500,300)
        self.setWindowIcon(QIcon('ljp.ico'))
        self.setWindowTitle('中文教程1')
        # 显示窗口
        self.show()

# 测试和调用，记住格式就好
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())