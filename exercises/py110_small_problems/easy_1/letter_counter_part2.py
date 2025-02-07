"""
Modify the word_sizes function from the previous exercise to exclude non-letters when determining word size. 
For instance, the word size of "it's" is 3, not 4.

Problem
Input: Strings continaing a mixture of alphabetical and non alphabetical characters.
Output: dictionary

Explicit Rules:
- Input is string of words seperated by spaces
- There can be zero or more workds
- words consist of any non-space character

Implicit Rules:
- 

Algorithm
- Split input word by ' ' to get a list of words.
- Cylce through list and get the length of each word.
- Calculate word length of alphabetical characters only.
- For each new word length create a key in the dictionary and set the value to 1
- For every other new word of a similar lengh retrieve that key from the dictionary and icrement it by 1


Code
"""

def word_sizes(input_string):
    
    output_dictionary = {}

    if len(input_string) > 0:
        for word in input_string.split(' '):

            key = len([character for character in word if character.isalpha()])
            
            if key not in output_dictionary:
                output_dictionary[key]  = 0        

            output_dictionary[key] += 1

    return output_dictionary

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

