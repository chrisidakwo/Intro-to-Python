"""Display the number of days for a given month in a given year.

RULE: Should be displayed as such:
'March 2005 has 31 days'

"""
import datetime


def isleapyear(year):
    """ Returns True if the argument year is a leap year, else returns False"""
    leap_status = ((year % 100 != 0) if (year % 4 == 0) else (year % 400 == 0))
    return leap_status

# Set global variables
DAYS_IN_A_MONTH = 31
MONTH_NAMES = "January", "February", "March", "April", "May", "June", "July", "August", "September", \
              "October", "November" "December"
# Get user input
MONTH = int(input("Enter a month: "))
YEAR = int(input("Enter a year: "))


# Set for months with 30 days
LIMITED_MONTHS = 9, 4, 6, 11  # A Tuple
if MONTH in LIMITED_MONTHS:
    DAYS_IN_A_MONTH = 30

# Set for February
# Take into account Leap years
if MONTH == 2 and not isleapyear(YEAR):
    DAYS_IN_A_MONTH = 28
elif MONTH == 2 and isleapyear(YEAR):
    DAYS_IN_A_MONTH = 29



print("{0} {1} has {3} days".format(MONTH_NAMES[MONTH - 1], YEAR, DAYS_IN_A_MONTH))






