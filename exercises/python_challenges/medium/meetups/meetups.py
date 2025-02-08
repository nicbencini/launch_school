"""
Meetups are a great way to meet people who share a common interest. Typically, meetups happen monthly on the same day of the week. For example, a meetup's meeting may be set as:

The first Monday of January 2021
The third Tuesday of December 2020
The teenth Wednesday of December 2020
The last Thursday of January 2021

In this program, we'll construct objects that represent a meetup date. Each object takes a month number (1-12) and a year (e.g., 2021). Your object should be able to determine 
the exact date of the meeting in the specified month and year. For instance, if you ask for the 2nd Wednesday of May 2021, the object should be able to determine that the meetup 
for that month will occur on the 12th of May, 2021.

The descriptors that may be given are strings: 'first', 'second', 'third', 'fourth', 'fifth', 'last', and 'teenth'. The case of the strings is not important; that is, 'first' and 
'fIrSt' are equivalent. Note that "teenth" is a made up word. There was a meetup whose members realized that there are exactly 7 days that end in '-teenth'. Therefore, it's 
guaranteed that each day of the week (Monday, Tuesday, ...) will have exactly one date that is the "teenth" of that day in every month. That is, every month has exactly one 
"teenth" Monday, one "teenth" Tuesday, etc. The fifth day of the month may not happen every month, but some meetup groups like that irregularity.

The days of the week are given by the strings 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', and 'Sunday'. Again, the case of the strings is not important.

problem:
to determine the date of a meetup in the given month and year

rules:
- initialized with a year and month
- takes a day followed by a descriptor
- return a date 

Data structure:
    Meetup (class):
        -initialized with year, month
        - day (method) takes a day and decriptor and outputs a date
    
Algorithm:
    - create a dictionary for all possible input words with a corresponding index
    - use date time to generate all possible dates within the month for the day given
    - select the relevant date based on the descriptor provided
    - return that date


"""
import datetime

class Meetup:

    DESCRIPTORS = {'first':0,
                   'second':1,
                   'third':2,
                   'fourth':3,
                   'last':-1
                   }

    def __init__(self, year, month):
        self._year = year
        self._month = month
    
    def day(self, day, descriptor):

        descriptor = descriptor.lower()

        dates = []
        
        date = datetime.date(self._year, self._month, 1)
        
        while True:

            if date.month != self._month:
                break

            if date.strftime('%A') == day:
                dates.append(date)

            date += datetime.timedelta(days=1)
        
        if descriptor in self.DESCRIPTORS.keys():
            return dates[self.DESCRIPTORS[descriptor]]
        
        elif descriptor == 'teenth':
            for date in dates:
                if 12 < date.day < 20:
                    return date 
                
        elif descriptor == 'fifth':
            if len(dates) == 5:
                return dates[4]
            
        else:
            return None





        
