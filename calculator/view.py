from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import QtGui


class SimpleCalcUI(QWidget):
    def __init__(self):
        super(SimpleCalcUI, self).__init__()

        self.setWindowTitle('Calculator')
        self.setFixedSize(300, 300)

        self.general_layout = QVBoxLayout()
        self.setLayout(self.general_layout)

        self.create_display()
        self.create_buttons()

    def create_display(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.general_layout.addWidget(self.display)

    def create_buttons(self):
        self.buttons = {}
        buttons_layout = QGridLayout()
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4)
                   }
        for btn_txt, position in buttons.items():
            self.buttons[btn_txt] = QPushButton(btn_txt)
            self.buttons[btn_txt].setFixedSize(50, 50)
            buttons_layout.addWidget(self.buttons[btn_txt], position[0], position[1])
        self.general_layout.addLayout(buttons_layout)

    def set_display_text(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def display_text(self):
        return self.display.text()

    def clear_display(self):
        self.set_display_text('')

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        if e.key() == Qt.Key_C:
            self.clear_display()
        else:
            permission = self.validate_input(e.text())
            if permission:
                self.set_display_text(self.display_text() + e.text())

    def validate_input(self, sign):
        operators = '+-**//%'
        last_char = self.display_text()[-1] if self.display_text() else ''

        if sign.isdecimal():  # no problems with digits
            return True
        if len(self.display_text()) == 0:  # first position can be digit, - or (
            return True if sign in '-(' else False
        if last_char == '(':
            return True if sign.isdecimal() or sign == '-' else False
        if sign in operators:
            return True if last_char not in operators else False
        if sign == '(':  # can be putted only after the operand
            return True if last_char in operators else False
        if sign == ')':  # only with presence of '(' and only after digit
            return True if '(' in self.display_text() and last_char.isdecimal() or last_char == ')' else False
        if last_char in operators and sign in operators:
            return False
        return False
