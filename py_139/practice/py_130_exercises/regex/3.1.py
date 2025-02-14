import re

string = """
reds and blues
the lazy cat sleeps
"""

print(re.findall(r'\b...\b', string))