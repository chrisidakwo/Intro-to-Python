""" Determining a Leap Year """

YEAR = int(input("Enter a year: "))

# Check if YEAR is a leap year
# ISLEAPYEAR = (YEAR % 4 == 0  and YEAR % 100 != 0) or (YEAR % 400 == 0) # You can also use this line instead of the one directly below
ISLEAPYEAR = ((YEAR % 100 != 0)  if (YEAR % 4 == 0) else (YEAR % 400 == 0))

if ISLEAPYEAR:
    print(YEAR, "is a leap year")
else:
    print(YEAR, "is not a leap year")
