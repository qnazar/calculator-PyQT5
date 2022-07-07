class TempConverter:
    def __init__(self):
        self.conversions = {'Celsius': self.to_celsius, 'Kelvin': self.to_kelvin, 'Fahrenheit': self.to_fahrenheit}

    @staticmethod
    def to_celsius(value, unit):
        if unit == 'Kelvin':
            result = value - 273.15
        elif unit == 'Fahrenheit':
            result = (value - 32) / 1.8
        else: result = value
        return result

    @staticmethod
    def to_fahrenheit(value, unit):
        if unit == 'Celsius':
            result = value * 1.8 + 32
        elif unit == 'Kelvin':
            result = (value-273.15) * 1.8 + 32
        else: result = value
        return result

    @staticmethod
    def to_kelvin(value, unit):
        if unit == 'Celsius':
            result = value + 273.15
        elif unit == 'Fahrenheit':
            result = value * 1.8 - 459.67
        else: result = value
        return result


class LengthConverter:
    def __init__(self):
        self.conversions = {}

    @staticmethod
    def to_metres():
        pass
