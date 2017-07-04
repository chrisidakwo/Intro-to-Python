"""Understanding and working with list comprehension"""

L = [x**2 for x in range(1, 7)]
print(L)
print()

# which would be the same thing as this:
L = []
for x in range(1, 7):
    L.append(x**2)

print(L)
print()


# ---------- The for clause can be followed by one or more if and for blocks
mixed = [4, 7, 9, "n", "z", 9.99, "df", 3, 4.0]
L = [x**2 for x in mixed if type(x) == int]
print(L)
print()

# which would be the same as:
L = []
for x in mixed:
    if type(x) == int:
        L.append(x**2)

print(L)


# ---------- Printing directly from comprehension
[print(y - 1) for y in range(1, 21)]
print()


# ---------- Working with a list
numbers = []
[numbers.append(z + 1) for z in range(0, 30)]
print(numbers)
print()


# ---------- Working with nested ifs
numbers = []
[numbers.append(z) for z in range(0, 31) if z % 2 == 0 and z != 30]
print(numbers)
print()


# ---------- Working with nested for
rows = range(1, 5)
cols = range(0, 3)
for row in rows:
    for col in cols:
        print(row, col)
print()

# cells = [print(row, col) for row in rows for col in cols]
# print(cells)
matrix = [(row, col) for row in rows for col in cols]
for row, col in matrix:
    print(row, col)
print()


# ---------- Working with a combination of nested for and if
[print(row, col) for row in rows for col in cols if row == 3]
