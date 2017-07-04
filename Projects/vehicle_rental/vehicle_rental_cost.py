"""This module provides a VehicleRentalCosts class"""
from rental_cost import RentalCost

# Symbol Constants
DAILY_RENTAL = 1
WEEKLY_RENTAL = 2
WEEKEND_RENTAL = 3


class VehicleRentalCosts:
    """This class provides the methods for maintaining 
    rental costs of vehicles"""
    def __init__(self):
        """Initialises vehicle rental costs empty"""
        self.__vehicle_rental_costs = dict()

    def get_rental_cost(self, v_type):
        """Returns a ``RentalCost`` object for the specified
        ``v_type``."""
        return self.__vehicle_rental_costs[v_type]

    def add_rental_cost(self, v_type, r_cost):
        """Adds a ``VehicleRentalCost`` object to dictionary
        with the key as ``v_type``
        
        @:param vtype ==> vehicle type.\n
        @:param r_cost ==> vehicle rental costs.
        """
        self.__vehicle_rental_costs[v_type] = r_cost

    def calc_rental_cost(self, v_type, rental_period, want_insurance,
                         km_driving):
        """Returns estimate of rental cost for provided parameter values.
        
        Returns dictionary with key/values:
        {"base_charges", "insur_rate", "num_free_km", "per_km_charge",
        "estimated_mileage_charge}
        """

        # Get vehicle cost
        vehicle_cost = self.get_rental_cost(v_type)

        # Compute rental charges
        rental_time = rental_period[1]

        rental_rate = int()
        rental_days = int()

        if rental_period[0] == DAILY_RENTAL:
            rental_rate = vehicle_cost.get_daily_rate()
            rental_period_value = DAILY_RENTAL
            rental_period_str = 'daily rental'
            rental_days = rental_time
        elif rental_period[0] == WEEKLY_RENTAL:
            rental_rate = vehicle_cost.get_weekly_rate()
            rental_period_value = WEEKLY_RENTAL
            rental_period_str = 'weekly rental'
            rental_days = rental_time * 7
        elif rental_period[0] == WEEKEND_RENTAL:
            rental_rate = vehicle_cost.get_weekend_rate()
            rental_period_value = WEEKEND_RENTAL
            rental_period_str = 'weekend rental'
            rental_days = 2

        # Get free kms, per km charge and insurance rate
        num_free_km = vehicle_cost.get_free_km()
        per_km_charge = vehicle_cost.get_per_km_charge()
        insurance_rate = vehicle_cost.get_insurance_rate()

        # Compute rental charge for selected rental period
        if not want_insurance:
            insurance_rate = 0

        # Compute base rental charges
        base_rental_charges = (rental_days * rental_rate) + \
                              (rental_days * insurance_rate)

        km_charged = km_driving - num_free_km
        if km_charged < 0:
            km_charged = 0

        estimated_mileage_charges = km_charged * per_km_charge

        return {
            "base_charges": base_rental_charges,
            "insur_rate": insurance_rate,
            "num_free_km": num_free_km,
            "per_km_charge": per_km_charge,
            "estimated_mileage_charges": estimated_mileage_charges
        }

# vc1 = RentalCost('24.99', '180.00', '45.00', '100', '.15', '14.99')
# vc2 = RentalCost('35.81', '220.00', '55.00', '0', '.20', '14.99')
# vc3 = RentalCost('55.00', '425.00', '110.00', '25', '.25', '24.99')
#
# vc = VehicleRentalCosts()
# vc.add_rental_cost('Car', vc1)
# print(vc.get_rental_cost('Car').get_costs())
# print(vc.calc_rental_cost('Car', (1, 3), True, 1450))
