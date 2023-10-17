import string
from unitgrade import hide
from cp import minput
from unittest.mock import patch
import io
import unittest
from unitgrade import UTestCase, Report
import math

def string_fixer(s):
    return s.strip().replace('  ', ' ')

class TestNormalWeight(UTestCase):
    
    def test_normal_weight_01(self):
        from cp.ex02.normal_weight import normal_weight
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            normal_weight(1.47)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("Normal weight is between 40 and 54 kg."))
    
    def test_normal_weight_02(self):
        from cp.ex02.normal_weight import normal_weight
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            normal_weight(1.96)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("Normal weight is between 72 and 96 kg."))




class TestSurvivalTemperature(UTestCase):
    def test_survival_temperature_01(self):
        from cp.ex02.survival_temperature import survival_temperature
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            survival_temperature(186,0.15)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("Survival temperature is -5.0 degrees."))

    
    def test_survival_temperature_02(self):
        from cp.ex02.survival_temperature import survival_temperature
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            survival_temperature(356,0.33)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("Survival temperature is -7.0 degrees."))




class TestUnitConversion(UTestCase):
    def test_unit_conversion_01(self):
        from cp.ex02.unit_conversion import unit_conversion
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            unit_conversion(4, 3)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("4 ft 3 in is equal to 130 cm."))
    
    def test_unit_conversion_02(self):
        from cp.ex02.unit_conversion import unit_conversion
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            unit_conversion(7, 2)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("7 ft 2 in is equal to 218 cm."))




class TestHadlock(UTestCase):
    def test_hadlock_01(self):
        from cp.ex02.hadlock import hadlock
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            hadlock(35, 36, 12)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("The estimated fetal weight is 5820.8 g."))

    def test_hadlock_02(self):
        from cp.ex02.hadlock import hadlock
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            hadlock(28.6, 29.6, 6.3)
            out = mock_stdout.getvalue()
            self.assertEqual(string_fixer(out), string_fixer("The estimated fetal weight is 2070.0 g."))




class Project1(Report):
    title = "Project 1"
    remote_url = "https://cp.pages.compute.dtu.dk/02002public/_static/evaluation/"

    abbreviate_questions = True
    questions = [
        (TestNormalWeight, 25),
        (TestSurvivalTemperature, 25),
        (TestUnitConversion, 25),
        (TestHadlock, 25),
    ]
    import cp

    pack_imports = [cp]


if __name__ == "__main__":
    from unitgrade import evaluate_report_student

    evaluate_report_student(Project1())
