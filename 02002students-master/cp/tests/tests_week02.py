import io
import unittest.mock
from unitgrade import Report
import cp
from unitgrade import UTestCase

def string_fixer(s):
    return s.strip().replace('  ', ' ')

class Week02FullName(UTestCase):
    def test_full_name(self):
        from cp.ex02.full_name import full_name
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            full_name('Donald', 'Duck')
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("Donald Duck"))


class Week02NextThousand(UTestCase):
    def test_next_thousand_01(self):
        from cp.ex02.next_thousand import next_thousand
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            next_thousand(123998)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("124000"))

    def test_next_thousand_02(self):
        from cp.ex02.next_thousand import next_thousand
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            next_thousand(-123998)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("-123000"))


class Week02NameLength(UTestCase):
    def test_name_length(self):
        from cp.ex02.name_length import name_length
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            name_length('Anita')
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("Your name consists of 5 characters."))


class Week02WindChill(UTestCase):
    def test_wind_chill_01(self):
        from cp.ex02.wind_chill import wind_chill
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            wind_chill(8, 12.8)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("Temperature: 8 degrees feels like 6 degrees."))

    def test_wind_chill_02(self):
        from cp.ex02.wind_chill import wind_chill
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            wind_chill(8, 25.8)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("Temperature: 8 degrees feels like 4 degrees."))

    def test_wind_chill_03(self):
        from cp.ex02.wind_chill import wind_chill
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            wind_chill(-2, 12.8)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("Temperature: -2 degrees feels like -6 degrees."))


class Week02NormalWeight(UTestCase):
    def test_normal_weight(self):
        from cp.ex02.normal_weight import normal_weight
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            normal_weight(1.73)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("Normal weight is between 56 and 74 kg."))


class Week02SurvivalTemperature(UTestCase):
    def test_survival_temperature(self):
        from cp.ex02.survival_temperature import survival_temperature
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            survival_temperature(200, 0.1)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("Survival temperature is -27.5 degrees."))


class Week02UnitConversion(UTestCase):
    def test_unit_conversion(self):
        from cp.ex02.unit_conversion import unit_conversion
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            unit_conversion(7, 5)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("7 ft 5 in is equal to 226 cm."))


class Week02Hadlock(UTestCase):
    def test_hadlock(self):
        from cp.ex02.hadlock import hadlock
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            hadlock(31.1, 30.2, 8.3)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("The estimated fetal weight is 2990.7 g."))

class Week02Tests(Report): #240 total.
    title = "Tests for week 02"
    pack_imports = [cp]
    individual_imports = []
    questions = [
                (Week02FullName, 10),
                (Week02NextThousand, 10),
                (Week02NameLength, 10),
                (Week02WindChill, 10),
                (Week02NormalWeight, 10),
                (Week02SurvivalTemperature, 10),
                (Week02UnitConversion, 10),
                (Week02Hadlock, 10),
                ]

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week02Tests())
