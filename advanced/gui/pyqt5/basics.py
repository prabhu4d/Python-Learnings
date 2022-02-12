from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Application(QMainWindow):
    WIDTH, HEIGHT = (400, 400)

    def __init__(self):
        super(Application, self).__init__()
        self.setGeometry(100, 100, self.WIDTH, self.HEIGHT)
        self.setWindowTitle("Counter")
        self.value = 0
        self.initUI()

    def initUI(self):
        self.label_count = QtWidgets.QLabel(self)
        self.label_count.setText(str(self.value))
        self.label_count.move(150, 150)

        self.btn_increment = QtWidgets.QPushButton(self)
        self.btn_increment.setText(" + ")
        self.btn_increment.move(250, 100)
        self.btn_increment.clicked.connect(self.increment_count)

        self.btn_decrement = QtWidgets.QPushButton(self)
        self.btn_decrement.setText(" - ")
        self.btn_decrement.move(50, 100)
        self.btn_decrement.clicked.connect(self.decrement_count)

        self.btn_reset = QtWidgets.QPushButton(self)
        self.btn_reset.setText(" 0 ")
        self.btn_reset.move(150, 100)
        self.btn_reset.clicked.connect(self.reset_count)

    def increment_count(self):
        self.value += 1
        self.update_count_label()

    def decrement_count(self):
        self.value -= 1
        self.update_count_label()

    def reset_count(self):
        self.value = 0
        self.update_count_label()

    def update_count_label(self):
        self.label_count.setText(f" {str(self.value)} ")
        self.updateUI()

    def updateUI(self):
        self.label_count.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = Application()

    win.show()
    sys.exit(app.exec_())


window()
