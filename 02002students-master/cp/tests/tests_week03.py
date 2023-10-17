from unitgrade import UTestCase, Report
import unittest.mock
import io
import cp
import math

class Week03BodyTemperature(UTestCase):
    def test_body_Temperature(self):
        with self.capture() as c:
            from cp.ex03.body_temperature import body_temperature
        result = body_temperature(34.5)
        self.assertEqual(result, 'Hypothermia')
        result = body_temperature(36.9)
        self.assertEqual(result, 'Normal')
        result = body_temperature(37.2)
        self.assertEqual(result, 'Slight fever')
        result = body_temperature(38.5)
        self.assertEqual(result, 'Fever')
        result = body_temperature(40.1)
        self.assertEqual(result, 'Hyperthermia')


class Week03CompareNumbers(UTestCase):
    def test_compare_numbers(self):
        with self.capture() as c:
            from cp.ex03.compare_numbers import compare_numbers
        result = compare_numbers(5.,3.)
        self.assertEqual(result, 'the first number is greater')
        result = compare_numbers(2.,7.)
        self.assertEqual(result, 'the second number is greater')
        result = compare_numbers(4.,4.)
        self.assertEqual(result, 'the numbers are equal')


class Week03BACCalculator(UTestCase):
    def test_BAC_calculator(self):
        with self.capture() as c:
            from cp.ex03.bac_calculator import bac_calculator
        result = bac_calculator(0.028, 80., "male", 2.)
        self.assertEqual(result,0.02147058823529411)
        result = bac_calculator(0.021, 70., "female", 2.)
        self.assertEqual(result,0.020545454545454547)

class Week03Ackermann(UTestCase):
    def test_ackermann(self):
        from cp.ex03.ackermann import ackermann
        self.assertEqual(ackermann(0, 0), 1)
        self.assertEqual(ackermann(0, 1), 2)
        self.assertEqual(ackermann(1, 0), 2)
        self.assertEqual(ackermann(1, 1), 3)
        self.assertEqual(ackermann(1, 2), 4)
        self.assertEqual(ackermann(2, 0), 3)
        self.assertEqual(ackermann(2, 1), 5)
        self.assertEqual(ackermann(2, 2), 7)
        self.assertEqual(ackermann(3, 0), 5)
        self.assertEqual(ackermann(3, 1), 13)
        self.assertEqual(ackermann(3, 2), 29)

class Week03Exponential(UTestCase):
    def test_exponential_with_positive_power(self):
        from cp.ex03.exponential import exponential
        self.assertEqual(exponential(2, 0), 1.0)
        self.assertEqual(exponential(2, 1), 2.0)
        self.assertEqual(exponential(2, 2), 4.0)
        self.assertEqual(exponential(3, 3), 27.0)
        self.assertEqual(exponential(5, 4), 625.0)

    def test_exponential_with_negative_power(self):
        from cp.ex03.exponential import exponential
        self.assertEqual(exponential(2, -1), 0.5)
        self.assertEqual(exponential(2, -2), 0.25)
        self.assertAlmostEqual(exponential(3, -3), 0.037037037037)
        self.assertAlmostEqual(exponential(5, -4), 5**(-4) )

    def test_exponential_with_zero_power(self):
        from cp.ex03.exponential import exponential
        self.assertEqual(exponential(2, 0), 1.0)
        self.assertEqual(exponential(3, 0), 1.0)
        self.assertEqual(exponential(5, 0), 1.0)


class Week03HeartAttack(UTestCase):

    def test_heart_attack_low(self):
        from cp.ex03.heart_attack import heart_attack
        self.assertEqual(heart_attack(25, 55, False), "low")
        self.assertEqual(heart_attack(16, 45, False), "low")
        self.assertEqual(heart_attack(30, 58, False), "low")

    def test_heart_attack_high(self):
        from cp.ex03.heart_attack import heart_attack
        self.assertEqual(heart_attack(45, 70, True), "high")
        self.assertEqual(heart_attack(11, 70, True), "high")

class Week03SolarPanelTests(UTestCase):
    
    def test_maybe(self):
        from cp.ex03.solar_panel import solar_panel
        self.assertEqual(solar_panel(True, False, False, False).strip().lower(), "maybe")

    def test_good_luck(self):
        from cp.ex03.solar_panel import solar_panel
        self.assertEqual(solar_panel(True, False, True, True).strip().lower()[:4], "haha")

    def test_probably_not1(self):
        from cp.ex03.solar_panel import solar_panel
        self.assertEqual(solar_panel(True, True, False, False).strip().lower(), "probably not")

    def test_probably_not2(self):
        from cp.ex03.solar_panel import solar_panel
        self.assertEqual(solar_panel(False, False, True, True).strip().lower(), "probably not")

    def test_sure(self):
        from cp.ex03.solar_panel import solar_panel
        self.assertEqual(solar_panel(False, False, False, False).strip().lower(), "sure")


class Week03TheFunctionToBisect(UTestCase):
    def test_f(self):
        from cp.ex03.bisect import f
        self.assertAlmostEqual(f(0), 0.1411200080598672)
        self.assertAlmostEqual(f(1),  0.4871688735635369 )
        self.assertAlmostEqual(f(2),  -0.9484917234010158)
        self.assertAlmostEqual(f(math.pi), 0.6145000731172406 )
        self.assertAlmostEqual(f(-10), 0.244199939520782)
        self.assertAlmostEqual(f(117),  -0.9996260520700749)


class Week03IsThereARoot(UTestCase):
    def test_root_exists(self):
        from cp.ex03.bisect import is_there_a_root
        self.assertTrue(is_there_a_root(1, 3))  # root exists between 0 and pi

    def test_no_root_exists(self):
        from cp.ex03.bisect import is_there_a_root
        self.assertIs(is_there_a_root(3.2, 3.8), False)  # no root exists between 0 and 2pi

    def test_root_not_found(self):
        from cp.ex03.bisect import is_there_a_root
        self.assertIs(is_there_a_root(1, 3.5), False)


class Week03Bisect(UTestCase):
    def test_base_case(self):
        from cp.ex03.bisect import bisect
        self.assertAlmostEqual(bisect(1, 3, 0.1), 1.8125)
        self.assertAlmostEqual(bisect(1, 5.5, 0.1), 4.0234375)

    def test_tolerances(self):
        from cp.ex03.bisect import bisect
        self.assertAlmostEqual(bisect(2, 3.5, 10), 2.75)
        self.assertAlmostEqual(bisect(2, 3.5, 0.1),  3.03125)

    def test_no_solution(self):
        from cp.ex03.bisect import bisect
        self.assertTrue(math.isnan(bisect(1, 3.5, 1)))


class Week03Tests(Report):
    title = "Tests for week 03"
    # version = 1.1
    # url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = [
                (Week03BodyTemperature, 10),
                (Week03CompareNumbers, 10),
                (Week03BACCalculator, 10),
                (Week03Ackermann, 10),
                (Week03Exponential, 10),
                (Week03HeartAttack, 10),
                (Week03SolarPanelTests, 10),
                (Week03TheFunctionToBisect, 5),
                (Week03IsThereARoot, 15),
                (Week03Bisect, 15),
                ]

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week03Tests())
