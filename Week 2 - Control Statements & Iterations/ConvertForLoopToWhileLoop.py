""" Converting a for loop to while loop """

SUM = 0
for i in range(4):
    if i % 3 == 0:
        print(i, "-", SUM)
        continue
    SUM += i

print("\n")

SUM = 0
i = 0
while i < 4:
    if i % 3 == 0:
        print(i, "-", SUM)
        # continue
    SUM += i
    i += 1

print("\n")

print(int(True))
