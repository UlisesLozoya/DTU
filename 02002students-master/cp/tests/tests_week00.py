from unitgrade import Report, UTestCase
import cp
import io
import unittest
from unittest.mock import patch

class SayHelloWorld(UTestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_say_hello(self, mock_stdout):
        import cp.ex00.say_hello
        lines = mock_stdout.getvalue().strip().splitlines()
        self.assertEqual(len(lines), 2, msg=f"Wrong number of lines. Your program should print(..) out two lines, you got: {lines}")
        print("Testing the first line")
        self.assertEqual(lines[0], "Hello", msg="You must have somehow changed the first print(...) statement in the program. Did you delete it?")  # Rem
        print("Testing the second line")
        self.assertEqual(lines[1], "World", msg="Your second print statement did not produce the correct output.")


class Week00Tests(Report):
    title = "Tests for week 00 (Try to complete this before the course start)"
    # version = 1.0
    # url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = [(SayHelloWorld, 10)]


if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week00Tests())
