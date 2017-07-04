"""Understanding & working with recursion"""

# This dummy function below, simply explains the concept of
# recursive functions
# def drinkCoffee(cup):
#     if cup is not empty:
#         cup.takeOneSip() # Take a sip
#         drinkCoffee(cup) # This will keep running until cup is empty
#     return "Cup is empty now!"


# Using the factorial of a number to understand how recursion works
# Using the basic example of factorial in Math
# where 1! = 1 and
# (n + 1)! = (n + 1) * n!
def factorial(n):
    """Assumes that n is an int > 0"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Producing the same output of the recursive function above,
# using a for loop
def factfor(n):
    """Assumes that n is an int > 0"""
    result = 1
    if n == 0:
        return result
    for k in range(n, 0, -1):
        result = result * k
    return result


# Producing the same output of the recursive function above,
# using a while loop
def factWhile(n):
    """Assumes that n is an int > 0"""
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result


# -------------------- Recursive implementation of the Fibonacci sequence
# 0 - 0
# 1 - 1
# 2 - 1
# 3 - 2
# 4 - 3
# 5 - 5
# 6 - 8
# 7 - 13


def fib(n):
    """Assumes n is an int >= 0
    Returns the Fibonacci of n"""
    if n == 0:  # ==> based on the idea that the Fibonacci of 0 is 0
        return 0
    elif n == 1:  # ==> based on the idea that the Fibonacci of 1 is 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Test the fib(n) function
def testFib(n):
    for i in range(n + 1):
        print("fib of {0} = {1}".format(i, fib(i)))

print(testFib(20))

