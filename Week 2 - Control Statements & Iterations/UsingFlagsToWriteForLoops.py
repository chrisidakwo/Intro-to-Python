""" Rewriting For Loops"""


# ---------- SAMPLE 1
# Use of break
SUM = 0
NUMBER = 0
while NUMBER < 20:
    NUMBER += 1
    SUM += NUMBER
    if SUM > 100:
        break
print("The number is", NUMBER)
print("The sum is", SUM)
print("\n")

# Without break
SUM = 0
NUMBER = 0
END = False
while NUMBER < 20 and not END:
    NUMBER += 1
    SUM += NUMBER
    if SUM >= 100:
        END = True
        print("The number is", NUMBER)
        print("The sum is", SUM)
    # else:
    #     END = False
print("\n")


# ---------- SAMPLE 2
# Use with continue
SUM = 0
NUMBER = 0
while NUMBER < 20:
    NUMBER += 1
    if NUMBER == 10 or NUMBER == 11:
        continue
    SUM += NUMBER
print("The sum is", SUM)


# Without continue: Version 1
SUM = 0
NUMBER = 0
FLAG = False
while NUMBER < 20:
    NUMBER += 1
    if NUMBER == 10 or NUMBER == 11:
        FLAG = True
    else:
        FLAG = False
    if not FLAG:
        SUM += NUMBER
print("The sum is", SUM)


# Without continue: Version 2
SUM = 0
NUMBER = 0
FLAG = False
while NUMBER < 20:
    NUMBER += 1
    if NUMBER == 10 or NUMBER == 11 and FLAG:
        FLAG = True
    else:
        FLAG = False
        SUM += NUMBER
print("The sum is", SUM)

