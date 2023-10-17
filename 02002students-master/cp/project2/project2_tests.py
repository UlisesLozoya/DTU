import string
from unitgrade import hide
from cp import minput
from unittest.mock import patch
import io
import unittest
from unitgrade import UTestCase, Report
import math


class TestTheFunctionToBisect(UTestCase):
    def test_f(self):
        from cp.ex03.bisect import f

        self.assertAlmostEqual(f(0), 0.1411200080598672)
        self.assertAlmostEqual(f(1), 0.4871688735635369)
        self.assertAlmostEqual(f(2), -0.9484917234010158)
        self.assertAlmostEqual(f(math.pi), 0.6145000731172406)
        self.assertAlmostEqual(f(-10), 0.244199939520782)
        self.assertAlmostEqual(f(117), -0.9996260520700749)


class TestIsThereARoot(UTestCase):
    def test_root_exists(self):
        from cp.ex03.bisect import is_there_a_root

        self.assertTrue(is_there_a_root(1, 3))  # root exists between 0 and pi

    def test_no_root_exists(self):
        from cp.ex03.bisect import is_there_a_root

        self.assertIs(
            is_there_a_root(3.2, 3.8), False
        )  # no root exists between 0 and 2pi

    def test_root_not_found(self):
        from cp.ex03.bisect import is_there_a_root

        self.assertIs(is_there_a_root(1, 3.5), False)


class TestBisect(UTestCase):
    def test_base_case(self):
        from cp.ex03.bisect import bisect

        self.assertAlmostEqual(bisect(1, 3, 0.1), 1.8125)
        self.assertAlmostEqual(bisect(1, 5.5, 0.1), 4.0234375)

    def test_tolerances(self):
        from cp.ex03.bisect import bisect

        self.assertAlmostEqual(bisect(2, 3.5, 10), 2.75)
        self.assertAlmostEqual(bisect(2, 3.5, 0.1), 3.03125)

    def test_no_solution(self):
        from cp.ex03.bisect import bisect

        self.assertTrue(math.isnan(bisect(1, 3.5, 1)))


class HangmanIsGuessed(UTestCase):
    def test_is_word_guessed(self):
        from cp.ex04.hangman import is_word_guessed

        self.assertTrue(is_word_guessed("dog", "tdohg"))
        self.assertTrue(is_word_guessed("dog", "tdohg"))
        self.assertIs(is_word_guessed("dog", ""), False)
        self.assertIs(is_word_guessed("species", "sdcbwegk"), False)
        self.assertTrue(is_word_guessed("species", "qseicps"))


class HangmanGuessedWord(UTestCase):
    def test_get_guessed_word(self):
        from cp.ex04.hangman import get_guessed_word

        self.assertEqual(get_guessed_word("cow", "kcw"), "c_ w")
        self.assertEqual(get_guessed_word("apple", ""), "_ _ _ _ _ ")
        self.assertEqual(get_guessed_word("tasks", "ws"), "_ _ s_ s")


class HangmanAvailableLetters(UTestCase):
    def test_get_available_letters(self):
        from cp.ex04.hangman import get_available_letters

        self.assertEqual(len(get_available_letters("")), 26)
        self.assertEqual(
            set(get_available_letters("bcdew")),
            set(string.ascii_lowercase).difference("bcdew"),
        )


