import re

string = """
blueberry
blackberry
black berry
strawberry
"""

print(len(re.findall(r'(black|blue)berry',string)))