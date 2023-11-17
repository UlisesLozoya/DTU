from unitgrade import Report
import cp
from unitgrade import UTestCase
import numpy as np

import os
os.chdir(os.path.join(os.path.dirname(cp.__file__), '..'))

class Week11Lists(UTestCase):
    def test_avg(self):
        from cp.ex11.list_exercises_numpy import avg
        result = avg(np.array([1,2,3,4,5]))
        self.assertEqual(result, 3.)
        result = avg(np.array([2,3,7,8,1,12,5,2,9]))
        self.assertAlmostEqual(result, 5.444444444444445)
    def test_conditional_max(self):
        from cp.ex11.list_exercises_numpy import conditional_max
        result = conditional_max(np.array([1.,2.,3.,4.,5.]), 3.)
        self.assertEqual(result, 2)
        result = conditional_max(np.array([2.,3.,7.,8.,1.,12.,5.,2.,9.]), 5.)
        self.assertEqual(result, 3)
    def test_vector_add(self):
        from cp.ex11.list_exercises_numpy import vector_add
        result = vector_add(np.array([1,2,3,4,5]), np.array([3,4,5,6,7]))
        self.assertEqual(result.tolist(), [4,6,8,10,12])
        result = vector_add(np.array([2,3,7,8,1,12,5,2,9]), np.array([8,4,3,4,5,6,7, 17,2]))
        self.assertEqual(result.tolist(), [10,7,10,12,6,18,12,19,11])
    def test_count_multiples(self):
        from cp.ex11.list_exercises_numpy import count_multiples
        result = count_multiples(np.array([1,2,3,4,5]), 3)
        self.assertEqual(result, 1)
        result = count_multiples(np.array([2,15,7,8,1,10,5,2,9]), 5)
        self.assertEqual(result, 3)
        result = count_multiples(np.array([2,15,8,1,10,5,2,9]), 7)
        self.assertEqual(result, 0)
    def test_return_multiples(self):
        from cp.ex11.list_exercises_numpy import return_multiples
        result = return_multiples(np.array([1,2,3,4,5]), 3)
        self.assertEqual(result.tolist(), [3])
        result = return_multiples(np.array([2,15,7,8,1,10,5,2,9]), 5)
        self.assertEqual(result.tolist(), [15,10,5])
        result = return_multiples(np.array([2,15,8,1,10,5,2,9]), 7)
        self.assertEqual(result.tolist(), [])

class Week11Subimage(UTestCase):
    def test_extract_subimage(self):
        from cp.ex11.extract_subimage import extract_subimage
        image = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
        result = extract_subimage(image, (0,0), (2,2))
        self.assertEqual(result.tolist(), [[1,2],[6,7]])
        result = extract_subimage(image, (1,2), (2,3))
        self.assertEqual(result.tolist(), [[8,9,10],[13,14,15]])
        result = extract_subimage(image, (0,2), (3,2))
        self.assertEqual(result.tolist(), [[3,4],[8,9],[13,14]])

class Week11Threshold(UTestCase):
    def test_threshold_image(self):
        from cp.ex11.threshold_image import threshold_image
        image = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
        result = threshold_image(image, 3)
        self.assertEqual(result.tolist(), [[0,0,0,1,1],[1,1,1,1,1],[1,1,1,1,1]])
        result = threshold_image(image, 9)
        self.assertEqual(result.tolist(), [[0,0,0,0,0],[0,0,0,0,1],[1,1,1,1,1]])
        result = threshold_image(image, 15)
        self.assertEqual(result.tolist(), [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

class Week11BacterialGrowth(UTestCase): 
    def test_load_data(self):
        from cp.ex11.bacterial_growth import load_data
        result = load_data()
        self.assertEqual(result.shape, (160,12))
        self.assertAlmostEqual(result[0,0], 1.44)
        self.assertAlmostEqual(result[159,11], 16.67)
    def test_threshold_exceeded(self):
        from cp.ex11.bacterial_growth import load_data, threshold_exceeded
        data = load_data()
        result = threshold_exceeded(data, 8.5)
        self.assertEqual(result.size, 160)
        result = threshold_exceeded(data, 9.)
        self.assertAlmostEqual(np.mean(result), 9.49375)


class Week11AverageGrowthCurve(UTestCase):
    def assertArrayAlmostEqual(self, a, b):
        self.assertIsNotNone(a)
        self.assertIsNone(np.testing.assert_almost_equal(a, b))

    def test_get_std(self):
        from cp.ex11.bacterial_growth import get_std
        data = np.ones((4,4))
        data[::2] = 2
        self.assertArrayAlmostEqual(get_std(data), np.array([0.5, 0.5, 0.5, 0.5]))
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])**2
        self.assertArrayAlmostEqual(get_std(data), np.array([20.04993766, 24.85960579, 29.69848481]))
        data = np.sqrt(np.arange(42)).reshape(6, 7).T
        self.assertArrayAlmostEqual(get_std(data), np.array([0.7781667, 0.3194126, 0.2433594, 0.2044697, 0.1797871, 0.1623305]))
    
    def test_get_mean(self):
        from cp.ex11.bacterial_growth import get_mean
        data = np.ones((4,4))
        data[::2] = 2
        self.assertArrayAlmostEqual(get_mean(data), np.array([1.5, 1.5, 1.5, 1.5]))
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])**2
        self.assertArrayAlmostEqual(get_mean(data), np.array([22., 31., 42.]))
        data = np.sqrt(np.arange(42)).reshape(6, 7).T
        self.assertArrayAlmostEqual(get_mean(data), np.array([1.5474032, 3.1461048, 4.1159174, 4.8947106, 5.5648609, 6.1622763]))


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

questions = [
                (Week11Lists, 25),
                (Week11Subimage, 10),
                (Week11Threshold, 10),
                (Week11BacterialGrowth, 20),
                (Week11AverageGrowthCurve, 20),
                (Week11Outliers, 20),
                (Week11BacterialArea, 20)
            ]


class Week11Tests(Report): #30 total.
    title = "Tests for week 11"
    #version = 0.1
    #url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = questions


if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week11Tests())
