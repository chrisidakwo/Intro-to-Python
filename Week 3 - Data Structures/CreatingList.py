""" Different ways of creating a list object 


Python has a special-purpose data type called an array
which is more like a C array and is little used



"""
from pprint import pprint

# ---------- USING THE LIST SYMBOL []
LIST1 = []  # An empty list
LIST2 = [2, 3, 4]  # Create a list with elements 2, 3, 4
LIST3 = ["red", "green", "blue"]  # Create a list of strings


# ---------- USING THE LIST CONSTRUCTOR list() and split()
LIST1 = list() # Same as []
LIST2 = list([2, 3, 4]) # Same as [2, 3, 4]
LIST3 = list(["red", "green", "blue"]) # Same as ["red", "green", "blue"]
LIST4 = list(range(2, 7)) # Create a list of elements 2, 3, 4, 5, 6
LIST5 = list("abcd")  # Creates a list with characters a, b, c, d
pprint(LIST4)
print(LIST5)
print("\n")


birthdayDate = "04/10/2012"
birthdayDateList = birthdayDate.split("/")
print(birthdayDateList)
# >>>
# Output: ['04', '10', '1997']

# You can now access the day using the [index] operator
day = birthdayDateList[0]
month = birthdayDateList[1]
year = birthdayDateList[2]
