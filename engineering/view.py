from PyQt5.QtWidgets import QPushButton, QGridLayout

from calculator.view import SimpleCalcUI


class EngineeringCalcUI(SimpleCalcUI):
    def __init__(self):
        super(EngineeringCalcUI, self).__init__()

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
                   '=': (3, 4),
                   '**': (0, 5),
                   '//': (1, 5),
                   '%': (2, 5),
                   '!': (3, 5)
                   }
        for btn_txt, position in buttons.items():
            self.buttons[btn_txt] = QPushButton(btn_txt)
            self.buttons[btn_txt].setFixedSize(50, 50)
            buttons_layout.addWidget(self.buttons[btn_txt], position[0], position[1])
        self.general_layout.addLayout(buttons_layout)
