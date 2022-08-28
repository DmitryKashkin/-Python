import sys
import time

from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, \
    QLineEdit, QCheckBox, QButtonGroup, QHBoxLayout, QVBoxLayout, QTextEdit, QGridLayout, \
    QMainWindow, QMessageBox, QInputDialog, QDialog, QDialogButtonBox
from PySide2.QtCore import QRect
from PySide2.QtGui import QFont, Qt
from TicTacToe import Ui_MainWindow
from ChooseDialog import Ui_ChooseDialog


class WarningDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WARNING!")
        QBtn = QDialogButtonBox.StandardButton.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        message = QLabel("СЮДА НЕ ХОДИ!")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.i_am = ''
        self.game_board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.i = 0
        self.j = 0
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.buttonGroup.buttonClicked.connect(self.click_btn)
        self.actionNew_Game.triggered.connect(self.new_game)
        self.new_game()

    def click_btn(self, btn: QPushButton):
        if btn.text() != '':
            self.warning_mesage()
        else:
            btn.setText(self.i_am)
            self.j = int(btn.objectName()[-2])
            self.i = int(btn.objectName()[-1])
            self.game_board[self.j][self.i] = self.i_am
            self.check_for_victory()
            print(self.game_board)

    def check_for_victory(self):

        pass

    def warning_mesage(self):
        dlg = WarningDialog()
        dlg.exec()

    def clear(self):
        for btn in self.buttonGroup.buttons():
            btn.setText('')
        self.game_board = [['', '', ''], ['', '', ''], ['', '', '']]

    def new_game(self):
        options = ("X", "0")
        pressed = False
        while not pressed:
            self.i_am, pressed = QInputDialog.getItem(self, "Вы за кого?", "Вы за кого?", options, 0, False)
        self.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
