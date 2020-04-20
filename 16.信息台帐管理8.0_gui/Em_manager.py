# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\datacode\6.ui_files\add_em_beta2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
# from QtGui import *
from PyQt5.QtCore import *
from Mysql_manager import *
import sys

# qtgui.QHeaderView.Stretch


# 主窗口 
class Em_manager(QtWidgets.QMainWindow):
    # 默认进入主窗口显示所有信息
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show_em() # 进主界面默认显示
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.show_tableview = QtWidgets.QTableView(self.centralwidget)
        self.show_tableview.setGeometry(QtCore.QRect(190, 0, 680, 651))
        self.show_tableview.setObjectName("show_tableview")
        # self.show_tableview.horizontalHeader().setSectionResizeMode(qtgui.QHeaderView.Stretch)
        

        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(20, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.del_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_btn.setGeometry(QtCore.QRect(20, 200, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.del_btn.setFont(font)
        self.del_btn.setObjectName("del_btn")
        self.modify_btn = QtWidgets.QPushButton(self.centralwidget)
        self.modify_btn.setGeometry(QtCore.QRect(20, 280, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.modify_btn.setFont(font)
        self.modify_btn.setObjectName("modify_btn")
        self.query_btn = QtWidgets.QPushButton(self.centralwidget)
        self.query_btn.setGeometry(QtCore.QRect(20, 360, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.query_btn.setFont(font)
        self.query_btn.setObjectName("query_btn")
        self.home_btn = QtWidgets.QPushButton(self.centralwidget)
        self.home_btn.setGeometry(QtCore.QRect(20, 440, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.home_btn.setFont(font)
        self.home_btn.setObjectName("quit_btn")
        self.quit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.quit_btn.setGeometry(QtCore.QRect(20, 520, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 信号与槽绑定
        self.add_btn.clicked.connect(self.goto_add_em)
        self.del_btn.clicked.connect(self.goto_del_em)
        self.query_btn.clicked.connect(self.goto_query_em)
        self.modify_btn.clicked.connect(self.goto_modify_em)
        self.home_btn.clicked.connect(self.show_em)
        self.quit_btn.clicked.connect(self.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_btn.setText(_translate("MainWindow", "添加员工信息"))
        self.del_btn.setText(_translate("MainWindow", "删除员工信息"))
        self.modify_btn.setText(_translate("MainWindow", "修改员工信息"))
        self.query_btn.setText(_translate("MainWindow", "查询员工信息"))
        self.quit_btn.setText(_translate("MainWindow", "退 出 系 统"))
        self.home_btn.setText(_translate("MainWindow","显示所有员工"))

    # 槽函数。跳转到对应窗口
    def goto_add_em(self):
        # 首先显示子窗口，后期实现主窗口不可编辑
        ae.show()
    def goto_del_em(self):
        de.show()
    def goto_query_em(self):
        qe.show()
    def goto_modify_em(self):
        print('有待测试')

    # 显示所有员工信息函数
    def show_em(self):
        # 首先从数据库读取相关文件,注意考虑是否需要类变量还是临时变量
        mm = Mysql_manager()
        with mm:
            result = mm.query_db() # 返回值对应fetchall
            row_num = mm.cur.rowcount # 数据库实例还在内存。所以self.cur.rowcount还在内存，可以调用
            # 建立数据模型 这里需要得到qtsql
            self.model = QtGui.QStandardItemModel(row_num,4) # 建立二维数据模型

            # 建立数据模型的水平表头
            title = ['姓名','部门','IP','MAC']
            self.model.setHorizontalHeaderLabels(title)
            # 将数据模型和显示视图进行绑定
            self.show_tableview.setModel(self.model)
            #下面这里设置列宽必须在设置model以后，否则实际不会生效
            self.show_tableview.setColumnWidth(0,170)
            self.show_tableview.setColumnWidth(1,170)
            self.show_tableview.setColumnWidth(2,170)
            self.show_tableview.setColumnWidth(3,170)
            # 循环方式实例每个元素数据，绑定过。实例的数据自动同步到view
            # result 是个二维元组集合
            num = 0 # 循环递增使用
            for i in result:
                # i就是一维元组了
                item0 = QtGui.QStandardItem(i[0])
                item1 = QtGui.QStandardItem(i[1])
                item2 = QtGui.QStandardItem(i[2])
                item3 = QtGui.QStandardItem(i[3])

                # 四个实例元素分别赋值给对应位置元素
                self.model.setItem(num,0,item0)
                self.model.setItem(num,1,item1)
                self.model.setItem(num,2,item2)
                self.model.setItem(num,3,item3)
                # 每次循环完item0-3重置，重新赋值了
                num += 1



# 添加员工信息对话窗口
class Add_em(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 452)
        self.welcome_label = QtWidgets.QLabel(Dialog)
        self.welcome_label.setGeometry(QtCore.QRect(120, 40, 141, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(22)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        self.user_label = QtWidgets.QLabel(Dialog)
        self.user_label.setGeometry(QtCore.QRect(50, 123, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.user_lineEdit.setGeometry(QtCore.QRect(170, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.dept_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.dept_lineEdit.setGeometry(QtCore.QRect(170, 190, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dept_lineEdit.setFont(font)
        self.dept_lineEdit.setObjectName("dept_lineEdit")
        self.dept_label = QtWidgets.QLabel(Dialog)
        self.dept_label.setGeometry(QtCore.QRect(50, 183, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.dept_label.setFont(font)
        self.dept_label.setObjectName("dept_label")
        self.ip_label = QtWidgets.QLabel(Dialog)
        self.ip_label.setGeometry(QtCore.QRect(50, 243, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName("ip_label")
        self.ip_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.ip_lineEdit.setGeometry(QtCore.QRect(170, 250, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_lineEdit.setFont(font)
        self.ip_lineEdit.setObjectName("ip_lineEdit")
        self.mac_label = QtWidgets.QLabel(Dialog)
        self.mac_label.setGeometry(QtCore.QRect(50, 303, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.mac_label.setFont(font)
        self.mac_label.setObjectName("mac_label")
        self.mac_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.mac_lineEdit.setGeometry(QtCore.QRect(170, 310, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mac_lineEdit.setFont(font)
        self.mac_lineEdit.setObjectName("mac_lineEdit")
        self.confirm_label = QtWidgets.QPushButton(Dialog)
        self.confirm_label.setGeometry(QtCore.QRect(40, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.confirm_label.setFont(font)
        self.confirm_label.setObjectName("confirm_label")
        self.cancel_label = QtWidgets.QPushButton(Dialog)
        self.cancel_label.setGeometry(QtCore.QRect(150, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cancel_label.setFont(font)
        self.cancel_label.setObjectName("cancel_label")
        self.quit_label = QtWidgets.QPushButton(Dialog)
        self.quit_label.setGeometry(QtCore.QRect(260, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.quit_label.setFont(font)
        self.quit_label.setObjectName("quit_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # 绑定信号与自定义槽
        self.confirm_label.clicked.connect(self.goto_add_confirm) # 注意不要和主窗口的goto_add_em混淆
        self.cancel_label.clicked.connect(self.goto_add_cancel)  # 实际上不是label，而是btn
        self.quit_label.clicked.connect(self.goto_add_quit)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.welcome_label.setText(_translate("Dialog", "添 加 员 工"))
        self.user_label.setText(_translate("Dialog", "用户名称："))
        # self.user_lineEdit.setText(_translate("Dialog", "aaaa-aaaa-aaaa"))
        # self.dept_lineEdit.setText(_translate("Dialog", "aaaa-aaaa-aaaa"))
        self.dept_label.setText(_translate("Dialog", "部门名称："))
        self.ip_label.setText(_translate("Dialog", "IP地址："))
        # self.ip_lineEdit.setText(_translate("Dialog", "aaaa-aaaa-aaaa"))
        self.mac_label.setText(_translate("Dialog", "MAC地址："))
        # self.mac_lineEdit.setText(_translate("Dialog", "aaaa-aaaa-aaaa"))
        self.confirm_label.setText(_translate("Dialog", "确 认"))
        self.cancel_label.setText(_translate("Dialog", "取 消"))
        self.quit_label.setText(_translate("Dialog", "退 出"))

    def goto_add_confirm(self): # 防止重名，中间加上add标签
        # 首先从lineEdit获取文本内容
        name = self.user_lineEdit.text()
        dept = self.dept_lineEdit.text()
        ip = self.ip_lineEdit.text()
        mac = self.mac_lineEdit.text()
        
        params = (name,dept,ip,mac)
        # 建立数据库连接
        mm = Mysql_manager()
        with mm:
            sql = 'insert into em_info values(%s,%s,%s,%s)'
            mm.exe_db(sql,params)
            print(mm.cur.rowcount) # 判断是否添加成功

    def goto_add_cancel(self):
        # 将文本框内容设置为空
        self.user_lineEdit.setText('')
        self.dept_lineEdit.setText('')
        self.ip_lineEdit.setText('')
        self.mac_lineEdit.setText('')
    def goto_add_quit(self):
        self.close()

# 删除员工信息弹出窗口
class Del_em(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 452)
        self.welcome_label = QtWidgets.QLabel(Dialog)
        self.welcome_label.setGeometry(QtCore.QRect(120, 50, 141, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(22)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        self.user_label = QtWidgets.QLabel(Dialog)
        self.user_label.setGeometry(QtCore.QRect(50, 203, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.user_lineEdit.setGeometry(QtCore.QRect(170, 210, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setText("")
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.ip_label = QtWidgets.QLabel(Dialog)
        self.ip_label.setGeometry(QtCore.QRect(50, 273, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName("ip_label")
        self.ip_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.ip_lineEdit.setGeometry(QtCore.QRect(170, 280, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_lineEdit.setFont(font)
        self.ip_lineEdit.setText("")
        self.ip_lineEdit.setObjectName("ip_lineEdit")
        self.confirm_label = QtWidgets.QPushButton(Dialog)
        self.confirm_label.setGeometry(QtCore.QRect(40, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.confirm_label.setFont(font)
        self.confirm_label.setObjectName("confirm_label")
        self.cancel_label = QtWidgets.QPushButton(Dialog)
        self.cancel_label.setGeometry(QtCore.QRect(150, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cancel_label.setFont(font)
        self.cancel_label.setObjectName("cancel_label")
        self.quit_label = QtWidgets.QPushButton(Dialog)
        self.quit_label.setGeometry(QtCore.QRect(260, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.quit_label.setFont(font)
        self.quit_label.setObjectName("quit_label")
        self.notice_label = QtWidgets.QLabel(Dialog)
        self.notice_label.setGeometry(QtCore.QRect(90, 110, 231, 16))
        self.notice_label.setObjectName("notice_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.welcome_label.setText(_translate("Dialog", "删 除 员 工"))
        self.user_label.setText(_translate("Dialog", "用户名称："))
        self.ip_label.setText(_translate("Dialog", "IP地址："))
        self.confirm_label.setText(_translate("Dialog", "确 认"))
        self.cancel_label.setText(_translate("Dialog", "取 消"))
        self.quit_label.setText(_translate("Dialog", "退 出"))
        self.notice_label.setText(_translate("Dialog", "提示：通过名称或者IP来删除用户信息"))

# 查询员工对话窗
class Query_em(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 452)
        self.welcome_label = QtWidgets.QLabel(Dialog)
        self.welcome_label.setGeometry(QtCore.QRect(120, 60, 141, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(22)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        self.user_label = QtWidgets.QLabel(Dialog)
        self.user_label.setGeometry(QtCore.QRect(50, 203, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.user_lineEdit.setGeometry(QtCore.QRect(170, 210, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setText("")
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.ip_label = QtWidgets.QLabel(Dialog)
        self.ip_label.setGeometry(QtCore.QRect(50, 273, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName("ip_label")
        self.ip_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.ip_lineEdit.setGeometry(QtCore.QRect(170, 280, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_lineEdit.setFont(font)
        self.ip_lineEdit.setText("")
        self.ip_lineEdit.setObjectName("ip_lineEdit")
        self.confirm_label = QtWidgets.QPushButton(Dialog)
        self.confirm_label.setGeometry(QtCore.QRect(40, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.confirm_label.setFont(font)
        self.confirm_label.setObjectName("confirm_label")
        self.cancel_label = QtWidgets.QPushButton(Dialog)
        self.cancel_label.setGeometry(QtCore.QRect(150, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cancel_label.setFont(font)
        self.cancel_label.setObjectName("cancel_label")
        self.quit_label = QtWidgets.QPushButton(Dialog)
        self.quit_label.setGeometry(QtCore.QRect(260, 370, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.quit_label.setFont(font)
        self.quit_label.setObjectName("quit_label")
        self.notice_label = QtWidgets.QLabel(Dialog)
        self.notice_label.setGeometry(QtCore.QRect(90, 150, 231, 16))
        self.notice_label.setObjectName("notice_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # 信号与自定义槽关联
        self.confirm_label.clicked.connect(self.goto_query_confirm)
        self.cancel_label.clicked.connect(self.goto_query_cancel)
        self.quit_label.clicked.connect(self.goto_query_quit)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.welcome_label.setText(_translate("Dialog", "查 询 员 工"))
        self.user_label.setText(_translate("Dialog", "用户名称："))
        self.ip_label.setText(_translate("Dialog", "IP地址："))
        self.confirm_label.setText(_translate("Dialog", "确 认"))
        self.cancel_label.setText(_translate("Dialog", "取 消"))
        self.quit_label.setText(_translate("Dialog", "退 出"))
        self.notice_label.setText(_translate("Dialog", "提示：通过名称或者IP来查询用户信息"))

    # 槽函数 三个按钮对应事件
    def goto_query_confirm(self):
        name = self.user_lineEdit.text()
        ip = self.ip_lineEdit.text()
        # 对获取到的内容进行判断
        if name == '' and ip == '':
            reply = QtWidgets.QMessageBox.about(self,'notice','请输入用户姓名或者IP地址')
        elif name == '':
            mm = Mysql_manager()
            with mm:
                sql = 'select * from em_info where em_ip = %s'
                result = mm.exe_db(sql,ip)
                if mm.cur.rowcount == 0:
                    reply = QtWidgets.QMessageBox.about(self,'注意','系统没有当前IP相关信息')
                else:
                    # 建立数据模型
                    # 从这里开始在qe里面编写代码，但是数据模型和视图都在em里面，注意self别用错
                    em.model = QtGui.QStandardItemModel(mm.cur.rowcount,4)
                    title = ['姓名','部门','IP','MAC']
                    em.model.setHorizontalHeaderLabels(title) # 设置表头
                    em.show_tableview.setModel(em.model)
                    em.show_tableview.setColumnWidth(0,170)
                    em.show_tableview.setColumnWidth(1,170)
                    em.show_tableview.setColumnWidth(2,170)
                    em.show_tableview.setColumnWidth(3,170)
                    num = 0
                    for i in result:
                        item0 = QtGui.QStandardItem(i[0])
                        item1 = QtGui.QStandardItem(i[1])
                        item2 = QtGui.QStandardItem(i[2])
                        item3 = QtGui.QStandardItem(i[3])

                        em.model.setItem(num,0,item0)
                        em.model.setItem(num,1,item1)
                        em.model.setItem(num,2,item2)
                        em.model.setItem(num,3,item3)
                        num += 1
                    self.close()
        elif ip == '': # 此时用户名肯定有内容
            mm = Mysql_manager()
            with mm:
                sql = 'select * from em_info where em_name = %s'
                result = mm.exe_db(sql,name)
                if mm.cur.rowcount == 0:
                    reply = QtWidgets.QMessageBox.about(self,'提示','没有当前用户信息')
                else:
                    em.model = QtGui.QStandardItemModel(mm.cur.rowcount,4)
                    title = ['姓名','部门','IP','MAC']
                    em.model.setHorizontalHeaderLabels(title)
                    em.show_tableview.setModel(em.model)
                    em.show_tableview.setColumnWidth(0,170)
                    em.show_tableview.setColumnWidth(1,170)
                    em.show_tableview.setColumnWidth(2,170)
                    em.show_tableview.setColumnWidth(3,170)

                    num = 0
                    for i in result:
                        item0 = QtGui.QStandardItem(i[0])
                        item1 = QtGui.QStandardItem(i[1])
                        item2 = QtGui.QStandardItem(i[2])
                        item3 = QtGui.QStandardItem(i[3])

                        em.model.setItem(num,0,item0)
                        em.model.setItem(num,1,item1)
                        em.model.setItem(num,2,item2)
                        em.model.setItem(num,3,item3)
                        num += 1
                    self.close()
        else:  # name和ip都有输入
            mm = Mysql_manager()
            with mm:
                sql = 'select * from em_info where em_name = %s and em_ip = %s'
                result = mm.exe_db(sql,(name,ip))
                if mm.cur.rowcount == 0:
                    reply = QtWidgets.QMessageBox.about(self,'提示','没有当前查询信息')
                else:
                    em.model = QtGui.QStandardItemModel(mm.cur.rowcount,4)
                    title = ['姓名','部门','IP','MAC']
                    em.model.setHorizontalHeaderLabels(title)
                    em.show_tableview.setModel(em.model)
                    em.show_tableview.setColumnWidth(0,170)
                    em.show_tableview.setColumnWidth(1,170)
                    em.show_tableview.setColumnWidth(2,170)
                    em.show_tableview.setColumnWidth(3,170)

                    num = 0
                    for i in result:
                        item0 = QtGui.QStandardItem(i[0])
                        item1 = QtGui.QStandardItem(i[1])
                        item2 = QtGui.QStandardItem(i[2])
                        item3 = QtGui.QStandardItem(i[3])

                        em.model.setItem(num,0,item0)
                        em.model.setItem(num,1,item1)
                        em.model.setItem(num,2,item2)
                        em.model.setItem(num,3,item3)
                        num += 1

    def goto_query_cancel(self):
        self.user_lineEdit.setText('')
        self.ip_lineEdit.setText('')

    def goto_query_quit(self):
        self.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # 先将主窗口和弹窗实例化
    em = Em_manager()
    # em.setupUi(em) # 该语句放到构造函数。方便默认显示数据
    em.show()

    ae = Add_em()
    ae.setupUi(ae)

    de = Del_em()
    de.setupUi(de)

    qe = Query_em()
    qe.setupUi(qe)

    sys.exit(app.exec_())
