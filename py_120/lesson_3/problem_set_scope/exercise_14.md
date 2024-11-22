# Exercise 14

```python
class A:
  def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)
```

When run the code will raise an `AttributeError` because the `A` class is not initialised in the `B` class `__init__` method so the instance variable `var_a` is not created. 