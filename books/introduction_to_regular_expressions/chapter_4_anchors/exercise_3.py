import re

string ="""
reds and blues
The lazy cat sleeps.
The number 623 is not a word. Or is it?
"""

print(len(re.findall(r'\b[a-z][a-z][a-z]\b', string, flags=re.IGNORECASE)))