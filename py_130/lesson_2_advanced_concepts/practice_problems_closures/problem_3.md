What will this code print? Try to answer without running the code:

Copy Code

```python
from functools import partial

def greet(name, greeting):
    return f"{greeting}, {name}!"

say_hello_to = partial(greet, greeting="Hello")
print(say_hello_to(name="Alice"))  # What will this print?
```



### Answer

