from unitgrade import Report, UTestCase
import unittest
import cp
import inspect


class Week09TestRectanglePerimeter(UTestCase):
    def make_rectangle(self, width, height):
        from cp.ex09.rectangle import Rectangle
        init_parameters = inspect.signature(Rectangle.__init__).parameters
        if len(init_parameters) == 5:  # If the class has already been extended to have a center
            return Rectangle(width, height, 0, 0)
        else:
            return Rectangle(width, height)

    def test_perimeter(self):
        self.assertEqual(self.make_rectangle(10, 4).get_perimeter(), 28)
        self.assertEqual(self.make_rectangle(4, 10).get_perimeter(), 28)
        self.assertEqual(self.make_rectangle(2, 8).get_perimeter(), 20)
        self.assertEqual(self.make_rectangle(15, 12).get_perimeter(), 54)
        self.assertEqual(self.make_rectangle(1, 1).get_perimeter(), 4)
        self.assertEqual(self.make_rectangle(10, 1).get_perimeter(), 22)


class Week09TestCorners(UTestCase):
    def test_corners(self):
        from cp.ex09.rectangle import Rectangle
        X, Y = Rectangle(2, 5, 3, 4).get_corners()
        self.assertEqual(X, [2.0, 2.0, 4.0, 4.0])
        self.assertEqual(Y, [1.5, 6.5, 6.5, 1.5])

        X, Y = Rectangle(1, 1, 3, 4).get_corners()
        self.assertEqual(X, [2.5, 2.5, 3.5, 3.5])
        self.assertEqual(Y, [3.5, 4.5, 4.5, 3.5])

        X, Y = Rectangle(1, 2, 8, 2).get_corners()
        self.assertEqual(X, [7.5, 7.5, 8.5, 8.5])
        self.assertEqual(Y, [1.0, 3.0, 3.0, 1.0])

        X, Y = Rectangle(7, 2, 3, 4).get_corners()
        self.assertEqual(X, [-0.5, -0.5, 6.5, 6.5])
        self.assertEqual(Y, [3.0, 5.0, 5.0, 3.0])


class Week09TestVector(UTestCase):
    def test_make_vector(self):
        from cp.ex09.vector import Vector

        v1 = Vector(2, 3)
        self.assertIsInstance(v1, Vector, msg="Must return a Vector instance.")
        self.assertEqual(v1.x, 2)
        self.assertEqual(v1.y, 3)

        v1 = Vector(3, 5)
        self.assertIsInstance(v1, Vector, msg="Must return a Vector instance.")
        self.assertEqual(v1.x, 3)
        self.assertEqual(v1.y, 5)

        v1 = Vector(10, 2)
        self.assertIsInstance(v1, Vector, msg="Must return a Vector instance.")
        self.assertEqual(v1.x, 10)
        self.assertEqual(v1.y, 2)


class Week09VectorAddition(unittest.TestCase):
    def test_add_positive_vectors(self):
        from cp.ex09.vector import Vector
        vector1 = Vector(2, 3)
        vector2 = Vector(4, 5)
        result = vector1.add(vector2)
        # Check that the original vectors are unchanged
        self.assertEqual((vector1.x, vector1.y), (2, 3))
        self.assertEqual((vector2.x, vector2.y), (4, 5))

        self.assertEqual(result.x, vector1.x + vector2.x)
        self.assertEqual(result.y, vector1.y + vector2.y)

    def test_add_negative_vectors(self):
        from cp.ex09.vector import Vector
        vector1 = Vector(-2, -3)
        vector2 = Vector(-4, -5)
        result = vector1.add(vector2)
        # Check that the original vectors are unchanged
        self.assertEqual((vector1.x, vector1.y), (-2, -3))
        self.assertEqual((vector2.x, vector2.y), (-4, -5))

        self.assertEqual(result.x, vector1.x + vector2.x)
        self.assertEqual(result.y, vector1.y + vector2.y)

    def test_add_mixed_vectors(self):
        from cp.ex09.vector import Vector
        vector1 = Vector(2, -3)
        vector2 = Vector(-4, 5)
        result = vector1.add(vector2)
        # Check that the original vectors are unchanged
        self.assertEqual((vector1.x, vector1.y), (2, -3))
        self.assertEqual((vector2.x, vector2.y), (-4, 5))

        self.assertEqual(result.x, vector1.x + vector2.x)
        self.assertEqual(result.y, vector1.y + vector2.y)


