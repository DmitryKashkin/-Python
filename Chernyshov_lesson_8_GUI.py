import random
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, \
    QLineEdit, QCheckBox, QButtonGroup, QHBoxLayout, QVBoxLayout
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont


class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.line_edit = self.button = self.lable_one = self.lable_two = None
        self.lables()
        self.buttons()
        self.line_edits()
        self.window_set()

    def line_edits(self):
        self.line_edit = QLineEdit(self)
        self.line_edit.setAlignment(Qt.AlignCenter)
        self.line_edit.move(130, 50)
        self.line_edit.resize(200, 20)

    def buttons(self):
        self.button = QPushButton('Clear', self)
        self.button.move(160, 110)
        self.button.clicked.connect(self.clear_entries)

    def lables(self):
        self.lable_one = QLabel('Enter Login', self)
        self.lable_one.setAlignment(Qt.AlignCenter)
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


class CheckBoxWindow(QWidget):
    def __init__(self):
        super(CheckBoxWindow, self).__init__()
        self.lables()
        self.check_boxes()
        self.window_set()

    def window_set(self):
        self.setGeometry(1000, 500, 400, 300)
        self.setWindowTitle('the survey')
        self.show()

    def lables(self):
        self.lable_one = QLabel('What time do you wake up?', self)
        self.lable_one.move(20, 20)
        self.lable_one.resize(200, 20)
        self.lable_two = QLabel('choose something', self)
        self.lable_two.move(20, 250)
        self.lable_two.setMinimumSize(200, 20)

    def check_boxes(self):
        morning_6 = QCheckBox('6 utra', self)
        morning_6.move(20, 80)
        morning_6.stateChanged.connect(self.print_choise)
        morning_7 = QCheckBox('7 utra', self)
        morning_7.move(20, 100)
        morning_7.stateChanged.connect(self.print_choise)
        never_sleep = QCheckBox('I never sleep', self)
        never_sleep.move(20, 120)
        never_sleep.stateChanged.connect(self.print_choise)

    def print_choise(self, state):
        sender = self.sender()
        if state == Qt.Checked:
            choose = f'Selected: {sender.text()}.'
        else:
            choose = f'Unselected: {sender.text()}.'
        self.lable_two.setText(choose)


class EveningSurvey(QWidget):
    def __init__(self):
        super(EveningSurvey, self).__init__()
        self.lables()
        self.check_boxes()
        self.display_widgets()
        self.window_set()

    def lables(self):
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignHCenter)
        title = QLabel('Evening Survey')
        title.setFont((QFont('Arial', 17)))
        question = QLabel('Насколько плодотворно прошел Ваш день?')
        question.setAlignment(Qt.AlignHCenter)
        title_h_box = QHBoxLayout()
        title_h_box.addStretch()
        title_h_box.addWidget(title)
        title_h_box.addStretch()
        ratings = ['Ужасно', 'Так себе', 'Нормально', 'Отлично']
        ratings_h_box = QHBoxLayout()
        ratings_h_box.setSpacing(80)
        ratings_h_box.addStretch()
        for rating in ratings:
            rate_label = QLabel(rating, self)
            ratings_h_box.addWidget(rate_label)
        ratings_h_box.addStretch()
        cb_h_box = QHBoxLayout()
        cb_h_box.setSpacing(100)
        scale_gb = QButtonGroup(self)
        cb_h_box.addStretch()
        for cb in range(len(ratings)):
            scale_cb = QCheckBox(str(cb), self)
            cb_h_box.addWidget(scale_cb)
            scale_gb.addButton(scale_cb)
        cb_h_box.addStretch()
        scale_gb.buttonClicked.connect(self.checkbox_clicked)
        close_button = QPushButton('Close', self)
        close_button.clicked.connect(self.close)
        v_box = QVBoxLayout()
        v_box.addLayout(title_h_box)
        v_box.addWidget(question)
        v_box.addStretch(1)
        v_box.addLayout(ratings_h_box)
        v_box.addLayout(cb_h_box)
        v_box.addStretch(2)
        v_box.addWidget(self.label)
        v_box.addWidget(close_button)
        self.setLayout(v_box)

    def checkbox_clicked(self, cb):
        self.label.setText(f'Selected: {cb.text()}')

    def check_boxes(self):
        pass

    def display_widgets(self):
        pass

    def window_set(self):
        self.setGeometry(1000, 500, 400, 200)
        self.setWindowTitle('Evening Survey')
        self.show()


style = """
    QWidget {
        background-color: "green";
        color: "white";
    }
    QPushButton {
        font-size: 16px;
        background-color: "darkgreen"
    }
    QLineEdit {
        background-color: "white";
        color: "black";
    }
    QLabel {
        font-size: 12pt;
    }
    QCheckBox {
        font-size: 12pt;
    }
"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(style)

    window = EveningSurvey()
    sys.exit(app.exec_())