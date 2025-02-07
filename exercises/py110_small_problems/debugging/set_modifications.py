"""
We want to remove certain items from a set while iterating over it, but the code below throws an error. Why is that and how can we fix it?

"""


data_set = {1, 2, 3, 4, 5}

for item in data_set:
    if item % 2 == 0:
        data_set.remove(item)

    
"""
The error is occuring because the code is removing items from the set while it is still iterating over it. This will cause the for loop to iterate over items which no longer exist.
To fix the code a second set should be created to which the items that need to be kept should be added as the loop iterates over the orignal set.
"""