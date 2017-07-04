"""How to write functions and work with variables"""
from random import randint, randrange, shuffle


# ---------- functions template structure
def do_something():
    print()


# ---------- A function to find the maximum of two numbers
def max(x, y):
    """Returns the maximum of x and y"""
    if x > y:
        return x
    else:
        return y


FRUITS = ["Apple", "Peach", "Banana", "Orange", "Guava", "Lemon"]


# ---------- Minimal function to randomize a list
# FIXME: Try re-writing this as a lambda function
def randomize_list(lst):
    shuffle(lst)
    return lst

print(FRUITS)
print(randomize_list(FRUITS))


x = 23
y = 24


# ---------- Just another function returning a tuple
def math_ops(a, b):
    x = 45
    y = 34
    return x, y

print(x)
print(y)
print(math_ops(7, 5))


# -------------------- Variable Scope
# FIXME: Carefully look through the function f(x) to understand the scope of variables
def f(x):
    def g():
        x = "abc"  # Assigning x to a new value
        print("x =", x)

    def h():
        z = x  # Assigning a variable to the value of global parameter, x
        print("z =", z)

    x = x + 1
    print("x =", x)
    h()
    g()
    print("x =", x)
    return g

x = 3
z = f(x)  # ==> z is a function
print("\nOutside of function now")
print("x =", x)
print("z =", z)
z()

# FIXME: Try re-writing the quadratic equations case study, likewise the BMI using functions
# FIXME: Also try writing a palindrome-check function using recursion
