"""
Write a program that will take a string of digits and return all the possible consecutive 
number series of a specified length in that string.

For example, the string "01234" has the following 3-digit series:

012
123
234
Likewise, here are the 4-digit series:

0123
1234
Finally, if you ask for a 6-digit series from a 5-digit string, you should throw an error.

problem:
write a program that will take a string of digits and return all the possible consecutive
number series of a specified length in that string

rules:
    - if larger number then series length is specified then value error should be returned
    - input is a string


algorithm:
    - cycle through characters 
    - check whether index + splice is longet then string length
    - if not return splice and append to output list


"""

class Series:

    def __init__(self, number_string):
        self._number_string = number_string
    
    def slices(self, slice_length):

        if slice_length > len(self._number_string):
            raise ValueError

        slice_list = []

        for i in range(len(self._number_string)):
            if (i + slice_length) < (len(self._number_string) + 1):

                character_list = [int(character) for character in self._number_string]
                
                slice_list.append(character_list[i:i + slice_length])
        
        return slice_list

