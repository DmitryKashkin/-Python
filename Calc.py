import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, \
    QLineEdit, QCheckBox, QButtonGroup, QHBoxLayout, QVBoxLayout, QTextEdit, QGridLayout, QMainWindow, QMessageBox
from QuestionareWidget import Ui_QuestionareWidget
from Calc_UI import Ui_Form


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.display=self.ui.display
        button_group = self.ui.buttonGroup
        button_group.buttonClicked.connect(self.button_clicked)
    #     scale_bg = QButtonGroup(self)
    #     scale_bg.addButton(self.ui.checkBox)
    #     scale_bg.addButton(self.ui.checkBox_2)
    #     scale_bg.addButton(self.ui.checkBox_3)
    #     scale_bg.addButton(self.ui.checkBox_4)
    #     scale_bg.buttonClicked.connect(self.checkboxClicked)
    #     close_button=self.ui.pushButton
    #     close_button.clicked.connect(self.close)
    #
    # def checkboxClicked(self, cb: QCheckBox):
    #     self.ui.label_7.setText(f'Выбрано: {self.ratings[cb.text()]} {cb.text()}')

    def button_clicked(self, button: QPushButton):

        if button.objectName() == 'button_clear':
            self.display.setText('0')
            return
        self.display.setText(button.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
