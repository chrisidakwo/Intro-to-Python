# coding=utf-8
"""This module provides class RentalAgencyUI, a console user interface.

Method ``start`` begins execution of the interface.
Raises IOError.
"""
from system_interface import VEHICLE_TYPES, SystemInterface
# from vehicle_factory import InvalidVinError
from vehicle_rental_cost import DAILY_RENTAL, WEEKLY_RENTAL, WEEKEND_RENTAL
from reservation_factory import Reservation


class RentalAgencyUI:
    """This class provides a console interface for the rental agency system."""
    def __init__(self, sys=SystemInterface()):
        """Stores the provided reference to the vehicle rental system"""
        self.__sys = sys

    def start(self):
        """Begins the command loop"""
        self.__display_welcome_screen()
        self.__display_menu()

        selection = self.__get_selection(7)

        while selection != 7:
            self.__execute_cmd(selection)
            self.__display_menu()
            selection = self.__get_selection(7)

        print("Thank you for using Crineon Vehicle Rental Agency")

    # Private Methods
    @staticmethod
    def __display_welcome_screen():
        """Displays welcome message and general instructions."""
        print("\n\n")
        print("**************************************************")
        print("    *Welcome to Crineon Vehicle Rental Agency*    ")
        print("**************************************************")

    @staticmethod
    def __display_menu():
        """Displays a list of menu options on the screen."""
        print("\n<<< MAIN MENU >>>")
        print("1 - Display vehicle types")
        print("2 - Check rental costs")
        print("3 - Check available vehicles")
        print("4 - Get cost of specific rental")
        print("5 - Make a reservation")
        print("6 - Cancel a reservation")
        print("7 - Quit\n")

    @staticmethod
    def __get_selection(num_selections, prompt="Enter: "):
        """Returns user-entered value in range of 1 to num_selections"""
        valid_input = False
        selection = int(input(prompt))

        while not valid_input:
            try:
                if selection < 1 or selection > num_selections:
                    print("* Invalid Entry *\n")
                    selection = int(input(prompt))
                else:
                    valid_input = True
            except ValueError:
                selection = int(input(prompt))

        return selection

    @staticmethod
    def __display_div_line(title=''):
        """Displays line of dashes with optional title"""
        if len(title) != 0:
            title = " " + title + " "
        print(title.center(70, "-"))

    def __execute_cmd(self, selection):
        """Executes command for provided menu selection"""
        if selection == 1:
            self.__cmd_display_vehicle_types()
        elif selection == 2:
            self.__cmd_display_vehicle_costs()
        elif selection == 3:
            self.__cmd_prompt_and_display_avail_vehicles()
        elif selection == 4:
            self.__cmd_display_specific_rental_cost()
        elif selection == 5:
            self.__cmd_make_reservation()
        elif selection == 6:
            self.__cmd_cancel_reservation()

    def __cmd_display_vehicle_types(self):
        """Displays vehicle types -> (Cars, Vans, Trucks)"""
        self.__display_div_line("Types of Vehicles Available for Rent")
        self.__display_vehicle_types()
        self.__display_div_line()

    def __cmd_display_vehicle_costs(self):
        """Displays rental costs for Cars, Vans, Trucks"""
        empty_string = ""
        blank_char = " "

        # Get vehicle type from user
        self.__display_vehicle_types()
        vehicle_type_num = self.__get_selection(len(VEHICLE_TYPES))
        vehicle_type = VEHICLE_TYPES[vehicle_type_num - 1]

        # Set column headings
        row1_colheadings = blank_char * 34 + format("Free", "8") + \
            format("Per Km", "12") + format("Insurance", "19")

        row2_colheadings = format("Daily", "9") + format("Weekly", "10") + \
            format("Weekend", "11") + format("Kilomtrs", "12") + \
            format("Charge", "12") + format("(per day)", "19")

        # Get vehicle costs
        costs = self.__sys.get_vehicle_costs(vehicle_type)

        # Build costs line to display
        costs_str = empty_string

        # field_widths = ("7", "8", "9", "7", "10", "17")
        field_widths = ("9", "12", "14", "10", "13", "18")
        for k in range(0, len(costs)):
            costs_str += format(costs[k], "<" + field_widths[k])

        # Display headings and costs line
        self.__display_div_line("Rental Charges for " + vehicle_type + "s")
        print()
        print(row1_colheadings + "\n" + row2_colheadings + "\n" + costs_str)
        self.__display_div_line()

    def __cmd_display_avail_vehicles(self, vehicle_type, numbered=False):
        """Displays unreserved vehicles of selected type.
        When a default argument is True, lists vehicles with sequential
        numbers at the start of the line of each vehicle description
        """
        avail_vehicles_list = self.__sys.get_avail_vehicles(vehicle_type)
        self.__display_div_line("Available " + vehicle_type + "s")

        # if avail_vehicles_list == []:
        if not avail_vehicles_list:  # ==> A more Pythonic way
            print("* No Vehicles Available of this Type *")
        elif numbered:
            for k, v in enumerate(avail_vehicles_list):
                k += 1
                print(str(k) + "-" + v.get_description())
        else:
            for v in avail_vehicles_list:
                print(v.get_description())

    def __cmd_prompt_and_display_avail_vehicles(self):
        """Prompts user for vehicle type, and displays all available
        vehicles of that type.
        """
        self.__display_vehicle_types()
        vehicle_type_num = self.__get_selection(len(VEHICLE_TYPES))
        vehicle_type = VEHICLE_TYPES[vehicle_type_num - 1]
        self.__cmd_display_avail_vehicles(vehicle_type)

    def __cmd_display_specific_rental_cost(self):
        """Prompts user for selections and displays rental cost"""
        # Get vehicle type and rental period from user
        self.__display_vehicle_types()
        vehicle_type_num = self.__get_selection(len(VEHICLE_TYPES))
        vehicle_type = VEHICLE_TYPES[vehicle_type_num - 1]

        # Assign tuple e.g. ("DAILY_RENTAL", "4)
        print()
        rental_period = self.__get_rental_period()

        # Prompt user for optional insurance
        want_insurance = input("\nWould you like to have insurance? (y/n): ")

        while want_insurance not in ("y", "Y", "n", "N"):
            want_insurance = input("\nWould you like to have insurance? (y/n): ")

        # Convert user response to Boolean value
        want_insurance = want_insurance in ("y", "Y")

        # Prompt user for num of kilometers expected to drive
        print("\nDistance you expect to drive? (in km)")
        num_kms = self.__get_selection(100, prompt="Kilomtrs: ")

        # Compute base rental cost
        rental_cost = self.__sys.calc_rental_cost(vehicle_type, rental_period,
                                                  want_insurance, num_kms)

        # Display estimated rental cost
        print()
        self.__display_div_line("ESTIMATED " + str(vehicle_type).upper() + " RENTAL COST")

        if want_insurance:
            print("Insurance rate of", rental_cost['insur_rate'], "per day")
        else:
            print("* You have opted out of insurance coverage *")

        if rental_period[0] == DAILY_RENTAL:
            print("\nDaily rental for", rental_period[1], "days would be $",
                  format(rental_cost['base_charges'], ".2f"))
        elif rental_period[0] == WEEKLY_RENTAL:
            print("\nWeekend rental is $", rental_cost['base_charges'])

        est_total_cost = rental_cost['base_charges'] + \
            rental_cost['estimated_mileage_charges']

        print("\nYour cost with an estimated mileage of", num_kms,
              "kilometers would be", format(est_total_cost, ".2f"))

        print("which includes", rental_cost['num_free_km'],
              "free kilometers and a charge of", format(rental_cost['per_km_charge'], ".2f"), "per km")

        self.__display_div_line()

    def __cmd_make_reservation(self):
        """Prompts user for vehicle vin and reserves vehicle"""
        # Get vehicle type
        self.__display_vehicle_types()
        vehicle_type_num = self.__get_selection(len(VEHICLE_TYPES))
        vehicle_type = VEHICLE_TYPES[vehicle_type_num - 1]

        if self.__sys.num_avail_vehicles(vehicle_type) == 0:
            print("Sorry - No available", VEHICLE_TYPES[vehicle_type_num - 1] + "s", "at the moment")
        else:
            self.__cmd_display_avail_vehicles(vehicle_type, numbered=True)
            avail_vehicles = self.__sys.get_avail_vehicles(vehicle_type)

            valid_input = False
            selected = ""

            while not valid_input:
                selected = input("\nEnter number of vehicles to reserve: ")

                if not selected.isdigit():
                    print("Please enter the number preceding the vehicle")
                elif int(selected) < 1 or \
                        int(selected) > self.__sys.num_avail_vehicles(vehicle_type):
                    print("\INVALID SELECTION - Please re-enter: ")
                else:
                    valid_input = True

            vin = avail_vehicles[int(selected) - 1].get_vin()
            vehicle = self.__sys.get_vehicle(vin)
            print(vehicle.get_description())

            vehicle.set_reserved(True)

            name = input("\nEnter first and last name: ")
            address = input("Enter address: ")
            credit_card = input("Enter credit card number")

            reservation = Reservation(name, address, credit_card)
            self.__sys.add_reservation(reservation)
            print("* Reservation successful! *")

    def __cmd_cancel_reservation(self):
        """Prompts user for credit card information and cancels reservation"""
        credit_card = input("Please enter your credit card number: ")

        if self.__sys.find_reservation(credit_card):
            print("Calling cancel_reservation of sys")
            confirmation = input("Are you sure you want to cancel reservation? (y/n): ")
            if confirmation in ('y', "Y"):
                self.__sys.cancel_reservation(credit_card)
                print("** RESERVATION CANCELLED **")
            else:
                print("** Reservation not cancelled **")
        else:
            print("* Reservation not Found! Invalid Credit Card Number Entered *")

    def __display_vehicle_types(self):
        """Displays the numbered selection of vehicle types"""
        print("\nEnter type of vehicle:")
        vehicle_types = self.__sys.get_vehicle_types()

        for k, v_type in enumerate(vehicle_types):
            k += 1
            print(k, "-", v_type)
        print()

    def __get_rental_period(self):
        """Prompts user for desired rental period
        
        Returns tuple of the form (x,n) where x is one of DAILY_RENTAL,
        WEEKLY_RENTAL or WEEKEND_RENTAL, and n is the number of those units,
        e.g. (DAILY_RENTAL, 3) three days of a daily rental.
        """

        print("Enter the rental period:")
        print("{0}-Daily {1}-Weekly {2}-Weekend".format(DAILY_RENTAL, WEEKLY_RENTAL, WEEKEND_RENTAL))

        valid_input = False

        while not valid_input:
            try:
                selection = int(input("Enter: "))
                while selection not in (DAILY_RENTAL, WEEKLY_RENTAL,
                                        WEEKEND_RENTAL):
                    print("* Incorrect entry. Please re-enter *\n")
                    selection = int(input("Enter: "))

                if selection == DAILY_RENTAL:
                    print("How many days do you need the vehicle?", end="")
                    num_days = self.__get_selection(14, prompt=" ")

                    if num_days > 6:
                        print("Why don't you consider a weekly rental?\n")

                    return DAILY_RENTAL, num_days
                elif selection == WEEKLY_RENTAL:
                    print("\nHow many weeks do you need the vehicle? (1-3): ")
                    num_weeks = self.__get_selection(3, prompt="Weeks: ")
                    return selection, num_weeks

                elif selection == WEEKEND_RENTAL:
                    return selection, 1

            except ValueError:
                print("* Invalid Input - Number Expected *\n")
