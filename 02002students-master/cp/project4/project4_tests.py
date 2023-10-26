from unitgrade import UTestCase, Report
import cp
import unittest

import os
os.chdir(os.path.join(os.path.dirname(cp.__file__), '..'))

class Week07Morse(UTestCase):
    def test_morse(self):
        from cp.ex07.morse_to_text import morse_to_text
        self.assertEqual(morse_to_text("-.. --- - ...  .- -. -..  -.. .- ... .... . ...  - . .-.. .-..  .- -. -.-. .. . -. -  - .- .-.. . ..."), "DOTS AND DASHES TELL ANCIENT TALES")
        self.assertEqual(morse_to_text("..  --. ---  - ---  - .... .  -.. . -. - .. ... -"), "I GO TO THE DENTIST")
        self.assertEqual(morse_to_text("- --- -.. .- -.--  .-- .- ...  -.-. .-.. . .- .-."), "TODAY WAS CLEAR")
        self.assertEqual(morse_to_text("- .... .  -- .- --. .. -.-.  --- ..-.  - .... .  ... ..- -."), "THE MAGIC OF THE SUN")
        self.assertEqual(morse_to_text("- .... .  .--- --- -.--  .. -.  -- -.--  .... . .- .-. -"), "THE JOY IN MY HEART")

class Week07AstronomicalSeason(UTestCase):
    def test_winter(self):
        from cp.ex07.astronomical_season import astronomical_season
        self.assertEqual(astronomical_season((21, 'dec')), 'winter')
        self.assertEqual(astronomical_season((15, 'feb')), 'winter')
        self.assertEqual(astronomical_season((19, 'mar')), 'winter')

    def test_spring(self):
        from cp.ex07.astronomical_season import astronomical_season
        self.assertEqual(astronomical_season((20, 'mar')), 'spring')
        self.assertEqual(astronomical_season((10, 'apr')), 'spring')
        self.assertEqual(astronomical_season((20, 'jun')), 'spring')

    def test_summer(self):
        from cp.ex07.astronomical_season import astronomical_season
        self.assertEqual(astronomical_season((21, 'jun')), 'summer')
        self.assertEqual(astronomical_season((5, 'jul')), 'summer')
        self.assertEqual(astronomical_season((22, 'sep')), 'summer')

    def test_autumn(self):
        from cp.ex07.astronomical_season import astronomical_season
        self.assertEqual(astronomical_season((23, 'sep')), 'autumn')
        self.assertEqual(astronomical_season((10, 'oct')), 'autumn')
        self.assertEqual(astronomical_season((20, 'dec')), 'autumn')


class Week08LanguageGuess(UTestCase):
    def test_letter_frequency(self):
        from cp.ex08.language_guess import frequency_letter
        self.assertAlmostEqual(frequency_letter('cp/ex08/files/hamlet.txt', 'a'), 7.6, places=1)
        self.assertAlmostEqual(frequency_letter('cp/ex08/files/hamlet.txt', 'e'), 12.0, places=1)

    def test_language_guess(self):
        from cp.ex08.language_guess import language_guess
        self.assertEqual(language_guess('cp/ex08/files/text1.txt'), 'English')
        self.assertEqual(language_guess('cp/ex08/files/text2.txt'), 'German')
        self.assertEqual(language_guess('cp/ex08/files/text3.txt'), 'French')
        self.assertEqual(language_guess('cp/ex08/files/names.txt'), 'Unknown')

class Week08GrowthExperiment(UTestCase):
    def test_growth_threshold_reached(self):
        from cp.ex08.growth_experiment import growth_threshold_reached
        self.assertAlmostEqual(growth_threshold_reached('cp/ex08/files/experiments', 8.5), 9.29375)
        self.assertAlmostEqual(growth_threshold_reached('cp/ex08/files/experiments', 5.1), 7.16875)
        self.assertAlmostEqual(growth_threshold_reached('cp/ex08/files/experiments', 10.0), 9.94375)



class Project4(Report):
    title = "Project 4"
    remote_url = "https://cp.pages.compute.dtu.dk/02002public/_static/evaluation/"

    abbreviate_questions = True
    questions = [(Week07Morse, 20),
                 (Week07AstronomicalSeason, 20),
                 (Week08LanguageGuess, 20),
                 (Week08GrowthExperiment, 20),
                ]
    import cp
    pack_imports = [cp]


if __name__ == "__main__":
    from unitgrade import evaluate_report_student
    evaluate_report_student(Project4())
