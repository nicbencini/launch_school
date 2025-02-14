import re

string = """
banana
orange
pineapples
strawberry
raspberry
grappler
"""

print(re.findall(r'(banana|orange)', string))

