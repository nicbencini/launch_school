"""
The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers. The first two Fibonacci numbers are 1 and 1. 
The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:

F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)

Write a function called fibonacci that computes the nth Fibonacci number, where nth is an argument passed to the function:

If you're familiar with the concept of recursive functions, don't try to write a recursive solution at this time; 
you'll do that in the next exercise. In other words, write a procedural function that doesn't try to call itself.

If you don't know about or understand recursion, don't worry about it. You'll learn soon enough.


Problem:
To write a function that computes the nth finbonacci number.

Input: Integer represeting the nth fibonacci number
Output: Input representing the fibonacci number

Rules:
- input Number will be positive and greater than zero
- input number can be less than 2

1 = 1
2 = 1
3 = 1 + 1 = 2
4 = 1 + 2 = 3
5 = 2 + 3 = 5
6 = 3 + 5 = 8

Algorithm:

# Create range up to given number
# Create empty variables to store numbers n-1 and n-2
# for each number in the range cycle through and replace n-1 with n-2 and n-1 with n-1 + n-2
# Create catchs for if the number is smaller than 2 it is equal to 1



"""

def fibonacci(number):

    number_1 = 1
    number_2 = 0

    for i in range(1, number):

        fibonacci_number = number_1 + number_2

        number_1 , number_2 = fibonacci_number , number_1
    
    return number_1





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

