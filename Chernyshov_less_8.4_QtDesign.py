import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, \
    QLineEdit, QCheckBox, QButtonGroup, QHBoxLayout, QVBoxLayout, QTextEdit, QGridLayout, QMainWindow, QMessageBox
from QuestionareWidget import Ui_QuestionareWidget


class MainWindow(QWidget):
    ratings = {'1': 'Ужасно', '2': 'Так себе', '3': 'Норм', '4': 'Отл'}

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_QuestionareWidget()
        self.ui.setupUi(self)
        scale_bg = QButtonGroup(self)
        scale_bg.addButton(self.ui.checkBox)
        scale_bg.addButton(self.ui.checkBox_2)
        scale_bg.addButton(self.ui.checkBox_3)
        scale_bg.addButton(self.ui.checkBox_4)
        scale_bg.buttonClicked.connect(self.checkboxClicked)
        close_button=self.ui.pushButton
        close_button.clicked.connect(self.close)

    def checkboxClicked(self, cb: QCheckBox):
        self.ui.label_7.setText(f'Выбрано: {self.ratings[cb.text()]} {cb.text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
