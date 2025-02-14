"""
Create a list where each number from the original list is squared using the map method.
"""

num_list = [1,2,3,4,5]

squared_list = map(lambda x: x*x, num_list)

print(list(squared_list))