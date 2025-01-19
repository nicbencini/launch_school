"""
Use map to create a list of lengths of each string in the original list.
"""

string_list = ['This', 'is', 'a', 'test']

print(list(map(lambda string: len(string), string_list)))