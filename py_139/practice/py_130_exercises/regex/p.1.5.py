
import re

string = """
blueberry
blackberry
black berry
strawberry
"""

print(re.findall(r'(blue|black)berry', string))