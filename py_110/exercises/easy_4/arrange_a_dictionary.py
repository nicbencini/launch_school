"""
Given a dictionary, return its keys sorted by the values associated with each key.
"""

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']

def get_values(key):
    return my_dict[key]
    

def order_by_value(input_dictionary):
    return sorted(input_dictionary, key= get_values)


print(order_by_value(my_dict) == keys)  # True
