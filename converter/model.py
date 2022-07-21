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
        self.conversions = {'Metres': self.to_metres, 'Kilometres': self.to_kilometres, 'Inches': self.to_inches,
                            'Centimetres': self.to_centimetres, 'Millimetres': self.to_millimetres,
                            'Miles': self.to_miles, 'Yards': self.to_yards, 'Feet': self.to_feet}

    @staticmethod
    def to_metres(value, unit):
        if unit == 'Kilometres':
            result = value * 1000
        elif unit == 'Inches':
            result = value * 0.254
        elif unit == 'Centimetres':
            result = value / 100
        elif unit == 'Millimetres':
            result = value / 1000
        elif unit == 'Miles':
            result = value * 1609.344
        elif unit == 'Yards':
            result = value * 0.9144
        elif unit == 'Feet':
            result = value * 0.3048
        else: result = value
        return result

    @staticmethod
    def to_kilometres(value, unit):
        if unit == 'Kilometres':
            return value
        m = LengthConverter.to_metres(value, unit)
        return m / 1000

    @staticmethod
    def to_centimetres(value, unit):
        if unit == 'Centimetres':
            return value
        m = LengthConverter.to_metres(value, unit)
        return m * 100

    @staticmethod
    def to_millimetres(value, unit):
        if unit == 'Millimetres':
            return value
        m = LengthConverter.to_metres(value, unit)
        return m * 1000

    @staticmethod
    def to_miles(value, unit):
        if unit == 'Miles':
            return value
        m = LengthConverter.to_metres(value, unit)
        return round(m * 0.000621371192, 3)

    @staticmethod
    def to_inches(value, unit):
        if unit == 'Inches':
            return value
        m = LengthConverter.to_metres(value, unit)
        return round(m * 39.3700787, 3)

    @staticmethod
    def to_yards(value, unit):
        if unit == 'Yards':
            return value
        m = LengthConverter.to_metres(value, unit)
        return round(m * 1.0936133, 3)

    @staticmethod
    def to_feet(value, unit):
        if unit == 'Feet':
            return value
        m = LengthConverter.to_metres(value, unit)
        return round(m * 3.2808399, 3)
