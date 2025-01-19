"""
Remove all None values from a list using the filter method.
"""

input_list = [1,2,3,None,4,5,None]

print(list(filter(lambda value: value != None, input_list)))