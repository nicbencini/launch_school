class Circle:
    def __init__(self, r):
        self.radius = r

    def __lt__(self, other)
        if not isinstance(other, Circle):
            return NotImplemented

        return self.radius < other.radius

    def __gt__(selfm other)
        if not isinstance(other, Circle):
            return NotImplemented

        return self.radius > other.radius

    def __le__(self, other)
        if not isinstance(other, Circle):
            return NotImplemented

        return self.radius <= other.radius

    def __ge__(self, other)
        if not isinstance(other, Circle):
            return NotImplemented

        return self.radius >= other.radius

    def __eq__(self, other)
        if not isinstance(other, Circle):
            return NotImplemented

        return self.radius == other.radius

    def __ne__(self, other)
        if not isinstance(other, Circle):
            return NotImplemented

        return self.radius != other.radius

circle1 = Circle(5)
circle2 = Circle(3)
circle3 = Circle(5)