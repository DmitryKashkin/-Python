import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from Calc_UI import Ui_SuperCalc as Ui_Form


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('Super Calc')
        self.display = self.ui.display
        self.clear()
        # self.reg_a = 0.0
        # self.reset()
        # self.result = ''
        # self.display.setText('0.0')
        button_group_number = self.ui.buttonGroup_num
        button_group_number.buttonClicked.connect(self.button_clicked_num)
        button_group_operation = self.ui.buttonGroup_oper
        button_group_operation.buttonClicked.connect(self.button_clicked_operation)
        button_point = self.ui.pushButton_point
        button_point.clicked.connect(self.button_clicked_point)
        button_equal = self.ui.equal
        button_equal.clicked.connect(self.equal)
        button_clear = self.ui.button_clear
        button_clear.clicked.connect(self.clear)

    def clear(self):
        self.reg_a = 0.0
        self.reset()
        self.result = ''
        self.display.setText('0.0')

    def equal(self):
        self.reg_a = eval(self.result)
        self.reset()
        self.refresh()

    def reset(self):
        self.reg_b = ''
        self.operation = ""
        self.new_line = ''
        self.multiplier = 10

    def button_clicked_num(self, button: QPushButton):
        if self.multiplier == 10:
            self.reg_a = self.reg_a * self.multiplier + int(button.text())
        else:
            self.reg_a = self.reg_a + int(button.text()) * self.multiplier
            self.multiplier /= 10
        self.refresh()

    def button_clicked_operation(self, button: QPushButton):
        if self.operation == "":
            self.operation = button.text()
            self.new_line = '\n'
            self.reg_b = str(self.reg_a)
            self.reg_a = 0.0
            self.multiplier = 10
            self.refresh()
        else:
            if self.reg_a == 0.0:
                self.operation = button.text()
                self.refresh()
                return
            self.equal()
            self.button_clicked_operation(button)

        #
        # if button.objectName() == 'button_clear':
        #     self.display.setText('')
        #     return
        # if button.objectName() == 'equal':
        #     self.display.setText(str(eval(self.display.text())))
        #     return
        #
        # self.display.setText(self.display.text() + button.text())

    def button_clicked_point(self):
        self.multiplier = 0.1

    def refresh(self):
        self.result = self.reg_b + self.operation + str(self.reg_a)
        self.display.setText(self.reg_b + self.operation + self.new_line + str(self.reg_a))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
