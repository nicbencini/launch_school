import re

string = """
Kx
BlacK
kelly
"""

print(re.findall(r'\b.*K.*\b', string))