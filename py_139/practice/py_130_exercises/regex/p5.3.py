import re

string = """
What's up, doc?
Say what? No way.
?
Who? What? Where? When? How?
"""

print(re.findall(r'.+\?$', string, flags=re.MULTILINE))