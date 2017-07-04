# coding=utf-8
class Car(object):
    wheels = 4

    def __init__(self, make, model):
        """"""
        self.__mpg = 0.0
        self.make = make
        self.model = model

    @staticmethod
    def move():
        return "Move + 1"

    def stop(self):
        return "Stop + 1"

    @classmethod
    def make_sound(cls):
        return cls.wheels


print(Car.move())
# 'move()' is a static method that can be accessed directly from the class
# without instantiating an object

mustang = Car("Ford", "Mustang")
print(mustang.stop())
print(mustang.make_sound())




