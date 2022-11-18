from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import time

# (venv) D:\Study\Projects\PycharmProjects\playground\fromdesigner>pyuic5 -x test.ui -o test.py


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 300, 300)  # x, y, width, height
        self.setWindowTitle('Maimuna APP')

        self.init_ui()

    def init_ui(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText('Label1')
        self.label1.move(50, 50)  # x, y

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText('Click')
        self.button1.move(100, 100)
        self.button1.clicked.connect(self.button1_click)

    def button1_click(self):
        text = self.button1.text()      # get the text attribute of the button
        self.label1.setText(text)
        self.update()

    def update(self):
        self.label1.adjustSize()    # adjust size to hold the text inside


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()






















