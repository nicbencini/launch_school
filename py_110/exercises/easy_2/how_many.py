"""
Write a function that counts the number of occurrences of each element in a given list. 
Once counted, print each element alongside the number of occurrences. 
Consider the words case sensitive e.g. ("suv" != "SUV").

Program:

Input: List
output: print String counting number of occurances

Rules:
- Take into account case

Algorithm:
-Create empty dictionary to store the word count
- cycle though items in list and using the word as a key create a count as the value
- increase the count when a duplicate item is found
- return the results as a string

"""

def count_occurrences(input_list):

    output_dictionary = {}

    for item in input_list:
        if item not in output_dictionary:
            output_dictionary[item] = 0
        
        output_dictionary[item] += 1
    
    for key in output_dictionary:
        print(f'{key} ==> {output_dictionary[key]}')
    
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# your output sequence may appear in a different sequence
#car => 4
#truck => 3
#SUV => 1
#motorcycle => 2