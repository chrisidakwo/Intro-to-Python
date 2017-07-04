"""Dummy class for explaining the concept of classes and objects"""


class Person:
    def __init__(self, name):
        self.name = name
        """The name of a given Person"""


someone = Person("Chris Idakwo")
print("His name is:", someone.name)
print()


class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name







print("\n-------------------------------------- Working with the Car Class --------------------------------------")


# Inheritance
class Car:  # <== Parent class
    """Model cars"""

    @classmethod
    def horn(self) -> None:
        """
        Horn
        
        :rtype: None
        """
        print("Horn!!!")

    def exclaim(self):
        print("I'm a car!")


class Toyota(Car):  # <== Child class
    def speed_limit(self) -> None:
        print("280km/h")

    def exclaim(self):
        print("I'm a Toyota! Which is a child of Car, but more Toyota-ish")

new_car = Car()
new_car.horn()
new_car.exclaim()
print()

new_toyota = Toyota()
new_toyota.horn()
new_toyota.exclaim()
new_toyota.speed_limit()


