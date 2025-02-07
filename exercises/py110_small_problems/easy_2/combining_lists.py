"""
Write a function that takes two lists as arguments and returns a set that contains 
the union of the values from the two lists. You may assume that both arguments will always be lists.

Program
Input: 2 lists
Output: Set

Implicit Rules:
-Both arguments will always be lists.

Explicit Rules:
-Function does not mutate the original lists.

Algorithm:
- Combine lists
- Create set from lists
"""

def union(list1, list2):
    return set(list1 + list2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
