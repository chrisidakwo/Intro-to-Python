""" Controlling Loop statements with user input """

DATA = int(input("Enter an integer (entering zero will end the program): "))

# Keep reading data until the user inputs 0
SUM = 0
while DATA != 0:
    SUM += DATA
    DATA = int(input("Enter an integer (entering zero will end the program): "))

print("This sum is", SUM)
