import io
import unittest
from unittest.mock import patch

from unitgrade import UTestCase, Report


class WaterHeight(UTestCase):
    def test_water_height(self):
        from cp.ex05.water_height import water_height

        self.assertEqual(water_height(5, [1, 2, 3]), 5)
        self.assertEqual(water_height(2, [1, 1]), 0)
        self.assertEqual(water_height(0, [1, 3]), 1)
        self.assertEqual(water_height(1, [1, 2, 3, 4, 5]), 6)
        self.assertEqual(water_height(2, [1, 12, 8, 4, 5]), 22)
        self.assertEqual(water_height(5, [1, 10, 3, 4, 5]), 18)


class Week05BestBuy(UTestCase):
    def test_bestbuy(self):
        from cp.ex05.best_buy import best_buy

        self.assertEqual(best_buy([3, 2, 1, 3, 5], 10, 0, False), 4)
        self.assertEqual(best_buy([3, 2, 1, 3, 5], 3, 1, False), 2)
        self.assertEqual(best_buy([3, 2, 1, 3, 5], 8, 4, True), 2)
        self.assertEqual(best_buy([3, 2, 1, 3, 5], 15, 4, True), 5)


class Week05TicTacToePrintBoard(UTestCase):
    def test_print_board(self):
        from cp.ex05.tictactoe import print_board

        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            print_board([["-", "X", "-"], ["-", "-", "O"], ["X", "-", "-"]])
            out = mock_stdout.getvalue().splitlines()
            self.assertEqual(len(out), 3, msg="You did not print out 3 separate lines")
            self.assertEqual(out[0], "-X-")
            self.assertEqual(out[1], "--O")
            self.assertEqual(out[2], "X--")


