from unitgrade import UTestCase, Report
import unittest
from unittest.mock import patch, mock_open
import cp
import io

import os
os.chdir(os.path.join(os.path.dirname(cp.__file__), '..'))

class Week08Loading(UTestCase):
    def test_load_txt2str(self):
        from cp.ex08.loading import load_txt2str
        out = load_txt2str('cp/ex08/files/hamlet.txt')
        self.assertEqual(len(out.splitlines()), 1, msg="You probably did not remove \n from the text")
    
    def test_load_txt2list(self):
        from cp.ex08.loading import load_txt2list
        out = load_txt2list('cp/ex08/files/hamlet.txt')
        self.assertTrue(len(out)>1, msg="You did not save each line in a separate list entry")

class Week08Saving(UTestCase):
    def test_save_str2txt(self):
        from cp.ex08.saving import save_str2txt
        import cp.ex08.saving as saving
        open_mock = mock_open()
        with patch("builtins.open", open_mock, create=True):
            save_str2txt("test-data", "output.txt")
        open_mock.assert_called_with("output.txt", "w")
        open_mock.return_value.write.assert_called_once_with("test-data")
    
    def test_save_list2txt(self):
        from cp.ex08.saving import save_list2txt
        import cp.ex08.saving as saving
        open_mock = mock_open()
        with patch("builtins.open", open_mock, create=True):
            save_list2txt(["test-data", "more-test-data"],"output.txt")
        open_mock.assert_called_with("output.txt", "w")
        open_mock.return_value.write.assert_called_with('more-test-data\n')


class Week08Counting(UTestCase):
    def test_count_words(self):
        from cp.ex08.counting import count_words
        self.assertEqual(count_words('hello world'), 2)
        self.assertEqual(count_words('hello'), 1)
        self.assertEqual(count_words(''), 0)
    
    def test_count_letters(self):
        from cp.ex08.counting import count_letters
        self.assertEqual(count_letters('hello world'), 10)
        self.assertEqual(count_letters('hello'), 5)
        self.assertEqual(count_letters(' '), 0)

    def test_count_words_letters(self):
        from cp.ex08.counting import count_words_letters
        self.assertEqual(count_words_letters('cp/ex08/files/hamlet.txt'), (645, 3062))


class Week08SaveCsv(UTestCase):
    def test_save_csv(self):
        from cp.ex08.save_csv import save_csv
        open_mock = mock_open()
        with patch("builtins.open", open_mock, create=True):
            save_csv([['a', 'b', 'c'], [1, 2, 3]], "output.csv")

        open_mock.assert_called_with("output.csv", "w")

class Week08NameOccurence(UTestCase):
    def test_name_occurence(self):
        from cp.ex08.name_occurence import name_occurence
        self.assertAlmostEqual(name_occurence('cp/ex08/files/efternavne.csv', 'Andersen'), 3.446267008547812)

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


class Week08Tests(Report):
    title = "Tests for week 08"
    #version = 0.1
    #url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = [(Week08Loading, 10),
                 (Week08Saving, 10),
                 (Week08Counting, 10),
                 (Week08SaveCsv, 10),
                 (Week08NameOccurence, 10),
                 (Week08LanguageGuess, 20),
                 (Week08GrowthExperiment, 20),
                ]

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week08Tests())
