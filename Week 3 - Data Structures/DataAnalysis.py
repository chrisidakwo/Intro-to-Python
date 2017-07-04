""" Data Analysis with list"""

NUMBER_OF_ELEMENTS = 5
NUMBERS = []  # Create a new list
SUM = 0

for i in range(NUMBER_OF_ELEMENTS):
    VALUE = int(input("Enter a new number: "))
    NUMBERS.append(VALUE)  # Add each number to the new list
    SUM += VALUE  # Recalculate sum

AVERAGE = SUM / NUMBER_OF_ELEMENTS  # Compute average

COUNT = 0  # The number of elements greater than the computed average
for i in range(NUMBER_OF_ELEMENTS):
    if NUMBERS[i] > AVERAGE:
        COUNT += 1

print("Average is: ", AVERAGE)
print("Number of elements greater than the average is: ", COUNT)
