"""
Write a function that takes a string argument consisting of a first name, a space,
 and a last name. The function should return a new string consisting of the last name, a comma, 
 a space, and the first name.

You may assume that the names don't include middle names, initials, or suffixes ("Jr.", "Sr.").

Problem
Input: String
Output: String

"""


def swap_name(input_name):
    name, surname = input_name.split(' ')
    return f'{surname}, {name}'




print(swap_name('Joe Roberts') == "Roberts, Joe")   # True



