class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, o):
        if isinstance(o, Point2d):
            return Point2d(self.x + o.x, self.y + o.y)
        elif isinstance(o, int):
            return Point2d(self.x + o, self.y + o)

        return self

    def __sub__(self, o):
        if isinstance(o, Point2d):
            return Point2d(self.x - o.x, self.y - o.y)
        elif isinstance(o, int):
            return Point2d(self.x - o, self.y - o)

        return self

    def __truediv__(self, o):
        if isinstance(o, Point2d):
            return Point2d(self.x / o.x, self.y / o.y)
        elif isinstance(o, int):
            return Point2d(self.x / o, self.y / o)

        return self

    def __mul__(self, o):
        if isinstance(o, Point2d):
            return Point2d(self.x * o.x, self.y * o.y)
        elif isinstance(o, int):
            return Point2d(self.x * o, self.y * o)

        return self

    def __eq__(self, o):
        if isinstance(o, Point2d):
            return self.x == o.x and self.y == o.y
        elif isinstance(o, int):
            return self.x == o and self.y == o

        return self

    def __ne__(self, o):
        if isinstance(o, Point2d):
            return self.x != o.x or self.y != o.y
        elif isinstance(o, int):
            return self.x != o or self.y != o

        return self

    def __str__(self):
        return str(self.x) + ", " + str(self.y)
