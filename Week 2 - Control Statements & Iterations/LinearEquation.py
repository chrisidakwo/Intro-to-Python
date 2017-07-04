""" Solving a linear equation.

Using the Cramer's rule to solve an equation of such:
ax + by = e
cx + dy = f


    Cramer's Rule
    ---------
    x = (ed - bf) / (ad - bc)
    y = (af - ec) / (ad - bc)
    
    RULE:
    if (ad - bc) = 0, report that 'the equation has no solution'

"""

# Set message constant
NOSOLUTION = "The equation has no solution"
# VALUES = []
# LETTERS = 'a', 'b', 'c', 'd', 'e', 'f'  # A Tuple
#
# for num in range(6):
#     USERINPUT = float(input("Enter the value of {0}. Can be a decimal value: ".format(LETTERS[num])))
#     VALUES.append(USERINPUT)

# Get the values of a, b, c, d, e, and f
VALUEA = float(input("Enter the value of a (can be a decimal value): "))
VALUEB = float(input("Enter the value of b (can be a decimal value): "))
VALUEC = float(input("Enter the value of c (can be a decimal value): "))
VALUED = float(input("Enter the value of d (can be a decimal value): "))
VALUEE = float(input("Enter the value of e (can be a decimal value): "))
VALUEF = float(input("Enter the value of f (can be a decimal value): "))

# VALUEA = VALUES[0]
# VALUEB = VALUES[1]
# VALUEC = VALUES[2]
# VALUED = VALUES[3]
# VALUEE = VALUES[4]
# VALUEF = VALUES[5]

# Calculate the value of (ad - bc)
SOLUTION = (VALUEA * VALUED) - (VALUEB * VALUEC)

ISSOLUTION = True if SOLUTION != 0 else False

if ISSOLUTION:
    # Calculate the value of x and y using Cramer's rule
    # x = (ed - bf) / (ad - bc)
    VALX = ((VALUEE * VALUED) - (VALUEB * VALUEF)) / ((VALUEA * VALUED) - (VALUEB * VALUEC))

    # y = (af - ec) / (ad - bc)
    VALY = ((VALUEA * VALUEF) - (VALUEE * VALUEC)) / ((VALUEA * VALUED) - (VALUEB * VALUEC))

    print("The value of x is: {0}\nThe value of y is: {1}".format(VALX, VALY))
else:
    print(NOSOLUTION)


# Test Values
# 9.0, 4.0, 3.0, -5.0, -6.0, -21.0 --> x is -2.0 and y is 3.0
# 1.0, 2.0, 2.0 3.0, 4.0, 5.0 --> The equation has no solution

# This example can be improved using a list and for loop, but we won't do that until we get to talk about lists
# We'll then see how we can improve this example

