import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PySide2.QtCore import Qt


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        QLabel('Enter Login', self).move(130, 20)
        QLabel('Login', self).move(90, 55)
        self.button = QPushButton('Clear', self)
        self.button.move(160, 110)
        self.line_edit = QLineEdit(self)
        self.line_edit.setAlignment(Qt.AlignLeft)
        self.line_edit.move(130, 50)
        self.line_edit.resize(200, 20)
        self.button.clicked.connect(self.clear_entries)
        self.window_set()



    def window_set(self):
        self.setGeometry(1000, 500, 400, 300)
        self.setWindowTitle('Login window')
        self.show()


    def clear_entries(self):
        sender = self.sender()
        if sender.text() == 'Clear':
            self.line_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())
