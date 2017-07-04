"""This module contains a Reservation class for storing details of a rental"""


class Reservation:
    """This class provides the methods for maintaining reservation information"""
    def __init__(self, name=str(), address=str(), credit_card=str(), vin=str()):
        """Initialises a ``Reservation`` object with ``name``, ``address``,
        ``credit_card``, and ``vin``"""
        self.__name = name
        self.__address = address
        self.__credit_card = credit_card
        self.__vin = vin

    def get_name(self) -> str:
        """Returns first and last name for reservation"""
        return self.__name

    def get_address(self) -> str:
        """Returns address for reservation"""
        return self.__address

    def get_credit_card(self) -> str:
        """Returns credit card on reservation"""
        return self.__credit_card

    def get_vin(self) -> str:
        """Returns vehicle identification number on reservation"""
        return self.__vin

    def __str__(self):
        return self.__name + ": " + self.__vin + "(VIN)"


# r1 = Reservation("Chris Idakwo", "Area 12/481, Lilongwe", "39099019930", "SBND9029LC23")
# print(r1)