class Week09VectorDotProduct(unittest.TestCase):

    def test_dot_product_with_positive_vectors(self):
        from cp.ex09.vector import Vector
        vector1 = Vector(2, 3)
        vector2 = Vector(4, 5)
        result = vector1.dot(vector2)
        self.assertEqual(result, vector1.x * vector2.x + vector1.y * vector2.y)

    def test_dot_product_with_negative_vectors(self):
        from cp.ex09.vector import Vector
        vector1 = Vector(-2, -3)
        vector2 = Vector(-4, -5)
        result = vector1.dot(vector2)
        self.assertEqual(result, vector1.x * vector2.x + vector1.y * vector2.y)

    def test_dot_product_with_mixed_vectors(self):
        from cp.ex09.vector import Vector
        vector1 = Vector(2, -3)
        vector2 = Vector(-4, 5)
        result = vector1.dot(vector2)
        self.assertEqual(result, vector1.x * vector2.x + vector1.y * vector2.y)


class Week09VectorScale(unittest.TestCase):

    def test_scale_positive_vector(self):
        from cp.ex09.vector import Vector
        vector1 = Vector(2, 3)
        scale_factor = 2
        scaled_vector = vector1.scale(scale_factor)

        self.assertEqual(scaled_vector.x, vector1.x * scale_factor)
        self.assertEqual(scaled_vector.y, vector1.y * scale_factor)

        # Check that the original vector is unchanged
        self.assertEqual((vector1.x, vector1.y), (2, 3))

    def test_scale_negative_vector(self):
        from cp.ex09.vector import Vector
        vector1 = Vector(-2, -3)
        scale_factor = 3
        scaled_vector = vector1.scale(scale_factor)

        self.assertEqual(scaled_vector.x, vector1.x * scale_factor)
        self.assertEqual(scaled_vector.y, vector1.y * scale_factor)

        # Check that the original vector is unchanged
        self.assertEqual((vector1.x, vector1.y), (-2, -3))

    def test_scale_mixed_vector(self):
        from cp.ex09.vector import Vector
        vector1 = Vector(2, -3)
        scale_factor = -1.5
        scaled_vector = vector1.scale(scale_factor)

        self.assertEqual(scaled_vector.x, vector1.x * scale_factor)
        self.assertEqual(scaled_vector.y, vector1.y * scale_factor)

        # Check that the original vector is unchanged
        self.assertEqual((vector1.x, vector1.y), (2, -3))


class Week09TranslatingRectangle(UTestCase):
    def test_move_vector(self):
        from cp.ex09.vector import Vector
        from cp.ex09.rectangle import Rectangle
        r = Rectangle(10, 4, 2, 2)
        r.translate(Vector(2, 3))
        self.assertEqual(r.x_c, 4)
        self.assertEqual(r.y_c, 5)

        r = Rectangle(1, 2, 1, 1)
        r.translate(Vector(4, 2))
        self.assertEqual(r.x_c, 5)
        self.assertEqual(r.y_c, 3)

        r = Rectangle(12, 14, 0, 0)
        r.translate(Vector(-5, 5))
        self.assertEqual(r.x_c, -5)
        self.assertEqual(r.y_c, 5)

        r = Rectangle(12, 13, -5, 2)
        r.translate(Vector(10, 12))
        self.assertEqual(r.x_c, 5)
        self.assertEqual(r.y_c, 14)


questions = [
    (Week09TestRectanglePerimeter, 10),
    (Week09TestVector, 10),
    (Week09VectorDotProduct, 10),
    (Week09VectorAddition, 10),
    (Week09VectorScale, 10),
    (Week09TranslatingRectangle, 10),
    (Week09TestCorners, 10),
]


class Week09Tests(Report):
    title = "Tests for week 09"
    # version = 1.0
    # url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = questions


if __name__ == '__main__':
    from unitgrade import evaluate_report_student

    evaluate_report_student(Week09Tests())
