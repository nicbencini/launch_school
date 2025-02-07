"""
Write some code that converts modern decimal numbers into their Roman number equivalents.

The Romans were a clever bunch. They conquered most of Europe and ruled it for hundreds of years. They invented concrete and straight roads and even bikinis. One thing they never discovered though was the number zero. This made writing and dating extensive histories of their exploits slightly more challenging, but the system of numbers they came up with is still in use today. For example the BBC uses Roman numerals to date their programmes.

The Romans wrote numbers using letters - I, V, X, L, C, D, M. Notice that these letters have lots of straight lines and are hence easy to hack into stone tablets.

Copy Code
 1  => I
10  => X
 7  => VII
 
There is no need to be able to convert numbers larger than about 3000. (The Romans themselves didn't tend to go any higher)

Wikipedia says: Modern Roman numerals ... are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero.

To see this in practice, consider the example of 1990. In Roman numerals, 1990 is MCMXC:

Copy Code
1000=M
900=CM
90=XC
2008 is written as MMVIII:

Copy Code
2000=MM
8=VIII

problem: TO write a class that converts a decimal number to a roman number

examples: 1789 MCC

rules: no need to convert numbers larger than 3000

data: 

RomanNumeral (Class):
    to_roman() (method)

algorithm:
    - craete result_string variable for ouput number
    - break down number into components:
        use % 10 to get integers and subtract from numner
            - use number convertor and append result to result_string variable
        use % 100 to get 10's and subtract from numner
            - use number convertor and append result to result_string variable
        use % 1000 to get 100's and subtract from numner
            - use number convertor and append result to result_string variable
        use % 10000 to get 1000's and subtract from numner
            - use number convertor and append result to result_string variable

    
    def number_convertor(number, range, markers ,increment)
        if number is <= range[0] + increment*3:
            for range in (range[0] + increment*3) += marker[0]
        if number is > (range[0] + increment*3) but < marker[1]:
            marker[0] + marker[1]
        if number is 5:
            marker[1]

            

"""

def number_convertor(number, num_range, markers, incrament):

    if number <= num_range[0] + incrament * 3:
        return markers[0]+''.join([markers[0] for _ in range(int(number/incrament)-1)])
    



print(number_convertor(7,[5,10],['V','X'],1))


def to_number(input_number):
    pass





