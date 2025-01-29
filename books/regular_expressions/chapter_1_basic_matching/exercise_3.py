import re

string = """
snapdragon
bearded dragon
dragoon
"""

print(len(re.findall(r'dragon', string)))