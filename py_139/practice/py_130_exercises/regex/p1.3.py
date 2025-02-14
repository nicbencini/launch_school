import re

string = """
snapdragon
bearded dragon
dragoon
"""

print(re.findall(r'dragon', string, flags=re.IGNORECASE))