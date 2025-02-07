"""

The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers. 
The first two Fibonacci numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, 
the sixth is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:

F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)

Write a function called fibonacci that computes the nth Fibonacci number, where nth is an argument passed to the function:

Problem:
    Write a function that computes the nth fibonacci number.

Rules:
    -the fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers.
    - numbers provided are greater than 0

Examples:
    - The first two Fibonacci numbers are 1 and 1.
    - The third number is 1 + 1 = 2
    - the fourth is 1 + 2 = 3
    - the fifth is 2 + 3 = 5
    - the sixth is 3 + 5 = 8

Algorithm:
    - If input number is smaller than 3 return 1
    - Define variable first_number and set to 1
    - Define variable second_number and set to 1
    - Cycle through range up to number provided
        - refine first_number = second_number
        - redefine second_number = first_number + second_number
    - Once loop is complete return second_number

"""

def fibonacci(number):
    
    
    first_number = 1
    second_number = 1

    for previous_number in range(1,number + 1):
        if previous_number > 2:
            first_number , second_number = second_number, first_number + second_number
    

    return second_number

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True