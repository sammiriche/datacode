# 程序的主界面
# 包含一个主窗口和多个dialog
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox,QHeaderView
import sys
from Mysql_manager import *
from Re_manager import * 

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

        # 绑定信号槽
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
            # self.tableView.setColumnWidth(0,190) # 第0列193宽度 
            # self.tableView.setColumnWidth(1,190)
            # self.tableView.setColumnWidth(2,190)
            # self.tableView.setColumnWidth(3,190)

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

    # 按钮的槽函数
    def query_clicked(self):
        pass
    def add_clicked(self):
        self.ae = Add_em()
        self.ae.show()
        # 类属性的推出按钮绑定到自身属性的显示方法（相当于刷新窗口显示）
        self.ae.quit_btn.clicked.connect(self.show_em)        
    def home_clicked(self):
        self.show_em()
    def modify_clicked(self):
        pass
    def del_clicked(self):
        pass
    def import_clicked(self):
        pass
    def export_clicked(self):
        pass
    def quit_clicked(self):
        self.close()

# 添加员工的对话窗口
class Add_em(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        pass
    def quit_clicked(self):
        self.close()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    em = Em_manager()
    em.show()

    # ae = Add_em()
    # ae.show()
    sys.exit(app.exec_())