"""
Write a function that takes a string as an argument and returns that string with every occurrence of a 
"number word" -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

You may assume that the string does not contain any punctuation.

Problem:
Input: String
Output: String with number words converted to digits

Rules:
string does not contain punctuation

Algorithm:
# Create dictionary relating the wordnumber to the digit
# Split sting at spaces to obtain a list of the words
# cycle through the list of the words and check wether it is in the dictionary, 
# if is return the associated digit otherwise return the word

"""


def word_to_digit(input_sentence):

    number_words = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9',
        'zero':'0'

    }

    words = input_sentence.split(' ')

    output_words = [word if word not in number_words.keys() else number_words[word] for word in words]

    return ' '.join(output_words)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True
