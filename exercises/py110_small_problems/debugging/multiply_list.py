"""

You want to multiply all elements of a list by 2. However, the function is not returning the expected result. Explain the bug, and provide a solution.

"""


def multiply_list(lst):
    for idx,item in enumerate(lst):
        lst[idx] *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])

# The bug was occuring because the muliplied value was not being inserted into the original list. Lists are mutable and are passed into functions by reference so to update the items in 
# the list the item that is being multiplied needs to be referenced using its index and reassigned to its multiplied value.