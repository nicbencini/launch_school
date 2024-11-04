"""
My little sister came back home from school with the following task: given a squared sheet of paper she has to cut it in pieces which, when assembled, 
give squares the sides of which form an increasing sequence of numbers. At the beginning it was lot of fun but little by little we were tired of seeing 
the pile of torn paper. So we decided to write a program that could help us and protects trees.

Task
Given a positive integral number n, return a strictly increasing sequence (list/array/string depending on the language) of numbers, so that the sum of the 
squares is equal to n².

If there are multiple solutions (and there will be), return as far as possible the result with the largest possible values:

Examples
decompose(11) must return [1,2,4,10]. Note that there are actually two ways to decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], 
since 9 is smaller than 10.

For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.

Note
Neither [n] nor [1,1,1,…,1] are valid solutions. If no valid solution exists, return nil, null, Nothing, None (depending on the language) or "[]" (C) ,{} (C++), [] (Swift, Go).

The function "decompose" will take a positive integer n and return the decomposition of N = n² as:

[x1 ... xk] or
"x1 ... xk" or
Just [x1 ... xk] or
Some [x1 ... xk] or
{x1 ... xk} or
"[x1,x2, ... ,xk]"


Problem:
    Create a function that takes a positive integer n and returns a list of numbers so that the sum of squares is equal to n squared.

Rules:
    - return list must include no repetitions and must be in increasing order
    - if multiple solutions exist list must contain largest possible values
    - if no valid solution exists return None

Examples:
    - decompose(11) must return [1,2,4,10]. Note that there are actually two ways to decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], 
    since 9 is smaller than 10.

    For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.

    
Algorithm:
    - create remainder variable and set it to the input_number squared
    - create output_number list

    - create range of integers up to given numbers and calcualte their square and add to square_pool
    -while reaminder != 0
        - while True:
            - get largest number from square_pool which is less than remainder
            - set remaider to remainder - largerst closest number

            - if remainder == 0 
                -break
            - if remainder < 0 :
                - remove largest number from square_pool and repeat
                - reset reaminder to input number squared
                - reset output_number list
        
        - if len(square_pool) == 1:
            return None

    - return output_number list
    

"""

def get_number_below(number, input_list):

    for num in input_list[::-1]:
        if num <= number:
            return num
    
    return None


def decompose(n):

    remainder = n**2
    output_number_list = []

    global_square_pool = [number**2 for number in range(1,n)]

    while remainder != 0:
        if sum(global_square_pool) == 1:
            break

        square_pool = global_square_pool.copy()
        while True:

            if len(square_pool) == 0:
                global_square_pool.pop(-1)
                remainder = n**2
                output_number_list = []
                break

            squared_number = get_number_below(remainder,square_pool)

            if squared_number == None:
                global_square_pool.pop(-1)
                remainder = n**2
                output_number_list = []
                break

            output_number_list.append(int(squared_number**0.5))
            square_pool.remove(squared_number)

            remainder = remainder - squared_number

            if remainder == 0:
                break

            if remainder < 0:
                global_square_pool.pop(-1)
                remainder = n**2
                output_number_list = []
                break


    if remainder == 0:
        return output_number_list[::-1]

print(decompose(5)== [3,4])
print(decompose(8)== None)
print(decompose(42)== None)


