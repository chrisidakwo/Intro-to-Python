""" Understanding what is True """

NAME = ""
if NAME:
    print(NAME)
else:
    print("NAME is an empty string")


NUMBER = 1
if NUMBER:
    print(NUMBER)
else:
    print("NUMBER is zero")


NAMES = []
if NAMES:
    print(NAMES)
else:
    print("NAMES is an empty list")

DECIMAL = 0.0
if DECIMAL:
    print(DECIMAL)
else:
    print("DECIMAL is", DECIMAL)

""" Python programs use this definition of "truthiness",
# which in this case is falsiness to check for empty data structures
# as well as false conditions """
print("\n\n")


# ---------- TYPE CONVERSION USING int(True) int(False)
print(int(True))
print(int(False))


# ---------- TYPE CONVERSION USING bool(int) bool(float)
print(bool(0))
print(bool(20))
print(bool(0.00))
print(bool(0.000000001)) # So long as it's no longer 0.00, it returns True
print(bool(10.25))
# Any number other than zero (0) returns a Boolean state of True


# ---------- BOOLEAN EXPRESSION
LILONGWE = True
if LILONGWE:
    print("Lilongwe is the capital city of Malawi\n")
else:
    print("Blantyre is the capital city of Malawi\n")


LENGTH = 5  # Set width/length of rectangle
if LENGTH > 5:  # greater than
    print("That's a longer rectangle!")
else:
    print("That's probably the rectangle!")


if LENGTH >= 5:  # 'greater than' OR 'equal to'
    print("That's the rectangle!")
else:
    print("That's a shorter rectangle!")


if LENGTH < 5:  # less than
    print("That's a shorter rectangle!")
else:
    print("That's probably the rectangle!")


if LENGTH <= 5:  # 'less than' OR 'equal to'
    print("That's the rectangle!")
else:
    print("That's a longer rectangle!")


if LENGTH == 5:  # equal to
    print("That's the rectangle!")
else:
    print("That's not the rectangle!")


LENGTHS = [1, 3, 5, 6, 7, 8]
if LENGTH in LENGTHS:
    print("202: Found rectangle!")
else:
    print("404: Rectangle Not Found")


# ---------- BOOLEAN OPERATORS 'not', 'and', 'or'
AGE = 21
GENDER = "Male"