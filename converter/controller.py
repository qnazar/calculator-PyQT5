from converter.view import MainConverterUI, TempUI, MassUI, LengthUI
from converter.model import TempConverter, MassConverter, LengthConverter
from main_view import MainUI


class ConvController:
    def __init__(self, uplevel: MainUI):
        self.main_ctrl = uplevel

        self.temp_ui = TempUI
        self.mass_ui = MassUI
        self.length_ui = LengthUI

        self.temp_model = TempConverter
        self.mass_model = MassConverter
        self.length_model = LengthConverter

    def initUI(self, mode='temp'):
        if mode == 'temp':
            self.view = self.temp_ui()
            self.model = self.temp_model()
            self.connect_signals()
            return self.view
        elif mode == 'mass':
            self.view = self.mass_ui()
            self.model = self.mass_model()
            self.connect_signals()
            return self.view
        elif mode == 'length':
            self.view = self.length_ui()
            self.model = self.length_model()
            self.connect_signals()
            return self.view

    def switch_to_mass(self):
        self.view = self.mass_ui()
        self.model = self.mass_model()
        self.main_ctrl.switch_to_converter('mass')

    def switch_to_temp(self):
        self.view = self.temp_ui()
        self.model = self.temp_model()
        self.main_ctrl.switch_to_converter('temp')

    def switch_to_length(self):
        self.view = self.length_ui()
        self.model = self.length_model()
        self.main_ctrl.switch_to_converter('length')

    def convert(self):
        to = self.model.conversions[self.view.out_unit.currentText()]
        result = to(float(self.view.input_area.text()), self.view.in_unit.currentText())
        self.view.set_out_text(str(result))

    def connect_signals(self):
        self.view.temperature.clicked.connect(self.switch_to_temp)
        self.view.length.clicked.connect(self.switch_to_length)
        self.view.mass.clicked.connect(self.switch_to_mass)
        self.view.result.clicked.connect(self.convert)
