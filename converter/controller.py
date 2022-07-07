from converter.view import MainConverterUI
from converter.model import TempConverter


class ConvController:
    def __init__(self):
        self.conv_ui = MainConverterUI
        self.model = TempConverter()

    def initUI(self):
        self.view = self.conv_ui()
        self.connect_signals()
        return self.view

    def convert(self):
        to = self.model.conversions[self.view.out_unit.currentText()]
        result = to(float(self.view.input_area.text()), self.view.in_unit.currentText())
        self.view.set_out_text(str(result))

    def connect_signals(self):
        self.view.result.clicked.connect(self.convert)
