# Exercise 10

```python

class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        self.color = color

birdie = Sparrow("sparrow", "brown")
print(birdie.species)               # What will this output?
```





The above code will raise an `Attribute Error` because in the `Sparrow` class the `__init__` method overrides the `__init__` method inherited from the `Bird` class and since the `__init__` method for `Bird` is not run the instance variable `species` does not get initialized. So when it is referenced on list ?? an `Attribute Error` will be raised.

To fix this the `Bird` class needs to be initialised in the `__init__` method of the `Sparrow` class by using the `super().__init__()` method.

