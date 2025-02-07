"""
Write a program that takes a word and a list of possible anagrams and 
selects the correct sub-list that contains the anagrams of the word.

For example, given the word "listen" and a list of candidates like "enlists", "google", 
"inlets", and "banana", the program should return a list containing "inlets". 
Please read the test suite for the exact rules of anagrams.

probelm:
write a program that takes a word and a list of possible anagrams and selects the correct
sub_list that contains the anagrams of the word.

rules:
- must retiurn a list of all possible anagrams
- returns an empty list if not anagram found
- case sensitive
- duplicates are counted
- if first letter is capital then first letter of anagram must be capital

Data:

Anagram(class) takes word as input
    - match(method) takes list of words as input

algorithm:
    - check if first letter in the list is capital
    - sort the word alphabetically
    - cycle through list of provided words to check against and sort words alphabetically
        - if there is a match check if capitalization matches provided word
        - if both checks pass add it to the output list


"""

class Anagram:

    def __init__(self, word):
        self._word = word
    

    @staticmethod
    def is_capitol(input_letter):
        if input_letter.upper() == input_letter:
            return True
        return False

    
    def match(self, word_list):

        output_list = []

        for wrd in word_list:

            if (''.join(sorted(wrd.lower())) == ''.join(sorted(self._word.lower())) and 
            self.is_capitol(wrd[0]) == self.is_capitol(self._word[0]) and
            self._word != wrd
            ):
                output_list.append(wrd)
        
        return output_list


def is_capitol(input_letter):
    if input_letter.upper() == input_letter:
        return True
    return False





