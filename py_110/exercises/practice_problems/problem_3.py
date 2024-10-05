"""
Create a function that takes a string argument and returns a copy of the string with every second 
character in every third word converted to uppercase. Other characters should remain the same.

Problem:
    - Create a function that takes a string argument and returns a copy of the string with every second character in every third word converted to uppercase

Rules:
    -only every third words affected
    -only every second character
    -all other words not affected

Examples:
    original = 'Lorem Ipsum is simply dummy text of the printing world'
    expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'


    original = 'It is a long established fact that a reader will be distracted'
    expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'


    original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
    expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"

Data:
    Input: string
    Output: modified string

Algorithm:
    - split string into list of words at spaces
    - cycle through list of words
        - if the word is a third word
            - if the character is a second character make uppercase and modify list
    - join words back in mutated list to form sentence
    - return sentence

"""

def modify_word(word_):
    return ''.join([character.upper() if index %2 != 0 else character 
                                      for index,character in enumerate(word_)])

def to_weird_case(sentence):
    word_list = sentence.split(' ')

    return ' '.join([modify_word(word) if (index + 1)%3 == 0 else word 
                                       for index,word in enumerate(word_list)])


original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)