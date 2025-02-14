"""
Use map to create a list of lengths of each string in the original list.
"""

string_list = ['this', 'is', 'a', 'test']

length_list = map(lambda x: len(x), string_list)

print(list(length_list))