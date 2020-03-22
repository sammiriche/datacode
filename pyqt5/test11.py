import sys
from PyQt5.QtWidgets import QWidget,qApp,QAction,QApplication,QMainWindow,QTextEdit
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('标题栏')
        self.setWindowIcon(QIcon('ljp.ico'))
        self.show()

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        exitAction = QAction(QIcon('lip.ico'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出程序提示')
        exitAction.triggered.connect(self.close)
        self.statusBar()

        menu = self.menuBar()
        fm = menu.addMenu('编辑')
        fm.addAction(exitAction)
        toolbar = self.addToolBar('text')
        toolbar.addAction(exitAction)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
