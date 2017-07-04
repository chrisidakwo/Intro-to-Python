# coding=utf-8

class Shape:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_xy(self):
        return self.__x, self.__y

    def set_xy(self, x, y):
        self.x, self.y = x, y

    def calc_area(self):
        raise NotImplementedError("")


class Circle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y)

    def calc_area(self):
        return self.x ** self.y


class Square(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y)

    def calc_area(self):
        return self.x / self.y


class Triangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y)

    # def calc_area(self):
    #     return self.x * self.y * 2


we = Triangle(34, 45)
print(we.calc_area())

we = Square(34, 45)
print(we.calc_area())

we = Circle(34, 45)
print(we.calc_area())
