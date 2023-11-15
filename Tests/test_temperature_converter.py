import unittest
from subprocess import run
from random import randrange

# test if file exists

from os import sep
executable = f"..{sep}temperature_converter.py"


class UnitConverters:
    #                               <from>
    #                       Kelvin, Celsius, Fahrenheit
    #           Kelvin        < >      +         +
    #   <to>    Celsius        +      < >        +
    #           Fahrenheit     +       +        < >
    temperature_map = (
        ("{}",                          "{} - 273.15",      "({} - 273.15) * 9/5 + 32"),
        ("{} + 273.15",                 "{}",               "{} * 9/5 + 32"),
        ("({} - 32) * 5/9 + 273.15",    "({} - 32) * 5/9",  "{}"))
    forbidden_temperature = (0, -273.15, -459.67)
    temperature_dict = {"Kelvin": 0, "Celsius": 1, "Fahrenheit": 2}

    def convert_temperature(self, value, from_, to):
        if value < self.forbidden_temperature[self.temperature_dict[from_]]:
            return None
        conv = eval(self.temperature_map[self.temperature_dict[from_]][self.temperature_dict[to]].format(value))
        return conv


class TestTemperatureConverter(unittest.TestCase):
    temp_converter = UnitConverters()
    def test_celsius_to_celsius_good_high(self):
        temperature = round((randrange(10000, 50000)/100), 2)
        input_data = f"{temperature}\nC\nC"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Celsius"), 2)
        expected_output = f"{expected_temperature} °C"

        process = run(['python', executable], input=input_data.encode(), capture_output=True, text=True)

        self.assertIn(expected_output, process.stdout)

    def test_celsius_to_celsius_good_medium(self):
        temperature = round((randrange(0, 10000)/100), 2)
        input_data = f"{temperature}\nC\nC"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Celsius"), 2)
        expected_output = f"{expected_temperature} °C"

        process = run(['python', executable], input=input_data.encode(), capture_output=True, text=True)

        self.assertIn(expected_output, process.stdout)

    def test_celsius_to_celsius_good_low(self):
        temperature = round((randrange(-27315, 0)/100), 2)
        input_data = f"{temperature}\nC\nC"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Celsius"), 2)
        expected_output = f"{expected_temperature} °C"

        process = run(['python', executable], input=input_data.encode(), capture_output=True, text=True)

        self.assertIn(expected_output, process.stdout)

    def test_celsius_to_celsius_bad(self):
        input_data = f"24degrees\nC\nC"
        expected_output = f"format of entered temperature is wrong, not a number"

        process = run(['python', executable], input=input_data.encode(), capture_output=True, text=True)

        self.assertIn(expected_output, process.stdout)

    def test_celsius_below_zero(self):
        temperature = round((randrange(-99999, -27315)/100), 2)
        input_data = f"{temperature}\nC\nC"
        expected_output = f"temperature is below absolute zero, conversion is not possible"

        process = run(['python', executable], input=input_data.encode(), capture_output=True, text=True)

        self.assertIn(expected_output, process.stdout)

    def test_celsius_to_fahrenheit_good_high(self):
        temperature = round((randrange(10000, 50000)/100), 2)
        input_data = f"{temperature}\nC\nF"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Fahrenheit"), 2)
        expected_output = f"{expected_temperature} °F"

        process = run(['python', executable], input=input_data.encode(), capture_output=True, text=True)

        self.assertIn(expected_output, process.stdout)

    def test_celsius_to_fahrenheit_good_medium(self):
        temperature = round((randrange(0, 10000)/100), 2)
        input_data = f"{temperature}\nC\nF"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Fahrenheit"), 2)
        expected_output = f"{expected_temperature} °F"

        process = run(['python', executable], input=input_data.encode(), capture_output=True, text=True)

        self.assertIn(expected_output, process.stdout)

    def test_celsius_to_fahrenheit_good_low(self):
        temperature = round((randrange(-27315, 0)/100), 2)
        input_data = f"{temperature}\nC\nF"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Fahrenheit"), 2)
        expected_output = f"{expected_temperature} °F"

        process = run(['python', executable], input=input_data.encode(), capture_output=True, text=True)

        self.assertIn(expected_output, process.stdout)

    def test_celsius_to_fahrenheit_bad(self):
        input_data = f"24degrees\nC\nF"
        expected_output = f"format of entered temperature is wrong, not a number"

        process = run(['python', executable], input=input_data.encode(), capture_output=True, text=True)

        self.assertIn(expected_output, process.stdout)

    def test_celsius_to_kelvin_good_high(self):
        temperature = round((randrange(10000, 50000)/100), 2)
        input_data = f"{temperature}\nC\nK"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Kelvin"), 2)
        expected_output = f"{expected_temperature} K"

        process = run(['python', executable], input=input_data.encode(), capture_output=True, text=True)

        self.assertIn(expected_output, process.stdout)

    def test_celsius_to_kelvin_good_medium(self):
        temperature = round((randrange(0, 10000)/100), 2)
        input_data = f"{temperature}\nC\nK"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Kelvin"), 2)
        expected_output = f"{expected_temperature} K"

        process = run(['python', executable], input=input_data.encode(), capture_output=True, text=True)

        self.assertIn(expected_output, process.stdout)

    def test_celsius_to_kelvin_good_low(self):
        temperature = round((randrange(-27315, 0)/100), 2)
        input_data = f"{temperature}\nC\nK"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Kelvin"), 2)
        expected_output = f"{expected_temperature} K"

        process = run(['python', executable], input=input_data.encode(), capture_output=True, text=True)

        self.assertIn(expected_output, process.stdout)

    def test_celsius_to_kelvin_bad(self):
        input_data = f"24degrees\nC\nK"
        expected_output = f"format of entered temperature is wrong, not a number"

        process = run(['python', executable], input=input_data.encode(), capture_output=True, text=True)

        self.assertIn(expected_output, process.stdout)

    def test_fahrenheit_to_celsius_good_high(self):
        pass

    def test_fahrenheit_to_celsius_good_medium(self):
        pass

    def test_fahrenheit_to_celsius_good_low(self):
        pass

    def test_fahrenheit_to_celsius_bad(self):
        pass

    def test_fahrenheit_to_fahrenheit_good_high(self):
        pass

    def test_fahrenheit_to_fahrenheit_good_medium(self):
        pass

    def test_fahrenheit_to_fahrenheit_good_low(self):
        pass

    def test_fahrenheit_to_fahrenheit_bad(self):
        pass

    def test_fahrenheit_to_kelvin_good_high(self):
        pass

    def test_fahrenheit_to_kelvin_good_medium(self):
        pass

    def test_fahrenheit_to_kelvin_good_low(self):
        pass

    def test_fahrenheit_to_kelvin_bad(self):
        pass

    def test_kelvin_to_celsius_good_high(self):
        pass

    def test_kelvin_to_celsius_good_medium(self):
        pass

    def test_kelvin_to_celsius_good_low(self):
        pass

    def test_kelvin_to_celsius_bad(self):
        pass

    def test_kelvin_to_fahrenheit_good_high(self):
        pass

    def test_kelvin_to_fahrenheit_good_medium(self):
        pass

    def test_kelvin_to_fahrenheit_good_low(self):
        pass

    def test_kelvin_to_fahrenheit_bad(self):
        pass

    def test_kelvin_to_kelvin_good_high(self):
        pass

    def test_kelvin_to_kelvin_good_medium(self):
        pass

    def test_kelvin_to_kelvin_good_low(self):
        pass

    def test_kelvin_to_kelvin_bad(self):
        pass

    def test_unit_1_wrong(self):
        unit_1 = randrange(65, 90)
        input_data = f"36.66\n\nC"
        expected_output = f"format of entered temperature is wrong, not a number"

        process = run(['python', executable], input=input_data.encode(), capture_output=True, text=True)

        self.assertIn(expected_output, process.stdout)

    def test_unit_2_wrong(self):
        pass


if __name__ == "__main__":
    unittest.main()
