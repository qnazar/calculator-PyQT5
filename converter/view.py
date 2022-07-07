from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QPushButton, QHBoxLayout, QLabel, \
    QComboBox, QLineEdit


class MainConverterUI(QWidget):
    name = None
    items = []

    def __init__(self):
        super(MainConverterUI, self).__init__()

        self.general_layout = QVBoxLayout()
        self.setLayout(self.general_layout)

        self.create_menu()
        self.create_label()
        self.in_unit = self.create_input_unit('From')
        self.input_area = self.create_display()

        self.result = QPushButton('Convert')
        self.result.setFixedSize(100, 40)

        self.general_layout.addWidget(self.result)

        self.out_unit = self.create_input_unit('To')
        self.output_area = self.create_display()
        self.output_area.setReadOnly(True)

    def create_menu(self):
        menu_layout = QHBoxLayout()
        self.mass = QRadioButton('Mass')
        self.length = QRadioButton('Length')
        menu_layout.addWidget(self.mass)
        menu_layout.addWidget(self.length)
        self.temperature = QRadioButton('Temperature')
        # self.temperature.setChecked(True)
        menu_layout.addWidget(self.temperature)
        menu_layout.setAlignment(Qt.AlignTop)
        self.general_layout.addLayout(menu_layout)

    def create_label(self):
        self.label = QLabel(self.name)
        self.label.setAlignment(Qt.AlignCenter)
        self.general_layout.addWidget(self.label)

    def create_input_unit(self, state):
        input_unit_layout = QHBoxLayout()
        label = QLabel(state)
        input_unit_layout.addWidget(label)
        input_unit = QComboBox()
        input_unit.addItems(self.items)
        input_unit_layout.addWidget(input_unit)
        self.general_layout.addLayout(input_unit_layout)
        return input_unit

    def create_display(self):
        display = QLineEdit()
        display.setFixedHeight(50)
        display.setAlignment(Qt.AlignLeft)
        self.general_layout.addWidget(display)
        return display

    def set_out_text(self, result):
        self.output_area.setText(result)


class TempUI(MainConverterUI):
    name = 'Temperature'
    items = ['Celsius', 'Kelvin', 'Fahrenheit']


class MassUI(MainConverterUI):
    name = 'Mass'
    items = ['Grams', 'Kilograms']


class LengthUI(MainConverterUI):
    pass
