from PyQt5.QtWidgets import QPushButton, QGridLayout

from calculator.view import SimpleCalcUI


class EngineeringCalcUI(SimpleCalcUI):
    def __init__(self):
        super(EngineeringCalcUI, self).__init__()
        self.setFixedSize(300, 400)

    def create_buttons(self):
        self.buttons = {}
        buttons_layout = QGridLayout()
        buttons = {'MS':  (0, 0),
                   'MR':  (0, 1),
                   'п':   (0, 2),
                   'e':   (0, 3),
                   'mod': (0, 4),
                   '√':   (1, 0),
                   '(':   (1, 1),
                   ')':   (1, 2),
                   '//':  (1, 3),
                   '/':   (1, 4),
                   'x²':  (2, 0),
                   '7':   (2, 1),
                   '8':   (2, 2),
                   '9':   (2, 3),
                   '*':   (2, 4),
                   'x^y': (3, 0),
                   '4':   (3, 1),
                   '5':   (3, 2),
                   '6':   (3, 3),
                   '-':   (3, 4),
                   'n!':  (4, 0),
                   '1':   (4, 1),
                   '2':   (4, 2),
                   '3':   (4, 3),
                   '+':   (4, 4),
                   'C':   (5, 0),
                   '+/-': (5, 1),
                   '0':   (5, 2),
                   '.':   (5, 3),
                   '=':   (5, 4)
                   }
        for btn_txt, position in buttons.items():
            self.buttons[btn_txt] = QPushButton(btn_txt)
            self.buttons[btn_txt].setFixedSize(50, 50)
            buttons_layout.addWidget(self.buttons[btn_txt], position[0], position[1])
        self.general_layout.addLayout(buttons_layout)
