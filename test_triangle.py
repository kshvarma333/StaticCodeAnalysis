""" Testing classify_triangle """
import unittest

from triangle import classify_triangle

class TestTriangles(unittest.TestCase):
    """ Testing classify_triangle function """

    def test_set_1(self) -> None:
        """ Testing value errors """
        with self.assertRaises(ValueError):
            classify_triangle("a", 2, 3)
        with self.assertRaises(ValueError):
            classify_triangle(1, "b", 3)
        with self.assertRaises(ValueError):
            classify_triangle(1, 2, "c")
        with self.assertRaises(ValueError):
            classify_triangle(-1, 2, 3)
        with self.assertRaises(ValueError):
            classify_triangle(1, 0, 3)
        with self.assertRaises(ValueError):
            classify_triangle(1, 2, -9)

    def test_set_2(self) -> None:
        """ Testing values for Equilateral traingle """
        self.assertEqual("Equilateral triangle", classify_triangle(1, 1, 1))
        self.assertEqual("Equilateral triangle", classify_triangle(2, 2, 2))
        self.assertEqual("Equilateral triangle", classify_triangle(3, 3, 3))
        self.assertEqual("Equilateral triangle", classify_triangle(4, 4, 4))

    def test_set_3(self) -> None:
        """ Testing values for Isosceless traingle """
        self.assertEqual("Isosceles triangle", classify_triangle(12, 12, 16))
        self.assertEqual("Isosceles triangle", classify_triangle(22, 22, 42))
        self.assertEqual("Isosceles triangle", classify_triangle(33, 33, 53))
        self.assertEqual("Isosceles triangle", classify_triangle(43, 43, 54))

    def test_set_4(self) -> None:
        """ Testing values for Right angle traingle """
        self.assertEqual("Right angle triangle", classify_triangle(3, 4, 5))
        self.assertEqual("Right angle triangle", classify_triangle(6, 8, 10))
        self.assertEqual("Right angle triangle", classify_triangle(7, 24, 25))
        self.assertEqual("Right angle triangle", classify_triangle(5, 12, 13))

    def test_set_5(self) -> None:
        """ Testing values for Scalen triangle """
        self.assertEqual("Scalen triangle", classify_triangle(3, 4, 6))
        self.assertEqual("Scalen triangle", classify_triangle(6, 8, 11))
        self.assertEqual("Scalen triangle", classify_triangle(7, 24, 26))
        self.assertEqual("Scalen triangle", classify_triangle(5, 12, 14))

    def test_set_6(self) -> None:
        """ Testing Non triangle values """
        self.assertEqual("Not a triangle", classify_triangle(1, 1, 3))
        self.assertEqual("Not a triangle", classify_triangle(1, 3, 7))
        self.assertEqual("Not a triangle", classify_triangle(4, 5, 26))
        self.assertEqual("Not a triangle", classify_triangle(5, 6, 14))


def main():
    """ main function """
    print("********************************************************")
    print(classify_triangle(1, 1, 1))
    print(classify_triangle(43, 43, 54))
    print(classify_triangle(5, 12, 13))
    print(classify_triangle(5, 12, 14))
    print(classify_triangle(1, 1, 3))
    print("************************ UNIT TEST ********************************")
    unittest.main(exit=False, verbosity=2)


if __name__ == '__main__':
    main()
