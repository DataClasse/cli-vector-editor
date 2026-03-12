import json
from src.shapes import (
    Point,
    Segment,
    Circle,
    Square,
    Oval,
    Rectangle,
)

TYPE_TO_CLASS = {
    "point": Point,
    "segment": Segment,
    "circle": Circle,
    "square": Square,
    "oval": Oval,
    "rectangle": Rectangle,
}

CLASS_TO_ARGS = {
    Point: ["x", "y"],
    Segment: ["x1", "y1", "x2", "y2"],
    Circle: ["x", "y", "r"],
    Square: ["x", "y", "side"],
    Oval: ["x", "y", "a", "b"],
    Rectangle: ["x", "y", "width", "height"],
}


def shape_to_dict(shape):
    cls = type(shape)
    args = [getattr(shape, attr) for attr in CLASS_TO_ARGS[cls]]
    return {"type": cls.__name__.lower(), "args": args}


def dict_to_shape(d):
    type_name = d["type"]
    if type_name not in TYPE_TO_CLASS:
        raise ValueError(f"Unknown shape type: {type_name}")
    return TYPE_TO_CLASS[type_name](*d["args"])


def save_canvas(canvas, path):
    data = [
        {"id": sid, "type": type(shape).__name__.lower(), "args": [getattr(shape, a) for a in CLASS_TO_ARGS[type(shape)]]}
        for sid, shape in canvas.list_shapes()
    ]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_canvas(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    from src.canvas import Canvas
    canvas = Canvas()
    max_id = 0
    for item in data:
        sid = item["id"]
        shape = dict_to_shape({"type": item["type"], "args": item["args"]})
        canvas._shapes.append((sid, shape))
        if sid >= max_id:
            max_id = sid
    canvas._next_id = max_id + 1
    return canvas
