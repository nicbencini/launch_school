import re

def fields(input_string):

    return re.split(r' *, *|\s+', input_string)


print(fields("Pete,201,Student"));    # ['Pete', '201', 'Student']
print(fields("Pete \t 201   ,  TA")); # ['Pete', '201', 'TA']
print(fields("Pete \t 201"));         # ['Pete', '201']
print(fields("Pete \n 201"));         # ['Pete', '\n', '201']