"""
Calculate the product of all numbers in a list using the reduce function.
"""

from functools import reduce

product = reduce(lambda x,y: x*y, [1,2,3,4,5,6])

print(product)