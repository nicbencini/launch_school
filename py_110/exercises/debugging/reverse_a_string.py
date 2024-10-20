"""
You have a function that is supposed to reverse a string passed as an argument. However, it's not producing the expected output. Explain the bug, and provide a solution.

"""

def reverse_string(string):

    output_string = ''

    for char in string:
        output_string = char + output_string

        print(output_string)

    
    
    return output_string

print(reverse_string("hello") == "olleh")

# The code was not working because the for loop on line 10 was appending the characters to the orginal string rather than to an empty string. This resulted in the reversed string
# being concatenated to the original string which produced an incorrect result.