"""VehicleFactory class module.

Raises InvalidFileFormatError and InvalidVinError
"""
from vehicle import Vehicle
from car import Car
from van import Van
from truck import Truck


class InvalidVinError(Exception):
    """Exception indicating that vin was not found"""
    pass


class VehicleFactory:
    """This class maintains a collection of Vehicle objects"""
    def __init__(self):
        """Initialises an empty list of vehicles"""
        self.__vehicles = []
        """A list of vehicles"""

    def get_vehicles(self, vin) -> Vehicle:
        """Returns Vehicles for provided vin. Raises InvalidVinError"""
        for vehicle in self.__vehicles:
            if vehicle.get_vin() == vin:
                return vehicle

        raise InvalidVinError

    def add_vehicle(self, vehicle):
        """Adds a new ``vehicle`` to list of vehicles"""
        self.__vehicles.append(vehicle)

    def num_avail_vehicles(self, vehicle_type):
        """Returns the number of available vehicles of ``vehicle_type``"""
        return len(self.get_avail_vehicles(vehicle_type))

    def get_avail_vehicles(self, vehicle_type):
        """Returns a list of unreserved Vehicles of ``vehicle_type``"""
        return [v for v in self.__vehicles
                if v.get_type() == vehicle_type
                and not v.is_reserved()]

    def reserve_vehicle(self, vin):
        """Reserve a ``Vehicle`` of ``vin``"""
        [v.set_reserved(True)
         for v in self.__vehicles
         if v.get_vin() == vin]

    def unreserve_vehicle(self, vin):
        """Removes a vehicle of ``vin`` from reservation.
        
        Sets ``self.__is_reserved`` to false
        """
        k = 0
        found = False
        while not found:
            if self.__vehicles[k].get_vin() == vin:
                self.__vehicles[k].set_reserved(False)
                found = True


# v1 = Car("Ford Fusion", "14.46", "5", "4", "FG1000")
# v2 = Van("Dodge Caravan", "26.30", "7", "TF1000")
# v3 = Truck("7.22", "10", "1", "HG1000")
# v = VehicleFactory()
# v.add_vehicle(v1)
# v.add_vehicle(v2)
# v.add_vehicle(v3)
#
# print(v.get_avail_vehicles('Car')[0].get_description())
# print(v.get_avail_vehicles('Van')[0].get_description())
# print(v.get_avail_vehicles('Truck')[0].get_description())
