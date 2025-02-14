import re

string = """
Henry
perch
golf
"""

print(re.findall(r'\b.*h.*\b', string, flags=re.IGNORECASE))