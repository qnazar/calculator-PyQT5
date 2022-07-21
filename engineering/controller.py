from functools import partial
from engineering.view import EngineeringCalcUI
from engineering.model import EngineModel
from calculator.controller import CalcController


class EngineCtrl(CalcController):
    def __init__(self):
        self.model = EngineModel()
        self.calc_ui = EngineeringCalcUI

    def initUI(self):
        self.view = self.calc_ui()
        self.connect_signals()
        return self.view

    def calculate_result(self):
        result = self.model.evaluate(expression=self.view.display_text())
        self.view.set_display_text(result)

    def build_expression(self, sub_exp):
        if self.view.display_text() == 'ERROR':
            self.view.clear_display()
        permission = self.validate_input(sub_exp)
        if sub_exp == 'n!' and permission:
            expression, last_operand = self.model.get_last_operand(self.view.display_text())
            expression = expression + str(self.model.factorial(eval(last_operand)))
        else:
            expression = self.view.display_text() + sub_exp if permission else self.view.display_text() + ''
        self.view.set_display_text(expression)

    def validate_input(self, sign):
        operators = '+-**//%'
        last_char = self.view.display_text()[-1] if self.view.display_text() else None
        if sign.isdecimal():  # no problems with digits
            return True
        if len(self.view.display_text()) == 0:  # first position can be digit, - or (
            return True if sign in '-(' else False
        if sign == '(':  # can be putted only after the operand
            return True if last_char in operators else False
        if sign == ')':  # only with presence of '(' and only after digit
            return True if '(' in self.view.display_text() and last_char.isdecimal() or last_char == ')' else False
        if sign == 'n!':
            return True if last_char.isdigit() or last_char == ')' else False
        if last_char in operators and sign in operators:
            return False
        return True

    def connect_signals(self):
        for btn_txt, btn in self.view.buttons.items():
            if btn_txt not in {'=', 'C', 'MS', 'MR'}:
                btn.clicked.connect(partial(self.build_expression, btn_txt))
        self.view.buttons['='].clicked.connect(self.calculate_result)
        self.view.display.returnPressed.connect(self.calculate_result)
        self.view.buttons['C'].clicked.connect(self.view.clear_display)
        return True
