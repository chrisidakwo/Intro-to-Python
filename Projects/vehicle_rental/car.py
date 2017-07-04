# coding=utf-8
"""This module provides a ``Car`` class, a subtype of the ``Vehicle`` class"""
from vehicle import Vehicle


class Car(Vehicle):
    """This class is a subtype of the ``Vehicle`` class.
    
    Contains additional attributes specific to a car, such as:
        - make and model
        - number of passengers
        - number of doors
    
    Supports polymorphism behaviour of method ``getDescription(self)``
    """
    def __init__(self, make_model, kmltrs, num_passengers, num_doors, vin):
        """Initialized with parameter values"""
        super().__init__(kmltrs=kmltrs, vin=vin)
        self.__make_model = make_model
        self.__num_passengers = num_passengers
        self.__num_doors = num_doors

    def get_description(self):
        """Returns complete description of a ``Car`` as a formatted string"""
        spacing = "   "
        description = format(self.__make_model, "<18") + spacing + \
            "passengers: " + self.__num_passengers + spacing + \
            "doors: " + format(self.__num_doors, "<2") + spacing + \
            Vehicle.get_description(self)

        return description
