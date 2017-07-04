"""Calculate BMI 

BMI             INTERPRETATION
Below 18.5      Underweight
18.5 - 24.9     Normal
25.0 - 29.9     Overweight
Above 30.0      Obese

BMI = weight / height * height

1in = 0.0254mtrs

"""
import math

# Prompt the user to enter weight in kg
WEIGHT = float(input("Enter your weight: "))

# Height in inches
HEIGHT = float(input("Enter your height: "))

# Convert height from inches to meter
METERS_PER_INCH = 0.0254
HEIGHT_IN_METRES = HEIGHT * METERS_PER_INCH

# Calculate BMI
BMI = WEIGHT / (math.pow(HEIGHT_IN_METRES, 2))

# Display result
print("BMI is", format(BMI, ".2f"))


if BMI < 18.5:
    print("Underweight")
elif BMI < 25.0:
    print("Normal")
elif BMI < 30.0:
    print("Overweight")
else:
    print("Obese")

