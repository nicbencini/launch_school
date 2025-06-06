"""
Create a function concatenate that takes any number of strings and concatenates them into a single string with a space in between.
"""
from functools import reduce


def concatenate(*args):
    return ' '.join(args)



print(concatenate("Launch", "School", "is", "great")) # Launch School is great
print(concatenate("I", "am", "working", "on", "the", "PY130", "course")) # I am working on the PY130 course