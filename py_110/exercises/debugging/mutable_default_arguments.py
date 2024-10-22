"""
We want to create a function that appends a given value to a list. However, the function seems to be behaving unexpectedly:
"""


def append_to_list(value, lst=[]):
    lst.append(value)

    print(lst)
    return lst


print(append_to_list(1) == [1])
print(append_to_list(2) == [2])