"""Sampling Generators and Decorators"""

# Generators
print(sum(range(1, 1001)))

result = [num for num in range(1, 1001)]
print(sum(result))


# result = 0
# for num in range(1, 1001):
#     result += num
# print(result)


def range1(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


print(type(range1))

ranger = range1(1, 1000001)
print(ranger)


# for num in ranger:
#     print(num)


# Decorators
def document_it(func):
    def new_function(*args, **kwargs):
        print("Running function: ", func.__name__)
        print("Positional arguments: ", args)
        print("Keyword arguments: ", kwargs)
        result = func(*args, **kwargs)
        print("Result: ", result)
        return result

    return new_function


def add_ints(a, b):
    return a + b


test = document_it(add_ints)  # Manual decorator
test(5, 3)
print(type(test))


@document_it  # <== calling a decorator function
def add_ints(a, b):
    return a + b


@document_it
def sub_int(a, b):
    return a - b


add_ints(5, 3)
sub_int(5, 3)
