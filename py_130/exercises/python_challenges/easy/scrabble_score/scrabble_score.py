"""
Write a program that, given a word, computes the Scrabble score for that word.

Letter Values. You'll need the following tile scores:

Letter	Value
A, E, I, O, U, L, N, R, S, T	1
D, G	2
B, C, M, P	3
F, H, V, W, Y	4
K	5
J, X	8
Q, Z	10
How to Score

Sum the values of all the tiles used in each word. For instance, lets consider the word CABBAGE which has the following letters and point values:

3 points for C
1 point for each A (there are two)
3 points for B (there are two)
2 points for G
1 point for E
Thus, to compute the final total (14 points), we count:

3 + 2*1 + 2*3 + 2 + 1
=> 3 + 2 + 6 + 3
=> 5 + 9
=> 14



algorithm:
    
"""

import re

class Scrabble:

    SCORE_DICTIONARY = {
        'AEIOULNRST':1,
        'DG':2,
        'BCMP':3,
        'FHVWY':4,
        'K':5,
        'JX':8,
        'QZ':10
    }

    def __init__(self, word):
        self._word = word

    def score(self):

        total_score = 0

        if self._word == None:
            return total_score

        cleaned_word = re.sub(r'\s','',self._word)

        for character in cleaned_word:
            for key in self.SCORE_DICTIONARY.keys():
                if character.upper() in key:
                    total_score += self.SCORE_DICTIONARY[key]
        
        return total_score

    @staticmethod
    def calculate_score(word):
        return Scrabble(word).score()
    




