"""
We defined a function intending to multiply the sum of numbers by a factor. However, the function raises an error. Why? How would you fix this code?
"""

def factor(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(factor(numbers, 2) == 20)

"""
The code raises an error because the name of the function is shadowing the in-built function sum(). So when this is used on line 6, the code calls the newly defined function within itself
since this requires two arguments, an error is raised. This can be fixed be renaming the function to a new name.

"""