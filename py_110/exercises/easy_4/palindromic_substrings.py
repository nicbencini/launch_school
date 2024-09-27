"""
Write a function that returns a list of all palindromic substrings of a string. 
That is, each substring must consist of a sequence of characters that reads the same forward and backward. 
The substrings in the returned list should be sorted by their order of appearance in the input string. Duplicate substrings should be included multiple times.

You may (and should) use the substrings function you wrote in the previous exercise.

For the purpose of this exercise, you should consider all characters and pay attention to case; that is, 'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are not. 
In addition, assume that single characters are not palindromes.

Problem:
Input: String
Output: palindromic substrings

Rules:
- Substrings sorted by order of appearance
- Palidrome reads same forwards and backwards
- Case should be taken into account
- Single characters are not palindromes

Algoritm:
- Use substrings function to extract all substrings
- Cycle through substrings and if len of string < 1 then skip
- Create sub function for checking if the string is a palindrome:
    -If reverse of word is equal to word then it is a palindrome
- If string is a palindrome append to output list

"""
def is_palindrome(input_string):
    if input_string == ''.join(reversed(list(input_string))) and len(input_string) > 1:
        return True
    
    return False

def leading_substrings(input_string):
    return [input_string[0:i+1] for i in range(len(input_string))]

def substrings(input_string):
    
    output_list = []

    for i in range(len(input_string)):
        new_string = input_string[i::]
        output_list.extend(leading_substrings(new_string))
    
    return output_list

def palindromes(input_string):
    substring_list = substrings(input_string)

    return [strng for strng in substring_list if is_palindrome(strng)]



print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True


