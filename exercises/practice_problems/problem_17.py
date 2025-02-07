"""
Create a function that takes a list of integers as an argument. The function should determine the minimum integer 
value that can be appended to the list so the sum of all the elements equal the closest prime number that is greater 
than the current sum of the numbers. For example, the numbers in [1, 2, 3] sum to 6. The nearest prime number greater 
than 6 is 7. Thus, we can add 1 to the list to sum to 7.

Notes:

The list will always contain at least 2 integers.
All values in the list must be positive (> 0).
There may be multiple occurrences of the various numbers in the list.


Problem:
    Create a function that takes a list of integers as an argument.
    The function should determine the 
    [minimum integer value that can be append to the list so] # chose minimum value from list
    [the sum of all the elements equal the closest prime number] # get closest prime number and check which elements can be combined to create the sum
    [that is greater than the current sum of numbers]. # must be greater than the current sum of numbers

Rules:
    - The list will always contain at least 2 integers
    - All values in the list will be > 0
    - The list will contain duplicates

Examples:
    print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7


    print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
    print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
    print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

    # Nearest prime to 163 is 167
    print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

Data:
    Input: list of integers
    Output: integer

Algorithm:
    - Sum all values in the list
    - Get nearest prime number
        - prime number is only divisible by 1 and itslef
        - create while loop
            - incrementally add 1 to the current value
            - check if that number is prime, if so return that values
                - get range of values from 2 up to number
                - check if values are divisible by number
                - if no values are divisible by the number return True
    - subtract prime number from sum of values in the list
    - return result


"""

def is_prime(number):
    
    for i in range(2,number):

        if number%i == 0:
            return False
    
    return True

def get_closest_prime(input_integer):
    
    while True:
        input_integer += 1
        
        if is_prime(input_integer):
            break
    
    return input_integer

def nearest_prime_sum(integer_list):
    
    sum_of_values = sum(integer_list)

    nearest_prime = get_closest_prime(sum_of_values)

    return nearest_prime - sum_of_values


print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)