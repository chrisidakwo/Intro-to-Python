""" Solving a quadratic equation.

ax2 + bx + c = 0
(b2 - 4ac) --> is the discriminant
if (b2 - 4ac) is positive, the equation has two real roots
if (b2 - 4ac) is negative, the equation has no real root
if (b2 - 4ac) is zero, the equation has one root

RULE:
- If discriminant is positive, display two roots
- If discriminant is zero, display one root
- Otherwise display "The equation has no real root"

"""

import math

# Set message constant
NOREALROOT = "The equation has no real root"

# Get the values of a, b, and c
VALUEA = float(input("Enter the value of a (can be a decimal value): "))
VALUEB = float(input("Enter the value of b (can be a decimal value): "))
VALUEC = float(input("Enter the value of c (can be a decimal value): "))

# Calculate the discriminant
DISCRIMINANT = math.pow(VALUEB, 2) - (4 * (VALUEA * VALUEC))

if DISCRIMINANT > 0.00:
	# Calculate the equation's roots
	R1 = (-VALUEB + math.sqrt(DISCRIMINANT)) / (2 * VALUEA)
	R2 = (-VALUEB - math.sqrt(DISCRIMINANT)) / (2 * VALUEA)

	# Print roots based on rules
	if DISCRIMINANT > 0.0:
		print("Root 1: {0}\nRoot 2: {1}".format(R1, R2))
	elif DISCRIMINANT == 0.0:
		print("Root: {0}".format(R1))
else:
    print(NOREALROOT)


