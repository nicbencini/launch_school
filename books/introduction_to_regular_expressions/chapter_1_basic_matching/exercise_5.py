import re

string = """
This line has spaces
This,line,has,commas,
No-spaces-or-commas
"""

print(len(re.findall(r',| ', string)))