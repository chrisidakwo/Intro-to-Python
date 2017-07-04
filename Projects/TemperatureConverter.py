"""Building programs with functions
Temperature Conversion Program
Converting from Celsius to Fahrenheit and
from Fahrenheit to Celsius"""

# FIXME: Add docstrings to the functions describing what & how they operate


def display_welcome():
    print("This program will convert a range of temperatures")
    print("Enter (F) to convert Fahrenheit to Celsius")
    print("Enter (C) to convert Celsius to Fahrenheit\n")


def get_convert_to():
    which = str(input("Enter selection: "))
    while which != "F" and which != "C":
        which = str(input("Enter selection: "))

    return which


def display_fahrenheit_to_celsius(start, end):
    print("\n  Degrees", " Degrees")
    print("Fahrenheit", "Celsius")

    for temp in range(start, (end + 1)):
        converted_temp = ((temp - 32) * (5 / 9))
        print("  ", format(temp, "4.1f"), "  ", format(converted_temp, "4.1f"))


def display_celsius_to_fahrenheit(start, end):
    print("\n  Degrees", " Degrees")
    print("  Celsius", "Fahrenheit")

    for temp in range(start, (end + 1)):
        converted_temp = (9/5 * temp) + 32
        print(" ", format(temp, "4.1f"), "  ", format(converted_temp, "4.1f"))


# ---------- main
# Display program welcome
display_welcome()

# Get which conversion from user
which = get_convert_to()

# Get range of temperatures to convert
temp_start = int(input("Enter starting temperature to convert: "))
temp_end = int(input("Enter ending temperature to convert: "))

# Display range of converted temperatures
if which == "F":
    display_fahrenheit_to_celsius(temp_start, temp_end)
else:
    display_celsius_to_fahrenheit(temp_start, temp_end)
