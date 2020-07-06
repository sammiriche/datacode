# 主要操作窗口，主显示类和几个附属小窗口

from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox,QPushButton,QHeaderView,QDialog,QLabel,QFileDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
from Mysql_manager import *
from Re_manager import *
from Excel_manager import *


class Em_manager(QWidget):
    def __init__(self):
        super().__init__()
        # 全局设置qss风格，然后在里面做选择器
        qss1 = '''
            QPushButton,QLineEdit
            {  
                /* 前景色 */  
                color:white;  
            
                /* 背景色 */  
                background-color:rgb(43,100,76);  
            
                /* 边框风格 */  
                border-style:outset;  
            
                /* 边框宽度 */  
                border-width:0.5px;  
            
                /* 边框颜色 */  
                border-color:rgb(255,255,255); 
            
                /* 边框倒角 */  
                border-radius:10px;  
            
                /* 内边距 */  
                padding:4px;  
            } 
            QPushButton:pressed
            {
                color:#00ff00;
                background-color:rgb(40, 85, 20); /*改变背景色*/
                border-style:inset;/*改变边框风格*/
                padding-left:6px;
                padding-top:6px;
                border-color:rgb(255,0,0);
            }
        '''

        self.setStyleSheet(qss1)
        self.setupUi(self)
        
    def setupUi(self, em_window):
        em_window.setObjectName("em_window")
        em_window.resize(960, 760)
        self.tableView = QtWidgets.QTableView(em_window)
        self.tableView.setGeometry(QtCore.QRect(0, 80, 960, 600))
        # 设置标题水平拉伸
        # 视图设置属性和模型无关
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setPointSize(10)
        self.tableView.setFont(font)  # 设置表格里面字体
        # self.tableView.setColumnWidth(4,200) # 这个设置必须在绑定model以后设置才生效
        # 只要不是qwidget或者mainwindow，都可以设置背景色成功。一级控件得使用其他方法
        self.tableView.setStyleSheet("background-image: url(./images/中间主体.png);")
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.bottom_frame = QtWidgets.QFrame(em_window)
        self.bottom_frame.setGeometry(QtCore.QRect(0, 680, 960, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.bottom_frame.setFont(font)
        self.bottom_frame.setStyleSheet("background-image: url(./images/底部横幅.png);")
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.home_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.home_btn.setGeometry(QtCore.QRect(50, 8, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(15)
        self.home_btn.setFont(font)
        self.home_btn.setObjectName("home_btn")
        self.modify_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.modify_btn.setGeometry(QtCore.QRect(50, 45, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(15)
        self.modify_btn.setFont(font)
        
        self.modify_btn.setObjectName("modify_btn")
        self.import_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.import_btn.setGeometry(QtCore.QRect(180, 45, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(12)
        self.import_btn.setFont(font)
       
        self.import_btn.setObjectName("import_btn")
        self.add_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.add_btn.setGeometry(QtCore.QRect(180, 8, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(15)
        self.add_btn.setFont(font)
        
        self.add_btn.setObjectName("add_btn")
        self.del_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.del_btn.setGeometry(QtCore.QRect(310, 8, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(15)
        self.del_btn.setFont(font)
        
        self.del_btn.setObjectName("del_btn")
        self.export_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.export_btn.setGeometry(QtCore.QRect(310, 45, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(12)
        self.export_btn.setFont(font)
        
        self.export_btn.setObjectName("export_btn")
        self.query_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.query_btn.setGeometry(QtCore.QRect(440, 8, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(15)
        self.query_btn.setFont(font)
       
        self.query_btn.setObjectName("query_btn")
        self.quit_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.quit_btn.setGeometry(QtCore.QRect(440, 45, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(15)
        self.quit_btn.setFont(font)
       
        self.quit_btn.setObjectName("quit_btn")
        self.query_lineEdit = QtWidgets.QLineEdit(self.bottom_frame)
        self.query_lineEdit.setGeometry(QtCore.QRect(580, 8, 261, 31))
        # 文本框背景提示文字
        self.query_lineEdit.setPlaceholderText('请输入IP地址或者姓名查询')
        font = QtGui.QFont()
        font.setPointSize(15)
        self.query_lineEdit.setFont(font)
        
        self.query_lineEdit.setText("")
        self.query_lineEdit.setObjectName("query_lineEdit")
        self.top_frame = QtWidgets.QFrame(em_window)
        self.top_frame.setGeometry(QtCore.QRect(0, 0, 960, 80))
        self.top_frame.setStyleSheet("background-image: url(./images/顶部横幅.png);")
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")

        self.retranslateUi(em_window)
        QtCore.QMetaObject.connectSlotsByName(em_window)
        em_window.setTabOrder(self.home_btn, self.add_btn)
        em_window.setTabOrder(self.add_btn, self.del_btn)
        em_window.setTabOrder(self.del_btn, self.query_btn)
        em_window.setTabOrder(self.query_btn, self.query_lineEdit)
        em_window.setTabOrder(self.query_lineEdit, self.modify_btn)
        em_window.setTabOrder(self.modify_btn, self.import_btn)
        em_window.setTabOrder(self.import_btn, self.export_btn)
        em_window.setTabOrder(self.export_btn, self.quit_btn)
        em_window.setTabOrder(self.quit_btn, self.tableView)

    def retranslateUi(self, em_window):
        _translate = QtCore.QCoreApplication.translate
        em_window.setWindowTitle(_translate("em_window", "Form"))
        self.home_btn.setText(_translate("em_window", "主   页"))
        self.modify_btn.setText(_translate("em_window", "修改员工"))
        self.import_btn.setText(_translate("em_window", "导入员工信息"))
        self.add_btn.setText(_translate("em_window", "添加员工"))
        self.del_btn.setText(_translate("em_window", "删除员工"))
        self.export_btn.setText(_translate("em_window", "导出员工信息"))
        self.query_btn.setText(_translate("em_window", "查询员工"))
        self.quit_btn.setText(_translate("em_window", "退出系统"))

        #信号槽绑定，注意在函数下面，缩进
        self.home_btn.clicked.connect(self.home_clicked)
        self.add_btn.clicked.connect(self.add_clicked)
        self.del_btn.clicked.connect(self.del_clicked)
        self.query_btn.clicked.connect(self.query_clicked)
        self.modify_btn.clicked.connect(self.modify_clicked)
        self.import_btn.clicked.connect(self.import_clicked)
        self.export_btn.clicked.connect(self.export_clicked)
        self.quit_btn.clicked.connect(self.quit_clicked)

    # 槽函数
    def home_clicked(self):
        # 通过调用单独的显示所有的函数（因为该函数还要被其他调用）
        self.show_em()
    def add_clicked(self):
        self.ae = Add_em()
        self.ae.show()
        # 信号槽绑定。子信号绑定父的槽函数
        # 这里绑定了。下面子窗口不要写绑定了。防止重复执行
        self.ae.quit_btn.clicked.connect(self.ae.close)
        self.ae.quit_btn.clicked.connect(self.show_em)
    def del_clicked(self):
        # 首先在这里获取行标，获取对应的值传递给子窗口
        # 首先获取鼠标选中的数据
        self.de = Del_em()
        
        row_num = self.tableView.currentIndex().row()
        if row_num == -1:
            print('请先选中需要删除的行')
            reply = QMessageBox.about(self,'提示','请选中删除的行')
        else:
            self.de.show() # 确认选中数据再弹出子窗口
            # model 初始化时已经建立
            name = self.model.item(row_num,0).text()
            dept = self.model.item(row_num,1).text()
            ip = self.model.item(row_num,2).text()
            mac = self.model.item(row_num,3).text()
            room = self.model.item(row_num,4).text()
            switch = self.model.item(row_num,5).text()
            port = self.model.item(row_num,6).text()

            # 传值给子窗口
            self.de.user_lineEdit.setText(name)
            self.de.dept_lineEdit.setText(dept)
            self.de.ip_lineEdit.setText(ip)
            self.de.mac_lineEdit.setText(mac)
            self.de.room_lineEdit.setText(room)
            self.de.switch_lineEdit.setText(switch)
            self.de.port_lineEdit.setText(port)

            # 禁止修改子窗口
            self.de.user_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
            self.de.dept_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
            self.de.ip_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
            self.de.mac_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
            self.de.room_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
            self.de.switch_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
            self.de.port_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)

            # 子窗口的信号槽绑定
            self.de.del_btn.clicked.connect(self.de.del_clicked)
            self.de.del_btn.clicked.connect(self.show_em)  # 刷新显示窗口作用

    def query_clicked(self): # 显示当个查询结果
        text = self.query_lineEdit.text()
        if text == '':
            print('请输入查询内容1')
            reply = QMessageBox.about(self,'提示','请输入内容再进行查询')
        else:
            rem = Re_manager()
            name = rem.is_name(text)
            ip = rem.is_ip(text)
            if name == None and ip == None:
                print('请输入正确的姓名或者IP地址')
                reply = QMessageBox.about(self,'提示','请输入正确的姓名或者IP地址')
            elif ip == None:
                # 通过姓名查询
                mm = Mysql_manager()
                with mm:
                    sql = 'select * from em_info where em_name = %s'
                    result = mm.exe_db(sql,name)
                    if mm.cur.rowcount == 0:
                        print('没有任何内容')
                        reply = QMessageBox.about(self,'提示','没有查询到任何内容')
                        self.query_lineEdit.setText('') # 查不到内容时，文本框清空
                    else:
                        # 重新建立数据模型与视图绑定
                        # 注意不要与类变量冲突，好像冲突也没事。每次调用又会覆盖
                        self.model = QStandardItemModel(mm.cur.rowcount,7)
                        # 数据模型抬头
                        title = ['姓名','部门','IP地址','MAC地址','房间号','交换机地址','交换机端口']
                        self.model.setHorizontalHeaderLabels(title)
                        # 无论查询结果是几个，返回都是二维元组
                        num = 0
                        for i in result:
                            item0 = QtGui.QStandardItem(i[0])
                            item1 = QtGui.QStandardItem(i[1])
                            item2 = QtGui.QStandardItem(i[2])
                            item3 = QtGui.QStandardItem(i[3])
                            item4 = QtGui.QStandardItem(str(i[4]))
                            item5 = QtGui.QStandardItem(i[5])
                            item6 = QtGui.QStandardItem(str(i[6]))

                            self.model.setItem(num,0,item0)
                            self.model.setItem(num,1,item1)
                            self.model.setItem(num,2,item2)
                            self.model.setItem(num,3,item3)
                            self.model.setItem(num,4,item4)
                            self.model.setItem(num,5,item5)
                            self.model.setItem(num,6,item6)
                            num += 1
                        self.tableView.setModel(self.model)
            else:
                # 通过IP地址查询
                mm = Mysql_manager()
                with mm:
                    sql = 'select * from em_info where em_ip = %s'
                    result = mm.exe_db(sql,ip)
                    if mm.cur.rowcount == 0:
                        print('无法查询到内容')
                        reply = QMessageBox.about(self,'提示','无法查询到任何IP内容')
                        self.query_lineEdit.setText('')
                    else:
                        self.model = QStandardItemModel(mm.cur.rowcount,7)
                        # 数据模型抬头
                        title = ['姓名','部门','IP地址','MAC地址','房间号','交换机地址','交换机端口']
                        self.model.setHorizontalHeaderLabels(title)
                        num = 0
                        for i in result:
                            item0 = QtGui.QStandardItem(i[0])
                            item1 = QtGui.QStandardItem(i[1])
                            item2 = QtGui.QStandardItem(i[2])
                            item3 = QtGui.QStandardItem(i[3])
                            item4 = QtGui.QStandardItem(i[4])
                            item5 = QtGui.QStandardItem(i[5])
                            item6 = QtGui.QStandardItem(i[6])

                            self.model.setItem(num,0,item0)
                            self.model.setItem(num,1,item1)
                            self.model.setItem(num,2,item2)
                            self.model.setItem(num,3,item3)
                            self.model.setItem(num,4,item4)
                            self.model.setItem(num,5,item5)
                            self.model.setItem(num,6,item6)
                            num += 1
                        self.tableView.setModel(self.model)
    def modify_clicked(self):
        # 同样考虑传值问题
        self.mo = Modify_em()
        row_num = self.tableView.currentIndex().row()
        if row_num == -1:
            print('请先选中需要修改的行')
            reply = QMessageBox.about(self,'提示','请先选中需要修改的行')
        else:
            self.mo.show()

            # 把选中数据传递给子窗口
            name = self.model.item(row_num,0).text()
            dept = self.model.item(row_num,1).text()
            ip = self.model.item(row_num,2).text()
            mac = self.model.item(row_num,3).text()
            room = self.model.item(row_num,4).text()
            switch = self.model.item(row_num,5).text()
            port = self.model.item(row_num,6).text()

            self.mo.user_lineEdit.setText(name)
            # 禁止修改姓名，否则不好定位
            self.mo.user_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
            self.mo.dept_lineEdit.setText(dept)
            self.mo.ip_lineEdit.setText(ip)
            self.mo.mac_lineEdit.setText(mac)
            self.mo.room_lineEdit.setText(room)
            self.mo.switch_lineEdit.setText(switch)
            self.mo.port_lineEdit.setText(port)
        
            # 子窗口信号槽 全部写在这里 可以写在else里面
            self.mo.modify_btn.clicked.connect(self.mo.modify_clicked)
            self.mo.modify_btn.clicked.connect(self.show_em)
            self.mo.reset_btn.clicked.connect(self.mo.reset_clicked)
            self.mo.quit_btn.clicked.connect(self.mo.quit_clicked)



        
    def import_clicked(self):
        im_path = QFileDialog.getOpenFileName(self,'选中需要导入的表格','D:\\pythoncode') # 返回的是列表
        ex = Excel_manager()
        ex.import_excel(im_path[0])
        reply = QMessageBox.about(self,'提示','数据导入成功')
        
    def export_clicked(self):
        ex_path = QFileDialog.getSaveFileName(self,'请选择保存路径','D:\\pythoncode','Excel Files(*.xlsx)') # 注意每个参数作用
        ex = Excel_manager()
        ex.export_excel(ex_path[0])
        reply = QMessageBox.about(self,'提示','数据成功导出到表格')
        
    def quit_clicked(self):
        print('程序退出')
        self.close()
        # 注意考虑多窗口关闭
    

    # 显示所有信息函数
    def show_em(self):
        # 建立后端数据模型，需要获取行列数
        mm = Mysql_manager()
        with mm:
            result = mm.show_db()
            # print(result)
            self.model = QStandardItemModel(mm.cur.rowcount,7)
            # 数据模型抬头
            title = ['姓名','部门','IP地址','MAC地址','房间号','交换机地址','交换机端口']
            self.model.setHorizontalHeaderLabels(title)
            # 通过遍历获取数据库单元格的值。然后赋值给模型的单元格
            num = 0
            for i in result:
                item0 = QtGui.QStandardItem(i[0])
                item1 = QtGui.QStandardItem(i[1])
                item2 = QtGui.QStandardItem(i[2])
                item3 = QtGui.QStandardItem(i[3])
                item4 = QtGui.QStandardItem(str(i[4])) # 数据库该列是整型，这里要求字符串
                item5 = QtGui.QStandardItem(i[5])
                item6 = QtGui.QStandardItem(str(i[6]))
                self.model.setItem(num,0,item0)
                self.model.setItem(num,1,item1)
                self.model.setItem(num,2,item2)
                self.model.setItem(num,3,item3)
                self.model.setItem(num,4,item4)
                self.model.setItem(num,5,item5)
                self.model.setItem(num,6,item6)
                num += 1
            
            self.tableView.setModel(self.model) # 视图和数据模型绑定

class Add_em(QDialog): # 这里用dialog的子类就可以实现背景图的设置生效
    def __init__(self):
        super().__init__()
        qss_add = '''
            QDialog{
                image:url(./images/添加窗口.png);
            }
            QPushButton{
                
                /* 前景色 */  
                color:white;  
            
                /* 背景色 */  
                background-color:rgb(43,100,76);  
            
                /* 边框风格 */  
                border-style:outset;  
            
                /* 边框宽度 */  
                border-width:0.5px;  
            
                /* 边框颜色 */  
                border-color:rgb(255,255,255); 
            
                /* 边框倒角 */  
                border-radius:10px;  
            
                /* 内边距 */  
                padding:4px; 
            }
            QLabel#title_label{
               font-color:rgb(0,255,0); 
            }
            QMessageBox{
                image:url()
            }
            
            '''
        
        self.setupUi(self)
        self.setStyleSheet(qss_add)
        
    def setupUi(self, add_form):
        add_form.setObjectName("add_form")
        add_form.resize(360, 540)
        # add_form.setStyleSheet("#add_form{\n"
        #     "image: url(./images/添加窗口.png);\n"
        #     "}")
        self.title_label = QtWidgets.QLabel(add_form)
        self.title_label.setGeometry(QtCore.QRect(90, 30, 171, 51))
        font = QtGui.QFont()
        font.setFamily("方正大黑简体")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.user_label = QtWidgets.QLabel(add_form)
        self.user_label.setEnabled(True)
        self.user_label.setGeometry(QtCore.QRect(34, 104, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_label.setFont(font)
        # self.user_label.setStyleSheet("QLable{color:white}")
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(add_form)
        self.user_lineEdit.setGeometry(QtCore.QRect(144, 104, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setText("")
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.dept_lineEdit = QtWidgets.QLineEdit(add_form)
        self.dept_lineEdit.setGeometry(QtCore.QRect(144, 154, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dept_lineEdit.setFont(font)
        self.dept_lineEdit.setObjectName("dept_lineEdit")
        self.dept_label = QtWidgets.QLabel(add_form)
        self.dept_label.setGeometry(QtCore.QRect(34, 154, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dept_label.setFont(font)
        self.dept_label.setObjectName("dept_label")
        self.add_btn = QtWidgets.QPushButton(add_form)
        self.add_btn.setGeometry(QtCore.QRect(27, 480, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.reset_btn = QtWidgets.QPushButton(add_form)
        self.reset_btn.setGeometry(QtCore.QRect(127, 480, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("reset_btn")
        self.quit_btn = QtWidgets.QPushButton(add_form)
        self.quit_btn.setGeometry(QtCore.QRect(227, 480, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        self.mac_label = QtWidgets.QLabel(add_form)
        self.mac_label.setGeometry(QtCore.QRect(34, 254, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mac_label.setFont(font)
        self.mac_label.setObjectName("mac_label")
        self.ip_label = QtWidgets.QLabel(add_form)
        self.ip_label.setGeometry(QtCore.QRect(34, 204, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName("ip_label")
        self.mac_lineEdit = QtWidgets.QLineEdit(add_form)
        self.mac_lineEdit.setGeometry(QtCore.QRect(144, 254, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mac_lineEdit.setFont(font)
        self.mac_lineEdit.setText("")
        self.mac_lineEdit.setObjectName("mac_lineEdit")
        self.ip_lineEdit = QtWidgets.QLineEdit(add_form)
        self.ip_lineEdit.setGeometry(QtCore.QRect(144, 204, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_lineEdit.setFont(font)
        self.ip_lineEdit.setText("")
        self.ip_lineEdit.setObjectName("ip_lineEdit")
        self.room_lineEdit = QtWidgets.QLineEdit(add_form)
        self.room_lineEdit.setGeometry(QtCore.QRect(144, 304, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.room_lineEdit.setFont(font)
        self.room_lineEdit.setText("")
        self.room_lineEdit.setObjectName("room_lineEdit")
        self.room_label = QtWidgets.QLabel(add_form)
        self.room_label.setGeometry(QtCore.QRect(34, 304, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.room_label.setFont(font)
        self.room_label.setObjectName("room_label")
        self.switch_label = QtWidgets.QLabel(add_form)
        self.switch_label.setGeometry(QtCore.QRect(34, 354, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.switch_label.setFont(font)
        self.switch_label.setObjectName("switch_label")
        self.switch_lineEdit = QtWidgets.QLineEdit(add_form)
        self.switch_lineEdit.setGeometry(QtCore.QRect(144, 354, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.switch_lineEdit.setFont(font)
        self.switch_lineEdit.setText("")
        self.switch_lineEdit.setObjectName("switch_lineEdit")
        self.port_lineEdit = QtWidgets.QLineEdit(add_form)
        self.port_lineEdit.setGeometry(QtCore.QRect(144, 404, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.port_lineEdit.setFont(font)
        self.port_lineEdit.setText("")
        self.port_lineEdit.setObjectName("port_lineEdit")
        
        self.port_label = QtWidgets.QLabel(add_form)
        self.port_label.setGeometry(QtCore.QRect(34, 404, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.port_label.setFont(font)
        self.port_label.setObjectName("port_label")

        self.retranslateUi(add_form)
        QtCore.QMetaObject.connectSlotsByName(add_form)
        add_form.setTabOrder(self.user_lineEdit, self.dept_lineEdit)
        add_form.setTabOrder(self.dept_lineEdit, self.ip_lineEdit)
        add_form.setTabOrder(self.ip_lineEdit, self.mac_lineEdit)
        add_form.setTabOrder(self.mac_lineEdit, self.room_lineEdit)
        add_form.setTabOrder(self.room_lineEdit, self.switch_lineEdit)
        add_form.setTabOrder(self.switch_lineEdit, self.port_lineEdit)
        add_form.setTabOrder(self.port_lineEdit, self.add_btn)
        add_form.setTabOrder(self.add_btn, self.reset_btn)
        add_form.setTabOrder(self.reset_btn, self.quit_btn)

    def retranslateUi(self, add_form):
        _translate = QtCore.QCoreApplication.translate
        add_form.setWindowTitle(_translate("add_form", "Form"))
        self.title_label.setText(_translate("add_form", "添 加 新 员 工"))
        self.user_label.setText(_translate("add_form", "姓    名："))
        self.dept_label.setText(_translate("add_form", "部    门："))
        self.add_btn.setText(_translate("add_form", "添  加"))
        self.reset_btn.setText(_translate("add_form", "重  置"))
        self.quit_btn.setText(_translate("add_form", "退  出"))
        self.mac_label.setText(_translate("add_form", "MAC 地址："))
        self.ip_label.setText(_translate("add_form", "IP 地 址："))
        self.room_label.setText(_translate("add_form", "房间编号："))
        self.switch_label.setText(_translate("add_form", "交换机地址："))
        self.port_label.setText(_translate("add_form", "交换机端口："))

        # 信号槽绑定
        self.add_btn.clicked.connect(self.add_clicked)
        self.reset_btn.clicked.connect(self.reset_clicked)
        # self.quit_btn.clicked.connect(self.quit_clicked)

    # 槽函数三个按钮
    def add_clicked(self):
        # 首先获取文本框的值，进行基本的合法性判断
        name = self.user_lineEdit.text()
        dept = self.dept_lineEdit.text()
        ip = self.ip_lineEdit.text()
        mac = self.mac_lineEdit.text()
        room = self.room_lineEdit.text()
        switch = self.switch_lineEdit.text()
        port = self.port_lineEdit.text()

        if name == '' or dept == '' or ip == '' or mac == '' \
            or room == '' or switch == '' or port == '':
            print('请完善员工信息')
            reply = QMessageBox.about(self,'提示','请先完善个人信息')
        else:
            rem = Re_manager()
            name = rem.is_name(name)
            dept = rem.is_dept(dept)
            ip = rem.is_ip(ip)
            mac = rem.is_mac(mac)
            room = rem.is_room(room)
            switch = rem.is_switch(switch)
            port = rem.is_port(port)
            if name == None or dept == None or ip == None or mac == None \
                or room == None or switch == None or port == None:
                print('请检查输入格式')
                reply = QMessageBox.about(self,'提示','请检查输入格式')
            else:
                # 符合要求，开始写入数据到数据库
                mm = Mysql_manager()
                with mm:
                    sql = 'insert into em_info values(%s,%s,%s,%s,%s,%s,%s)' 
                    mm.exe_db(sql,(name,dept,ip,mac,room,switch,port))
                    print('更新成功')
                    reply = QMessageBox.about(self,'提示','员工信息更新成功')
                    
            # 无论是格式失败还是添加成功，清空员工信息框,调用重置函数即可
            self.reset_clicked()



    def reset_clicked(self):
        # 所有文本框清空
        self.user_lineEdit.setText('')
        self.dept_lineEdit.setText('')
        self.ip_lineEdit.setText('')
        self.mac_lineEdit.setText('')
        self.room_lineEdit.setText('')
        self.switch_lineEdit.setText('')
        self.port_lineEdit.setText('')

    def quit_clicked(self):
        # self.close()
        pass
        # 绑定写在上级窗口，方便调用上级函数

class Del_em(QDialog):
    def __init__(self):
        super().__init__()
        qss_del = '''
            QDialog{
                image:url(./images/添加窗口.png);
            }
            QPushButton{
                 /* 前景色 */  
                color:white;  
            
                /* 背景色 */  
                background-color:rgb(43,100,76);  
            
                /* 边框风格 */  
                border-style:outset;  
            
                /* 边框宽度 */  
                border-width:0.5px;  
            
                /* 边框颜色 */  
                border-color:rgb(255,255,255); 
            
                /* 边框倒角 */  
                border-radius:10px;  
            
                /* 内边距 */  
                padding:4px; 
            }
            '''
        self.setStyleSheet(qss_del)
        self.setupUi(self)
    def setupUi(self, del_form):
        del_form.setObjectName("del_form")
        del_form.resize(360, 540)
        self.title_label = QtWidgets.QLabel(del_form)
        self.title_label.setGeometry(QtCore.QRect(70, 30, 211, 51))
        font = QtGui.QFont()
        font.setFamily("方正大黑简体")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.user_label = QtWidgets.QLabel(del_form)
        self.user_label.setEnabled(True)
        self.user_label.setGeometry(QtCore.QRect(34, 104, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_label.setFont(font)
        self.user_label.setStyleSheet("")
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(del_form)
        self.user_lineEdit.setGeometry(QtCore.QRect(144, 104, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setText("")
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.dept_lineEdit = QtWidgets.QLineEdit(del_form)
        self.dept_lineEdit.setGeometry(QtCore.QRect(144, 154, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dept_lineEdit.setFont(font)
        self.dept_lineEdit.setObjectName("dept_lineEdit")
        self.dept_label = QtWidgets.QLabel(del_form)
        self.dept_label.setGeometry(QtCore.QRect(34, 154, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dept_label.setFont(font)
        self.dept_label.setObjectName("dept_label")
        self.del_btn = QtWidgets.QPushButton(del_form)
        self.del_btn.setGeometry(QtCore.QRect(27, 480, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.del_btn.setFont(font)
        self.del_btn.setObjectName("del_btn")
        self.cancel_btn = QtWidgets.QPushButton(del_form)
        self.cancel_btn.setGeometry(QtCore.QRect(190, 480, 121, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName("cancel_btn")
        self.mac_label = QtWidgets.QLabel(del_form)
        self.mac_label.setGeometry(QtCore.QRect(34, 254, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mac_label.setFont(font)
        self.mac_label.setObjectName("mac_label")
        self.ip_label = QtWidgets.QLabel(del_form)
        self.ip_label.setGeometry(QtCore.QRect(34, 204, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName("ip_label")
        self.mac_lineEdit = QtWidgets.QLineEdit(del_form)
        self.mac_lineEdit.setGeometry(QtCore.QRect(144, 254, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mac_lineEdit.setFont(font)
        self.mac_lineEdit.setText("")
        self.mac_lineEdit.setObjectName("mac_lineEdit")
        self.ip_lineEdit = QtWidgets.QLineEdit(del_form)
        self.ip_lineEdit.setGeometry(QtCore.QRect(144, 204, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_lineEdit.setFont(font)
        self.ip_lineEdit.setText("")
        self.ip_lineEdit.setObjectName("ip_lineEdit")
        self.room_lineEdit = QtWidgets.QLineEdit(del_form)
        self.room_lineEdit.setGeometry(QtCore.QRect(144, 304, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.room_lineEdit.setFont(font)
        self.room_lineEdit.setText("")
        self.room_lineEdit.setObjectName("room_lineEdit")
        self.room_label = QtWidgets.QLabel(del_form)
        self.room_label.setGeometry(QtCore.QRect(34, 304, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.room_label.setFont(font)
        self.room_label.setObjectName("room_label")
        self.switch_label = QtWidgets.QLabel(del_form)
        self.switch_label.setGeometry(QtCore.QRect(34, 354, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.switch_label.setFont(font)
        self.switch_label.setObjectName("switch_label")
        self.switch_lineEdit = QtWidgets.QLineEdit(del_form)
        self.switch_lineEdit.setGeometry(QtCore.QRect(144, 354, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.switch_lineEdit.setFont(font)
        self.switch_lineEdit.setText("")
        self.switch_lineEdit.setObjectName("switch_lineEdit")
        self.port_lineEdit = QtWidgets.QLineEdit(del_form)
        self.port_lineEdit.setGeometry(QtCore.QRect(144, 404, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.port_lineEdit.setFont(font)
        self.port_lineEdit.setText("")
        self.port_lineEdit.setObjectName("port_lineEdit")
        self.port_label = QtWidgets.QLabel(del_form)
        self.port_label.setGeometry(QtCore.QRect(34, 404, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.port_label.setFont(font)
        self.port_label.setObjectName("port_label")

        self.retranslateUi(del_form)
        QtCore.QMetaObject.connectSlotsByName(del_form)
        del_form.setTabOrder(self.user_lineEdit, self.dept_lineEdit)
        del_form.setTabOrder(self.dept_lineEdit, self.ip_lineEdit)
        del_form.setTabOrder(self.ip_lineEdit, self.mac_lineEdit)
        del_form.setTabOrder(self.mac_lineEdit, self.room_lineEdit)
        del_form.setTabOrder(self.room_lineEdit, self.switch_lineEdit)
        del_form.setTabOrder(self.switch_lineEdit, self.port_lineEdit)
        del_form.setTabOrder(self.port_lineEdit, self.del_btn)
        del_form.setTabOrder(self.del_btn, self.cancel_btn)

    def retranslateUi(self, del_form):
        _translate = QtCore.QCoreApplication.translate
        del_form.setWindowTitle(_translate("del_form", "Form"))
        self.title_label.setText(_translate("del_form", "删 除 当 前 员 工"))
        self.user_label.setText(_translate("del_form", "姓    名："))
        self.dept_label.setText(_translate("del_form", "部    门："))
        self.del_btn.setText(_translate("del_form", "确 认 删 除"))
        self.cancel_btn.setText(_translate("del_form", "取 消 操 作"))
        self.mac_label.setText(_translate("del_form", "MAC 地址："))
        self.ip_label.setText(_translate("del_form", "IP 地 址："))
        self.room_label.setText(_translate("del_form", "房间编号："))
        self.switch_label.setText(_translate("del_form", "交换机地址："))
        self.port_label.setText(_translate("del_form", "交换机端口："))

        # 绑定信号槽
        # self.del_btn.clicked.connect(self.del_clicked)
        self.cancel_btn.clicked.connect(self.cancel_clicked)

    # 槽函数。
    def del_clicked(self):
        # 已经从鼠标选中获取相应数值，不用做合法性判断
        name = self.user_lineEdit.text()
        mm = Mysql_manager()
        with mm:
            sql = 'delete from em_info where em_name = %s'
            mm.exe_db(sql,name)
            print('信息删除成功')
            reply = QMessageBox.about(self,'提示',f'{name}的个人信息删除成功')
            # 删除成功，直接调用取消退出
            self.cancel_clicked()
    def cancel_clicked(self):
        self.close()

class Modify_em(QDialog):
    def __init__(self):
        super().__init__()
        qss_modify = '''
            QDialog{
                image:url(./images/添加窗口.png);
            }
            QPushButton{
                 /* 前景色 */  
                color:white;  
            
                /* 背景色 */  
                background-color:rgb(43,100,76);  
            
                /* 边框风格 */  
                border-style:outset;  
            
                /* 边框宽度 */  
                border-width:0.5px;  
            
                /* 边框颜色 */  
                border-color:rgb(255,255,255); 
            
                /* 边框倒角 */  
                border-radius:10px;  
            
                /* 内边距 */  
                padding:4px; 
            }
            QMessageBox{
                image:url()
            }
            '''
        self.setStyleSheet(qss_modify)
        self.setupUi(self)
        
    def setupUi(self, modify_form):
        modify_form.setObjectName("modify_form")
        modify_form.resize(360, 540)
        self.title_label = QtWidgets.QLabel(modify_form)
        self.title_label.setGeometry(QtCore.QRect(90, 30, 171, 51))
        font = QtGui.QFont()
        font.setFamily("方正大黑简体")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.user_label = QtWidgets.QLabel(modify_form)
        self.user_label.setEnabled(True)
        self.user_label.setGeometry(QtCore.QRect(34, 104, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_label.setFont(font)
        self.user_label.setStyleSheet("")
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(modify_form)
        self.user_lineEdit.setGeometry(QtCore.QRect(144, 104, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setText("")
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.dept_lineEdit = QtWidgets.QLineEdit(modify_form)
        self.dept_lineEdit.setGeometry(QtCore.QRect(144, 154, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dept_lineEdit.setFont(font)
        self.dept_lineEdit.setObjectName("dept_lineEdit")
        self.dept_label = QtWidgets.QLabel(modify_form)
        self.dept_label.setGeometry(QtCore.QRect(34, 154, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dept_label.setFont(font)
        self.dept_label.setObjectName("dept_label")
        self.modify_btn = QtWidgets.QPushButton(modify_form)
        self.modify_btn.setGeometry(QtCore.QRect(27, 480, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modify_btn.setFont(font)
        self.modify_btn.setObjectName("modify_btn")
        self.reset_btn = QtWidgets.QPushButton(modify_form)
        self.reset_btn.setGeometry(QtCore.QRect(127, 480, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("reset_btn")
        self.quit_btn = QtWidgets.QPushButton(modify_form)
        self.quit_btn.setGeometry(QtCore.QRect(227, 480, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        self.mac_label = QtWidgets.QLabel(modify_form)
        self.mac_label.setGeometry(QtCore.QRect(34, 254, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mac_label.setFont(font)
        self.mac_label.setObjectName("mac_label")
        self.ip_label = QtWidgets.QLabel(modify_form)
        self.ip_label.setGeometry(QtCore.QRect(34, 204, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName("ip_label")
        self.mac_lineEdit = QtWidgets.QLineEdit(modify_form)
        self.mac_lineEdit.setGeometry(QtCore.QRect(144, 254, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mac_lineEdit.setFont(font)
        self.mac_lineEdit.setText("")
        self.mac_lineEdit.setObjectName("mac_lineEdit")
        self.ip_lineEdit = QtWidgets.QLineEdit(modify_form)
        self.ip_lineEdit.setGeometry(QtCore.QRect(144, 204, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_lineEdit.setFont(font)
        self.ip_lineEdit.setText("")
        self.ip_lineEdit.setObjectName("ip_lineEdit")
        self.room_lineEdit = QtWidgets.QLineEdit(modify_form)
        self.room_lineEdit.setGeometry(QtCore.QRect(144, 304, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.room_lineEdit.setFont(font)
        self.room_lineEdit.setText("")
        self.room_lineEdit.setObjectName("room_lineEdit")
        self.room_label = QtWidgets.QLabel(modify_form)
        self.room_label.setGeometry(QtCore.QRect(34, 304, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.room_label.setFont(font)
        self.room_label.setObjectName("room_label")
        self.switch_label = QtWidgets.QLabel(modify_form)
        self.switch_label.setGeometry(QtCore.QRect(34, 354, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.switch_label.setFont(font)
        self.switch_label.setObjectName("switch_label")
        self.switch_lineEdit = QtWidgets.QLineEdit(modify_form)
        self.switch_lineEdit.setGeometry(QtCore.QRect(144, 354, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.switch_lineEdit.setFont(font)
        self.switch_lineEdit.setText("")
        self.switch_lineEdit.setObjectName("switch_lineEdit")
        self.port_lineEdit = QtWidgets.QLineEdit(modify_form)
        self.port_lineEdit.setGeometry(QtCore.QRect(144, 404, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.port_lineEdit.setFont(font)
        self.port_lineEdit.setText("")
        self.port_lineEdit.setObjectName("port_lineEdit")
        self.port_label = QtWidgets.QLabel(modify_form)
        self.port_label.setGeometry(QtCore.QRect(34, 404, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.port_label.setFont(font)
        self.port_label.setObjectName("port_label")

        self.retranslateUi(modify_form)
        QtCore.QMetaObject.connectSlotsByName(modify_form)
        modify_form.setTabOrder(self.user_lineEdit, self.dept_lineEdit)
        modify_form.setTabOrder(self.dept_lineEdit, self.ip_lineEdit)
        modify_form.setTabOrder(self.ip_lineEdit, self.mac_lineEdit)
        modify_form.setTabOrder(self.mac_lineEdit, self.room_lineEdit)
        modify_form.setTabOrder(self.room_lineEdit, self.switch_lineEdit)
        modify_form.setTabOrder(self.switch_lineEdit, self.port_lineEdit)
        modify_form.setTabOrder(self.port_lineEdit, self.modify_btn)
        modify_form.setTabOrder(self.modify_btn, self.reset_btn)
        modify_form.setTabOrder(self.reset_btn, self.quit_btn)

    def retranslateUi(self, modify_form):
        _translate = QtCore.QCoreApplication.translate
        modify_form.setWindowTitle(_translate("modify_form", "Form"))
        self.title_label.setText(_translate("modify_form", "修改员工信息"))
        self.user_label.setText(_translate("modify_form", "姓    名："))
        self.dept_label.setText(_translate("modify_form", "部    门："))
        self.modify_btn.setText(_translate("modify_form", "修  改"))
        self.reset_btn.setText(_translate("modify_form", "重  置"))
        self.quit_btn.setText(_translate("modify_form", "退  出"))
        self.mac_label.setText(_translate("modify_form", "MAC 地址："))
        self.ip_label.setText(_translate("modify_form", "IP 地 址："))
        self.room_label.setText(_translate("modify_form", "房间编号："))
        self.switch_label.setText(_translate("modify_form", "交换机地址："))
        self.port_label.setText(_translate("modify_form", "交换机端口："))
        

    # 槽函数
    def modify_clicked(self):
        # 数据已经合法性判断过。
        name = self.user_lineEdit.text()
        dept = self.dept_lineEdit.text()
        ip = self.ip_lineEdit.text()
        mac = self.mac_lineEdit.text()
        room = self.room_lineEdit.text()
        switch = self.switch_lineEdit.text()
        port = self.port_lineEdit.text()

        if dept == '' or ip == '' or mac == '' or room == '' or switch == '' or port == '':
            print('信息不完整')
            reply = QMessageBox.about(self,'提示','请完善员工信息')
        else:
            rem = Re_manager()
            dept = rem.is_dept(dept)
            ip = rem.is_ip(ip)
            mac = rem.is_mac(mac)
            room = rem.is_room(room)
            switch = rem.is_switch(switch)
            port = rem.is_port(port)
            if  dept == None or ip == None or mac == None or room == None \
                or switch == None or port == None:
                print('格式不符合')
                reply = QMessageBox.about(self,'提示','请检查格式是否符合要求')
            else:
                mm = Mysql_manager()
                with mm:
                    sql = 'update em_info set em_dept = %s,em_ip = %s,em_mac = %s,em_room = %s,em_switch = %s, \
                        em_port = %s where em_name = %s'
                    mm.exe_db(sql,(dept,ip,mac,room,switch,port,name))
                    print('信息更新成功')
                    reply = QMessageBox.about(self,'提示',f'{name}的信息更新成功')
                    self.close()

    def reset_clicked(self):
        # 重置所有输入框
        self.user_lineEdit.setText('')
        self.dept_lineEdit.setText('')
        self.ip_lineEdit.setText('')
        self.mac_lineEdit.setText('')
        self.room_lineEdit.setText('')
        self.switch_lineEdit.setText('')
        self.port_lineEdit.setText('')
    def quit_clicked(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    em = Em_manager()
    em.show()

    # ae = Add_em()
    # ae.show()
    # de = Del_em()
    # de.show()
    # mo = Modify_em()
    # mo.show()
    sys.exit(app.exec_())