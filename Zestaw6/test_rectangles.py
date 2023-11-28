import unittest
from rectangles import *


class TestRectangle(unittest.TestCase):
    def test_str(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(rect), "[(1, 2), (3, 4)]")

    def test_repr(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(repr(rect), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect1, rect2)

    def test_ne(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(5, 6, 7, 8)
        self.assertNotEqual(rect1, rect2)

    def test_center(self):
        rect = Rectangle(1, 2, 5, 6)
        self.assertEqual(rect.center(), Point(3.0, 4.0))

    def test_area(self):
        rect = Rectangle(1, 2, 5, 6)
        self.assertEqual(rect.area(), 16)

    def test_move(self):
        rect = Rectangle(1, 2, 3, 4)
        rect.move(2, 3)
        self.assertEqual(rect, Rectangle(3, 5, 5, 7))


if __name__ == "__main__":
    unittest.main()
