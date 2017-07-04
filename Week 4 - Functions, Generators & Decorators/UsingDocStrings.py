"""Writing understandable codes using Docstrings"""


# Sample Docstring
def print_if_true(th):
    """Prints the first argument is a second argument is true
    The operations is:
        1. Check whether the **second** argument is true
        2. If it is, print the **first** argument"""

    return th()

help(print_if_true)
print(print_if_true.__doc__)

