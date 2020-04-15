from PyQt5 import QtGui,QtCore,QtSql
from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication,QGridLayout
from PyQt5.QtWidgets import QGroupBox,QVBoxLayout,QHBoxLayout,QTableView
from PyQt5.QtWidgets import QPushButton
import sys

class Example(QMainWindow):
    def setupUi(self):
        self.setWindowTitle('测试表格输出')
        self.resize(800,600)

        # 创建一个窗口部件 该窗口就是整个窗口
        # 整个窗口设置了一个布局，就是网格布局
        self.widget = QWidget()
        # self.widget.resize(500,500)
        # 创建一个网格布局
        self.grid_layout = QGridLayout()
        # 将窗口（部件）设置为网格布局
        # 或者说在网格布局加入窗口部件
        self.widget.setLayout(self.grid_layout)
        # self.grid_layout.addWidget(self.widget)

        # 左侧五个功能按钮组合组成一个按钮组
        self.group_box = QGroupBox('操作按钮组合') # 所有部件实例化
        # 设置这个组合方便当成一个整体等下添加到网格布局当中
        # 设置一个纵向布局的对象准备给这五个按钮
        self.group_box_layout = QVBoxLayout()
        self.group_box.setLayout(self.group_box_layout)

        # 创建右侧的表格部件
        self.table_widget = QTableView()
        # 把按钮组和表格部件添加到整体的网格布局当中去
        self.grid_layout.addWidget(self.group_box,0,0)
        self.grid_layout.addWidget(self.table_widget,0,1)

        # 进入左侧子模块对单独按钮进行设置
        self.show_button = QPushButton('显示所有信息')
        self.add_button = QPushButton('添加员工信息')
        self.del_button = QPushButton('删除员工信息')
        self.modify_button = QPushButton('修改员工信息')
        self.query_button = QPushButton('查询员工信息')

        # 将上述按钮假如按钮组布局
        self.group_box_layout.addWidget(self.show_button)
        self.group_box_layout.addWidget(self.add_button)
        self.group_box_layout.addWidget(self.del_button)
        self.group_box_layout.addWidget(self.modify_button)
        self.group_box_layout.addWidget(self.query_button)

        self.setCentralWidget(self.widget) # 尚未理解
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.setupUi()
    ex.show()
    sys.exit(app.exec_())