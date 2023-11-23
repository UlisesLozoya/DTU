from unitgrade import Report, UTestCase
import unittest
import cp
import inspect
import numpy as np

class Week12CprCheck(UTestCase):
    def test_cpr_check(self):
        from cp.ex12.cpr_check import cpr_check
        self.assertEqual(cpr_check('1111111111'), False)
        self.assertEqual(cpr_check('1111111118'), True)
        # The following CPR numbers are randomly generated, don't worry ;)
        self.assertEqual(cpr_check('0577561362'), True)
        self.assertEqual(cpr_check('9497763417'), True)
        self.assertEqual(cpr_check('3422336957'), True)
        self.assertEqual(cpr_check('0409275504'), False)
        self.assertEqual(cpr_check('1466340617'), False)
        self.assertEqual(cpr_check('4213233632'), True)

class Week12PolygonInit(UTestCase):
    def assertArrayAlmostEqual(self, a, b):
        self.assertIsNotNone(a)
        self.assertIsNone(np.testing.assert_almost_equal(a, b))

    def test_polygon_init(self):
        from cp.ex12.polygon import Polygon

        P = Polygon([(0, 12), (12, 1), (1, 0), (0, 0)])
        self.assertArrayAlmostEqual(P.x, np.array([0, 12, 1, 0]))
        self.assertArrayAlmostEqual(P.y, np.array([12, 1, 0, 0]))

        P = Polygon([(0, 3), (3, 1), (1, 0), (0, 0)])
        self.assertArrayAlmostEqual(P.x, np.array([0, 3, 1, 0]))
        self.assertArrayAlmostEqual(P.y, np.array([3, 1, 0, 0]))

        P = Polygon([(4, -1), (1, 4), (1, 0), (0, 0)])
        self.assertArrayAlmostEqual(P.x, np.array([4, 1, 1, 0]))
        self.assertArrayAlmostEqual(P.y, np.array([-1, 4, 0, 0]))

        P= Polygon([(0, 10), (1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 3), (7, 2), (8, -3), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (0, 10)])
        self.assertArrayAlmostEqual(P.x, np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 0]))
        self.assertArrayAlmostEqual(P.y, np.array([10, 9, 8, 7, 6, 5, 3, 2, -3, 2, 3, 4, 5, 6, 7, 10]))

class Week12PolygonGetArea(UTestCase):
    def test_polygon_area(self):
        from cp.ex12.polygon import Polygon
        P = Polygon([(0, 12), (12, 1), (1, 0), (0, 0)])
        self.assertEqual(P.get_area(),72.5)

        P = Polygon([(0, 3), (1, 1), (3, 1), (0, 0)])
        self.assertEqual(P.get_area(),2.5)

        P= Polygon([(4, -1), (1, 4), (1, 0), (0, 0)])
        self.assertEqual(P.get_area(),6.5)

        P= Polygon([(0, 0), (-3, 3), (-1, -3)])
        self.assertEqual(P.get_area(),6.0)

        P= Polygon([(0, -1), (1, 1), (-1, 0), (0, 0)])
        self.assertEqual(P.get_area(),1.0)

        P= Polygon([(0, 10), (1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 3), (7, 2), (8, -3), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (0, 10)])
        self.assertEqual(P.get_area(),4.5)

class Week12PolygonGetPerimeter(UTestCase):
    def test_polygon_perimeter(self):
        from cp.ex12.polygon import Polygon
        P = Polygon([(0, 3), (3, 1), (1, 0), (0, 0)])
        self.assertAlmostEqual(P.get_perimeter(), 9.8416192529637, places=7)

        P = Polygon([(0, 2), (1, 1), (2, 1), (0, 0)])
        self.assertAlmostEqual(P.get_perimeter(), 6.650281539872885, places=7)

        P = Polygon([(4, -1), (1, 4), (1, 0), (0, 0)])
        self.assertAlmostEqual(P.get_perimeter(), 14.95405752046296, places=7)

        P = Polygon([(0, 0), (-3, 3), (-1, -3)])
        self.assertAlmostEqual(P.get_perimeter(), 13.729473667624424, places=7)

        P = Polygon([(0, -1), (1, 1), (-1, 0), (0, 0)])       
        self.assertAlmostEqual(P.get_perimeter(), 6.47213595499958, places=7)

        P = Polygon([(0, 10), (1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 3), (7, 2), (8, -3), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (0, 10)])
        self.assertAlmostEqual(P.get_perimeter(), 31.596007466253397, places=7)

 
class Week12PolygonSmooth(UTestCase):
    def assertArrayAlmostEqual(self, a, b):
        self.assertIsNotNone(a)
        self.assertIsNone(np.testing.assert_almost_equal(a, b))

    def test_polygon_smooth(self):
        from cp.ex12.polygon import Polygon
        P = Polygon([(1, 2), (2, 3), (3, 4), (4, 5), (3, 2), (2, 2.5)])
        P.smooth_polygon(alpha=0.2)
        self.assertArrayAlmostEqual(P.x, np.array([1.2, 2., 3., 3.8, 3., 2. ]))
        self.assertArrayAlmostEqual(P.y, np.array([2.15, 3., 4., 4.6, 2.35, 2.4 ]))

        P.smooth_polygon(alpha=0.2)
        self.assertArrayAlmostEqual(P.x, np.array([1.36, 2.02, 2.98, 3.64, 2.98, 2.02]))
        self.assertArrayAlmostEqual(P.y, np.array([2.26, 3.015, 3.96 , 4.315, 2.58 , 2.37 ]))

        P.smooth_polygon(alpha=0.5)
        self.assertArrayAlmostEqual(P.x, np.array([1.69 , 2.095, 2.905, 3.31 , 2.905, 2.095]))
        self.assertArrayAlmostEqual(P.y, np.array([2.47625, 3.0625 , 3.8125 , 3.7925 , 2.96125, 2.395  ]))

        P.smooth_polygon(alpha=0.5)
        self.assertArrayAlmostEqual(P.x, np.array([1.8925 , 2.19625, 2.80375, 3.1075 , 2.80375, 2.19625]))
        self.assertArrayAlmostEqual(P.y, np.array([2.6025   , 3.1034375, 3.62     , 3.5896875, 3.0275   , 2.556875 ]))

      

questions = [
        (Week12CprCheck, 10),
        (Week12PolygonInit,10),
        (Week12PolygonGetArea,20),
        (Week12PolygonGetPerimeter,20),
        (Week12PolygonSmooth,20)
        ]

class Week12Tests(Report):
    title = "Tests for week 12"
    #version = 1.0
    #url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = questions

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week12Tests())
