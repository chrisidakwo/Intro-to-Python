"""To test block of codes and ideas"""
from copy import copy
from random import randint, randrange

print("\nFirst:")
numbers = [print(x) for x in range(0, 7)]
print()
print("Second:")
for x in list(range(0, 7)):
    print(x)

FRUITS = ["Apple", "Banana", "Guava", "Orange", "Mango", "Pawpaw", "Tangerine"]
print(FRUITS)


# ---------- RANDOMISE THE ORDER OF ITEMS IN A LIST
def randomize_list(x):
    """Randomize a list

    x ==> the list to randomize.
    y ==> a copy of x.
    z ==> the new randomized list.
    """
    y = copy(x)
    z = []
    count = 0
    while count < len(x):
        if y:
            r1 = randint(0, (len(y) - 1))
            z.append(y[r1])
            y.remove(y[r1])
            count += 1

    return z

print(randomize_list(FRUITS))


def randomise_list(x):
    """Randomize a list"""
    l = len(x) - 1
    n = []
    while l >= 0:
        for item in x:
            if item[-1]:
                r = randrange(0, len(x))
            else:
                r = randint(0, l)

            n.insert(r, item)
            l -= 1

    return n

print(randomise_list(FRUITS))
