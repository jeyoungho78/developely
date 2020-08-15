import sys

from MdIP import change_ip
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class AppWinIP(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Change Origin IP', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(lambda: change_ip("origin"))

        btn = QPushButton('Change Test IP', self)
        btn.move(50, 100)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(lambda: change_ip("new"))

        self.setWindowTitle('Change IP')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppWinIP()
    sys.exit(app.exec_())
