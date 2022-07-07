from functools import partial
from engineering.view import EngineeringCalcUI
from calculator.model import evaluate
from calculator.controller import CalcController


class EngineCtrl(CalcController):
    def __init__(self):
        self.model = evaluate
        self.calc_ui = EngineeringCalcUI
