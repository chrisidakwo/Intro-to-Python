# coding=utf-8
"""This module provides a Vehicle class"""


class Vehicle(object):
    """A vehicle for rent by Crineon Vehicle Rental Agency
    The Vehicle class holds the:
        - km/ltrs, 
        - VIN (Vehicle Identification Number), and
        - reserved flag of the vehicle.
    
    Attributes:
        kmltrs: The integral number of kilometers driven on the vehicle.
        vin: A string representing the identification number of the vehicle. 
    
    Contains attributes common to all vehicles: km/ltrs,
    VIN and reserved (Boolean). Provides polymorphic behaviour
    for method ``getDescription(self)``.
    """

    def __init__(self, kmltrs=str(), vin=str()):
        """Initialises a Vehicle object with ``kmltrs`` and ``vin`` information."""
        self.__kmltrs = kmltrs
        self.__vin = vin
        self.__reserved = False

    def get_type(self):
        """Returns the type of vehicle (car, truck, van)"""
        return type(self).__name__

    def get_vin(self) -> str():
        """Retrieve Vehicle Identification Number of vehicle.
        
        :rtype: str
        """
        return self.__vin

    def get_description(self):
        """Returns the generic description common to all vehicle types"""
        description = "Km/ltrs:" + format(self.__kmltrs, ">6") + "   " +\
                      "VIN: " + format(self.__vin, ">12")
        return description

    def set_reserved(self, reserved):
        """Sets the reserve flag to a Boolean of True or False"""
        self.__reserved = reserved

    def is_reserved(self):
        """Returns True if vehicle is reserved; False otherwise."""
        return self.__reserved
