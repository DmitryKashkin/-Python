import random
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PySide2.QtCore import Qt


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.line_edit = self.button = self.lable_one = self.lable_two = None
        self.lables()
        self.buttons()
        self.line_edits()
        self.window_set()

    def line_edits(self):
        self.line_edit = QLineEdit(self)
        self.line_edit.setAlignment(Qt.AlignLeft)
        self.line_edit.move(130, 50)
        self.line_edit.resize(200, 20)

    def buttons(self):
        self.button = QPushButton('Clear', self)
        self.button.move(160, 110)
        self.button.clicked.connect(self.clear_entries)

    def lables(self):
        self.lable_one = QLabel('Enter Login', self)
        self.lable_one.move(130, 20)
        self.lable_one.resize(200, 20)
        self.lable_two = QLabel('Login', self)
        self.lable_two.move(90, 55)

    def window_set(self):
        self.setGeometry(1000, 500, 400, 300)
        self.setWindowTitle('Login window')
        self.show()

    def clear_entries(self):
        sender = self.sender()
        if sender.text() == 'Clear':
            self.line_edit.clear()
            self.lable_one.setText(str(random.random()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())
