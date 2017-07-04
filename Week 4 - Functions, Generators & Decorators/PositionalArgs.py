"""Positional, Keyword Arguments in Python Functions"""
import math


def power(x, y):
    """Assumes x is the number, and y is the power"""
    return math.pow(x, y)

a = 5
b = 7
# print(subtraction(5, 7))
# print(power(5, 3))


def menu(wine, entree=None, dessert="pudding"):
    return {"wine": wine, "entree": entree, "dessert": dessert}

print(menu('chardonnay', 'chicken', "cake"))
print(menu("chardonnay", dessert="bagel", entree="beef"))


def buggy(arg, result=list()):
    result.append(arg)
    print(result)


def buggy(arg, result=None):
    if result == None:
        result = []
    result.append(arg)
    print(result)

name = "Jones"

buggy("Chris")
buggy("Marvin")


# Positional Arguments with *
def print_args(*args):
    print("Positional argument tuple: ", args)

print_args("Chris", 1, 2, "1", 34.56, [])


def print_kwargs(*args, **kwargs):
    print("Keyword arguments:", kwargs)

print_kwargs(wine="Chardonnay", entree="Chicken", dessert="Pudding")

