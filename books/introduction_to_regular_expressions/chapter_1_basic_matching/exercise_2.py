import re

string = """
Henry
perch
golf
"""

print(len(re.findall(r'H', string, flags=re.I)))