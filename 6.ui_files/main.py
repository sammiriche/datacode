#  这是一个通用的调用ui转换文件的模板

import sys
from PyQt5.QtWidgets import QWidget,QApplication
# 导入UI转换的py文件
from Ui_c import Ui_Form

# 新建类。继承一个基本窗口类，和刚刚UI转换的类
# 这样可以调用UI转换的类里的方法（继承）
class Mywindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # 注意把自己这个实例传进去

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mywindow()
    w.show()
    sys.exit(app.exec_())