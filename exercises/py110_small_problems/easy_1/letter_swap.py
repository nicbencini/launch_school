"""
Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and that the string will always contain at least one word. 
You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, 
or repeated spaces.

Problem
Input: String of words seperated by spaces
Output: String

Explicit Rules:
- Words contain at least one letter
- String contain at least one word
- Strings only contain words and spaces
- No leading or trailing or repeated spaces

Algorithm:
- Split words in string by ' ' to obtain list of words
- for each word in string get first and last character
- Use f string to swap first and last character
- Return string

Code

"""

def swap(input_string):
    
    output_words = []

    for word in input_string.split(' '):
       word_list = list(word)
       word_list[0], word_list[-1] = word_list[-1] , word_list[0]

       output_words.append(''.join(word_list))


    return ' '.join(output_words)

      

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
