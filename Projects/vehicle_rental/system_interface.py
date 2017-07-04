"""This module provides a SystemInterface class for the Vehicle Rental Program.


    Vehicles File Format
    --------------------
    The format for the vehicles file contains comma-separated values with the
    indicated header lines for cars, vans, and trucks.
    
        #CARS#\n
        make_model, kmltrs, num_passengers, num_doors, vin
        ....\n
        
        #VANS#\n
        make-model, kmltrs, num passengers, vin
        ....\n
        
        #TRUCKS#
        kmltrs, length, num rooms, vin
        ....\n
    
    Vehicle Cost File Format
    ------------------------
    The format for the rental costs file includes a header line, followed by
    three lines of comma-separated values for cars, vans, and trucks.
    
        daily, weekly, weekend, free miles, mileage charge, insurance
        
    The following exceptions are raised: IOError, InvalidFileFormatError.
"""
from vehicle_factory import VehicleFactory, Car, Van, Truck
from vehicle_rental_cost import RentalCost, VehicleRentalCosts
from reservation_factory import ReservationFactory, Reservation

# Constants
VEHICLE_TYPES = ('Car', 'Van', 'Truck')
VEHICLES_FILENAME = 'VehiclesStock.txt'
VEHICLES_COSTS_FILENAME = 'RentalCost.txt'


# Exception Class
class InvalidFileFormatError(Exception):
    """Exception indicating invalid file in file_name"""
    def __init__(self, header, file_name):
        self.__header = header
        self.__file_name = file_name

    def __str__(self):
        """Returns a string representation of the Error; an error message"""
        return 'File Format Error: File header ' + self.__header +\
               'expected in file ' + self.__file_name


class SystemInterface:
    """This class provides the interface for the vehicle rental program"""
    def __init__(self):
        """Populates vehicles and rental costs from file. Raise IOError."""
        self.__vehicles = VehicleFactory()
        self.__vehicle_costs = VehicleRentalCosts()
        self.__reservations = ReservationFactory()
        self.__vehicle_info_file = None

        try:
            self.__vehicle_info_file = open(VEHICLES_FILENAME)  # ==> "r" is not specified bcos that's the default value
            self.__rental_cost_file = open(VEHICLES_COSTS_FILENAME)

            # self.__populate_vehicles(self.__vehicle_info_file)
            self.__populate_costs(self.__rental_cost_file)
        except InvalidFileFormatError as e:
            print(e)
            raise IOError
        except IOError:
            if self.__vehicle_info_file is None:
                print("File not Found: ", VEHICLES_COSTS_FILENAME)
            else:
                print("File not Found: ", VEHICLES_COSTS_FILENAME)
            raise IOError

    def num_avail_vehicles(self, vehicle_type):
        """Returns the number of available vehicles. Returns 0 if no
        vehicle is available.
        """
        return self.__vehicles.num_avail_vehicles(vehicle_type)

    def get_vehicle(self, vin):
        """Returns ``Vehicle`` type for given ``vin``."""
        return self.__vehicles.get_vehicles(vin)

    @staticmethod
    def get_vehicle_types():
        """Returns all vehicle types as a tuple of strings"""
        return VEHICLE_TYPES

    def get_vehicle_costs(self, vehicle_type):
        """Returns vehicle costs for provided vehicle type as a list.
        
        List of form [daily_rate, weekly_rate, weekend_rate,
                      num_free_km, per_km_charge, insur_rate]
        """
        return self.__vehicle_costs.get_rental_cost(vehicle_type).get_costs()

    def get_avail_vehicles(self, vehicle_type):
        """Returns a list of descriptions of unreserved vehicles."""
        avail_vehicles = self.__vehicles.get_avail_vehicles(vehicle_type)
        return [vehicle for vehicle in avail_vehicles]

    def is_reserved(self, vin):
        """Returns the reservations status of a ``Vehicle`` of ``vin``."""
        return self.__reservations.is_reserved(vin)

    def check_reservation(self, credit_card):
        """Returns True if a reservation exists; False otherwise."""
        return self.__reservations.check_reservation(credit_card)

    def find_reservation(self, credit_card):
        """Returns a ``Reservation`` if one exists; ``None`` otherwise."""
        return self.__reservations.find_reservation(credit_card)

    def add_reservation(self, reservation=Reservation()):
        """Creates a new reservation and marks vehicle as reserved."""
        self.__reservations.add_reservation(reservation)
        self.__vehicles.get_vehicles(reservation.get_vin())

    def cancel_reservation(self, credit_card):
        """Cancels a ``Reservation`` made with provided ``credit_card``"""
        vin = self.__reservations.get_vin_for_reservation(credit_card)
        self.__vehicles.unreserve_vehicle(vin)
        self.__reservations.cancel_reservation(credit_card)

    def calc_rental_cost(self, vehicle_type, rental_period,
                         want_insurance, km_driving):
        """Returns an estimate of rental cost in form of a dictionary"""
        return self.__vehicle_costs.calc_rental_cost(vehicle_type,
                                                     rental_period,
                                                     want_insurance,
                                                     km_driving)

    # Private Methods
    def __populate_vehicles(self, vehicle_file):
        """Gets vehicles from ``vehicle_file``.
        
        Raises InvalidFileFormatError.
        """
        empty_str = "\n"

        # Initialise vehicle file headers
        vehicle_file_headers = ('#CARS#', '#VANS#', '#TRUCKS#')
        vehicle_type_index = 0

        # Read first line of file ==> #CARS# expected
        vehicle_str = vehicle_file.readline()
        # vehicle_info = vehicle_str.rstrip().split(",")
        # file_header_found = vehicle_info[0]
        vehicle_info = vehicle_str.rstrip()
        file_header_found = vehicle_info
        expected_header = vehicle_file_headers[0]

        if file_header_found != expected_header:
            raise InvalidFileFormatError(expected_header, VEHICLES_FILENAME)
        else:
            # Read next line of file
            vehicle_str = vehicle_file.readline()

            while vehicle_str != empty_str:
                # Convert comma-separated string into list of strings
                vehicle_info = vehicle_str.rstrip().split(",")

                if vehicle_info[0][0] == "#":
                    print(vehicle_info[0][0])
                    vehicle_type_index += 1
                    file_header_found = vehicle_info[0]
                    expected_header = vehicle_file_headers[vehicle_type_index]

                    if file_header_found != expected_header:
                        raise InvalidFileFormatError(expected_header, VEHICLES_FILENAME)
                else:
                    # Create new vehicle object of the proper type
                    if file_header_found == "#CARS":
                        vehicle = Car(*vehicle_info)
                    elif file_header_found == "#VANS#":
                        vehicle = Van(*vehicle_info)
                    elif file_header_found == "#TRUCKS#":
                        vehicle = Truck(*vehicle_info)

                    # Add new vehicle to vehicles lists
                        self.__vehicles.add_vehicle(vehicle)

                # Read next line of vehicle information
                vehicle_str = vehicle_file.readline()

    def __populate_costs(self, cost_file):
        """Populates RentalCost objects from provided file object"""

        # Skip file header & read first line of file
        cost_file.readline()
        cost_str = cost_file.readline()

        for v_type in VEHICLE_TYPES:
            # Strip off newline character and split into list
            cost_info = cost_str.rstrip().split(",")

            [cost_item.strip() for cost_item in cost_info]

            # Add vehicle type, rental cost as key/value to dictionary
            self.__vehicle_costs.add_rental_cost(v_type, RentalCost(*cost_info))

            # read next line of vehicle costs
            cost_str = cost_file.readline()

# ss = SystemInterface()
# print(ss.get_vehicle_costs('Van'))
