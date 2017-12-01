class Point:
    def __init__(self, x: int, y: int):
        self.__x = self.__y = 0
        self.x = x
        self.y = y

    @staticmethod
    def validate_coord(v):
        if type(v) != int:
            raise TypeError('integer expected')
        if v < 0:
            raise ValueError('positive value expected')
        return v

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = self.validate_coord(x)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = self.validate_coord(y)

    def __repr__(self):
        return 'P({}, {})'.format(self.__x, self.__y)

    def __eq__(self, p):
        assert type(p) is Point
        return self.x == p.x and self.y == p.y

    def __gt__(self, p):
        assert type(p) is Point
        return self.x > p.x or self.y > p.y

    def __ge__(self, p):
        assert type(p) is Point
        return self.x >= p.x or self.y >= p.y

    def __lt__(self, p):
        assert type(p) is Point
        return self.x < p.x and self.y < p.y

    def __le__(self, p):
        assert type(p) is Point
        return self.x <= p.x and self.y <= p.y

