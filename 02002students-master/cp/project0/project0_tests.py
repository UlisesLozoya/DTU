from unitgrade import Report, UTestCase
import cp
import io
import unittest
from unittest.mock import patch

class HelloWorld(UTestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_say_hello(self, mock_stdout):
        from cp.ex00 import say_hello
        # lib = importlib.reload(say_hello)
        lines = mock_stdout.getvalue().strip().splitlines()

        self.assertEqual(len(lines), 2, msg=f"Wrong number of lines. Your program should print(..) out two lines, you got: {lines}, {say_hello.__file__}")

        print("Testing the first line")
        self.assertEqual(lines[0], "Hello", msg="You must have somehow changed the first print(...) statement in the program. Did you delete it?")  # Rem

        print("Testing the second line")
        self.assertEqual(lines[1], "World", msg="Your second print statement did not produce the correct output.") # Remember the output must be capitalized.


class Project0(Report):
    title = "Project for week 00 (Try to complete this before the course starts)"
    remote_url = "https://cp.pages.compute.dtu.dk/02002public/_static/evaluation/"

    pack_imports = [cp]
    individual_imports = []
    questions = [
                (HelloWorld, 10),
                ]

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Project0())
