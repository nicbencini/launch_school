"""
As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight. 
If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before 
midnight.

Write two functions that each take a time of day in 24 hour format, and return the number of minutes before 
and after midnight, respectively. Both functions should return a value in the range 0 through 1439.

You may not use Python's datetime module.

Disregard Daylight Savings and Standard Time and other irregularities.

Program:
Input: String
Output: integer represeting minutes

Algorithm:
- Split string into minutes and hours using ':' character.
- Multiply hours by 60 to get number of minutes
- Add values together to get total number of minutes.
- If function is before midnight subtract from 24*60
"""

def after_midnight(time_string):

    values = time_string.split(':')

    hours_value = int(values[0])
    minute_value = int(values[1])

    if hours_value == 24:
        hours_value = 0

    return hours_value*60 + minute_value

def before_midnight(time_string):

    values = time_string.split(':')

    hours_value = int(values[0])
    minute_value = int(values[1])

    if hours_value == 0:
        hours_value = 24

    return 24*60 - hours_value*60 - minute_value


print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
