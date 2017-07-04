""" Working with and manipulating list objects """
import copy

#----------------- len() sum() max() min() OPERATORS
list1 = [2, 3, 4, 1, 32]
length = len(list1) # Return the length of the List
maximumValue = max(list1) # Return item with the maximum value
minimumValue = min(list1) # Return item with minimum value in the List
sumValue = sum(list1) # Sum of all items in a List

print(length)
print(maximumValue)
print(minimumValue)
print(sumValue)
print("\n\n")

a = [1, 2, 3]
b = a
print(b)
# >>>
# >>> Output: [1, 2, 3]

a[0] = "Hmm"
print(a)
# >>>
# >>> Output: ["Hmm", 2, 3]

print(b)
# >>>
# >>> Output: ["Hmm", 2, 3]



#----------------- INDEX OPERATOR []
myList = [5.6, 4.5, 3.3, 13.2, 4.0, 34.44, 34.0, 45.45, 99.993, 11123]
print(myList[2])

# You can read items and perform an operation on them
# Here, we are reassigning the value of myList[2]
# which is 3.3 to a new value - which is the addition of
# myList[0] and myList[1] and that would be: 5.6 + 4.5
# myList[2] would have a new value of 10.1
myList[2] = myList[0] + myList[1]
print(myList[2])

# Accessing items based on their index position
# >>> myList[0] = 5.6
# >>> myList[1] = 4.5
# >>> myList[2] = 3.3
# >>> myList[3] = 13.2
# >>> ...
# >>> myList[n] = value
# n representing the index position  of the last item
# in the list would the length of the list minus 1
# for myList, the last item would be myList[9]
# considering the length of the list is 10

for i in range(len(myList)):
    myList[i] = i
    print(myList)


i = 0
while i < len(myList):
    print(myList[i])
    i += 1

print("\n\n")
print(myList[-2])
print("\n\n")





# ----------------- LIST SLICING [start: end]
# Remember, Python will not output the value of the index it ends at.
# But it will always output the value of the index it begins at
myList = [5.6, 4.5, 3.3, 13.2, 4.0, 34.44, 34.0, 45.45, 99.993, 11123]
slicedList = myList[2:5]
print(slicedList)
print("\n")
# >>>
# Output: [3.3, 13.2, 4.0, 34.44]

# This is the same and myList[0:5] will print from the start to index 5
myList[:5]

# This would print from index 3 to the end of the list
myList[3:]

# Funny, but this is the same as myList[3:] above.
myList[3:-1]

# When counting from the end of the list, you start with
# -1, -2, -3, -4, .... up to -N

nums = [2, 3, 5, 7, 9, 1]
print(nums[2:4]) # Prints from index position 2 to 4
print(myList[1:4]) # Prints from index position 1 to 4
print(myList[1:]) # Prints everything from index position 1
print(nums[:2]) # Prints from index position 0 to 2
print(nums[1: -3]) #Prints from index position 1 to -3
print("\n\n")





#----------------- "+", "*", "in/not", "in" OPERATORS
list1 = [2,3]
list2 = [1,9]
list3 = list1 + list2 # Joining two Lists using "+"
print(list3)

list4 = 3 * list1 # Replicate List elements (3 times) using "*"
print(list4)

list1 = [2, 3, 5, 8, 33, 21]
print(10 in list1) # Determines the trueness of the existence of an item in a List using "in"
print(10 not in list1) # Determines if an item exists in a List using "not in"
print("\n\n")





#----------------- Traversing Elements in a for LOOP
for u in myList: # For each item in myList, assign it to the variable "u"
    print(u) # Print the variable and return if any more item(s) remains in the List

print("\n")

for i in range(0, len(myList), 2): # for each count in the range from 0 to 10, skip by 2
    print(myList[i]) # It prints the item at 0, and then skips by 2 to print the next item

print("\n\n")





#----------------- ">", ">=", "<", "<=", "==", "!=" OPERATORS
list1 = ["green", "red", "blue"]
list2 = ["red", "blue", "green"]
print(list2 == list1)
print(list2 != list1)
print(list2 >= list1)
print(list2 > list1)
print(list2 < list1)
print(list2 <= list1)

# Search List using membership operator "in"=
NAMES = ["Danny", "Victor", "Larry", "Victoria", "Laura"]
FINDNAME = "Danny" in NAMES
print(FINDNAME)
print("\n\n")


