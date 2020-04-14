import sys
from PyQt5.QtWidgets import QWidget,QTableView,QApplication,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import *
from Mysql_manager import *

class Example(QWidget):
    def __init__(self):
        super().__init__()

    def setupUi(self):
        # MVC 模式  mode添加数据源  viewer qtableview实例 通过controller控制
        self.model = QStandardItemModel(3,4)
        title = ['姓名','部门','IP','MAC']
        self.model.setHorizontalHeaderLabels(title) # 设置表格抬头

        self.tableview = QTableView()  # 设置viewer
        self.tableview.horizontalHeader().setStretchLastSection(True)
        # self.tableview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 将M和C进行关联
        self.tableview.setModel(self.model)


        # 给表格添加数据（给model添加数据）
        mm = Mysql_manager('localhost','root','root',3306,'milkbottle')
        with mm:
            sql = 'select * from em_info'
            mm.cur.execute(sql)
            result = mm.cur.fetchall()
            # for i in result:
            #     print(i[2])
            m = 0
            for i in result:
                item0 = QStandardItem(i[0])  # 分别取得姓名 部门 ip  mac
                item1 = QStandardItem(i[1])
                item2 = QStandardItem(i[2])
                item3 = QStandardItem(i[3])
                self.model.setItem(m,0,item0)
                self.model.setItem(m,1,item1)
                self.model.setItem(m,2,item2)
                self.model.setItem(m,3,item3)
                m += 1


        # 设置布局 不加这三行不显示列表控件
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableview)
        self.setLayout(self.layout)
        self.resize(600,600)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.setupUi()
    sys.exit(app.exec_())

