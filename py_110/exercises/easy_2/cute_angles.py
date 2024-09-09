"""
Write a function that takes a floating point number representing an angle between 0 and 360 degrees 
and returns a string representing that angle in degrees, minutes, and seconds. You should use a degree symbol (°) 
to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. 
There are 60 minutes in a degree, and 60 seconds in a minute.

Note: You can use the following constant to represent the degree symbol:

Program:

Input:Float 
Output: String

Rules:
- input will be float between 0 and 360
- 60 seconds in minute
- 60 minutes in degree

Examples:

4.4 = 
degrees = 4
minutes = 0.455 * 60 = 27.3
seconds = 0.3 * 60

Algorithm:
- Use modulus function to get number of degrees by 
- Use remainder to calcuate minutes
- Use remainder of minutes to calculate seconds
- output result as string using f string

"""

def dms(input_number):
    
    degrees = input_number-input_number%1
    minutes_decimal = (input_number%1) * 60 
    seconds_decimal = minutes_decimal%1 * 60

    print(f'{int(degrees)}\u00B0{int(minutes_decimal)}\'{int(seconds_decimal)}')
    

DEGREE = "\u00B0"


# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
