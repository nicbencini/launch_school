"""
A prime number is a positive number that is evenly divisible only by itself and 1. 
Thus, 23 is prime since its only divisors are 1 and 23. However, 24 is not prime since it has divisors of 1, 2, 3, 4, 6, 8, 12, and 24. Note that the number 1 is not prime.

Write a function that takes a positive integer as an argument and returns true if the number is prime, false if it is not prime.

You may not use any of Python's add-on packages to solve this problem. Your task is to programmatically determine whether a number is prime without relying on 
functions that already do that for you.

Program:
Input: Integer
Output: Bool

Rules:
- Prime numbers are only divisible by self
- Numbers should be cleaned to remove '_'

Examples:

Algorithm:
# Clean number to remove '_'
# Cycle through all integers up to the chosen number
# If the number is divisible by a number smaller than itself break loop and return False
    #Create helper fucntion to check if number is divisible 
# If loop continues until chosen number return true
"""

def is_divisible(number_1, number_2):



    return number_1 % number_2 == 0

def is_prime(input_number):
    
    input_number = int(input_number)

    if input_number == 1:
        return True

    for i in range(2, input_number + 1):

        if i != input_number  and is_divisible(input_number, i):

            return False
        
    return True


print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True
