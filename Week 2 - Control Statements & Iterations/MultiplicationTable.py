""" Sampling nested loops """

# Let's write a program that prints a multiplication table
# from 1 to 6. You could extend it if you wanted to

# Display header text
print("\n    Multiplication Table\n")

# Display the number title
print("  |", end="")
for j in range(1, 7):
    print(format(j, "5d"), end="")
print() # Jump to a new line
print("---------------------------------")

# Display table body
for i in range(1, 7):
    print(i, "|", end="")
    for j in range(1, 7):
        # Display the product of numbers and align properly
        print(format(i * j, "5d"), end="")
    print() # Jump to a new line
print("\n")

