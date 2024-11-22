# Exercise 13

```python
class Tree:
    def __init__(self):
        self.type = "Generic Tree"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"
```

When an instance of `Pine` is created the `type` attribute would have the string `Pine Tree`. This is because even though the `Tree` class is being inherited and initalised within the `__init__` method for the `Pine` class, the instance variable `type` is being reassigned to the value `"Pine Tree"` on line 8.