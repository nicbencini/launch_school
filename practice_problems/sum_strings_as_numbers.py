"""
Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java

Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.

Problem:
    Return the string representation of the sum of two string integers

Rules:
    - Cannot use int() function
    - Integers are very larger

Examples:
    print(sum_strings("1", "1") == "2")
    print(sum_strings("123", "456") == "579")

    9999 + 9999

    9+9 = 18
    remainder = 1
    string = 8
    9+9+1 =19
    remiander = 1
    string = 9


Data:
    Input_1: first integer as string
    Input_2: second integer as string
    Output: String of integer result

Algorithm:
    - Create output_number list
    - Convert first integer into list of infividual strings and reverse it
    - Convert second integer into list of individual strings and reverse it
    - Create variable called remainder and set it to 0
    - Cycle through longest list of integer
        - check if equivalent item exists in second integer list
            - if so convert the individual item to an int and add them together adn to the remainder
            - if the result > 10 set remainder == 1 and add the result of number % 10 to output_number_list
            - if result < 10 set reminder == 0 and add the result of number % 10 to output_number_list
        - if equivalent item does not exist:
            - add remainder + first integer number to output_number_list
            - set remainder == 0



"""


def sum_strings(str_1, str_2):

    output_number = []

    first_integer = list(str_1)[::-1]
    second_integer = list(str_2)[::-1]

    remainder = 0


    for i in range (max(len(first_integer),len(second_integer))):

        num_1 = 0
        num_2 = 0

        if i < len(first_integer):
            num_1 = first_integer[i]
        
        if i < len(second_integer):
            num_2 = second_integer[i]

        result = int(num_1) + int(num_2) + remainder

        if result >= 10:
            remainder = 1
        else:
            remainder = 0
        
        output_number.append(str(result%10))

    if remainder == 1:
        output_number.append(str(remainder))
    
    output_number = output_number[::-1]

    if len(output_number) > 0 and output_number[0] == '0':
        output_number = output_number[1::]
    
    return ''.join(output_number)

print(sum_strings("1", "1") == "2")
print(sum_strings("123", "456") == "579")

print(sum_strings("9999999999", "456"))
print(9999999999 + 456)
print(sum_strings("9999999999", "456") == str(9999999999 + 456))

print(sum_strings("0", "0"))