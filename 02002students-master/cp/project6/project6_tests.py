from unitgrade import UTestCase, Report
import numpy as np

class Week11Outliers(UTestCase):
    def assertArrayEqual(self, a, b):
        self.assertIsNotNone(a)
        self.assertIsNone(np.testing.assert_array_equal(a, b))

    def test_outliers1(self):
        from cp.ex11.outliers import outliers
        from cp.ex11.bacterial_growth import load_data
        self.assertArrayEqual(outliers(load_data()), np.array([50, 96, 104]))

    def test_outliers2(self):
        from cp.ex11.outliers import outliers
        np.random.seed(43)
        data = (np.random.rand(160, 20)*2)**2
        self.assertArrayEqual(outliers(data), np.array([19, 39, 68, 92, 101, 154]))

    def test_outliers3(self):
        from cp.ex11.outliers import outliers
        np.random.seed(48)
        data = (np.random.rand(300, 12)*2)**2
        self.assertArrayEqual(outliers(data), np.array([ 25,  98, 128, 145, 151, 196, 201, 230, 239, 273, 277, 287]))

class Week11BacterialArea(UTestCase):
    def test_bacterial_area(self):
        from cp.ex11.bacterial_area import bacterial_area
        path = 'cp/ex11/files/bacteria.npy'
        self.assertAlmostEqual(bacterial_area(path), 0.3757223140495868)

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
            (Week11Outliers, 20),
            (Week11BacterialArea, 20),
            (Week12PolygonGetPerimeter,20),
            (Week12PolygonSmooth,20)
            ]
class Project6(Report):
    title = "Project 6"
    remote_url = "https://cp.pages.compute.dtu.dk/02002public/_static/evaluation/"

    abbreviate_questions = True
    questions = questions
    import cp
    pack_imports = [cp]


if __name__ == "__main__":
    from unitgrade import evaluate_report_student
    evaluate_report_student(Project6())
