import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, \
    QLineEdit, QCheckBox, QButtonGroup, QHBoxLayout, QVBoxLayout, QTextEdit, QGridLayout, QMainWindow, QMessageBox
from QuestionareWidget import Ui_QuestionareWidget


class MainWindow(QWidget):
    ratings = {'0': 'Ужасно', '1': 'Так себе', '2': 'Норм', '3': 'Отл'}
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui=Ui_QuestionareWidget
        # self.ui.setupUI(self)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())