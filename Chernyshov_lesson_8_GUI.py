import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class MainWindow(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.setGeometry(*args)
        self.setWindowTitle('My window')
        self.lable = QLabel(self)
        self.lable.move(60, 30)
        self.lable.setText('Press')
        self.button = QPushButton('Ok', self)
        self.button.move(80, 70)
        self.button.clicked.connect(self.button_clicked)
        self.show()

        # self.initialize_ui(*args)

    # def initialize_ui(self, *args):

    def button_clicked(self):
        self.lable.setText('yes')
        self.lable.move(70, 40)
        self.button.setText('Ya!')
        self.button.move(90, 80)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow(100, 100, 400, 300)
    sys.exit(app.exec_())
