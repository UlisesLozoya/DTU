import cp
from unitgrade import Report
from unitgrade import UTestCase


class Week07HaveEqualLength(UTestCase):
    def test_equal_length_tuples(self):
        from cp.ex07.have_equal_length import have_equal_length

        self.assertIs(have_equal_length((1, 2, 3), (4, 5, 6)), True)

    def test_unequal_length_tuples(self):
        from cp.ex07.have_equal_length import have_equal_length

        self.assertIs(have_equal_length((1, 2, 3), (4, 5)), False)

    def test_empty_tuples(self):
        from cp.ex07.have_equal_length import have_equal_length

        self.assertIs(have_equal_length((), ()), True)

    def test_one_empty_tuple(self):
        from cp.ex07.have_equal_length import have_equal_length

        self.assertIs(have_equal_length((1, 2, 3), ()), False)

    def test_nested_tuples(self):
        from cp.ex07.have_equal_length import have_equal_length

        self.assertIs(have_equal_length((1, (2, 3), 4), (5, (6, 7), 8)), True)


class Week07LastDifference(UTestCase):
    def test_last_element_difference(self):
        from cp.ex07.last_difference import last_difference

        self.assertEqual(last_difference((10, 7, 8, 20, 30.0), (5, 15, 35.0)), -5.0)
        self.assertEqual(last_difference((1, 2, 3.0), (4, 5, 6.0)), -3.0)


class Week07MultipleValues(UTestCase):
    def test_returning_multiple_values(self):
        from cp.ex07.returning_multiple_values import returning_multiple_values

        self.assertEqual(
            returning_multiple_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
            ([6, 7, 8, 9, 10], 1),
        )
        self.assertEqual(
            returning_multiple_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), ([], 1)
        )
        self.assertEqual(
            returning_multiple_values([-1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0),
            ([2, 3, 4, 5, 6, 7, 8, 9, 10], -1),
        )


class Week07BoxPacking(UTestCase):
    def assertTupleAlmostEqual(self, first, second, places=None, msg=None, delta=None):
        self.assertEqual(len(first), len(second))
        for a, b in zip(first, second):
            self.assertAlmostEqual(a, b, places, msg, delta)

    def test_box_packing(self):
        from cp.ex07.box_packing import box_packing

        self.assertTupleAlmostEqual(box_packing((2, 5), (4, 2.1)), (0, 2.9))
        self.assertTupleAlmostEqual(box_packing((4, 2.1), (5, 2)), (0, 0.1))
        self.assertTupleAlmostEqual(box_packing((4, 2.1), (5, 5)), (0, 0))
        self.assertTupleAlmostEqual(box_packing((4, 2.1), (1, 1.1)), (3, 1))
        self.assertTupleAlmostEqual(box_packing((2, 5), (2, 5)), (0, 0))
        self.assertTupleAlmostEqual(box_packing((5, 5), (2, 5)), (3, 0))


class Week07Hue(UTestCase):
    def test_hue(self):
        from cp.ex07.rgb_to_hue import rgb_to_hue

        self.assertEqual(rgb_to_hue((0.6, 0.2, 0.3)), 345.0)
        self.assertEqual(rgb_to_hue((0.3, 0.6, 0.2)), 105.0)
        self.assertEqual(rgb_to_hue((0.1, 0.1, 0.2)), 240.0)
        self.assertEqual(rgb_to_hue((0.2, 0.25, 0.3)), 210.0)
        self.assertEqual(rgb_to_hue((0.9, 0.9, 0.3)), 60.0)
        self.assertEqual(rgb_to_hue((0.6, 0.8, 0.8)), 180.0)
        self.assertEqual(rgb_to_hue((1.0, 0.1, 0.1)), 0.0)
        self.assertEqual(rgb_to_hue((0.7, 0.6, 0.7)), 300.0)
        self.assertEqual(rgb_to_hue((0.5, 0.1, 0.6)), 288.0)


class Week07CodeShift(UTestCase):
    def test_code_shift(self):
        from cp.ex07.code_shift import code_shift

        turn = (1, 2, 3, 4)
        result = code_shift((5, 3, 7, 2), turn)
        self.assertEqual(result, (6, 5, 0, 6))
        turn = (-1, 2, -3, 4)
        result = code_shift((2, 4, 8, 1), turn)
        self.assertEqual(result, (1, 6, 5, 5))
        turn = (1, -2, 3, -4)
        result = code_shift((9, 0, 2, 7), turn)
        self.assertEqual(result, (0, 8, 5, 3))


class Week07Morse(UTestCase):
    def test_morse(self):
        from cp.ex07.morse_to_text import morse_to_text

        self.assertEqual(
            morse_to_text(
                "-.. --- - ...  .- -. -..  -.. .- ... .... . ...  - . .-.. .-..  .- -. -.-. .. . -. -  - .- .-.. . ..."
            ),
            "DOTS AND DASHES TELL ANCIENT TALES",
        )
        self.assertEqual(
            morse_to_text("..  --. ---  - ---  - .... .  -.. . -. - .. ... -"),
            "I GO TO THE DENTIST",
        )
        self.assertEqual(
            morse_to_text("- --- -.. .- -.--  .-- .- ...  -.-. .-.. . .- .-."),
            "TODAY WAS CLEAR",
        )
        self.assertEqual(
            morse_to_text(
                "- .... .  -- .- --. .. -.-.  --- ..-.  - .... .  ... ..- -."
            ),
            "THE MAGIC OF THE SUN",
        )
        self.assertEqual(
            morse_to_text("- .... .  .--- --- -.--  .. -.  -- -.--  .... . .- .-. -"),
            "THE JOY IN MY HEART",
        )


class Week07AstronomicalSeason(UTestCase):
    def test_winter(self):
        from cp.ex07.astronomical_season import astronomical_season

        self.assertEqual(astronomical_season((21, "dec")), "winter")
        self.assertEqual(astronomical_season((15, "feb")), "winter")
        self.assertEqual(astronomical_season((19, "mar")), "winter")

    def test_spring(self):
        from cp.ex07.astronomical_season import astronomical_season

        self.assertEqual(astronomical_season((20, "mar")), "spring")
        self.assertEqual(astronomical_season((10, "apr")), "spring")
        self.assertEqual(astronomical_season((20, "jun")), "spring")

    def test_summer(self):
        from cp.ex07.astronomical_season import astronomical_season

        self.assertEqual(astronomical_season((21, "jun")), "summer")
        self.assertEqual(astronomical_season((5, "jul")), "summer")
        self.assertEqual(astronomical_season((22, "sep")), "summer")

    def test_autumn(self):
        from cp.ex07.astronomical_season import astronomical_season

        self.assertEqual(astronomical_season((23, "sep")), "autumn")
        self.assertEqual(astronomical_season((10, "oct")), "autumn")
        self.assertEqual(astronomical_season((20, "dec")), "autumn")


class Week07Tests(Report):  # 240 total.
    title = "Tests for week 07"
    # version = 0.1
    # url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = [
        (Week07HaveEqualLength, 10),
        (Week07LastDifference, 10),
        (Week07MultipleValues, 10),
        (Week07BoxPacking, 10),
        (Week07Hue, 10),
        (Week07CodeShift, 10),
        (Week07Morse, 10),
        (Week07AstronomicalSeason, 10),
    ]


if __name__ == "__main__":
    from unitgrade import evaluate_report_student

    evaluate_report_student(Week07Tests())
