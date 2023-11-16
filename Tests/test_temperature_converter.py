import unittest
from subprocess import run, PIPE, Popen
from random import randint

from os import sep, path, abort
executable = f"Source{sep}temperature_converter.py"

if not path.exists(executable):
    print(f"Fatal error: executable \'{executable}\' not found!")
    abort()

class UnitConverters:
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
        temperature = round((randint(10000, 50000)/100), 2)
        input_data = f"{temperature}\nC\nC\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Celsius"), 2)
        expected_output = f"{expected_temperature} °C"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_celsius_to_celsius_good_medium(self):
        temperature = round((randint(0, 10000)/100), 2)
        input_data = f"{temperature}\nC\nC\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Celsius"), 2)
        expected_output = f"{expected_temperature} °C"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_celsius_to_celsius_good_low(self):
        temperature = round((randint(-27315, 0)/100), 2)
        input_data = f"{temperature}\nC\nC\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Celsius"), 2)
        expected_output = f"{expected_temperature} °C"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_celsius_bad(self):
        input_data = f"24degrees\nC\nC\n"
        expected_output = f"format of entered temperature is wrong, not a number"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_celsius_below_zero(self):
        temperature = round((randint(-99999, -27315)/100), 2)
        input_data = f"{temperature}\nC\nC\n"
        expected_output = f"temperature is below absolute zero, conversion is not possible"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_celsius_to_fahrenheit_good_high(self):
        temperature = round((randint(10000, 50000)/100), 2)
        input_data = f"{temperature}\nC\nF\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Fahrenheit"), 2)
        expected_output = f"{expected_temperature} °F"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_celsius_to_fahrenheit_good_medium(self):
        temperature = round((randint(0, 10000)/100), 2)
        input_data = f"{temperature}\nC\nF\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Fahrenheit"), 2)
        expected_output = f"{expected_temperature} °F"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_celsius_to_fahrenheit_good_low(self):
        temperature = round((randint(-27315, 0)/100), 2)
        input_data = f"{temperature}\nC\nF\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Fahrenheit"), 2)
        expected_output = f"{expected_temperature} °F"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_celsius_to_kelvin_good_high(self):
        temperature = round((randint(10000, 50000)/100), 2)
        input_data = f"{temperature}\nC\nK\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Kelvin"), 2)
        expected_output = f"{expected_temperature} K"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_celsius_to_kelvin_good_medium(self):
        temperature = round((randint(0, 10000)/100), 2)
        input_data = f"{temperature}\nC\nK\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Kelvin"), 2)
        expected_output = f"{expected_temperature} K"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_celsius_to_kelvin_good_low(self):
        temperature = round((randint(-27315, 0)/100), 2)
        input_data = f"{temperature}\nC\nK\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Celsius", "Kelvin"), 2)
        expected_output = f"{expected_temperature} K"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_fahrenheit_to_celsius_good_high(self):
        temperature = round((randint(21200, 93200)/100), 2)
        input_data = f"{temperature}\nF\nC\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Fahrenheit", "Celsius"), 2)
        expected_output = f"{expected_temperature} °C"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_fahrenheit_to_celsius_good_medium(self):
        temperature = round((randint(3200, 21200)/100), 2)
        input_data = f"{temperature}\nF\nC\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Fahrenheit", "Celsius"), 2)
        expected_output = f"{expected_temperature} °C"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_fahrenheit_to_celsius_good_low(self):
        temperature = round((randint(-45967, -3200)/100), 2)
        input_data = f"{temperature}\nF\nC\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Fahrenheit", "Celsius"), 2)
        expected_output = f"{expected_temperature} °C"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_fahrenheit_to_fahrenheit_good_high(self):
        temperature = round((randint(21200, 93200)/100), 2)
        input_data = f"{temperature}\nF\nF\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Fahrenheit", "Fahrenheit"), 2)
        expected_output = f"{expected_temperature} °F"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_fahrenheit_to_fahrenheit_good_medium(self):
        temperature = round((randint(3200, 21200)/100), 2)
        input_data = f"{temperature}\nF\nF\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Fahrenheit", "Fahrenheit"), 2)
        expected_output = f"{expected_temperature} °F"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_fahrenheit_to_fahrenheit_good_low(self):
        temperature = round((randint(-45967, -3200)/100), 2)
        input_data = f"{temperature}\nF\nF\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Fahrenheit", "Fahrenheit"), 2)
        expected_output = f"{expected_temperature} °F"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_fahrenheit_bad(self):
        input_data = f"24degrees\nF\nF\n"
        expected_output = f"format of entered temperature is wrong, not a number"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_fahrenheit_below_zero(self):
        temperature = round((randint(-99999, -45967)/100), 2)
        input_data = f"{temperature}\nF\nF\n"
        expected_output = f"temperature is below absolute zero, conversion is not possible"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_fahrenheit_to_kelvin_good_high(self):
        temperature = round((randint(21200, 93200)/100), 2)
        input_data = f"{temperature}\nF\nK\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Fahrenheit", "Kelvin"), 2)
        expected_output = f"{expected_temperature} K"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_fahrenheit_to_kelvin_good_medium(self):
        temperature = round((randint(3200, 21200)/100), 2)
        input_data = f"{temperature}\nF\nK\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Fahrenheit", "Kelvin"), 2)
        expected_output = f"{expected_temperature} K"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_fahrenheit_to_kelvin_good_low(self):
        temperature = round((randint(-45967, -3200)/100), 2)
        input_data = f"{temperature}\nF\nK\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Fahrenheit", "Kelvin"), 2)
        expected_output = f"{expected_temperature} K"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_kelvin_to_celsius_good_high(self):
        temperature = round((randint(37315, 77315)/100), 2)
        input_data = f"{temperature}\nK\nC\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Kelvin", "Celsius"), 2)
        expected_output = f"{expected_temperature} °C"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_kelvin_to_celsius_good_medium(self):
        temperature = round((randint(27315, 37315)/100), 2)
        input_data = f"{temperature}\nK\nC\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Kelvin", "Celsius"), 2)
        expected_output = f"{expected_temperature} °C"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_kelvin_to_celsius_good_low(self):
        temperature = round((randint(0, 27315)/100), 2)
        input_data = f"{temperature}\nK\nC\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Kelvin", "Celsius"), 2)
        expected_output = f"{expected_temperature} °C"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_kelvin_to_fahrenheit_good_high(self):
        temperature = round((randint(37315, 77315)/100), 2)
        input_data = f"{temperature}\nK\nF\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Kelvin", "Fahrenheit"), 2)
        expected_output = f"{expected_temperature} °F"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_kelvin_to_fahrenheit_good_medium(self):
        temperature = round((randint(27315, 37315)/100), 2)
        input_data = f"{temperature}\nK\nF\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Kelvin", "Fahrenheit"), 2)
        expected_output = f"{expected_temperature} °F"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_kelvin_to_fahrenheit_good_low(self):
        temperature = round((randint(0, 27315)/100), 2)
        input_data = f"{temperature}\nK\nF\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Kelvin", "Fahrenheit"), 2)
        expected_output = f"{expected_temperature} °F"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_kelvin_to_kelvin_good_high(self):
        temperature = round((randint(37315, 77315)/100), 2)
        input_data = f"{temperature}\nK\nK\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Kelvin", "Kelvin"), 2)
        expected_output = f"{expected_temperature} K"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_kelvin_to_kelvin_good_medium(self):
        temperature = round((randint(27315, 37315)/100), 2)
        input_data = f"{temperature}\nK\nK\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Kelvin", "Kelvin"), 2)
        expected_output = f"{expected_temperature} K"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_kelvin_to_kelvin_good_low(self):
        temperature = round((randint(0, 27315)/100), 2)
        input_data = f"{temperature}\nK\nK\n"
        expected_temperature = round(self.temp_converter.convert_temperature(temperature, "Kelvin", "Kelvin"), 2)
        expected_output = f"{expected_temperature} K"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_kelvin_bad(self):
        input_data = f"24degrees\nK\nK"
        expected_output = f"format of entered temperature is wrong, not a number"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_kelvin_below_zero(self):
        temperature = round((randint(-10000, -1)/100), 2)
        input_data = f"{temperature}\nK\nK\n"
        expected_output = f"temperature is below absolute zero, conversion is not possible"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_unit_1_wrong(self):
        while True:
            unit_1 = chr(randint(65, 90))
            if unit_1 not in ["C", "F", "K"]:
                break
        input_data = f"36.66\n{unit_1}\nC\n"
        expected_output = f"unit not recognized"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])

    def test_unit_2_wrong(self):
        while True:
            unit_2 = chr(randint(65, 90))
            if unit_2 not in ["C", "F", "K"]:
                break
        input_data = f"36.66\nC\n{unit_2}\n"
        expected_output = f"unit not recognized"

        process = Popen(['python', executable], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)

        self.assertIn(expected_output, process.communicate(input=input_data)[0])


if __name__ == "__main__":
    unittest.main()
