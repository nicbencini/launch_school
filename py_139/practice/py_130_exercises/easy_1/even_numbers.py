"""
Obtain only the even numbers from a list using the filter function.
"""

input_list = [1,2,3,4,5,6]

even_numbers = filter(lambda x: x%2==0, input_list)

print(list(even_numbers))