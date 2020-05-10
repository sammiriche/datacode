# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pythoncode\19.信息台账管理10.0\images\login_beta4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import *
# import pic
import sys

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 400)
        # Form.setStyleSheet("#Form{\n"
        #     "background-image: url(:/login_bg2.png);\n"
        #     "}")

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./login_bg2.png")))  
        self.setPalette(palette)

        # self.tableView = QtWidgets.QTableView(Form)
        # self.tableView.setGeometry(QtCore.QRect(225, 111, 421, 301))
        # self.tableView.setStyleSheet("background-image: url(:/login_bg2.png);")
        # self.tableView.setObjectName("tableView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

# import pic

if __name__ == "__main__":
    app = QApplication(sys.argv)
    uu = Ui_Form()
    uu.setupUi(uu)
    uu.show()
    sys.exit(app.exec_())
