import re

string = """
<h1>Main Heading</h1>
<h1>Another Main Heading</h1>
<h1>ABC</h1> <p>Paragraph</p> <h1>DEF</h1><p>Done</p>
"""

print(re.findall(r'<h1>([a-z]| )*</h1>', string, flags=re.IGNORECASE|re.MULTILINE))