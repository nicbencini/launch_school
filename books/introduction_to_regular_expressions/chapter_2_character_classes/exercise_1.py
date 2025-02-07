import re

string ="""
Kitchen Kaboodle
Reds and blues
kitchen Servers
"""

print(len(re.findall(r'[K,k,s]', string)))