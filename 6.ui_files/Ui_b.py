# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pythoncode\6.ui_files\b.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys, os
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "matebook"))
        self.pushButton.setText(_translate("Form", "退出按钮"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    w = Ui_Form()    
    w.setupUi(form)               
    # w.show()
    sys.exit(app.exec_())