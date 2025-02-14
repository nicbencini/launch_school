import re

string = """
https://launchschool.com/
http://mail.google.com/mail/u/0/#inbox
htpps://example.com
Go to http://launchschool.com/
https://user.example.com/a.cgi?a=p&c=0 hello
    https://launchschool.com/
"""

print(re.findall(r'^\s*https*://\S*\s*$', string, flags=re.MULTILINE))