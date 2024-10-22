"""
We have a list of lists and want to duplicate it. After making the copy, we modify the original list, but the copied list also seems to be affected:

"""


import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])

"""
The issue is that on line 10 a shallow copy is being created of the list which copies the othermost level of the orignial list only. The items within the sublists are referened not copied.
So when an item of one of the sublists of the orignal list is modified then the sublist within the copied list will also be modifed since they are the same sublist. 
"""