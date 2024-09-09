"""
Write a function that takes a string consisting of zero or more space-separated words 
and returns a dictionary that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.

Problem
Input: String of words seperated by spaces
Output: Dictionary with the key being the length of the word and the value being the number of words of that length

Explicit Rules:
- Input is string of words seperated by spaces
- There can be zero or more workds
- words consist of any non-space character

Implicit Rules:
- 

Algorithm
- Split input word by ' ' to get a list of words.
- Cylce through list and get the length of each word.
- For each new word length create a key in the dictionary and set the value to 1
- For every other new word of a similar lengh retrieve that key from the dictionary and icrement it by 1

Code
"""

# All of these examples should print True

def word_sizes(input_string):
    
    output_dictionary = {}

    if len(input_string) > 0:
        for word in input_string.split(' '):

            key = len(word)

            if key not in output_dictionary:
                output_dictionary[key]  = 0        

            output_dictionary[key] += 1

    return output_dictionary




string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})


