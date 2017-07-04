""" Working with List functions """
import random

LST = [30, 1, 2, 1, 0]

print(LST.index(1), "\n")  # The index() function
print(LST.count(1), "\n")  # The count() function
print(LST, "\n")

LST.append(40)  # The append() function
print(LST, "\n")

LST.insert(1, 40)  # The insert() function
print(LST, "\n")

LST.extend([1, 43])  # The extend() function
print(LST, "\n")

LST.remove(1)  # The remove function
print(LST, "\n")

LST.pop(1)  # The pop() function
print(LST, "\n")

LST.sort()
print(LST, "\n")

LST.reverse()
print(LST, "\n")

random.shuffle(LST)
print(LST, "\n")
