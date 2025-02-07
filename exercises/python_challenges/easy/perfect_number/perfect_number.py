"""
The Greek mathematician Nicomachus devised a classification scheme for natural numbers 
(1, 2, 3, ...), identifying each as belonging uniquely to the categories of abundant, 
perfect, or deficient based on a comparison between the number and the sum of its 
positive divisors (the numbers that can be evenly divided into the target number with 
no remainder, excluding the number itself). For instance, the positive divisors of 15 are 1,
 3, and 5. This sum is known as the Aliquot sum.

Perfect numbers have an Aliquot sum that is equal to the original number.
Abundant numbers have an Aliquot sum that is greater than the original number.
Deficient numbers have an Aliquot sum that is less than the original number.
Examples:

6 is a perfect number since its divisors are 1, 2, and 3, and 1 + 2 + 3 = 6.
28 is a perfect number since its divisors are 1, 2, 4, 7, and 14 and 1 + 2 + 4 + 7 + 14 = 28.
15 is a deficient number since its divisors are 1, 3, and 5 and 1 + 3 + 5 = 9 which is less than 15.
24 is an abundant number since its divisors are 1, 2, 3, 4, 6, 8, and 12 and 1 + 2 + 3 + 4 + 6 + 8 + 12 = 36 which is greater than 24.
Prime numbers 7, 13, etc. are always deficient since their only divisor is 1.


problem:
Write a program that can tell whether a number is perfect, abundant, or deficient.

rules:
     - postive divisors are the numbers that can be evenly divided into the target number with no remainder
     - aliquot sum is the sum of a numbers positive divisors
     - perfect number -> aliquot sum is equal to the original number
     - abundant number -> aliquot sum is greater than the original number
     - deficient number -> aliquot sum is less than original number
     - input must be postive integer

Data: 

PerfectNumber (class):
    - classify (static method)
        - input: postive integer
        - output: string classifier

Algorithm:

    positive_divisor method:
        - cycle through integers smaller than but not equalt to the number given:
        - if % with number is zero append to output list
    
    aliquot_sum method:
        - return sum of all postive divisors
    
    classify method:
        - obtian aliquot sum
            - if aliquot sum == number return 'perfect'
            - if aliquot sum > number return 'abundant'
            - if aliquot sum < number return 'deficient'
        

"""

class PerfectNumber:
    
    @staticmethod
    def _positive_divisor(number):

        divisors = []

        for i in range(1,number):
            if number % i == 0:
                divisors.append(i)
        
        return divisors

    @classmethod
    def _aliquot_sum(cls, number):

        return sum(cls._positive_divisor(number))
    
    @classmethod
    def classify(cls, number):

        if number < 1:
            raise ValueError('Input must be a positive integer')
        
        aliquot_sum = cls._aliquot_sum(number)
        
        if aliquot_sum == number:
            return 'perfect'
        elif aliquot_sum > number:
            return 'abundant'
        else:
            return 'deficient'


