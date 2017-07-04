# coding=utf-8
"""This program performs the tasks of a vehicle rental agency, including the 
display of vehicle information and the ability to make/cancel reservations
"""
from system_interface import SystemInterface
from rental_agency_ui import RentalAgencyUI

try:
    # Create system with populated data from file
    sys = SystemInterface()

    # Associate user interface with system
    ui = RentalAgencyUI(sys)

    # Start the user interface
    ui.start()
except IOError:
    print("** PROGRAM TERMINATION (IO Error) **")
