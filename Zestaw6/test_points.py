import unittest
from points import *


class TestPoint(unittest.TestCase):
    def test_str(self):
        point = Point(1, 2)
        self.assertEqual(str(point), "(1, 2)")

    def test_repr(self):
        point = Point(1, 2)
        self.assertEqual(repr(point), "Point(1, 2)")

    def test_eq(self):
        point1 = Point(1, 2)
        point2 = Point(1, 2)
        self.assertEqual(point1, point2)

    def test_ne(self):
        point1 = Point(1, 2)
        point2 = Point(3, 4)
        self.assertNotEqual(point1, point2)

    def test_add(self):
        point1 = Point(1, 2)
        point2 = Point(3, 4)
        result = point1 + point2
        self.assertEqual(result, Point(4, 6))

    def test_sub(self):
        point1 = Point(3, 5)
        point2 = Point(1, 2)
        result = point1 - point2
        self.assertEqual(result, Point(2, 3))

    def test_mul(self):
        point1 = Point(1, 2)
        point2 = Point(3, 4)
        result = point1 * point2
        self.assertEqual(result, 11)

    def test_cross(self):
        point1 = Point(1, 2)
        point2 = Point(3, 4)
        result = point1.cross(point2)
        self.assertEqual(result, -2)

    def test_length(self):
        point = Point(3, 4)
        result = point.length()
        self.assertEqual(result, 5.0)


if __name__ == "__main__":
    unittest.main()
