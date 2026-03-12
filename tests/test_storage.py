import tempfile
import pytest
from src.canvas import Canvas
from src.shapes import Point, Circle, Oval, Rectangle
from src.storage import save_canvas, load_canvas, dict_to_shape, shape_to_dict


def test_shape_to_dict_and_back():
    p = Point(1, 2)
    d = shape_to_dict(p)
    assert d["type"] == "point"
    assert d["args"] == [1, 2]
    assert dict_to_shape(d).x == p.x and dict_to_shape(d).y == p.y


def test_save_and_load_canvas_roundtrip():
    c = Canvas()
    c.add(Point(1, 2))
    c.add(Circle(0, 0, 5))
    c.add(Oval(0, 0, 4, 2))
    c.add(Rectangle(10, 10, 8, 6))
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        path = f.name
    try:
        save_canvas(c, path)
        loaded = load_canvas(path)
        orig = c.list_shapes()
        rest = loaded.list_shapes()
        assert len(orig) == len(rest) == 4
        for (i1, s1), (i2, s2) in zip(orig, rest):
            assert i1 == i2
            assert type(s1) == type(s2)
            assert shape_to_dict(s1) == shape_to_dict(s2)
    finally:
        import os
        os.unlink(path)


def test_load_canvas_preserves_ids():
    c = Canvas()
    c.add(Point(0, 0))
    c.add(Point(1, 1))
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        path = f.name
    try:
        save_canvas(c, path)
        loaded = load_canvas(path)
        items = loaded.list_shapes()
        assert items[0][0] == 1 and items[1][0] == 2
        next_id = loaded.add(Point(2, 2))
        assert next_id == 3
    finally:
        import os
        os.unlink(path)
