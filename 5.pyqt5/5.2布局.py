# import sys
# from PyQt5.QtWidgets import QWidget,QPushButton,QApplication

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.run()

#     def run(self):
#         self.setGeometry(300,300,300,350)
#         self.setWindowTitle('布局测试')
#         b1 = QPushButton('剪刀',self)
#         b1.move(50,200)
#         b2 = QPushButton('石头',self)
#         b2.move(150,200)
#         b3 = QPushButton('布',self)
#         b3.move(250,200)

#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QHBoxLayout,\
    QVBoxLayout

class Example(QWidget):
    # 箱式布局 水平布局
    def __init__(self):
        super().__init__()
        self.Init_UI()
    def Init_UI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('布局测试')

        b1 = QPushButton('剪刀',self)
        b1.move(50,200)
        b2 = QPushButton('石头',self)
        b2.move(150,200)
        b3 = QPushButton('布',self)
        b3.move(250,200)

        # 布局设置
        hbox = QHBoxLayout()
        hbox.addStretch(2)
        hbox.addWidget(b1)
        hbox.addWidget(b2)
        hbox.addWidget(b3)
        
        # vbox = QVBoxLayout()
        self.setLayout(hbox) # 加了这个才表示添加了布局

        self.show()  # 该语句放到最后执行
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())