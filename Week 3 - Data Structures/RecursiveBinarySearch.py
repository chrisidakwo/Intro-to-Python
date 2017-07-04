"""Binary search using recursion"""


def search(lst, e):
    """Assumes lst is a list, and the elements are sorted
    in an ascending order.
    
    Returns True if e exists in lst and False otherwise"""

    def binary_search(lst, e, low, high):
        if high == low:
            d = lst[low] == e
            return "Index = {0}".format(low)

        mid = (low + high) // 2
        if lst[mid] == e:
            return "Index = {0}".format(mid)
        elif lst[mid] > e:
            if low == mid:  # ==> there's nothing left to search
                return -1
            else:
                return binary_search(lst, e, low, mid - 1)
        else:
            return binary_search(lst, e, mid + 1, high)

    if len(lst) == 0:
        return -1
    else:
        return binary_search(lst, e, 0, (len(lst) - 1))


nums = list(range(20, 1000))
print(search(nums, 853))



