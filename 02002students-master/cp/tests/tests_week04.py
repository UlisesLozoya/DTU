from unitgrade import UTestCase, Report
import unittest
from unittest.mock import patch
import cp
import io


def string_fixer(s):
    return s.strip().replace("  ", " ")


class Week04Palindrome(UTestCase):
    def test_is_palindrome(self):
        from cp.ex04.palindrome import is_palindrome

        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("kk"))
        self.assertTrue(is_palindrome("m"))
        self.assertIs(is_palindrome("gentleman"), False)
        self.assertIs(is_palindrome("ma"), False)


class Week04Bug(UTestCase):
    def test_nice_sign(self):
        from cp.ex04.bug import nice_sign

        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            nice_sign("hello")
            out = mock_stdout.getvalue()

            self.assertEqual(
                len(out.splitlines()), 3, msg="You did not print out 3 seperate lines"
            )
            l1 = out.splitlines()[0]
            l2 = out.splitlines()[1]
            l3 = out.splitlines()[2]

            self.assertEqual(string_fixer(l1), "---------")
            self.assertEqual(string_fixer(l2), "| hello |")
            self.assertEqual(string_fixer(l3), "---------")

    def test_last_bug(self):
        from cp.ex04.bug import last_bug

        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            last_bug()
            out = mock_stdout.getvalue()

            self.assertEqual(
                len(out.splitlines()), 3, msg="You did not print out 3 seperate lines"
            )
            l1 = out.splitlines()[0]
            l2 = out.splitlines()[1]
            l3 = out.splitlines()[2]

            self.assertEqual(l1, "------------------------------")
            self.assertEqual(l2, "| I have written my last bug |")
            self.assertEqual(l3, "------------------------------")


class Week04Math(UTestCase):
    def test_square_root(self):
        from cp.ex04.mathematics import square_root

        self.assertAlmostEqual(square_root(9), 3, places=3)
        self.assertAlmostEqual(square_root(25), 5, places=3)

    def test_pi(self):
        from cp.ex04.mathematics import ramanujan

        self.assertAlmostEqual(ramanujan(), 3.1416, places=3)


class Week04Parenthesis(UTestCase):
    def test_matching(self):
        from cp.ex04.parenthesis import matching

        self.assertTrue(matching("3x(y+x)"))
        self.assertTrue(matching("3x"))
        self.assertTrue(matching("3x(y+(x-1))"))
        self.assertTrue(matching("3(x-8)^2(y+(x-1))"))
        self.assertIs(matching("3x(y+x))"), False)
        self.assertIs(matching("(3x(y+x)"), False)

    def test_innermost(self):
        from cp.ex04.parenthesis import find_innermost_part

        self.assertEqual(find_innermost_part("(3+x)"), "3+x")
        self.assertEqual(find_innermost_part("3+x"), "3+x")
        self.assertEqual(find_innermost_part("3x((y+2)y+x)"), "y+2")
        self.assertEqual(find_innermost_part("3x((y+(1 - q^2)y+x))"), "1 - q^2")

    def test_find_index_of_equality(self):
        from cp.ex04.parenthesis import find_index_of_equality

        self.assertEqual(find_index_of_equality("()"), 1)
        self.assertEqual(find_index_of_equality("(()())"), 3)
        self.assertEqual(find_index_of_equality("())"), 2)
        self.assertEqual(find_index_of_equality("())((((("), 2)
        # self.assertEqual(find_index_of_equality(""), 0)
        self.assertEqual(find_index_of_equality(")(()())("), 4)


class Week04Dialogue(UTestCase):
    def test_print_the_dialogue(self):
        from cp.ex04.parenthesis import print_the_dialogue

        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            print_the_dialogue("He said: ''How are you doing?''")
            out = mock_stdout.getvalue()
            self.assertEqual(out.strip(), "How are you doing?")

    def test_print_the_dialogue_twolines(self):
        from cp.ex04.parenthesis import print_the_dialogue

        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            print_the_dialogue(
                "He: ''How are you doing?'' She: ''Still stuck on my 02002 programming problems''."
            )
            out = mock_stdout.getvalue()
            self.assertEqual(
                out.strip(),
                "How are you doing?\nStill stuck on my 02002 programming problems",
            )


class Week04Prefix(UTestCase):
    def test_common_prefix(self):
        from cp.ex04.prefix import common_prefix

        self.assertEqual(common_prefix("cat", "cawabunga"), "ca")
        self.assertEqual(common_prefix("caterpillar", "catapult"), "cat")
        self.assertEqual(common_prefix("cat", "dog"), "")

    def test_common_prefix3(self):
        from cp.ex04.prefix import common_prefix3

        self.assertEqual(common_prefix3("cat", "cawabunga", "catapult"), "ca")
        self.assertEqual(common_prefix3("cawabunga", "cow", "catapult"), "c")
        self.assertEqual(common_prefix3("selenium", "sealant", "sensei"), "se")
        self.assertEqual(common_prefix3("selenium", "apple", "sensei"), "")


class Week04Tests(Report):
    title = "Tests for week 04"
    # version = 1.0
    # url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    questions = [
        (Week04Math, 10),
        (Week04Palindrome, 10),
        (Week04Bug, 10),
        (Week04Parenthesis, 10),
        (Week04Dialogue, 10),
        (Week04Prefix, 10),
    ]


if __name__ == "__main__":
    from unitgrade import evaluate_report_student

    evaluate_report_student(Week04Tests())
