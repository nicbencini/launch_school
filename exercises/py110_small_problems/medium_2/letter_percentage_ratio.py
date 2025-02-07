"""
Write a function that takes a string and returns a dictionary containing the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.


Input: String
Output: Dictionary

Rules:
# All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively.
# Each value should be rounded to 2 decimal points
# String will always contain at least one character

Algorithm:
# Create empty dictionary with keys as requried
# Cycle through each character in the word
# Use if statment to check whether the character is lower, upper or neither
# Append result to a counter
# when loop is done calculate percentage and store in dictionary as sting
# Return dictionary


"""

def letter_percentages(input_string):

    upper_counter = 0
    lower_counter = 0
    neither_counter = 0


    for character in input_string:
        if character.isupper():
            upper_counter += 1
        elif character.islower():
            lower_counter += 1
        else:
            neither_counter +=1


    result = {
        'lowercase': f'{(lower_counter/len(input_string) * 100):.2f}',
        'uppercase': f'{(upper_counter/len(input_string) * 100):.2f}',
        'neither': f'{(neither_counter/len(input_string) * 100):.2f}'
    }

    return result

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}

print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)


