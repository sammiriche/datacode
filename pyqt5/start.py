from Ui_layout import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
if __name__ =='__main__':
    app = QApplication(sys.argv)
    form = QtWidgets.QWidget()
    aa = Ui_Form()
    aa.setupUi(form)
    form.show()
    sys.exit(app.exec_())
    