from src.cli import parse_command, create_shape_from_command


def test_parse_add_point():
    cmd = parse_command("add point 1 2")
    assert cmd is not None
    assert cmd["action"] == "add"
    assert cmd["shape"] == "point"
    assert cmd["args"] == [1.0, 2.0]


def test_parse_add_circle():
    cmd = parse_command("add circle 0 0 5")
    assert cmd["action"] == "add"
    assert cmd["shape"] == "circle"
    assert cmd["args"] == [0.0, 0.0, 5.0]


def test_parse_list():
    cmd = parse_command("list")
    assert cmd["action"] == "list"
    assert "shape" not in cmd or cmd.get("shape") is None


def test_parse_delete():
    cmd = parse_command("delete 3")
    assert cmd["action"] == "delete"
    assert cmd["id"] == 3


def test_parse_quit():
    cmd = parse_command("quit")
    assert cmd["action"] == "quit"


def test_parse_invalid_empty():
    cmd = parse_command("")
    assert cmd is None or cmd.get("action") == "invalid"


def test_create_shape_point():
    cmd = parse_command("add point 1 2")
    shape = create_shape_from_command(cmd)
    assert shape is not None
    assert shape.__class__.__name__ == "Point"
    assert shape.x == 1 and shape.y == 2


def test_create_shape_circle():
    cmd = parse_command("add circle 0 0 5")
    shape = create_shape_from_command(cmd)
    assert shape is not None
    assert shape.__class__.__name__ == "Circle"
    assert shape.r == 5


def test_create_shape_invalid_args_returns_none():
    cmd = parse_command("add point 1")  # не хватает y
    shape = create_shape_from_command(cmd)
    assert shape is None


def test_parse_save():
    cmd = parse_command("save shapes.json")
    assert cmd["action"] == "save"
    assert cmd["path"] == "shapes.json"


def test_parse_load():
    cmd = parse_command("load shapes.json")
    assert cmd["action"] == "load"
    assert cmd["path"] == "shapes.json"


def test_create_shape_oval():
    cmd = parse_command("add oval 0 0 5 3")
    shape = create_shape_from_command(cmd)
    assert shape is not None
    assert shape.__class__.__name__ == "Oval"
    assert shape.a == 5 and shape.b == 3


def test_create_shape_rectangle():
    cmd = parse_command("add rectangle 0 0 10 4")
    shape = create_shape_from_command(cmd)
    assert shape is not None
    assert shape.__class__.__name__ == "Rectangle"
    assert shape.width == 10 and shape.height == 4
