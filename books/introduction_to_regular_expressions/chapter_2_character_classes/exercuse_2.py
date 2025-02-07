import re

string = """
My cats, Butterscotch and Pudding, like to
sleep on my cot with me, but they cut my sleep
short with acrobatics when breakfast time rolls
around. I need a robotic cat feeder.
"""

print(len(re.findall(r'[cb][aou][t]', string, flags=re.I)))