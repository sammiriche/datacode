# import sys
# from PyQt5.QtWidgets import QWidget,QLabel,QApplication

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.run()

#     def run(self):
#         label1 = QLabel('按钮1',self) # 这里把self传递进去有什么用？
#         label1.move(15,20)
#         label2 = QLabel('按钮2',self)
#         label2.move(15,40)
#         label3 = QLabel('按钮3',self)
#         label3.move(15,60)
#         self.setGeometry(300,300,300,300)
#         self.setWindowTitle('布局')
#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

