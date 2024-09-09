"""
Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number 
appears among the first five.

Example 1

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.

Example 2

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.

Program:
Input: 6 integers from user
Output: String

Algorithm:
- Use input function to get 6 values from user.
- Store values in list.
- Check whether the last entery is already in the list and return string
"""

number_1 = input('Enter the 1st number: ')
number_2 = input('Enter the 2nd number: ')
number_3 = input('Enter the 3rd number: ')
number_4 = input('Enter the 4th number: ')
number_5 = input('Enter the 5th number: ')
last_number = input('Enter the last number: ')

number_list = [number_1, number_2, number_3, number_4, number_5]

if last_number in number_list:
    print(f'{last_number} is in {','.join(number_list)}')
else:
    print(f'{last_number} is not in {','.join(number_list)}')