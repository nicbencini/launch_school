import re

string = """
Kitchen Kaboodle
Reds and blues
kitchen Servers
"""

print(re.findall(r'[Kks]', string))