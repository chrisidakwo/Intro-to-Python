# coding=utf-8
"""This model provides a ``Truck`` class. A subtype of the ``Vehicle`` class."""

from vehicle import Vehicle


class Truck(Vehicle):
    """This class contains a subtype of the ``Vehicle`` class.
    
    Contains additional attributes length and num of rooms storage capacity.
    Supports polymorphic behaviour of method ``getDescription(self)``.
    """
    def __init__(self, kmltrs, length, num_rooms, vin):
        """Initialise with ``kmltrs``, ``length``, ``num_rooms``, ``vin``."""
        super().__init__(kmltrs=kmltrs, vin=vin)
        self.__length = length
        self.__num_rooms = num_rooms

    def get_description(self):
        """Returns a complete description of a ``Truck`` as a formatted string"""
        spacing = "   "
        description = "length(feet):" + format(self.__length, ">3") + spacing +\
                      "rooms:" + format(self.__num_rooms, ">2") + spacing +\
                      Vehicle.get_description(self)

        return description
