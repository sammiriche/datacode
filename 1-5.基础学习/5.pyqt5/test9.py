# 强制窗口在屏幕中间

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QDesktopWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        self.resize(400,400)
        self.center() # 调用单独定义的方法
        self.setWindowTitle('中文编程5 ，测试屏幕居中窗口')
        self.show()
    
    def center(self): # 窗口居中方法
        # 获取窗口对象 注意计算方法。move到的位置是左上角的位置
        desktop = app.desktop()
        left_x = (desktop.width()-self.width())*0.5
        left_y = (desktop.height()-self.height())*0.5
        self.move(left_x,left_y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())