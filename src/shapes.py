class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Segment:
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    def __repr__(self):
        return f"Segment({self.x1}, {self.y1}, {self.x2}, {self.y2})"


class Circle:
    def __init__(self, x: float, y: float, r: float):
        self.x, self.y, self.r = x, y, r

    def __repr__(self):
        return f"Circle({self.x}, {self.y}, {self.r})"


class Square:
    def __init__(self, x: float, y: float, side: float):
        self.x, self.y, self.side = x, y, side

    def __repr__(self):
        return f"Square({self.x}, {self.y}, {self.side})"
