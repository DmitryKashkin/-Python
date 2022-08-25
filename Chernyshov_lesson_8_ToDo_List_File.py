import json
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, \
    QLineEdit, QCheckBox, QButtonGroup, QHBoxLayout, QVBoxLayout, QTextEdit, QGridLayout, QMainWindow, QMessageBox
from PySide2.QtCore import Qt, Slot, Signal
from PySide2.QtGui import QFont


class ToDoListWidget(QWidget):
    done_signal = Signal(str, str)
    warning_signal = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.dict_todo = {}
        self.day_meet = []
        self.init_ui()
        for it in self.dict_todo:
            it.clicked.connect(self.it_is_done)

    def init_ui(self):
        main_grid = QGridLayout()
        todo_title = QLabel('ToDo List')
        todo_title.setFont(QFont('Arial', 24))
        todo_title.setAlignment(Qt.AlignCenter)
        mustdo_label = QLabel('Надо сделать')
        mustdo_label.setFont(QFont('Arial', 20))
        mustdo_label.setAlignment(Qt.AlignCenter)
        appts_label = QLabel('Запланированнные встречи')
        appts_label.setFont(QFont('Arial', 20))
        appts_label.setAlignment(Qt.AlignCenter)
        mustdo_grid = QGridLayout()
        mustdo_grid.setContentsMargins(5, 5, 5, 5)
        mustdo_grid.addWidget(mustdo_label, 0, 0, 1, 2)

        for position in range(1, 15):
            checkbox = QCheckBox()
            checkbox.setObjectName(str(position))
            linedit = QLineEdit('')
            linedit.setMinimumWidth(200)
            mustdo_grid.addWidget(checkbox, position, 0)
            mustdo_grid.addWidget(linedit, position, 1)
            self.dict_todo[checkbox] = linedit

        for i in self.dict_todo:
            self.dict_todo[i].setText('fdgdfgfg')
            print(i, 'dsfdf', self.dict_todo[i])

        A_16 = QFont('Arial', 16)
        morning_label = QLabel('Утро')
        morning_label.setFont(A_16)
        noon_label = QLabel("Обед")
        noon_label.setFont(A_16)
        evening_label = QLabel('Вечер')
        evening_label.setFont(A_16)
        appt_v_box = QVBoxLayout()
        appt_v_box.setContentsMargins(5, 5, 5, 5)
        evening_entry = QTextEdit()
        noon_entry = QTextEdit()
        morning_entry = QTextEdit()
        appt_v_box.addWidget(appts_label)
        appt_v_box.addWidget(morning_label)
        appt_v_box.addWidget(morning_entry)
        appt_v_box.addWidget(noon_label)
        appt_v_box.addWidget(noon_entry)
        appt_v_box.addWidget(evening_label)
        appt_v_box.addWidget(evening_entry)
        self.day_meet = [morning_entry, noon_entry, evening_entry]
        main_grid.addWidget(todo_title, 0, 0, 1, 2)
        main_grid.addLayout(mustdo_grid, 1, 0)
        main_grid.addLayout(appt_v_box, 1, 1)
        self.setLayout(main_grid)

    def it_is_done(self):
        sender = self.sender()
        if not self.dict_todo[sender].text():
            sender.setChecked(False)
            self.warning_signal.emit(sender.objectName())
            return
        if sender.isChecked():
            self.done_signal.emit(sender.objectName(), self.dict_todo[sender].text())

    @Slot()
    def clear_todo_list(self):
        for it in self.day_meet:
            it.clear()
        for checkbox, edit in self.dict_todo.items():
            checkbox.setChecked(False)
            edit.setText('')

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:/temp')[0]
        with open(fname, 'r') as f:
            data = json.load(f)
        for it in self.day_meet:
            it.setText(data[1].pop(0))
        for checkbox, edit in self.dict_todo.items():
            checkbox_state = data[0][checkbox.objectName()][0]
            checkbox.setChecked(checkbox_state)
            edit.setText(data[0][checkbox.objectName()][1])

    def load_todo_list(self):
        self.showDialog()

    def save_todo_list(self):
        data = ['', '']
        todo = {}
        fname = QFileDialog.getSaveFileName(self, 'Save file', 'c:/temp')[0]
        with open(fname, 'w') as f:
            for checkbox, edit in self.dict_todo.items():
                todo[checkbox.objectName()] = [checkbox.isChecked(), edit.text()]
            data[0] = todo
            todo = []
            for item in self.day_meet:
                todo.append(item.toPlainText())
            data[1] = todo
            json.dump(data, f)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.todo = ToDoListWidget()
        self.todo.done_signal.connect(self.it_is_done)
        self.todo.warning_signal.connect(self.warning_done)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('ToDo List')
        close_button = QPushButton('Close')
        close_button.clicked.connect(self.close)
        clear_button = QPushButton('Clear')
        clear_button.clicked.connect(self.todo.clear_todo_list)
        load_button = QPushButton('Load')
        load_button.clicked.connect(self.todo.load_todo_list)
        save_button = QPushButton('Save')
        save_button.clicked.connect(self.todo.save_todo_list)
        h_box = QHBoxLayout()
        h_box.addWidget(clear_button)
        h_box.addWidget(close_button)
        h_box.addWidget(load_button)
        h_box.addWidget(save_button)
        v_box = QVBoxLayout()
        v_box.addWidget(self.todo)
        v_box.addLayout(h_box)
        widget = QWidget(self)
        widget.setLayout(v_box)
        self.setCentralWidget(widget)
        self.setMaximumHeight(500)
        self.show()

    @Slot(str, str)
    def it_is_done(self, number, description):
        QMessageBox().information(self, 'Внимание!', f'Дело "{description}" под №{number} выполнено!',
                                  QMessageBox.Ok, QMessageBox.Ok)

    @Slot(str)
    def warning_done(self, number):
        QMessageBox().warning(self, 'Внимание!', f'Дело №{number} не заполнено!',
                              QMessageBox.Ok, QMessageBox.Ok)


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
    # app.setStyleSheet(style)

    window = MainWindow()
    sys.exit(app.exec_())
