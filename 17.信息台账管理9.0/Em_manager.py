# 程序的主界面
# 包含一个主窗口和多个dialog
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox,QHeaderView,QFileDialog
from PyQt5.QtCore import pyqtSignal
import sys
from Mysql_manager import *
from Re_manager import * 
from Excel_manager import *

class Em_manager(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height()) # 设置禁止拉伸
        self.show_em()
        

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(970, 761)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(215, 111, 760, 611))
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStyleSheet("QHeaderView::section{background:green;}")
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # 水平拉伸铺满

        self.add_btn = QtWidgets.QPushButton(Form)
        self.add_btn.setGeometry(QtCore.QRect(40, 240, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.del_btn = QtWidgets.QPushButton(Form)
        self.del_btn.setGeometry(QtCore.QRect(40, 310, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.del_btn.setFont(font)
        self.del_btn.setObjectName("del_btn")
        self.modify_btn = QtWidgets.QPushButton(Form)
        self.modify_btn.setGeometry(QtCore.QRect(40, 380, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.modify_btn.setFont(font)
        self.modify_btn.setObjectName("modify_btn")
        self.query_btn = QtWidgets.QPushButton(Form)
        self.query_btn.setGeometry(QtCore.QRect(40, 450, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.query_btn.setFont(font)
        self.query_btn.setObjectName("query_btn")
        self.import_btn = QtWidgets.QPushButton(Form)
        self.import_btn.setGeometry(QtCore.QRect(40, 520, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.import_btn.setFont(font)
        self.import_btn.setObjectName("import_btn")
        self.export_btn = QtWidgets.QPushButton(Form)
        self.export_btn.setGeometry(QtCore.QRect(40, 590, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.export_btn.setFont(font)
        self.export_btn.setObjectName("export_btn")
        self.quit_btn = QtWidgets.QPushButton(Form)
        self.quit_btn.setGeometry(QtCore.QRect(40, 670, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        self.home_btn = QtWidgets.QPushButton(Form)
        self.home_btn.setGeometry(QtCore.QRect(40, 170, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.home_btn.setFont(font)
        self.home_btn.setObjectName("home_btn")
        self.title_label = QtWidgets.QLabel(Form)
        self.title_label.setGeometry(QtCore.QRect(320, 20, 411, 71))
        font = QtGui.QFont()
        font.setFamily("方正大黑简体")
        font.setPointSize(25)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("QLabel{\n"
            "    rgb(255, 0, 0);\n"
            "    font: 25pt \"华文隶书\";\n"
            "}")
        self.title_label.setObjectName("title_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 绑定信号槽----------------
        self.home_btn.clicked.connect(self.home_clicked)
        self.add_btn.clicked.connect(self.add_clicked)
        self.del_btn.clicked.connect(self.del_clicked)
        self.modify_btn.clicked.connect(self.modify_clicked)
        self.query_btn.clicked.connect(self.query_clicked)
        self.import_btn.clicked.connect(self.import_clicked)
        self.export_btn.clicked.connect(self.export_clicked)
        self.quit_btn.clicked.connect(self.quit_clicked)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "主 界 面"))
        self.add_btn.setText(_translate("Form", "添 加 员 工"))
        self.del_btn.setText(_translate("Form", "删 除 员 工"))
        self.modify_btn.setText(_translate("Form", "修 改 员 工"))
        self.query_btn.setText(_translate("Form", "查 询 员 工"))
        self.import_btn.setWhatsThis(_translate("Form", "从excel导入信息"))
        self.import_btn.setText(_translate("Form", "导入员工信息"))
        self.export_btn.setText(_translate("Form", "导出员工信息"))
        self.quit_btn.setText(_translate("Form", "退 出 系 统"))
        self.home_btn.setText(_translate("Form", "主      页"))
        self.title_label.setText(_translate("Form", "员  工  信  息  管  理  系  统"))
    
    # 显示所有员工信息
    def show_em(self):
        # 首先获取实际行数
        mm = Mysql_manager()
        with mm:
            result = mm.db_show() # 返回二维元组
            # 显示控件已经建立，现在建立数据模型
            self.model = QtGui.QStandardItemModel(mm.cur.rowcount,4)
            self.title = ['姓名','部门','IP地址','MAC地址']
            self.model.setHorizontalHeaderLabels(self.title) 
            # self.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch) # 垂直拉伸铺满
            self.tableView.setModel(self.model) # 将控件和模型进行关联

            num = 0
            for i in result:
                item0 = QtGui.QStandardItem(i[0]) # 获取到的是姓名
                item1 = QtGui.QStandardItem(i[1])
                item2 = QtGui.QStandardItem(i[2])
                item3 = QtGui.QStandardItem(i[3])

                # 将数据显示到对应位置
                self.model.setItem(num,0,item0) # num行 0列，数值
                self.model.setItem(num,1,item1)
                self.model.setItem(num,2,item2)
                self.model.setItem(num,3,item3)

                num += 1

    def show_singel(self,result): # 这里的参数就是发射的返回值
        # 对接收的数据做显示处理
        # 建立数据模型
        print('跳转到主窗口显示单个函数成功')
        mm = Mysql_manager()
        with mm:
            self.model = QtGui.QStandardItemModel(len(result),4)
            title = ['姓名','部门','IP','MAC']
            self.model.setHorizontalHeaderLabels(title)
            self.tableView.setModel(self.model)
            num = 0
            for i in result:
                item0 = QtGui.QStandardItem(i[0])
                item1 = QtGui.QStandardItem(i[1])
                item2 = QtGui.QStandardItem(i[2])
                item3 = QtGui.QStandardItem(i[3])

                self.model.setItem(num,0,item0)
                self.model.setItem(num,1,item1)
                self.model.setItem(num,2,item2)
                self.model.setItem(num,3,item3)

                num += 1

    # 按钮的槽函数
    def query_clicked(self):
        self.qe = Query_em()
        self.qe.mysignal.connect(self.show_singel)  # 关联到显示单个的函数
        self.qe.show()
    def add_clicked(self):
        self.ae = Add_em()
        self.ae.show()
        # 类属性的推出按钮绑定到自身属性的显示方法（相当于刷新窗口显示）
        self.ae.quit_btn.clicked.connect(self.show_em)
    def home_clicked(self):
        self.show_em()
    def modify_clicked(self):
        # 首先获取鼠标选中的行标
        row_number = self.tableView.currentIndex().row()
        if row_number == -1:
            print('请先选择需要修改的行')
            reply = QMessageBox.about(self,'提示','请先选中需要修改的行')
        else:
            # 想办法把行标传值给子窗口
            self.mod = Modify_em()
            # 首先从对应行标从数据库中读取对应值
            name = self.model.item(row_number,0).text() # 获取对应行0列的文本值
            dept = self.model.item(row_number,1).text()
            ip = self.model.item(row_number,2).text()
            mac = self.model.item(row_number,3).text()
            self.mod.user_lineEdit.setText(name)
            self.mod.user_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
            self.mod.dept_lineEdit.setText(dept)
            self.mod.ip_lineEdit.setText(ip)
            self.mod.mac_lineEdit.setText(mac)


            self.mod.show()
    def del_clicked(self):
        self.de = Del_em()
        self.de.show()
    def import_clicked(self):
        # 打开文件对话框获取文件路径
        im_path = QFileDialog.getOpenFileName(self,'选择文件路径','D:\\pythoncode')
        # print(im_path) # 注意这里返回的是元组
        ex = Excel_manager()
        ex.import_excel(im_path[0])
        reply = QMessageBox.about(self,'提示','导表成功')
    def export_clicked(self):
        ex_path = QFileDialog.getSaveFileName(self,'保存文件路径','D:\\pythoncode','Excel files (*.xlsx)')
        # print(ex_path)
        ex = Excel_manager()
        ex.export_excel(ex_path[0])
        reply = QMessageBox.about(self,'提示','数据成功导出到表格')
    def quit_clicked(self):
        self.close()

# 添加员工的对话窗口
class Add_em(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height())
    def setupUi(self, Form):
        Form.setObjectName("Form")

        #下面两行设置只允许编辑当前窗口
        Form.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint | QtCore.Qt.Tool)
        Form.setWindowModality(QtCore.Qt.ApplicationModal)

        Form.resize(471, 495)
        self.title_label = QtWidgets.QLabel(Form)
        self.title_label.setGeometry(QtCore.QRect(150, 60, 171, 51))
        font = QtGui.QFont()
        font.setFamily("方正大黑简体")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.user_label = QtWidgets.QLabel(Form)
        self.user_label.setGeometry(QtCore.QRect(100, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(Form)
        self.user_lineEdit.setGeometry(QtCore.QRect(210, 150, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.dept_lineEdit = QtWidgets.QLineEdit(Form)
        self.dept_lineEdit.setGeometry(QtCore.QRect(210, 200, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dept_lineEdit.setFont(font)
        self.dept_lineEdit.setObjectName("dept_lineEdit")
        self.dept_label = QtWidgets.QLabel(Form)
        self.dept_label.setGeometry(QtCore.QRect(100, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dept_label.setFont(font)
        self.dept_label.setObjectName("dept_label")
        self.add_btn = QtWidgets.QPushButton(Form)
        self.add_btn.setGeometry(QtCore.QRect(95, 390, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.reset_btn = QtWidgets.QPushButton(Form)
        self.reset_btn.setGeometry(QtCore.QRect(195, 390, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("reset_btn")
        self.quit_btn = QtWidgets.QPushButton(Form)
        self.quit_btn.setGeometry(QtCore.QRect(295, 390, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        self.mac_label = QtWidgets.QLabel(Form)
        self.mac_label.setGeometry(QtCore.QRect(100, 300, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mac_label.setFont(font)
        self.mac_label.setObjectName("mac_label")
        self.ip_label = QtWidgets.QLabel(Form)
        self.ip_label.setGeometry(QtCore.QRect(100, 250, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName("ip_label")
        self.mac_lineEdit = QtWidgets.QLineEdit(Form)
        self.mac_lineEdit.setGeometry(QtCore.QRect(210, 300, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mac_lineEdit.setFont(font)
        self.mac_lineEdit.setText("")
        self.mac_lineEdit.setObjectName("mac_lineEdit")
        self.ip_lineEdit = QtWidgets.QLineEdit(Form)
        self.ip_lineEdit.setGeometry(QtCore.QRect(210, 250, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_lineEdit.setFont(font)
        self.ip_lineEdit.setText("")
        self.ip_lineEdit.setObjectName("ip_lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 绑定信号槽
        self.add_btn.clicked.connect(self.add_clicked)
        self.reset_btn.clicked.connect(self.reset_clicked)
        self.quit_btn.clicked.connect(self.close) # 这个信号绑定了两个槽，而且写在两个类里面。。

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title_label.setText(_translate("Form", "添 加 新 员 工"))
        self.user_label.setText(_translate("Form", "姓    名："))
        self.dept_label.setText(_translate("Form", "部    门："))
        self.add_btn.setText(_translate("Form", "添  加"))
        self.reset_btn.setText(_translate("Form", "重  置"))
        self.quit_btn.setText(_translate("Form", "退  出"))
        self.mac_label.setText(_translate("Form", "MAC 地址："))
        self.ip_label.setText(_translate("Form", "IP 地 址："))

    def add_clicked(self):
        # 获取文本框的值
        name = self.user_lineEdit.text()
        dept = self.dept_lineEdit.text()
        ip = self.ip_lineEdit.text()
        mac = self.mac_lineEdit.text()
        # 进行输入值检查
        if name == '' or dept == '' or ip == '' or mac == '':
            print('关键项输入不能为空')
            reply = QMessageBox.about(self,'提示','关键项输入不能为空')
        else:
            rem = Re_manager()
            name = rem.is_name(name)
            dept = rem.is_dept(dept)
            ip = rem.is_ip(ip)
            mac = rem.is_mac(mac)
            if name == None or dept == None or ip == None or mac == None:
                print('格式不符合要求')
                reply = QMessageBox.about(self,'提示','格式不符合正则要求')
            else:
                # 都符合要求，准备写入数据库
                mm = Mysql_manager()
                with mm:
                    sql = 'insert into em_info values(%s,%s,%s,%s)'
                    mm.db_exe(sql,(name,dept,ip,mac))
                    print('添加信息成功')
                    reply = QMessageBox.about(self,'提示','员工信息添加成功')
                    # 添加成功后清空文本框
                    self.user_lineEdit.setText('')
                    self.dept_lineEdit.setText('')
                    self.ip_lineEdit.setText('')
                    self.mac_lineEdit.setText('')

                    
        
    def reset_clicked(self):
        self.user_lineEdit.setText('')
        self.dept_lineEdit.setText('')
        self.ip_lineEdit.setText('')
        self.mac_lineEdit.setText('')
    def quit_clicked(self):
        self.close()
    
# 删除员工对话窗口
class Del_em(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height()) # 禁止拉伸
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(456, 347)
        self.title_label = QtWidgets.QLabel(Form)
        self.title_label.setGeometry(QtCore.QRect(150, 60, 251, 51))
        font = QtGui.QFont()
        font.setFamily("方正大黑简体")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.user_label = QtWidgets.QLabel(Form)
        self.user_label.setGeometry(QtCore.QRect(100, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(Form)
        self.user_lineEdit.setGeometry(QtCore.QRect(212, 150, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.ip_lineEdit = QtWidgets.QLineEdit(Form)
        self.ip_lineEdit.setGeometry(QtCore.QRect(210, 200, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_lineEdit.setFont(font)
        self.ip_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ip_lineEdit.setObjectName("ip_lineEdit")
        self.ip_label = QtWidgets.QLabel(Form)
        self.ip_label.setGeometry(QtCore.QRect(98, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName("ip_label")
        self.del_btn = QtWidgets.QPushButton(Form)
        self.del_btn.setGeometry(QtCore.QRect(95, 260, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.del_btn.setFont(font)
        self.del_btn.setObjectName("del_btn")
        self.reset_btn = QtWidgets.QPushButton(Form)
        self.reset_btn.setGeometry(QtCore.QRect(195, 260, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("reset_btn")
        self.quit_btn = QtWidgets.QPushButton(Form)
        self.quit_btn.setGeometry(QtCore.QRect(295, 260, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        self.tip_label = QtWidgets.QLabel(Form)
        self.tip_label.setGeometry(QtCore.QRect(170, 110, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tip_label.setFont(font)
        self.tip_label.setObjectName("tip_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        #  绑定信号槽
        self.del_btn.clicked.connect(self.del_clicked)
        self.reset_btn.clicked.connect(self.reset_clicked)
        self.quit_btn.clicked.connect(self.quit_clicked)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title_label.setText(_translate("Form", "删除员工信息"))
        self.user_label.setText(_translate("Form", "姓    名："))
        self.ip_label.setText(_translate("Form", "IP 地 址："))
        self.del_btn.setText(_translate("Form", "删  除"))
        self.reset_btn.setText(_translate("Form", "重  置"))
        self.quit_btn.setText(_translate("Form", "退  出"))
        self.tip_label.setText(_translate("Form", "通过使用人或者IP删除信息"))

    def del_clicked(self):
        name = self.user_lineEdit.text()
        ip = self.ip_lineEdit.text()
        if name == '' and ip == '':
            print('请至少输入一个条件')
            reply = QMessageBox.about(self,'提示','至少输入一个条件来删除')
        else:
            # 正则判断
            mm = Mysql_manager()
            rem = Re_manager()
            name = rem.is_name(name)
            ip = rem.is_ip(ip)
            if name == None and ip == None:
                print('输入格式不正确')
                reply = QMessageBox.about(self,'提示','输入格式不正确')
            elif name == None:  # 这里开始至少一个不为0
                with mm:
                    sql = 'delete from em_info where em_ip = %s'
                    mm.db_exe(sql,ip)
                    if mm.cur.rowcount == 0:
                        print('没有该IP相关信息')
                        reply = QMessageBox.about(self,'提示','没有该IP的相关信息')
                    else:
                        print('删除成功')
                        reply = QMessageBox.about(self,'提示',f'{ip}的相关信息已删除')
            elif ip == None:
                with mm:
                    sql = 'delete from em_info where em_name = %s'
                    mm.db_exe(sql,name)
                    if mm.cur.rowcount == 0:
                        print('没有该员工信息')
                        reply = QMessageBox.about(self,'提示','数据库没有该员工信息')
                    else:
                        print('删除成功')
                        reply = QMessageBox.about(self,'提示',f'{name}的相关信息已删除')
            else: # 最后一种情况，两个文本框都有内容
                with mm:
                    sql = 'select * from em_info where em_name = %s and em_ip = %s'
                    mm.db_exe(sql,(name,ip))
                    if mm.cur.rowcount == 0:
                        print('没有相关信息')
                        reply = QMessageBox.about(self,'提示','没有相关信息')
                    else:
                        print('删除成功')
                        reply = QMessageBox.about(self,'提示','信息删除成功')
        # 无论如何，清空文本框
        self.user_lineEdit.setText('')
        self.ip_lineEdit.setText('')
            

    def reset_clicked(self):
        self.user_lineEdit.setText('')
        self.ip_lineEdit.setText('')
    def quit_clicked(self):
        self.close()

# 查询员工对话窗口
class Query_em(QWidget):
    # 自定义一个发射信号，方便传递值给主窗口
    mysignal = pyqtSignal(tuple) # 这里一定要加返回值类型 # 自定义信号定义为类变量，放在类申明下面

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height())
        #下面两行设置只允许编辑当前窗口
        # self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint | QtCore.Qt.Tool)
        # self.setWindowModality(QtCore.Qt.ApplicationModal)


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(456, 347)
        self.title_label = QtWidgets.QLabel(Form)
        self.title_label.setGeometry(QtCore.QRect(150, 60, 171, 51))
        font = QtGui.QFont()
        font.setFamily("方正大黑简体")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.user_label = QtWidgets.QLabel(Form)
        self.user_label.setGeometry(QtCore.QRect(100, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(Form)
        self.user_lineEdit.setGeometry(QtCore.QRect(212, 150, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.ip_lineEdit = QtWidgets.QLineEdit(Form)
        self.ip_lineEdit.setGeometry(QtCore.QRect(210, 200, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_lineEdit.setFont(font)
        # self.ip_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password) # 设置显示模式，这里不需要
        self.ip_lineEdit.setObjectName("ip_lineEdit")
        # 默认设置不可编辑
        
        self.ip_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        # self.ip_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus) #  可以键盘鼠标都编辑

        self.ip_label = QtWidgets.QLabel(Form)
        self.ip_label.setGeometry(QtCore.QRect(98, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName("ip_label")
        self.query_btn = QtWidgets.QPushButton(Form)
        self.query_btn.setGeometry(QtCore.QRect(95, 280, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.query_btn.setFont(font)
        self.query_btn.setObjectName("query_btn")
        self.reset_btn = QtWidgets.QPushButton(Form)
        self.reset_btn.setGeometry(QtCore.QRect(195, 280, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("reset_btn")
        self.quit_btn = QtWidgets.QPushButton(Form)
        self.quit_btn.setGeometry(QtCore.QRect(295, 280, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        self.tip_label = QtWidgets.QLabel(Form)
        self.tip_label.setGeometry(QtCore.QRect(170, 110, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tip_label.setFont(font)
        self.tip_label.setObjectName("tip_label")
        self.name_radioButton = QtWidgets.QRadioButton(Form)
        self.name_radioButton.setGeometry(QtCore.QRect(110, 250, 101, 16))
        self.name_radioButton.setChecked(True)  # 设置默认选中状态
        self.name_radioButton.setObjectName("name_radioButton")
        self.ip_radioButton = QtWidgets.QRadioButton(Form)
        self.ip_radioButton.setGeometry(QtCore.QRect(260, 250, 101, 16))
        # self.ip_radioButton.setChecked(True)
        self.ip_radioButton.setObjectName("ip_radioButton")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.user_lineEdit, self.ip_lineEdit)
        Form.setTabOrder(self.ip_lineEdit, self.name_radioButton)
        Form.setTabOrder(self.name_radioButton, self.ip_radioButton)
        Form.setTabOrder(self.ip_radioButton, self.query_btn)
        Form.setTabOrder(self.query_btn, self.reset_btn)
        Form.setTabOrder(self.reset_btn, self.quit_btn)

        # 信号槽绑定  单选按钮
        self.name_radioButton.clicked.connect(self.name_radio_btn_clicked)
        self.ip_radioButton.clicked.connect(self.ip_radio_btn_clicked)

        # 信号槽绑定  提交等按钮 提交前有个checked判断
        self.query_btn.clicked.connect(self.query_clicked)
        self.reset_btn.clicked.connect(self.reset_clicked)
        self.quit_btn.clicked.connect(self.quit_clicked)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title_label.setText(_translate("Form", "查询员工信息"))
        self.user_label.setText(_translate("Form", "姓    名："))
        self.ip_label.setText(_translate("Form", "IP 地 址："))
        self.query_btn.setText(_translate("Form", "查  询"))
        self.reset_btn.setText(_translate("Form", "重  置"))
        self.quit_btn.setText(_translate("Form", "退  出"))
        self.tip_label.setText(_translate("Form", "通过使用人或者IP查询信息"))
        self.name_radioButton.setText(_translate("Form", "通过姓名查询"))
        self.ip_radioButton.setText(_translate("Form", "通过IP查询"))

    # radiobutton选中后调用函数
    def name_radio_btn_clicked(self):
        print('name按钮单击')
        self.user_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ip_lineEdit.setText('') # 把非选中项设置为空
        self.ip_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
    def ip_radio_btn_clicked(self):
        print('ip按钮单击')
        self.ip_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.user_lineEdit.setText('')
        self.user_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)

    # 普通按钮槽函数
    def query_clicked(self):
        if self.user_lineEdit == '' and self.ip_lineEdit == '':
            print('请输入查询条件')
        else:
            # 根据单选按钮判断
            mm = Mysql_manager()
            with mm:
                if self.name_radioButton.isChecked() == True: # 注意这里的判断条件，后面括号不能少
                    sql = 'select * from em_info where em_name = %s'
                    name = self.user_lineEdit.text()
                    result = mm.db_exe(sql,name)
                    if mm.cur.rowcount == 0:
                        print('没有相关信息')
                        reply = QMessageBox.about(self,'提示','查不到相关信息')
                    else:
                        # 这个时候把result发射到主窗口
                        print(type(result))
                        print(result)
                        self.mysignal.emit(result)
                else: # 通过IP查询
                    sql = 'select * from em_info where em_ip = %s'
                    ip = self.ip_lineEdit.text()
                    print(f'this {ip}')
                    result = mm.db_exe(sql,ip)
                    if mm.cur.rowcount == 0:
                        print('没有相关信息')
                        reply = QMessageBox.about(self,'提示','查不到相关IP信息')
                    else:
                        self.mysignal.emit(result)

    def reset_clicked(self):
        self.ip_lineEdit.setText('')
        self.user_lineEdit.setText('')
    def quit_clicked(self):
        self.close()

# 修改员工窗口
class Modify_em(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(471, 495)
        self.title_label = QtWidgets.QLabel(Form)
        self.title_label.setGeometry(QtCore.QRect(150, 60, 171, 51))
        font = QtGui.QFont()
        font.setFamily("方正大黑简体")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.user_label = QtWidgets.QLabel(Form)
        self.user_label.setGeometry(QtCore.QRect(100, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_label.setFont(font)
        self.user_label.setObjectName("user_label")
        self.user_lineEdit = QtWidgets.QLineEdit(Form)
        self.user_lineEdit.setGeometry(QtCore.QRect(210, 150, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.dept_lineEdit = QtWidgets.QLineEdit(Form)
        self.dept_lineEdit.setGeometry(QtCore.QRect(210, 200, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dept_lineEdit.setFont(font)
        self.dept_lineEdit.setObjectName("dept_lineEdit")
        self.dept_label = QtWidgets.QLabel(Form)
        self.dept_label.setGeometry(QtCore.QRect(100, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dept_label.setFont(font)
        self.dept_label.setObjectName("dept_label")
        self.modify_btn = QtWidgets.QPushButton(Form)
        self.modify_btn.setGeometry(QtCore.QRect(95, 390, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modify_btn.setFont(font)
        self.modify_btn.setObjectName("modify_btn")
        self.quit_btn = QtWidgets.QPushButton(Form)
        self.quit_btn.setGeometry(QtCore.QRect(295, 390, 80, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        self.mac_label = QtWidgets.QLabel(Form)
        self.mac_label.setGeometry(QtCore.QRect(100, 300, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mac_label.setFont(font)
        self.mac_label.setObjectName("mac_label")
        self.ip_label = QtWidgets.QLabel(Form)
        self.ip_label.setGeometry(QtCore.QRect(100, 250, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_label.setFont(font)
        self.ip_label.setObjectName("ip_label")
        self.mac_lineEdit = QtWidgets.QLineEdit(Form)
        self.mac_lineEdit.setGeometry(QtCore.QRect(210, 300, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mac_lineEdit.setFont(font)
        self.mac_lineEdit.setText("")
        self.mac_lineEdit.setObjectName("mac_lineEdit")
        self.ip_lineEdit = QtWidgets.QLineEdit(Form)
        self.ip_lineEdit.setGeometry(QtCore.QRect(210, 250, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ip_lineEdit.setFont(font)
        self.ip_lineEdit.setText("")
        self.ip_lineEdit.setObjectName("ip_lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.user_lineEdit, self.dept_lineEdit)
        Form.setTabOrder(self.dept_lineEdit, self.ip_lineEdit)
        Form.setTabOrder(self.ip_lineEdit, self.mac_lineEdit)
        Form.setTabOrder(self.mac_lineEdit, self.modify_btn)
        Form.setTabOrder(self.modify_btn, self.quit_btn)

        # modify的两个按钮槽函数
        self.modify_btn.clicked.connect(self.modify_clicked)
        self.quit_btn.clicked.connect(self.quit_clicked)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title_label.setText(_translate("Form", "修改员工信息"))
        self.user_label.setText(_translate("Form", "姓    名："))
        self.dept_label.setText(_translate("Form", "部    门："))
        self.modify_btn.setText(_translate("Form", "修  改"))
        self.quit_btn.setText(_translate("Form", "退  出"))
        self.mac_label.setText(_translate("Form", "MAC 地址："))
        self.ip_label.setText(_translate("Form", "IP 地 址："))

    def modify_clicked(self):
        # 连接数据库 把修改写进数据库
        # 首先获取文本框数据
        rem = Re_manager()
        name = self.user_lineEdit.text() # 没有变，不需要加判断语句
        dept = self.dept_lineEdit.text()
        ip = self.ip_lineEdit.text()
        mac = self.mac_lineEdit.text()
        if dept == '' or ip == '' or mac == '':
            print('修改内容需要填写')
            reply = QMessageBox.about(self,'提示','请完善修改内容')
        else:
            dept = rem.is_dept(dept)
            ip = rem.is_ip(ip)
            mac = rem.is_mac(mac)
            if dept == None or ip == None or mac == None:
                print('格式不符合要求')
                reply = QMessageBox.about(self,'提示','请按照格式修改相关内容')
            else:
                # 将数据更新到数据库
                mm = Mysql_manager()
                with mm:
                    sql = 'update em_info set em_dept = %s,em_ip = %s,em_mac = %s where em_name = %s'
                    mm.db_exe(sql,(dept,ip,mac,name))
                    print('信息更新')
                    reply = QMessageBox.about(self,'提示',f'{name}的信息修改成功')
                    self.close() # 修改完成关闭窗口，不然文本框还有内容不好处理

    def quit_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    em = Em_manager()
    em.show()

    # ae = Add_em()
    # ae.show()
    # de = Del_em()
    # de.show()
    # qe = Query_em()
    # qe.show()
    # mo = Modify_em()
    # mo.show()
    sys.exit(app.exec_())