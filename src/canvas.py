class Canvas:
    def __init__(self):
        self._shapes = []
        self._next_id = 1

    def add(self, shape):
        sid = self._next_id
        self._next_id += 1
        self._shapes.append((sid, shape))
        return sid

    def delete(self, shape_id: int):
        self._shapes = [(i, s) for i, s in self._shapes if i != shape_id]

    def list_shapes(self):
        return list(self._shapes)
