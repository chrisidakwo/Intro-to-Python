import copy


FRUITS = ["Apple", "Peach", "Banana", "Orange", "Guava", "Lemon"]
FRUITS2 = ["Apple", "Apples", "Apple1", "Apple2", "Appl"]
print(FRUITS, "\n")

# Sort items in a list in asc & desc order
FRUITS.sort(reverse=True)
print(FRUITS)


# Sort items using temporal sort function
print(sorted(FRUITS))
print()


# Find the min & max values in a list
print(min(FRUITS2))
print(max(FRUITS2))
print()


# Looping through a list
i = 0
for fruit in FRUITS:
    print(i, "-", fruit)
    i += 1

print()

# More Pythonic way
for num, fruit in enumerate(FRUITS):
    print(num, "-", fruit)


text1 = "Lorem ipsum dolor"
text2 = "Lorem ipsum - dolor - sit, amet"
text2 = text2.replace(",", "-")

text1List = text1.split()
print(text1List)

text2List = text2.split("-")
print(text2List)

tempString = ",".join(text2List)
print(tempString)


a = [1, 2, 3, 4, 5, 6, 7, 9, [2, 3, [4, 5]]]
print(a)
b = a.copy()
c = copy.copy(a)
d = copy.deepcopy(b)

a.append(45)
print(b)


# Pop an item form a list
# poppedFruit = FRUITS.pop(-1)
# print(poppedFruit)
# print(FRUITS)


# Delete items in a list
# del FRUITS[2]  # del is a command, not a function
# print(FRUITS)
#
# removedFruit = FRUITS.remove(FRUITS[0])
# print(removedFruit)
# print(FRUITS)
print()


# Comprehensions
matrix = [[1, 2], [2, 3], [3, 4]]
# numbers = [x for x in range(5) if x != 3]
# print(numbers)

[print(sub) for item in matrix for sub in item]


# for item in matrix:
#     for sub in item:
#         print(sub)




# NAMES = [fruit for fruit in FRUITS if fruit == "Apple"]
# print(NAMES)
#
#
# NAMES = []
# for fruit in FRUITS:
#     if fruit == "Apple":
#         NAMES.append(0)
#     else:
#         NAMES.append(fruit)
#
# print(NAMES)
#


# [print(fruit) for fruit in FRUITS]
#
# for fruit in FRUITS:
#     print(fruit)


# TODO: Working with Else in Comprehensions
