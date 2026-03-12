from src.shapes import Point, Segment, Circle, Square, Oval, Rectangle


def parse_command(line: str):
    line = line.strip()
    if not line:
        return None
    parts = line.split()
    action = parts[0].lower()
    if action == "add":
        if len(parts) < 2:
            return {"action": "invalid"}
        shape = parts[1].lower()
        try:
            args = [float(x) for x in parts[2:]]
        except ValueError:
            return {"action": "invalid"}
        return {"action": "add", "shape": shape, "args": args}
    if action == "list":
        return {"action": "list"}
    if action in ("quit", "exit", "q"):
        return {"action": "quit"}
    if action == "save":
        if len(parts) != 2:
            return {"action": "invalid"}
        return {"action": "save", "path": parts[1]}
    if action == "load":
        if len(parts) != 2:
            return {"action": "invalid"}
        return {"action": "load", "path": parts[1]}
    if action == "delete":
        if len(parts) != 2:
            return {"action": "invalid"}
        try:
            return {"action": "delete", "id": int(parts[1])}
        except ValueError:
            return {"action": "invalid"}
    return {"action": "invalid"}


def create_shape_from_command(cmd):
    if not cmd or cmd.get("action") != "add" or "args" not in cmd:
        return None
    shape_name = cmd.get("shape")
    args = cmd.get("args", [])
    if shape_name == "point" and len(args) == 2:
        return Point(args[0], args[1])
    if shape_name == "segment" and len(args) == 4:
        return Segment(args[0], args[1], args[2], args[3])
    if shape_name == "circle" and len(args) == 3:
        return Circle(args[0], args[1], args[2])
    if shape_name == "square" and len(args) == 3:
        return Square(args[0], args[1], args[2])
    if shape_name == "oval" and len(args) == 4:
        return Oval(args[0], args[1], args[2], args[3])
    if shape_name == "rectangle" and len(args) == 4:
        return Rectangle(args[0], args[1], args[2], args[3])
    return None
