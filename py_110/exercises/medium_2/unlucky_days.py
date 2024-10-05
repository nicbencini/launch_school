"""
Some people believe that Fridays that fall on the 13th day of the month are unlucky days. Write a function that takes a year as an argument and 
returns the number of Friday the 13ths in that year. You may assume that the year is greater than 1752, which is when the United Kingdom 
adopted the modern Gregorian Calendar. You may also assume that the same calendar will remain in use for the foreseeable future.

Problem:
To write a function that takes a year as an argument and returns the number of Friday the 13ths as an integer.

Rules:
# The year is greater than 1752
# Will be used for the forseeable future

Examples:
print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True

Data:
Input: Integer representing year 
Output: Integer representing number of friday the 13ths

Algorithm:
# Create Friday the 13th counter
# Get day of the week of first day of the year
# Get first friday:
    # Create dictionary of days of the week up till Friday
    # Get new years day and see how many days to the first friday
    # Modify date to the first firsday and return date time
# Cycle through fridays in the year and age the date
# If the date is 13 then add 1 to the counter



"""
from datetime import datetime as dt
from datetime import timedelta

days_to_friday = {'Monday': 4,
                  'Tuesday': 3,
                  'Wednesday': 2,
                  'Thursday': 1,
                  'Friday': 0,
                  'Saturday': 6,
                  'Sunday' : 5

}

def first_friday(year):

    date = dt.strptime(f'January 01, {year}', '%B %d, %Y')

    new_years_day = date.strftime('%A')

    days_remaining = days_to_friday[new_years_day]

    return dt.strptime(f'January {1+days_remaining:2d}, {year}', '%B %d, %Y')


def friday_the_13ths(year):

    friday_13th_count = 0

    friday_date = first_friday(year)

    while True:

        if friday_date.strftime('%d') == '13':
            friday_13th_count += 1

        friday_date = friday_date + timedelta(days=7)

        if friday_date.strftime('%Y') != f'{year}':
            break

    return friday_13th_count

    
    

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True