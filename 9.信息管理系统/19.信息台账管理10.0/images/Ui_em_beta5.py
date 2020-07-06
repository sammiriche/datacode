# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pythoncode\19.信息台账管理10.0\images\em_beta5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_em_window(object):
    def setupUi(self, em_window):
        em_window.setObjectName("em_window")
        em_window.resize(960, 760)
        self.tableView = QtWidgets.QTableView(em_window)
        self.tableView.setGeometry(QtCore.QRect(0, 80, 960, 600))
        self.tableView.setStyleSheet("background-image: url(:/中间主体.png);")
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.bottom_frame = QtWidgets.QFrame(em_window)
        self.bottom_frame.setGeometry(QtCore.QRect(0, 680, 960, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.bottom_frame.setFont(font)
        self.bottom_frame.setStyleSheet("background-image: url(:/底部横幅.png);")
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.home_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.home_btn.setGeometry(QtCore.QRect(50, 8, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(15)
        self.home_btn.setFont(font)
        self.home_btn.setStyleSheet("QPushButton\n"
"{  \n"
"    /* 前景色 */  \n"
"    color:white;  \n"
" \n"
"    /* 背景色 */  \n"
"    background-color:rgb(43,100,76);  \n"
" \n"
"    /* 边框风格 */  \n"
"    border-style:outset;  \n"
" \n"
"    /* 边框宽度 */  \n"
"    border-width:0.5px;  \n"
" \n"
"    /* 边框颜色 */  \n"
"    border-color:rgb(255,255,255);  \n"
" \n"
"    /* 边框倒角 */  \n"
"    border-radius:10px;  \n"
"\n"
" \n"
"    /* 内边距 */  \n"
"    padding:4px;  \n"
"} \n"
"QPushButton:pressed\n"
"{\n"
"    color:#00ff00;\n"
"    background-color:rgb(40, 85, 20); /*改变背景色*/\n"
"    border-style:inset;/*改变边框风格*/\n"
"    padding-left:6px;\n"
"    padding-top:6px;\n"
"    border-color:rgb(255,0,0);\n"
"\n"
"}\n"
"")
        self.home_btn.setObjectName("home_btn")
        self.modify_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.modify_btn.setGeometry(QtCore.QRect(50, 45, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(15)
        self.modify_btn.setFont(font)
        self.modify_btn.setStyleSheet("QPushButton\n"
"{  \n"
"    /* 前景色 */  \n"
"    color:white;  \n"
" \n"
"    /* 背景色 */  \n"
"    background-color:rgb(43,100,76);  \n"
" \n"
"    /* 边框风格 */  \n"
"    border-style:outset;  \n"
" \n"
"    /* 边框宽度 */  \n"
"    border-width:0.5px;  \n"
" \n"
"    /* 边框颜色 */  \n"
"    border-color:rgb(255,255,255);  \n"
" \n"
"    /* 边框倒角 */  \n"
"    border-radius:10px;  \n"
"\n"
" \n"
"    /* 内边距 */  \n"
"    padding:4px;  \n"
"} \n"
"QPushButton:pressed\n"
"{\n"
"    color:#00ff00;\n"
"    background-color:rgb(40, 85, 20); /*改变背景色*/\n"
"    border-style:inset;/*改变边框风格*/\n"
"    padding-left:6px;\n"
"    padding-top:6px;\n"
"    border-color:rgb(255,0,0);\n"
"\n"
"}\n"
"")
        self.modify_btn.setObjectName("modify_btn")
        self.import_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.import_btn.setGeometry(QtCore.QRect(180, 45, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(12)
        self.import_btn.setFont(font)
        self.import_btn.setStyleSheet("QPushButton\n"
"{  \n"
"    /* 前景色 */  \n"
"    color:white;  \n"
" \n"
"    /* 背景色 */  \n"
"    background-color:rgb(43,100,76);  \n"
" \n"
"    /* 边框风格 */  \n"
"    border-style:outset;  \n"
" \n"
"    /* 边框宽度 */  \n"
"    border-width:0.5px;  \n"
" \n"
"    /* 边框颜色 */  \n"
"    border-color:rgb(255,255,255);  \n"
" \n"
"    /* 边框倒角 */  \n"
"    border-radius:10px;  \n"
"\n"
" \n"
"    /* 内边距 */  \n"
"    padding:4px;  \n"
"} \n"
"QPushButton:pressed\n"
"{\n"
"    color:#00ff00;\n"
"    background-color:rgb(40, 85, 20); /*改变背景色*/\n"
"    border-style:inset;/*改变边框风格*/\n"
"    padding-left:6px;\n"
"    padding-top:6px;\n"
"    border-color:rgb(255,0,0);\n"
"\n"
"}\n"
"")
        self.import_btn.setObjectName("import_btn")
        self.add_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.add_btn.setGeometry(QtCore.QRect(180, 8, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(15)
        self.add_btn.setFont(font)
        self.add_btn.setStyleSheet("QPushButton\n"
"{  \n"
"    /* 前景色 */  \n"
"    color:white;  \n"
" \n"
"    /* 背景色 */  \n"
"    background-color:rgb(43,100,76);  \n"
" \n"
"    /* 边框风格 */  \n"
"    border-style:outset;  \n"
" \n"
"    /* 边框宽度 */  \n"
"    border-width:0.5px;  \n"
" \n"
"    /* 边框颜色 */  \n"
"    border-color:rgb(255,255,255);  \n"
" \n"
"    /* 边框倒角 */  \n"
"    border-radius:10px;  \n"
"\n"
" \n"
"    /* 内边距 */  \n"
"    padding:4px;  \n"
"} \n"
"QPushButton:pressed\n"
"{\n"
"    color:#00ff00;\n"
"    background-color:rgb(40, 85, 20); /*改变背景色*/\n"
"    border-style:inset;/*改变边框风格*/\n"
"    padding-left:6px;\n"
"    padding-top:6px;\n"
"    border-color:rgb(255,0,0);\n"
"\n"
"}\n"
"")
        self.add_btn.setObjectName("add_btn")
        self.del_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.del_btn.setGeometry(QtCore.QRect(310, 8, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(15)
        self.del_btn.setFont(font)
        self.del_btn.setStyleSheet("QPushButton\n"
"{  \n"
"    /* 前景色 */  \n"
"    color:white;  \n"
" \n"
"    /* 背景色 */  \n"
"    background-color:rgb(43,100,76);  \n"
" \n"
"    /* 边框风格 */  \n"
"    border-style:outset;  \n"
" \n"
"    /* 边框宽度 */  \n"
"    border-width:0.5px;  \n"
" \n"
"    /* 边框颜色 */  \n"
"    border-color:rgb(255,255,255);  \n"
" \n"
"    /* 边框倒角 */  \n"
"    border-radius:10px;  \n"
"\n"
" \n"
"    /* 内边距 */  \n"
"    padding:4px;  \n"
"} \n"
"QPushButton:pressed\n"
"{\n"
"    color:#00ff00;\n"
"    background-color:rgb(40, 85, 20); /*改变背景色*/\n"
"    border-style:inset;/*改变边框风格*/\n"
"    padding-left:6px;\n"
"    padding-top:6px;\n"
"    border-color:rgb(255,0,0);\n"
"\n"
"}\n"
"")
        self.del_btn.setObjectName("del_btn")
        self.export_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.export_btn.setGeometry(QtCore.QRect(310, 45, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(12)
        self.export_btn.setFont(font)
        self.export_btn.setStyleSheet("QPushButton\n"
"{  \n"
"    /* 前景色 */  \n"
"    color:white;  \n"
" \n"
"    /* 背景色 */  \n"
"    background-color:rgb(43,100,76);  \n"
" \n"
"    /* 边框风格 */  \n"
"    border-style:outset;  \n"
" \n"
"    /* 边框宽度 */  \n"
"    border-width:0.5px;  \n"
" \n"
"    /* 边框颜色 */  \n"
"    border-color:rgb(255,255,255);  \n"
" \n"
"    /* 边框倒角 */  \n"
"    border-radius:10px;  \n"
"\n"
" \n"
"    /* 内边距 */  \n"
"    padding:4px;  \n"
"} \n"
"QPushButton:pressed\n"
"{\n"
"    color:#00ff00;\n"
"    background-color:rgb(40, 85, 20); /*改变背景色*/\n"
"    border-style:inset;/*改变边框风格*/\n"
"    padding-left:6px;\n"
"    padding-top:6px;\n"
"    border-color:rgb(255,0,0);\n"
"\n"
"}\n"
"")
        self.export_btn.setObjectName("export_btn")
        self.query_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.query_btn.setGeometry(QtCore.QRect(440, 8, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(15)
        self.query_btn.setFont(font)
        self.query_btn.setStyleSheet("QPushButton\n"
"{  \n"
"    /* 前景色 */  \n"
"    color:white;  \n"
" \n"
"    /* 背景色 */  \n"
"    background-color:rgb(43,100,76);  \n"
" \n"
"    /* 边框风格 */  \n"
"    border-style:outset;  \n"
" \n"
"    /* 边框宽度 */  \n"
"    border-width:0.5px;  \n"
" \n"
"    /* 边框颜色 */  \n"
"    border-color:rgb(255,255,255);  \n"
" \n"
"    /* 边框倒角 */  \n"
"    border-radius:10px;  \n"
"\n"
" \n"
"    /* 内边距 */  \n"
"    padding:4px;  \n"
"} \n"
"QPushButton:pressed\n"
"{\n"
"    color:#00ff00;\n"
"    background-color:rgb(40, 85, 20); /*改变背景色*/\n"
"    border-style:inset;/*改变边框风格*/\n"
"    padding-left:6px;\n"
"    padding-top:6px;\n"
"    border-color:rgb(255,0,0);\n"
"\n"
"}\n"
"")
        self.query_btn.setObjectName("query_btn")
        self.quit_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.quit_btn.setGeometry(QtCore.QRect(440, 45, 111, 31))
        font = QtGui.QFont()
        font.setFamily("华文隶书")
        font.setPointSize(15)
        self.quit_btn.setFont(font)
        self.quit_btn.setStyleSheet("QPushButton\n"
"{  \n"
"    /* 前景色 */  \n"
"    color:white;  \n"
" \n"
"    /* 背景色 */  \n"
"    background-color:rgb(43,100,76);  \n"
" \n"
"    /* 边框风格 */  \n"
"    border-style:outset;  \n"
" \n"
"    /* 边框宽度 */  \n"
"    border-width:0.5px;  \n"
" \n"
"    /* 边框颜色 */  \n"
"    border-color:rgb(255,255,255);  \n"
" \n"
"    /* 边框倒角 */  \n"
"    border-radius:10px;  \n"
"\n"
" \n"
"    /* 内边距 */  \n"
"    padding:4px;  \n"
"} \n"
"QPushButton:pressed\n"
"{\n"
"    color:#00ff00;\n"
"    background-color:rgb(40, 85, 20); /*改变背景色*/\n"
"    border-style:inset;/*改变边框风格*/\n"
"    padding-left:6px;\n"
"    padding-top:6px;\n"
"    border-color:rgb(255,0,0);\n"
"\n"
"}\n"
"")
        self.quit_btn.setObjectName("quit_btn")
        self.query_lineEdit = QtWidgets.QLineEdit(self.bottom_frame)
        self.query_lineEdit.setGeometry(QtCore.QRect(580, 8, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.query_lineEdit.setFont(font)
        self.query_lineEdit.setStyleSheet("QLineEdit\n"
"{  \n"
"    /* 前景色 */  \n"
"    color:white;  \n"
" \n"
"    /* 背景色 */  \n"
"    background-color:rgb(43,100,76);  \n"
" \n"
"    /* 边框风格 */  \n"
"    border-style:outset;  \n"
" \n"
"    /* 边框宽度 */  \n"
"    border-width:0.5px;  \n"
" \n"
"    /* 边框颜色 */  \n"
"    border-color:rgb(255,255,255);  \n"
" \n"
"    /* 边框倒角 */  \n"
"    border-radius:10px;  \n"
"\n"
" \n"
"    /* 内边距 */  \n"
"    padding:4px;  \n"
"} \n"
"\n"
"")
        self.query_lineEdit.setText("")
        self.query_lineEdit.setObjectName("query_lineEdit")
        self.top_frame = QtWidgets.QFrame(em_window)
        self.top_frame.setGeometry(QtCore.QRect(0, 0, 960, 80))
        self.top_frame.setStyleSheet("background-image: url(:/顶部横幅.png);")
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

import pic_rc
