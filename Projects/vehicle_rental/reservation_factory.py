"""This module performs operations on ``Reservation`` class"""
from reservation import Reservation


class ReservationFactory:
    """This class provides the methods for maintaining rental reservations"""
    def __init__(self):
        """Initialises empty collection of reservations"""
        self.__reservations = dict()

    def is_reserved(self, vin=str()):
        """Returns True if reservation for vin; False otherwise"""
        return vin in self.__reservations

    def get_vin_for_reservation(self, credit_card=str()) -> str:
        """Returns vin of vehicles reserved with ``credit_card``"""
        return self.__reservations[credit_card].get_vin()

    def add_reservation(self, reservation=Reservation()):
        """Add a new reservation"""
        self.__reservations[reservation.get_credit_card()] = reservation

    def check_reservation(self, credit_card=str()):
        """Return True if ``credit_card`` in ``self.reservations``;
         False otherwise"""
        return credit_card in self.__reservations

    def find_reservation(self, credit_card=str()):
        """Returns a reservation if ``credit_card`` in
         ``self.__reservations``"""
        if credit_card in self.__reservations:
            return self.__reservations[credit_card]

        return None

    def cancel_reservation(self, credit_card=str()):
        """Deletes reservation matching the provided ``credit_card`` number"""
        del self.__reservations[credit_card]

