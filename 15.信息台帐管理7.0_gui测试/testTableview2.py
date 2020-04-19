from PyQt5 import QtGui,QtCore,QtSql
from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication,QGridLayout,QDialog
from PyQt5.QtWidgets import QGroupBox,QVBoxLayout,QHBoxLayout,QTableView
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import *
import sys
from Mysql_manager import *

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


        # 绑定显示所有按钮到方法
        self.show_button.clicked.connect(self.show_data)

        self.setCentralWidget(self.widget) # 尚未理解

    def show_data(self):
        # 先实例数据库连接方法
        mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
        with mm:
            sql = 'select * from em_info'
            mm.cur.execute(sql)
            # 取得行数，方便反馈给qtableview
            row_qtable = mm.cur.rowcount
            print(row_qtable)
            # 建立数据模型
            self.model = QStandardItemModel(row_qtable,4) # 标准项目模型，一个项目item对应一个值
            # 抬头
            title = ['姓名','部门','IP','MAC']
            self.model.setHorizontalHeaderLabels(title)

            #建立数据视图
            # self.table_view = QTableView() 前面已经建立过
            # 关联数据模型到view
            self.table_widget.setModel(self.model)
            # 给每一个model 的元素值赋值并且绑定到view里面
            # 首先取出全部数据
            result = mm.cur.fetchall()
            num = 0
            for i in result:
                item0 = QStandardItem(i[0])  # 每一次循环都是临时变量 可以理解将字符串转换成item这种数据格式
                item1 = QStandardItem(i[1])
                item2 = QStandardItem(i[2])
                item3 = QStandardItem(i[3])

                # 给模型的每一个元素赋值 每次循环填写一行
                self.model.setItem(num,0,item0) # 行标，列表，qstandardtem类型值
                self.model.setItem(num,1,item1)
                self.model.setItem(num,2,item2)
                self.model.setItem(num,3,item3)
                num += 1
            

                # 循环

class Add_dialog(QDialog):
    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.setupUi()
    ex.show()
    # ex.widget.show()
    sys.exit(app.exec_())