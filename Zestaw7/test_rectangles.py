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

    def test_intersection(self):
        rect1 = Rectangle(1, 1, 4, 4)
        rect2 = Rectangle(2, 2, 5, 5)
        result = rect1.intersection(rect2)
        self.assertEqual(str(result), "[(2, 2), (4, 4)]")

    def test_cover(self):
        rect1 = Rectangle(1, 1, 3, 3)
        rect2 = Rectangle(2, 2, 4, 4)
        result = rect1.cover(rect2)
        self.assertEqual(str(result), "[(1, 1), (4, 4)]")
    def test_make4(self):
        rect = Rectangle(1, 1, 4, 4)
        rect1, rect2, rect3, rect4 = rect.make4()

        self.assertEqual(rect1, Rectangle(1, 1, 2.5, 2.5))
        self.assertEqual(rect2, Rectangle(2.5, 1, 4, 2.5))
        self.assertEqual(rect3, Rectangle(1, 2.5, 2.5, 4))
        self.assertEqual(rect4, Rectangle(2.5, 2.5, 4, 4))

if __name__ == "__main__":
    unittest.main()
