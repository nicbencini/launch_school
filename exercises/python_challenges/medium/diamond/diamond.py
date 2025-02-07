"""
problem:
To create a diamond pattern for the letter provided

rules:
    -the first row contains one 'A'
    -the last row contains one 'A'
    -all rows except first and last have 2 identical letters
    -the diamond is horizontally symmetric
    -the diamond is vertically symmetric
    -the letters form a diamond shape
    -the top half has letters in ascending order
    -the bottom half has letters in descending order

data:
    -Diamond(class):
        -make_diamond(class method)

examples:
    "  A  \n" \
    " B B \n" \
    "C   C\n" \
    " B B \n" \
    "  A  \n"

    1 = 1
    2 = 3
    3 = 5
    4 = 7

algorithm:
    - create list of letters from which to obtain count
    - get count from letters
    - create empty string of spaces based on letter count
        -max row width = (letter count*2 -1) + 2
    - cycle through the list of letters until the target letter is reached and replace 
        the space in the string with the letter based on its location in the diamond
        - index = floor(max_row_length /2)
        - index = floor(previous index/2)
        - index from back = -1 - index
    - add to final output string
"""
import math

class Diamond:

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @classmethod
    def make_diamond(cls, letter):

        top_triangle = []
        bottom_triangle = []
        
        index = cls.alphabet.index(letter)
        max_row_width = ((index)*2)+1
        template = list(' '*max_row_width)

        r_index = 0

        for i in range(index+1):
            row = template.copy()
            
            if i == 0:
                r_index = math.floor(max_row_width/2)
            else:
                r_index = r_index -1
            
            l_index = -1 - r_index
            
            row[r_index] = cls.alphabet[i]
            row[l_index] = cls.alphabet[i]

            output_row = ''.join(row)+'\n'
            
            top_triangle.append(output_row)

            if i < index:
                bottom_triangle.append(output_row)
        
        return ''.join(top_triangle + bottom_triangle[::-1])

