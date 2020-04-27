# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\datacode\6.ui_files\em_beta3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(970, 761)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(215, 111, 771, 611))
        self.tableView.setObjectName("tableView")
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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
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
