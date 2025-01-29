import re

string = """
banana
orange
pineapples
strawberry
raspberry
grappler
"""

print(len(re.findall(r'banana|orange|apple|strawberry', string)))