"""
Write a function that takes one argument, a list of integers, 
and returns the average of all the integers in the list, rounded down to the integer component of the average. 
The list will never be empty, and the numbers will always be positive integers.

Program
Input: List of integers
Output: Integer representing average

Rules:
- List will never be empty
- The numbers will always be positive integers.

Algorithm
- Use average fuction to calcualte average of integers in the list
- Use int fucntion to round down to the integer component

"""

def average(input_list):
    return int(sum(input_list)/len(input_list))

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True
