from functools import partial
from calculator.view import SimpleCalcUI
from calculator.model import evaluate


class CalcController:
    def __init__(self):
        self.model = evaluate
        self.calc_ui = SimpleCalcUI

    def initUI(self):
        self.view = self.calc_ui()
        self.connect_signals()
        return self.view

    def calculate_result(self):
        result = self.model(expression=self.view.display_text())
        self.view.set_display_text(result)

    def build_expression(self, sub_exp):
        if self.view.display_text() == 'ERROR':
            self.view.clear_display()
        permission = self.validate_input(sub_exp)
        expression = self.view.display_text() + sub_exp if permission else self.view.display_text() + ''
        self.view.set_display_text(expression)

    def validate_input(self, sign):
        operands = '+-**//%'
        if sign.isdecimal():  # no problems with digits
            return True
        if len(self.view.display_text()) == 0:  # first position can be digit, - or (
            return True if sign in '-(' else False
        if sign == '(':  # can be putted only after the operand
            return True if self.view.display_text()[-1] in operands else False
        if sign == ')':  # only with presence of '(' and only after digit
            return True if '(' in self.view.display_text() and self.view.display_text()[-1].isdecimal() else False
        if self.view.display_text()[-1] in operands and sign in operands:
            return False
        return True

    def connect_signals(self):
        for btn_text, btn in self.view.buttons.items():
            if btn_text not in {'=', 'C'}:
                btn.clicked.connect(partial(self.build_expression, btn_text))
        self.view.buttons['='].clicked.connect(self.calculate_result)
        self.view.display.returnPressed.connect(self.calculate_result)
        self.view.buttons['C'].clicked.connect(self.view.clear_display)
        return True
