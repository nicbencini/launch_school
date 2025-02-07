"""
Write a program that, given a natural number and a set of one or more other numbers, can find the sum of all the multiples of the numbers in the set that are less than the first number. 
If the set of numbers is not given, use a default set of 3 and 5.

For instance, if we list all the natural numbers up to, but not including, 20 that are multiples of either 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, and 18. 
The sum of these multiples is 78.

problem:
write a program that, 
given a natural number and a set of one or more other numbers, 
can find the sum of [all the multiples of number in the set]
that are less than the first number

rules:
    - if set not given use a defaults ser of 3 and 5

examples:

    20 --> 3,5,6,9,10,12,15,18 --> 78

Data:

    SumOfMultiples (class):
        - set of numbers(instance variable)
        - sum_up_to (method)

Algorithm:

    -if set of numbers not provided use {3,5}
    - cycle through all numbers smaller than number provided:
        - check if number is a multiple of any number in the set
        - if so add to output number
    -return output_number

"""

class SumOfMultiples:

    _multiples_set = {3,5}

    def __init__(self, *args):
        self.instance_multiples_set = (set(args))
    
    
    @classmethod
    def sum_up_to(cls, number):

        result = []

        for i in range (1, number):
            for multiple in cls._multiples_set:
                if i%multiple == 0:
                    result.append(i)

        return sum(set(result))

    def to(self, number):

        result = []

        for i in range (1, number):
            for multiple in self.instance_multiples_set:
                if i%multiple == 0:
                    result.append(i)

        return sum(set(result))


print(SumOfMultiples.sum_up_to(4))
