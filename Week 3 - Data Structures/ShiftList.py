""" Shift the first item to the end of the list """

# ----------------- SHIFTING LISTS
FRUITS = ["Apple", "Banana", "Guava", "Orange", "Mango", "Pawpaw", "Tangerine"]
print("Original list:\n", FRUITS, "\n")


# Create function to shift the first item to the end of the list
def shift(lst):
    """ Shifting position of list items """
    temp = lst[0]  # Retain the first element

    # Shift elements left
    for i in range(1, len(lst)):
        lst[i - 1] = lst[i]
    # Move the first element to fill in the last position
    lst[len(lst) - 1] = temp
    print(lst)


# Shift list and output result
print("Shifted list: ")
shift(FRUITS)

print("\n")
