"""
Take the number 735291 and rotate it by one digit to the left, getting 352917. 
Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. 
Keep the first two digits fixed in place and rotate again to get 321759. Keep the first 
three digits fixed in place and rotate again to get 321597. 

Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. 
The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument and returns the maximum rotation of that integer. 
You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.

Input: number
Output: rotated number

Examples:

735291
352917 -> first digit becomes last digit
3_29175 -> second digit becomes last digit
32_1759 -> third digit becomes last digit
321_597 -> fourth digit becomes last digit
3215_79 -> fifth digit becomes last digit

Algorithm:
# create sub algorithm to rotate list
    # slice list at first item and append it to the end
# create sub algorithm that rotates list at a given index:
    # slice list at that index and rotate back portion of list
    # concatenate two sliced lists back together
# convert number to string
# for range(0-len(string)) use sub algorithm to rotate the list at the given range index
# convert list back to string then to integer and return


"""

def rotate_string(lst):
    return lst[1::] + lst[0]


def rotate_at_index(string, index):

    string_beginning = string[:index]
    string_end = string[index::]

    return string_beginning + rotate_string(string_end)


def max_rotation(number):
    
    number_string = str(number)

    for index in range(len(number_string)-1):

        number_string = rotate_at_index(number_string, index)
    
    return int(number_string)


print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True
