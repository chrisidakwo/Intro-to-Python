# coding=utf-8
"""Working with properties"""


class Dog(object):
    """Defines a Dog"""
    def __init__(self, name, age, tail=True):
        self.__name = name
        self.age = age
        self.tail = tail

    @property
    def __namen(self):
        """Name of a dog"""
        return self.__name

    @property
    def namen(self):
        return self.__namen




f = Dog("Ricky", 5)
print(f.namen)
# f.name = "Honey"
print(type(f.namen))


