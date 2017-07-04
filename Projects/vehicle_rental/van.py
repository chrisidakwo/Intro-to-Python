# coding=utf-8
"""This module provides a ``Van`` class, a subtype of the ``Vehicle`` class."""
from vehicle import Vehicle


class Van(Vehicle):
    """This class is a subtype of the ``Vehicle`` class.
    
    Contains additional attributes of make and mode, and num of passengers.
    Supports polymorphic behaviour of method ``getDescription(self)``
    """
    def __init__(self, make_model, kmltrs, num_passengers, vin):
        """Initialise with ``make-model``, ``kmltrs``,
        ``num_passengers``, ``vin``.
        """
        super().__init__(kmltrs=kmltrs, vin=vin)
        self.__make_model = make_model
        self.__num_passengers = num_passengers

    def get_description(self):
        """Returns complete description of a ``Van`` as a formatted string."""
        spacing = "   "
        description = format(self.__make_model, "<22") + spacing +\
            "passengers:" + format(self.__num_passengers, ">2") +\
            spacing + Vehicle.get_description(self)

        return description
