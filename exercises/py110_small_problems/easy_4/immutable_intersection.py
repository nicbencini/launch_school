"""
Transform two lists into frozen sets and find their common elements.
"""

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})

def intersection(input_1, input_2):
    set1 = set(input_1)
    set2 = set(input_2)

    return set1.intersection(set2)

print(intersection(list1, list2) == expected_result) # True
