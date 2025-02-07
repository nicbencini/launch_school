"""
Implement octal to decimal conversion. Given an octal input string, your program should produce a decimal output. 
Treat invalid input as octal 0. Note that the only valid digits in an octal number are 0, 1, 2, 3, 4, 5, 6, and 7.

Note: Implement the conversion yourself. Don't use any built-in or library methods that perform the necessary conversions for you. 
In this exercise, the code necessary to perform the conversion is what we're looking for.

About Octal (Base-8)

Decimal is a base-10 system. A number 233 in base 10 notation can be understood as a linear combination of powers of 10:

The rightmost digit gets multiplied by 10^0 = 1
The next digit gets multiplied by 10^1 = 10
The digit after that gets multiplied by 10^2 = 100
The digit after that gets multiplied by 10^3 = 1000
...
The n_th_ digit gets multiplied by 10^n-1.
All of these values are then summed.
Thus:

Copy Code
  233 # decimal
= 2*10^2 + 3*10^1 + 3*10^0
= 2*100  + 3*10   + 3*1
Octal numbers are similar, but they use a base-8 system. A number 233 in base 8 can be understood as a linear combination of powers of 8:

The rightmost digit gets multiplied by 8^0 = 1
The next digit gets multiplied by 8^1 = 8
The digit after that gets multiplied by 8^2 = 64
The digit after that gets multiplied by 8^3 = 512
...
The n_th_ digit gets multiplied by 8^n-1.
All of these values are then summed.
Thus:

Copy Code
  233 # octal
= 2*8^2 + 3*8^1 + 3*8^0
= 2*64  + 3*8   + 3*1
= 128   + 24    + 3
= 155

problem:
write a program that produces a decimal output from an octal

rules:
- octal number are 0, 1, 2, 3, 4, 5, 6, and 7
- invalid octals should be treated as octal 0
- decimal digits get multiplied by 10^n-1
- octal digits get multiplied by 8^n-1

examples:
    130 = 1*(8^2) + 3*(8^1) + 0*(8^0) = 88

data:

Octal(class):
    - init variables: number
    - to_decimal(method)
        - returns integer

algorithm:
    -reverse string
    -cycle through characters in string:
        - convert character to integer
        - if integere is < 0 or larger than 7 return 0
        - multiply integer by  8^n-1
        - add to output_list
    -return sum of output_list

"""

class Octal:

    def __init__(self, octal_string):

        self._octal_string = octal_string
    
    def to_decimal(self):

        ordered_string = self._octal_string[::-1]
        converted_numbers = []

        for i, character in enumerate(ordered_string):

            if not character.isdigit():
                return 0

            oct_number = int(character)
            if oct_number >=8 or oct_number < 0:
                return 0                   
        
            
            converted_numbers.append(oct_number * (8**i))

        return sum(converted_numbers)



