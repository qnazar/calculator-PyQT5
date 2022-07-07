from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QPushButton, QHBoxLayout, QLabel, \
    QComboBox, QLineEdit


class MainConverterUI(QWidget):
    def __init__(self):
        super(MainConverterUI, self).__init__()
        self.setWindowTitle('Converter')
        self.setFixedSize(300, 300)

        self.general_layout = QVBoxLayout()
        self.setLayout(self.general_layout)

        self.create_menu()
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
        mass = QRadioButton('Mass')
        length = QRadioButton('Length')
        menu_layout.addWidget(mass)
        menu_layout.addWidget(length)
        temperature = QRadioButton('Temperature')
        temperature.setChecked(True)
        menu_layout.addWidget(temperature)
        menu_layout.setAlignment(Qt.AlignTop)
        self.general_layout.addLayout(menu_layout)

    def create_input_unit(self, state):
        input_unit_layout = QHBoxLayout()
        label = QLabel(state)
        input_unit_layout.addWidget(label)
        input_unit = QComboBox()
        input_unit.addItems(['Celsius', 'Kelvin', 'Fahrenheit'])
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