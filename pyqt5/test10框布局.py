# import sys
# from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QHBoxLayout,QVBoxLayout

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.run()

#     def run(self):
#         okButton = QPushButton('确认')
#         cancelButton = QPushButton('取消')
#         # 下面创建水平布局
#         hbox = QHBoxLayout()
#         hbox.addStretch(3)
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)

#         # vbox = QVBoxLayout()
#         # vbox.addStretch(1)
#         # vbox.addLayout(hbox)
        
#         self.setLayout(hbox)
#         # self.setLayout(hbox)
#         self.setGeometry(300,300,300,300)
#         self.setWindowTitle('水平和垂直布局')
#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# 表格布局
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('表格布局')
        self.show()

        grid = QGridLayout()
        self.setLayout(grid)
        names = ['cls','bck','','close',\
            '7','8','9','/','4','5','6','*','1','2','3',\
                '-','0','.','=','+']
                # 列表推导式
                # 生成列表。列表的元素是两个数字组成的元组
        # positions = [(i,j) for i in range(5) for j in range(4)]
        positions = []
        for i in range(5):
            for j in range(4):
                positions.append((i,j))

        for position,name in zip(positions,names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button,*position)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())