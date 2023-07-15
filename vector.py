class Vector:

    MAX_COORD = 100
    MIN_COORD = 0

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        print(self.norm(self.x, self.y))

    def get_coords(self):
        return self.x, self.y

    @staticmethod
    def norm(x, y):
        return x*x + y*y

v = Vector(10, 20)
print(Vector.norm(5, 6))
