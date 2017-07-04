"""Working with multi-dimensional lists"""

import random

# ---- INITIALIZING LIST WITH INPUT OR RANDOM VALUES
matrix = []

numberOfRows = eval(input("Enter the number of rows: "))
numberOfColumns = eval(input("Enter the number of columns: "))

for row in range(numberOfRows):
    matrix.append([])  # Add an empty new row
    for column in range(numberOfColumns):
        # value = eval(input("Enter a number and press Enter: "))
        # matrix[row].append(value)
        matrix[row].append(random.randint(0, 99))
        # We could either randomly generate
        # or use user input as commented eval(input) lines above

for x in matrix:
    print(x)

print("\n")
print(matrix)
print("\n\n")

# ---- PRINTING ELEMENTS IN A TWO-DIMENSIONAL LIST
print("Printing elements in a two-dimensional List:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Assume a list is given
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()  # Print a new line. The elements appear in one line without this

# Or you can write as below:
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        print(matrix[row][column], end=" ")
    print()  # Print a new line. The elements appear in one line without this

print("\n\n")

# ---- SUMMING ALL ELEMENTS
print("Printing the sum of all int elements in a two-dimensional List:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Assume a list is given

total = 0
for row in matrix:
    for value in row:
        total += value

print("Total is", total)
print("\n\n")

# ---- SUMMING ELEMENTS BY COLUMN
print("Printing the sum of int elements, in a two-dimensional List, by column:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Assume a list is given

for column in range(len(matrix[0])):  # 0 1 2
    total = 0
    for row in range(len(matrix)):  # 0 1 2
        total += matrix[row][column]
    print("Sum for column", column, "is:", total)

print("\n\n")

# ---- FINDING THE ROW WITH THE LARGEST SUM
print("Find the row with the largest sum if int elements:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Assume a list is given

maxRow = sum(matrix[0])  # Get sum of the first row
indexOfMaxRow = 0  # initialize the variable to hold index value of row with maximum sum

for row in range(1, len(
        matrix)):  # Start from position 1 because we have already summed values in position 0 in the maxRow variable
    if sum(matrix[row]) > maxRow:
        maxRow = sum(matrix[row])
        indexOfMaxRow = row
print("Row", indexOfMaxRow, "has the maximum sum of", maxRow)
print("\n\n")

# ---- RANDOM SHUFFLING
print("Randomly shuffle all elements in a two-dimensional List:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Assume a list is given

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        i = random.randint(0, len(matrix) - 1)
        j = random.randint(0, len(matrix[row]) - 1)

        # Swap matrix[row][column] with matrix[i][j]
        matrix[row][column], matrix[i][j] = matrix[i][j], matrix[row][column]

print(matrix)
print("\n\n")

# ---- SORTING
points = [[4, 2], [1, 7], [4, 5], [1, 2], [1, 1], [4, 1]]
points.sort()
print(points)
print("\n\n")

# --- EXERCISES
# 1. Create a 2D-List of 3 rows & 4 columns with values as 0
matrix = []
numberOfRows = 3
numberOfColumns = 4

for row in range(numberOfRows):
    matrix.append([])
    for column in range(numberOfColumns):
        matrix[row].append(0)
print(matrix)
print("\n\n")

# 2. Create a 2D-List with different number of elements in a row
matrix = []
numberOfRows = random.randint(2, 12)
numberOfColumns = 4

for row in range(numberOfRows):
    matrix.append([])
    for column in range(numberOfColumns):
        matrix[row].append(random.randint(0, 99))
print(matrix)