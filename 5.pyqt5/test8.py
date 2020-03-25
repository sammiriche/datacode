# 信号槽---消息确认框
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        self.setGeometry(500,500,500,500)
        self.setWindowTitle('中文编程4')
        self.show()
    
    def closeEvent(self,event): # 关闭窗口按钮自动调用该方法，这里重写了该方法，所以函数名不能自己改
        reply = QMessageBox.question(self,'message','确定退出吗',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        print('关闭按钮测试')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
