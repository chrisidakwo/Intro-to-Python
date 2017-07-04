""" Experiment using "else" in a while loop """

NUMBERS = [1, 3, 5]
POSITION = 0
while POSITION < len(NUMBERS):
    NUMBER = NUMBERS[POSITION]
    if NUMBER % 2 == 0:
        print("Found even number", NUMBER)
        break
    POSITION += 1
else: # break not called
    print("No even number found!")
    