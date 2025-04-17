import re

text = """"Frequently."

"How often?"

"Well, some hundreds of times."
"""

print(f'<p>{re.sub(r"(\n\n)", '</p>\n\n<p>', text).strip()}</p>')