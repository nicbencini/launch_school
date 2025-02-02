import re

string = """
reds and blues
the lazy cat sleeps
"""

print(len(re.findall(r'\s\S\S\S\s', string)))