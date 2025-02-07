"""
Write a program that can calculate the Hamming distance between two DNA strands.

A mutation is simply a mistake that occurs during the creation or copying of a nucleic acid, 
in particular DNA. Because nucleic acids are vital to cellular functions, mutations tend to 
cause a ripple effect throughout the cell. Although mutations are technically mistakes, a very 
rare mutation may equip the cell with a beneficial attribute. In fact, the macro effects of
evolution are attributable to the accumulated result of beneficial microscopic mutations over many generations.

The simplest and most common type of nucleic acid mutation is a point mutation, which replaces one 
base with another at a single nucleotide.

By counting the number of differences between two homologous DNA strands taken from different genomes 
with a common ancestor, we get a measure of the minimum number of point mutations that could have 
occurred on the evolutionary path between the two strands.

This is called the Hamming distance.

Copy Code
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^
The Hamming distance between these two DNA strands is 7.

The Hamming distance is only defined for sequences of equal length. If you have two sequences 
of unequal length, you should compute the Hamming distance over the shorter length.


problem: to create a function that calculates the point mutation between two different DNA strands

rules:

        - if two letters in equivalent positions are not equal
        - if one string is longer than the other all additional letters should be counted
        - if both strings are empty hamming distance is zero
        - if longer string is a repetition of the shorter string then the hamming distance is not counted

examples:
            GAGCCTACTAACGGGAT
            CATCGTAATGACGGCCT
            ^ ^ ^  ^ ^    ^^

            AGGCTAGCGGTAGGAC
            AAACTAGGGGAAACTA
             ^^    ^  


data structure:

    - DNA (class): initialized with a string representing a DNA sequence
        - variables: dna_string
        - hamming_distance (method): calculates the hamming distance between the DNA and another string

algorithm:
    - check whether strings are both empty if so return 0
    - check whether strings are the same length:
        - if True:
                - cycle through each letter in the string and check wether letters match
        - if False:
                - cycle through each letter in shorter string
                - check whether letters match
    - return count of mismatched letters

"""

class DNA:

    def __init__(self, dna_string):
        self._dna_string = dna_string
    
    def hamming_distance(self, other):

        hamming_distance_counter = 0

        string_list = [self._dna_string, other]
        sorted_strings = sorted(string_list, key=len)
        
        for i, _ in enumerate(sorted_strings[0]):

            if sorted_strings[0][i] != sorted_strings[1][i]:
                hamming_distance_counter +=1
        
        return hamming_distance_counter

