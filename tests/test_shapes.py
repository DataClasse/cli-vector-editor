import pytest
from src.shapes import Point, Segment, Circle, Square, Oval, Rectangle


def test_point_repr():
    p = Point(1, 2)
    assert repr(p) == "Point(1, 2)"


def test_segment_repr():
    s = Segment(0, 0, 10, 10)
    assert repr(s) == "Segment(0, 0, 10, 10)"


def test_circle_repr():
    c = Circle(0, 0, 5)
    assert repr(c) == "Circle(0, 0, 5)"


def test_square_repr():
    sq = Square(0, 0, 4)
    assert repr(sq) == "Square(0, 0, 4)"


def test_oval_repr():
    o = Oval(0, 0, 5, 3)
    assert repr(o) == "Oval(0, 0, 5, 3)"


def test_rectangle_repr():
    r = Rectangle(0, 0, 10, 4)
    assert repr(r) == "Rectangle(0, 0, 10, 4)"
