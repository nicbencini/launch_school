"""
The time of day can be represented as the number of minutes before or after midnight. 
If the number of minutes is positive, the time is after midnight. 
If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm). 
Your function should work with any integer input.

You may not use Python's datetime module.
Disregard Daylight Savings and Standard Time and other complications.

Program:
Input: Positive or negative integer
Output: String showing time of day

Example:

125 ==>
Hours = 125//60
Minutes = int(125%60)

Algorithm:
- Check whether integer is positive or negative
- Calcualte number of minutes and hours the integer represents
- Convert this to the time of day by subtracting from 24 if negative
- Return result in correct format

int_format(int, format)
-create string of '0'
-substitute '0' in sting with values form integer
- return string
"""

def format_integer(int, format):

    output = list(format)
    integer_string = str(int)
    for i in range(-1,-len(integer_string), -1):
        output[i] = str(int)[i]
    
    return ''.join(output)
                   

def time_of_day(input_number):
    hours = (abs(input_number)//60)%24
    min = abs(input_number) % 60

    if input_number < 0:
        hours = 23 - hours
        min = 60 - min

    print(f'{hours}:{min}')
    return(f'{hours}:{min}') 



print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
