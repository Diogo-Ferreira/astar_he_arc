class City(object):
    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = float(x_pos)
        self.y_pos = float(y_pos)
        self.connections = {}
        self.gx = 0
        self.parent = None

    def add_connection_to(self, to, distance):
        self.connections[to] = float(distance)

    def __str__(self):
        return self.name

    def __getitem__(self, item):
        if item in self.connections:
            return self.connections[item]
        else:
            return 0

    def __hash__(self):
        return str(self.name).__hash__()

    def __iter__(self):
        """Allows to iterate each connections"""
        return self.connections.items().__iter__()

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, City):
            return self.name == other.name
        else:
            return super.__eq__(other)
