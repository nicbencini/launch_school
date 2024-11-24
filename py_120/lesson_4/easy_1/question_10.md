# Question 10

Suppose you have the following class:

Copy Code

```python
class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count
```

Explain what the `_cats_count` variable is, what it does in this class, and how it works. Write some code to test your theory.

### Answer

The `_cats_count` variable is a class variable which is assigned the integer 0. Every time the `Cats` class is initalized the `_cats_count` variable gets increased by 1. The `cats_count` method returns the current value of the `_cats_count`. This value is stored in the class and gets incremented by 1 every time a new class object is initialized.

```python
cat_1 = Cat('persian')
print(Cat.cats_count)
cat_2 = Cat('street')
print(Cat.cats_count)
cat_3 = Cat('tabby')
print(Cat.cats_count)


```