class Week05TicTacToeGetGameState(UTestCase):
    def test_get_game_state(self):
        from cp.ex05.tictactoe import get_game_state

        self.assertEqual(
            get_game_state([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]), "-"
        )
        self.assertEqual(
            get_game_state([["X", "X", "X"], ["-", "-", "-"], ["-", "-", "-"]]), "X"
        )
        self.assertEqual(
            get_game_state([["-", "-", "-"], ["X", "X", "X"], ["-", "-", "-"]]), "X"
        )
        self.assertEqual(
            get_game_state([["X", "-", "-"], ["-", "X", "-"], ["O", "O", "X"]]), "X"
        )
        self.assertEqual(
            get_game_state([["X", "-", "-"], ["-", "X", "-"], ["O", "O", "O"]]), "O"
        )
        self.assertEqual(
            get_game_state([["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]), "Draw"
        )


class Week05TicTacToeUpdateBoard(UTestCase):
    def test_update_board(self):
        from cp.ex05.tictactoe import update_board

        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            self.assertEqual(
                update_board(
                    [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], "X", [1, 0]
                ),
                [["-", "-", "-"], ["X", "-", "-"], ["-", "-", "-"]],
            )
            self.assertEqual(
                update_board(
                    [["X", "X", "-"], ["-", "-", "-"], ["-", "-", "-"]], "O", [0, 2]
                ),
                [["X", "X", "O"], ["-", "-", "-"], ["-", "-", "-"]],
            )
            self.assertEqual(
                update_board(
                    [["-", "-", "-"], ["X", "X", "X"], ["-", "-", "-"]], "X", [2, 0]
                ),
                [["-", "-", "-"], ["X", "X", "X"], ["X", "-", "-"]],
            )
            self.assertEqual(
                update_board(
                    [["X", "-", "-"], ["-", "X", "-"], ["O", "O", "X"]], "O", [1, 2]
                ),
                [["X", "-", "-"], ["-", "X", "O"], ["O", "O", "X"]],
            )
            self.assertEqual(
                update_board(
                    [["X", "-", "-"], ["-", "X", "-"], ["O", "O", "O"]], "X", [0, 2]
                ),
                [["X", "-", "X"], ["-", "X", "-"], ["O", "O", "O"]],
            )
            self.assertEqual(
                update_board(
                    [["O", "-", "-"], ["O", "X", "-"], ["O", "X", "X"]], "O", [0, 2]
                ),
                [["O", "-", "O"], ["O", "X", "-"], ["O", "X", "X"]],
            )
            out = mock_stdout.getvalue()
            self.assertEqual(out, "", "You should not print anything for valid moves")
        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            update_board(
                [["O", "-", "-"], ["O", "X", "-"], ["O", "X", "X"]], "O", [0, 0]
            )
            out = mock_stdout.getvalue().strip()
            self.assertEqual(out, "Invalid move!")


class Week05TicTacToeMain(UTestCase):
    def test_tictactoe_main(self):
        from cp.ex05.tictactoe import tictactoe

        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            tictactoe([["X", "X", "-"], ["-", "O", "-"], ["O", "-", "-"]], "O", [0, 2])
            out = mock_stdout.getvalue().splitlines()
            self.assertEqual(len(out), 4, msg="You did not print out 4 separate lines")
            self.assertEqual(out[0], "XXO")
            self.assertEqual(out[1], "-O-")
            self.assertEqual(out[2], "O--")
            self.assertEqual(out[3], "Player O won!")


class Week06SpellCheck(UTestCase):
    def test_spell_check(self):
        from cp.ex06.spell_check import spell_check

        corrections = {
            "occurence": "occurrence",
            "apsolute": "absolute",
            "teh": "the",
            "acess": "access",
            "occured": "occurred",
            "exampel": "example",
        }
        text = "The apsolute acess to teh data occured in this exampel"
        self.assertEqual(
            spell_check(text, corrections),
            "The absolute access to the data occurred in this example",
        )
        text2 = "The first occurence of teh mean apsolute error formula look at teh exampel below"
        self.assertEqual(
            spell_check(text2, corrections),
            "The first occurrence of the mean absolute error formula look at the example below",
        )
        self.assertEqual(
            spell_check("We can handle teh damag", {"damag": "damage"}),
            "We can handle teh damage",
        )
        self.assertEqual(
            spell_check("We can handle teh damag.", {"damag": "damage"}),
            "We can handle teh damage.",
        )
        text3 = "The apsolute acess to teh, data occured in this exampel."
        self.assertEqual(
            spell_check(text3, corrections),
            "The absolute access to the, data occurred in this example.",
        )


class Week06MultiTap(UTestCase):
    def test_multi_tap(self):
        from cp.ex06.multi_tap import multi_tap

        self.assertEqual(
            multi_tap([7, 7, 7, 7, 6, 6, 6], [0, 0.7, 0.8, 0.9, 1, 1.1, 1.2]), "PRO"
        )
        self.assertEqual(
            multi_tap(
                [4, 4, 4, 0, 2, 6, 0, 4, 4, 2, 7, 7, 9, 9, 9],
                [
                    0.1,
                    0.3,
                    0.6,
                    1.0,
                    1.2,
                    1.4,
                    1.7,
                    2.0,
                    2.2,
                    2.5,
                    2.9,
                    3.9,
                    4.3,
                    4.4,
                    4.8,
                ],
            ),
            "I AM HAPPY",
        )
        self.assertEqual(
            multi_tap(
                [7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 8, 8, 3],
                [0.1, 0.5, 0.8, 1.2, 2.6, 3.7, 4.1, 4.2, 4.5, 4.9, 5.1, 5.4, 5.6, 5.9],
            ),
            "SPROUD",
        )
        self.assertEqual(
            multi_tap(
                [
                    4,
                    4,
                    4,
                    2,
                    2,
                    2,
                    3,
                    3,
                    0,
                    4,
                    4,
                    4,
                    2,
                    2,
                    2,
                    3,
                    3,
                    0,
                    2,
                    2,
                    2,
                    2,
                    2,
                    9,
                    9,
                    9,
                ],
                [
                    0.3,
                    0.7,
                    0.8,
                    1.1,
                    1.3,
                    1.5,
                    1.7,
                    1.8,
                    2.1,
                    2.4,
                    2.7,
                    3.0,
                    3.4,
                    3.7,
                    3.9,
                    4.0,
                    4.3,
                    4.5,
                    4.7,
                    5.0,
                    6.4,
                    7.9,
                    8.3,
                    8.5,
                    8.7,
                    9.0,
                ],
            ),
            "ICE ICE BABY",
        )
        self.assertEqual(
            multi_tap(
                [
                    5,
                    5,
                    5,
                    4,
                    4,
                    4,
                    8,
                    8,
                    8,
                    3,
                    3,
                    0,
                    5,
                    5,
                    5,
                    2,
                    8,
                    8,
                    4,
                    4,
                    4,
                    0,
                    5,
                    5,
                    5,
                    4,
                    4,
                    4,
                    7,
                    7,
                    7,
                    7,
                    8,
                ],
                [
                    0.7,
                    0.9,
                    1.2,
                    1.6,
                    1.7,
                    2.0,
                    2.4,
                    2.5,
                    2.8,
                    3.2,
                    3.5,
                    3.7,
                    3.9,
                    4.3,
                    4.6,
                    4.8,
                    5.0,
                    5.3,
                    5.6,
                    6.3,
                    6.7,
                    6.8,
                    7.1,
                    7.3,
                    7.5,
                    7.8,
                    8.0,
                    8.1,
                    8.3,
                    8.5,
                    8.7,
                    8.9,
                    9.3,
                ],
            ),
            "LIVE LAUGH LIST",
        )


class Project3(Report):
    title = "Project 3"
    remote_url = "https://cp.pages.compute.dtu.dk/02002public/_static/evaluation/"

    abbreviate_questions = True
    questions = [
        (Week05BestBuy, 10),
        (WaterHeight, 10),
        (Week05TicTacToePrintBoard, 5),
        (Week05TicTacToeGetGameState, 10),
        (Week05TicTacToeUpdateBoard, 10),
        (Week06SpellCheck, 21),
        (Week06MultiTap, 21),
    ]
    import cp

    pack_imports = [cp]


if __name__ == "__main__":
    from unitgrade import evaluate_report_student

    evaluate_report_student(Project3())
