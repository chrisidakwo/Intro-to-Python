"""
    not, and, or
"""

# User input
NUMBER = int(input("Enter an integer: "))

# and operator
if NUMBER % 2 == 0 and NUMBER % 3 == 0:
    print(NUMBER, "is divisible by 2 and 3")

# or operator
if NUMBER % 2 == 0 or NUMBER % 3 == 0:
    print(NUMBER, "is divisible by 2 or 3")

# not operator
if (NUMBER % 2 == 0 or NUMBER % 3 == 0) and \
    not (NUMBER % 2 == 0 and NUMBER % 3 == 0):
    print(NUMBER, "is divisible by 2 or 3, and not both")



True and True