# ----------------- LIST COMPREHENSION
list1 = [x for x in range(5)]  # Returns a List of 0, 1, 2, 3, 4
print(list1)

list2 = [1.5 * x for x in list1]
print(list2)

list3 = [x for x in list2 if x < 3.0]
print(list3)

print("\n\n")


# ----------------- LIST METHODS
# ----- append(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort(), copy()
list1 = [2, 3, 4, 1, 32, 4]
list1.append(19)
print(list1)
# >>>
# Output: [2, 3, 4, 1, 32, 4, 19]

listCounter = list1.count(4)  # Returns the number of times "4" appears in the List
print(listCounter)

list2 = [99, 54]
list1.extend(list2)  # Used to join two Lists, just like the "+" or "+=" operator
print(list1)

# The above would produce the same output as
# list1 += list2

# If we had to use append, it would have been added as a list item
# list1.append(list2)
# print(list1)
# >>>
# Output: [2, 3, 4, 1, 32, 4, [99, 54]]  # This is what it would have looked like
# A list within a list. Bu that was not our desired output


# names = ["Danny", "Victor", "Larry", "Victoria", "Laura"]
# findIndex = names.index("Victoria") # Returns the index position of the item
# print(findIndex)
# >>>
# >>> Output: 3

findIndex = list1.index(32)  # Returns the index position of the item
print(findIndex)

list1.insert(1, 25)  # Insert the number 25 at index position 1
print(list1)

# pop() removes an item from the List stack,
# but you can still retrieve that item and hold in a variable
poppedItem = list1.pop(1)
print(poppedItem)
# >>>
# >>> Output: 3

popped = list1.pop()  # When passed no value, it pops the last item in the List
print(popped)
# >>>
# >>> Output: 4

# Delete an item using the 'del' command
del list1[0]
print(list1, "\n")

# Removes an item from the List,
# and you cannot access or hold the removed item in a variable
trial = list1.remove(32)
print(trial, "\n")  # This will return "None"

list1.sort()  # This would sort the List in an ascending order
print(list1)

list1.reverse()  # This would reverse the order of the List
print(list1)

# This copies the items in list1 into copiedList
# and should list1 be updated, so also will copiedList
copiedList = list1.copy()
print(copiedList)

# However, to only copy items from one List to another without the update of the parent List
# affecting the copied List, use any of:
listCopy = [x for x in list1]

# or

listCopy = [] + list1
# By doing any of the above, updating list1 doesn't affect the content of listCopy
# Or import and use the copy modules as such:
listCopy = copy.copy(list1)
# Use deepcopy() where the list to be copied has other inner lists
listCopy = copy.deepcopy(list1)


# Convert a list into a string separated  by a predefined delimiter
NAMES = ["Danny", "Victor", "Larry", "Victoria", "Laura"]
delimeter = ","  # let's use comma as the delimiter here
NAMES_STRING = delimeter.join(NAMES)  # Join list items into comma-separated strings
# that is, a string delimited by commas
print(NAMES_STRING)


# Sort the items in a list
NAMES = ["Danny", "Victor", "Larry", "Victoria", "Laura"]
NAMES.sort()  # Reorders the list in an ascending alphabetic order
NAMES.sort(reverse=True)  # Reorders the list in a descending alphabetic order
NAMES.reverse()  # Reverses the order of a list

# Create a new reordered list that does not affect the original list
# You can also specify extra parameters such as reverse, etc 
sortedNames = sorted(NAMES, reverse=True)


print("\n\n")





#----------------- SPLIT STRINGS INTO LIST
items = "Jane John Peter Susan".split() # Split a string into a list
print(items) # In this case, the string is delimited by white spaces

# In this case, the string is delimited by commas ","
items = "Jane, John, Peter, Susan".split(",")
print(items)

date = "09/20/2012".split("/")
print(date)
print("\n\n")





#----------------- INPUTTING LISTS
lst = []
print("Enter 10 numbers: ")
for i in range(10):
    lst.append(int(input()))
print(lst)

names = []
print("Enter 10 names: ")
for i in range(10):
    names.append(str(input()))
print(names)

# Read numbers as a string from the console
s = input("Enter 10 numbers separated by commas: ")
items = s.split(",") # Extract items from the string
lst = [int(x) for x in items]
print(lst)

print("\n\n")
