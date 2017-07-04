"""This module provides a ``VehicleCost`` class"""


class RentalCost:
    """This class provides the methods for maintaining rental costs."""
    def __init__(self, daily_rate, weekly_rate, weekend_rate, free_km,
                 per_km_chrg, insur_rate):
        """"""
        self.__daily_rate = daily_rate
        self.__weekly_rate = weekly_rate
        self.__weekend_rate = weekend_rate
        self.__free_km = free_km
        self.__per_km_chrg = per_km_chrg
        self.__insur_rate = insur_rate

    def get_daily_rate(self):
        """Returns daily rental rate of vehicle."""
        return float(self.__daily_rate)

    def get_weekly_rate(self):
        """Returns weekly rental rate of vehicle."""
        return float(self.__weekly_rate)

    def get_weekend_rate(self):
        """Returns weekend rental rate of vehicle."""
        return float(self.__weekend_rate)

    def get_free_km(self):
        """Returns number of free miles for vehicle rental."""
        return int(self.__free_km)

    def get_per_km_charge(self):
        """Returns per km charge for vehicle rental."""
        return float(self.__per_km_chrg)

    def get_insurance_rate(self):
        """Returns daily insurance rate for vehicle"""
        return float(self.__insur_rate)

    def get_costs(self):
        """Returns a list containing all costs for vehicle"""
        return [self.__daily_rate, self.__weekly_rate,
                self.__weekend_rate, self.__free_km,
                self.__per_km_chrg, self.__insur_rate]


# vc = RentalCost('24.99', '180.00', '45.00', '100', '.15', '14.99')
# print(vc.get_daily_rate())
# print(vc.get_weekly_rate())
# print(vc.get_weekend_rate())
# print(vc.get_free_km())
# print(vc.get_per_km_charge())
# print(vc.get_insurance_rate())
# print(vc.get_costs())
