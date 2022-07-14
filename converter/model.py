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


class MassConverter:
    def __init__(self):
        self.conversions = {'Grams': self.to_grams, 'Kilograms': self.to_kilograms, 'Milligrams': self.to_milligrams,
                            'Pounds': self.to_pounds, 'Ounce': self.to_ounce}

    @staticmethod
    def to_grams(value, unit):
        if unit == 'Kilograms':
            result = value * 1000
        elif unit == 'Milligrams':
            result = value / 1000
        elif unit == 'Pounds':
            result = value * 453.59237
        elif unit == 'Ounce':
            result = value * 28.349
        else: result = value
        return result

    @staticmethod
    def to_kilograms(value, unit):
        if unit == 'Kilograms':
            return value
        grams = MassConverter.to_grams(value, unit)
        return grams / 1000

    @staticmethod
    def to_milligrams(value, unit):
        if unit == 'Milligrams':
            return value
        grams = MassConverter.to_grams(value, unit)
        return grams * 1000

    @staticmethod
    def to_pounds(value, unit):
        if unit == 'Pounds':
            return value
        elif unit == 'Ounce':
            return value / 16
        grams = MassConverter.to_grams(value, unit)
        return grams * 0.0022046

    @staticmethod
    def to_ounce(value, unit):
        if unit == 'Ounce':
            return value
        elif unit == 'Pounds':
            return value * 16
        grams = MassConverter.to_grams(value, unit)
        return grams * 0.0352739619

class LengthConverter:
    def __init__(self):
        self.conversions = {'Metres': self.to_metres, 'Inches': self.to_inches}

    @staticmethod
    def to_metres(value, unit):
        pass

    @staticmethod
    def to_inches(value, unit):
        pass
