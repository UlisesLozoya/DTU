import io
import unittest
from unittest.mock import patch

import cp
from unitgrade import Report
from unitgrade import UTestCase


class Week05Average(UTestCase):
    def test_average(self):
        from cp.ex05.average import calculate_average

        self.assertAlmostEqual(calculate_average([1, 2, 3, 4, 5]), 3)
        self.assertAlmostEqual(calculate_average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5.5)


class Week05ConditionedMax(UTestCase):
    def test_conditioned_maximum(self):
        from cp.ex05.conditioned_maximum import conditioned_maximum

        self.assertAlmostEqual(conditioned_maximum([1, 2, 3, 4, 5], 3), 2)
        self.assertAlmostEqual(conditioned_maximum([1, 2, 3, 4, 5], 6), 5)

    def test_conditioned_maximum_name(self):
        from cp.ex05.conditioned_maximum import conditioned_maximum_name

        self.assertEqual(
            conditioned_maximum_name(
                [1, 2, 3, 4, 5], ["one", "two", "three", "four", "five"], 3
            ),
            "two",
        )
        self.assertEqual(
            conditioned_maximum_name(
                [1, 2, 3, 4, 5], ["one", "two", "three", "four", "five"], 6
            ),
            "five",
        )


class Week05Shortwords(UTestCase):
    def test_shortwords(self):
        from cp.ex05.short_words import short_words

        self.assertEqual(short_words("This is a string", 4), "is a")
        self.assertEqual(short_words("This is a string", 5), "This is a")
        self.assertEqual(short_words("This is a string", 1), "")
        self.assertEqual(short_words("Oneword", 2), "")


class Week05Rectangular(UTestCase):
    def test_is_rectangular(self):
        from cp.ex05.rectangular import is_rectangular

        self.assertTrue(is_rectangular([[1, 2, 3], [4, 5, 6]]))
        self.assertTrue(is_rectangular([[1, 2], ["cat", "dog"], [5, 6]]))
        self.assertTrue(is_rectangular([[1, 2, 3, 4, 5, 6]]))
        self.assertTrue(is_rectangular([[1], [2], [3], [4], [5], [6]]))
        self.assertIs(is_rectangular([[1, 2, 3], [4, 5]]), False)
        self.assertIs(is_rectangular([[1, 2, 3], [4, 5, 6], []]), False)


class Week05VectorMath(UTestCase):
    def test_vector_add(self):
        from cp.ex05.vector_add import vector_add

        self.assertEqual(vector_add([1, 2, 3], [4, 5, 6]), [5, 7, 9])


class Week05Multiples(UTestCase):
    def test_count_multiples(self):
        from cp.ex05.multiples import count_multiples

        self.assertEqual(count_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), 3)
        self.assertEqual(count_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), 5)
        self.assertEqual(count_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), 0)

    def test_multiples_list(self):
        from cp.ex05.multiples import multiples_list

        self.assertEqual(multiples_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [3, 6, 9])
        self.assertEqual(
            multiples_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [2, 4, 6, 8, 10]
        )
        self.assertEqual(multiples_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), [])


class Week05WaterHeights(UTestCase):
    def test_water_height(self):
        from cp.ex05.water_height import water_height

        self.assertEqual(water_height(5, [1, 2, 3]), 5)
        self.assertEqual(water_height(2, [1, 1]), 0)
        self.assertEqual(water_height(0, [1, 3]), 1)


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


class Week05Tests(Report):
    title = "Tests for week 05"
    # version = 0.1
    # url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = [
        (Week05Average, 5),
        (Week05ConditionedMax, 10),
        (Week05Shortwords, 5),
        (Week05Rectangular, 10),
        (Week05VectorMath, 10),
        (Week05Multiples, 10),
        (Week05WaterHeights, 10),
        (Week05BestBuy, 10),
        (Week05TicTacToePrintBoard, 10),
        (Week05TicTacToeGetGameState, 10),
        (Week05TicTacToeUpdateBoard, 10),
        (Week05TicTacToeMain, 10),
    ]


if __name__ == "__main__":
    from unitgrade import evaluate_report_student

    evaluate_report_student(Week05Tests())
