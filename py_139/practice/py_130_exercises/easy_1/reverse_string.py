"""
Use a generator expression to yield each character of a string in reverse order.
"""

string = 'This is a test'

def reverse_string(input_string):

    reversed_string = input_string[::-1]

    for char in reversed_string:
        yield char

print(list(reverse_string(string)))