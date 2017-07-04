"""Basic search algorithms for working with lists"""
from random import randint


# -------------------- Working with linear search
# Search through a list using a key
# If a match is found, return the element's index,
# else return -1
def linearSearch(lst, key):
    for i in range(len(lst)):
        if key == lst[i]:
            return i

    return -1  # Not found

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# i = linearSearch(nums, 6)
# j = linearSearch(nums, 23)
# print(i)
# print(j)

nums = list(range(100000000))
i = linearSearch(nums, 83201912)
print(i)


# -------------------- Working with binary search
# Version 1
def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1

    mid = (low + high) // 2
    if key < lst[mid]:
        high = mid - 1
    elif key == lst[mid]:
        return mid
    else:
        low = mid + 1


# Version 2
def binary_Search(lst, key):
    low = 0
    high = len(lst) - 1

    while high >= low:
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1

    return -1  # Not found

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# i = binarySearch(nums, 6)
# j = binarySearch(nums, 23)
# print(i)
# print(j)

nums = list(range(100000000))
i = binary_Search(nums, 83201912)
print(i)
