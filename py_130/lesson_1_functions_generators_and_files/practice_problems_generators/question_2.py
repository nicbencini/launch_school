"""
Create a generator function that generates the reciprocals of the numbers from 1 to n, where n is an argument to the function. 
Use a for loop to print each value.
"""

def reciprocal(number):
    for i in range (1,number + 1):
        yield 1/i

for i in reciprocal(7):
    print(i)