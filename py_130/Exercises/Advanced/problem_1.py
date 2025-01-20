"""

Write a program that prints the longest sentence in a string based on the number of words. You should also print the number of words in the longest sentence.

Sentences may end with periods (.), exclamation points (!), or question marks (?). You should treat any sequence of characters that are not spaces or sentence-ending 
characters as a word. Thus, -- should count as a word. Log the longest sentence and its word count. Pay attention to the expected output, and be sure you preserve the 
punctuation from the end of the sentence.

Note that this problem is about manipulating and processing strings. As such, every detail about the string matters (e.g., case, punctuation, tabs, spaces, etc.).


problem:
    - Write a program that PRINTS the longest sentence in a string based on the number of words.
    - You should also print the number of words in the longest sentence

Rules:
    - Sentences end with (.)(!)(?)
    - Any sequence of characters that are not spaces or sentence ending are words
    - Log longest sentence by its word count
    - Preserve puntuation from end of sentence

Examples:


Data:
    Input: string
    Output: print of longest sentance and number of words


Algorithm:
    - Split string into sentences:
        - split string at '.'
            -cycle through list and re-split the items in the list at '!'
                -cycle through list and re-split the items in the list at '?'
    
    - for each item in the sentence list split them into words at ' '.
    - count length of list and return item with longest word count using sorted

"""

def split_at(string_list, seperator):

    output = []

    for sentence in string_list:
        if seperator in sentence:
            output.extend([substring + seperator for substring in 
                           sentence.split(seperator) if 
                           substring not in '.?!'])
        else:
            output.append(sentence)
    
    return output

def count_words(sentence):

    sentence.lstrip()

    words = [string for string in sentence.split(' ') if len(string) > 0]

    return len(words)

def process_sentence(callback, iter, sentence):

    output = [sentence]

    for item in iter:
        output = callback(output, item)
    
    return output

def longest_sentence(input_string):

    sentence_list = process_sentence(split_at, '!?.', input_string)

    longest_sentence = sorted(sentence_list,key=count_words)[-1]

    print(longest_sentence + '\n\n' + 
          f'The longest sentence has {count_words(longest_sentence)} words.\n')


long_text = (
    'Four score and seven years ago our fathers brought forth on this '
    'continent a new nation, conceived in liberty, and dedicated to the '
    'proposition that all men are created equal. Now we are engaged in a '
    'great civil war, testing whether that nation, or any nation so '
    'conceived and so dedicated, can long endure. We are met on a great '
    'battlefield of that war. We have come to dedicate a portion of that '
    'field, as a final resting place for those who here gave their lives '
    'that that nation might live. It is altogether fitting and proper that '
    'we should do this.'
)

longer_text = long_text + (
    'But, in a larger sense, we can not dedicate, we can not consecrate, '
    'we can not hallow this ground. The brave men, living and dead, who '
    'struggled here, have consecrated it, far above our poor power to add '
    'or detract. The world will little note, nor long remember what we say '
    'here but it can never forget what they did here. It is for us the '
    'living, rather, to be dedicated here to the unfinished work which '
    'they who fought here have thus far so nobly advanced. It is rather '
    'for us to be here dedicated to the great task remaining before us -- '
    'that from these honored dead we take increased devotion to that '
    'cause for which they gave the last full measure of devotion -- that '
    'we here highly resolve that these dead shall not have died in vain '
    '-- that this nation, under God, shall have a new birth of freedom -- '
    'and that government of the people, by the people, for the people, '
    'shall not perish from the earth.'
)

longest_sentence(long_text)
# Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.
#
# The longest sentence has 30 words.

longest_sentence(longer_text)
# It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
#
# The longest sentence has 86 words.

longest_sentence("Where do you think you're going? What's up, Doc?")
# Where do you think you're going?
#
# The longest sentence has 6 words.

longest_sentence("To be or not to be! Is that the question?")
# To be or not to be!
#
# The longest sentence has 6 words.