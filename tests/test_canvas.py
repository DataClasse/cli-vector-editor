from src.canvas import Canvas
from src.shapes import Point, Circle


def test_canvas_add_and_list():
    c = Canvas()
    c.add(Point(1, 2))
    c.add(Circle(0, 0, 5))
    items = c.list_shapes()
    assert len(items) == 2
    assert items[0][0] == 1 and items[0][1].__class__.__name__ == "Point"
    assert items[1][0] == 2 and items[1][1].__class__.__name__ == "Circle"


def test_canvas_delete():
    c = Canvas()
    c.add(Point(1, 2))
    c.add(Point(3, 4))
    c.delete(1)
    items = c.list_shapes()
    assert len(items) == 1
    assert items[0][0] == 2
