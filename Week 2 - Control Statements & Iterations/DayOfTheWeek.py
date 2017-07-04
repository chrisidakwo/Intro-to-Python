"""Predict the name of the day of the week based on a given year, month and day number


    Using Zeller's congruence algorithm
    -----------------
    
    h = (q + ( (26 * (m + 1)) / 10) + k + (k / 4) + (j / 4) + (5 * j)) % 7
    
    Rules:
    * h is the day of the week.
    * q is the day of the month.
    * m is the month.
    * j is the century ---> (year // 100).
    * k is the year of the century --> year % 100.
    
"""

# Set global variables
H = ""  # Day of the week
DAY_NAME = "" # Name of the day of the week
DAYS = "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
# MONTHS = "January", "February", "March", "April", "May", "June", "July", "August",\
#          "September", "October", "November", "December"

YEAR = int(input("Enter year: "))
M = int(input("Enter month (1 - 12): "))
Q = int(input("Enter the day of the month (1 - 31): "))


# Calculate the century
J = YEAR // 100  # Integer division, we don't need a float value

# Calculate the year of the century
K = YEAR % 100  # Get the remainder of the division

# h = (q + ( (26 * (m + 1)) / 10) + k + (k / 4) + (j / 4) + (5 * j)) % 7
# Determine day of the week
H = (Q + ((26 * (M + 1)) // 10) + K + (K // 4) + (J // 4) + (5 * J)) % 7


if H == 0:
    DAY_NAME = DAYS[0]
elif H == 1:
    DAY_NAME = DAYS[1]
elif H == 2:
    DAY_NAME = DAYS[2]
elif H == 3:
    DAY_NAME = DAYS[3]
elif H == 4:
    DAY_NAME = DAYS[4]
elif H == 5:
    DAY_NAME = DAYS[5]
elif H == 6:
    DAY_NAME = DAYS[6]
else:
    DAY_NAME = "H is out of range"

print("Day of the week is: {0}".format(DAY_NAME))

# We can enhance example using a for loop


# for day in range(len(DAYS)):
#     if day == int(H):
#         print("Day of the week is: {0}".format(DAYS[day]))
#
# print("\n")