class Hangman(UTestCase):
    def test_hangman_startup(self):
        from cp.ex04.hangman import hangman

        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            try:
                with unittest.mock.patch("builtins.input", minput([None])):
                    hangman("cow", guesses=4)
            except GeneratorExit as e:
                pass
            out = mock_stdout.getvalue()
        lines = out.splitlines()
        self.assertEqual(len(lines), 4, msg="You must print 4 lines")
        self.assertEqual(
            lines[0],
            "Hangman! To save Bob, you must guess a 3 letter word within 4 attempts.",
            msg="First printed line is wrong",
        )
        self.assertEqual(lines[1], "----", msg="Second printed line is wrong")
        self.assertEqual(
            lines[2], "You have 4 guesses left.", msg="Third printed line is wrong"
        )
        self.assertTrue(
            "." in lines[3] and ":" in lines[3],
            msg="Your fourth line must have both a colon and a period",
        )

        fp = lines[3].split(".")[0].split(":")[1].strip()
        self.assertEqual(len(fp), 26, msg="The alphabet has 26 letters.")
        self.assertEqual(
            set(fp), set(string.ascii_lowercase), msg="You failed to print the alphabet"
        )

    def chk_alphabet(self, line, missing):
        self.assertTrue(
            "." in line and ":" in line,
            msg="Your alphabet printout must have both a colon and a period",
        )
        fp = line.split(".")[0].split(":")[1].strip()
        ab = set([c for c in string.ascii_lowercase if c not in missing])
        self.assertEqual(
            len(fp), len(ab), msg="The alphabet printout has to few characters"
        )
        self.assertEqual(set(fp), ab, msg="You failed to print the alphabet")

    def test_hangman_correct(self):
        from cp.ex04.hangman import hangman

        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            try:
                with unittest.mock.patch("builtins.input", minput(["w", None])):
                    hangman("cow", guesses=4)
            except GeneratorExit as e:
                pass
            out = mock_stdout.getvalue()
        lines = out.splitlines()
        self.assertEqual(len(lines), 8, msg="You must print 8 lines")
        self.assertEqual(
            lines[-4], "Good guess: _ _ w", msg="Format guessed word correctly"
        )
        self.assertEqual(lines[-3], "----")
        self.assertEqual(
            lines[-2], "You have 3 guesses left.", msg="Third printed line is wrong"
        )
        self.chk_alphabet(lines[-1], missing="w")

    def test_hangman_false(self):
        from cp.ex04.hangman import hangman

        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            try:
                with unittest.mock.patch("builtins.input", minput(["q", None])):
                    hangman("doggy", guesses=4)
            except GeneratorExit as e:
                pass
            out = mock_stdout.getvalue()
        lines = out.splitlines()
        self.assertEqual(len(lines), 8, msg="You must print 8 lines")
        self.assertEqual(
            lines[-4], "Oh no: _ _ _ _ _ ", msg="Format guessed word correctly"
        )
        self.assertEqual(lines[-3], "----")
        self.assertEqual(
            lines[-2], "You have 3 guesses left.", msg="Third printed line is wrong"
        )
        self.chk_alphabet(lines[-1], missing="q")

    def test_hangman_win(self):
        from cp.ex04.hangman import hangman

        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            try:
                with unittest.mock.patch(
                    "builtins.input", minput(["q", "d", "g", "o", "y", None])
                ):
                    hangman("doggy", guesses=8)
            except GeneratorExit as e:
                pass
            out = mock_stdout.getvalue()
        lines = out.splitlines()
        self.assertEqual(len(lines), 22, msg="You must print 22 lines")
        self.assertTrue(lines[-1], "Your score is 20")

    # @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_hangman_loose(self):
        from cp.ex04.hangman import hangman

        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            try:
                with unittest.mock.patch("builtins.input", minput(["%"])):
                    hangman("cat", guesses=5)
            except GeneratorExit as e:
                pass
            out = mock_stdout.getvalue()
        lines = out.splitlines()
        self.assertEqual(len(lines), 5, msg="You must print 5 lines")
        self.assertTrue(lines[-1], "Game over :-(. Your score is 0 points.")


class Project2(Report):
    title = "Project 2"
    remote_url = "https://cp.pages.compute.dtu.dk/02002public/_static/evaluation/"

    abbreviate_questions = True
    questions = [
        (TestTheFunctionToBisect, 5),
        (TestIsThereARoot, 15),
        (TestBisect, 15),
        (HangmanIsGuessed, 10),
        (HangmanGuessedWord, 10),
        (HangmanAvailableLetters, 10),
        (Hangman, 30),
    ]
    import cp

    pack_imports = [cp]


if __name__ == "__main__":
    from unitgrade import evaluate_report_student

    evaluate_report_student(Project2())
