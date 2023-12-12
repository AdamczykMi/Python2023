import pytest
from rectangles import Rectangle
from points import Point

def test_rectangle_from_points():
    point1 = Point(1, 2)
    point2 = Point(3, 4)
    rectangle = Rectangle.from_points((point1, point2))
    assert rectangle == Rectangle(1, 2, 3, 4)

def test_rectangle_attributes():
    rectangle = Rectangle(1, 2, 5, 6)
    assert rectangle.top == 6
    assert rectangle.left == 1
    assert rectangle.bottom == 2
    assert rectangle.right == 5
    assert rectangle.width == 4
    assert rectangle.height == 4
    assert rectangle.topleft == Point(1, 6)
    assert rectangle.bottomleft == Point(1, 2)
    assert rectangle.topright == Point(5, 6)
    assert rectangle.bottomright == Point(5, 2)

def test_rectangle_center():
    rectangle = Rectangle(1, 2, 5, 6)
    assert rectangle.center == Point(3, 4)

def test_rectangle_area():
    rectangle = Rectangle(1, 2, 5, 6)
    assert rectangle.area() == 16

def test_rectangle_move():
    rectangle = Rectangle(1, 2, 5, 6)
    rectangle.move(2, -1)
    assert rectangle == Rectangle(3, 1, 7, 5)

def test_rectangle_intersection():
    rectangle1 = Rectangle(1, 2, 5, 6)
    rectangle2 = Rectangle(3, 4, 7, 8)
    intersection = rectangle1.intersection(rectangle2)
    assert intersection == Rectangle(3, 4, 5, 6)

def test_rectangle_cover():
    rectangle1 = Rectangle(1, 2, 5, 6)
    rectangle2 = Rectangle(3, 4, 7, 8)
    cover = rectangle1.cover(rectangle2)
    assert cover == Rectangle(1, 2, 7, 8)

def test_rectangle_make4():
    rectangle = Rectangle(1, 2, 5, 6)
    rects = rectangle.make4()
    assert rects == (
        Rectangle(1, 2, 3, 4),
        Rectangle(3, 2, 5, 4),
        Rectangle(1, 4, 3, 6),
        Rectangle(3, 4, 5, 6)
    )


