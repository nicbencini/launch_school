# Exercise 12

```python

class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound

class Lion(Cat):
    sound = "roar"

print(Lion.make_sound())

#What will the code output and why
```

The code will print `'roar'` because the class variable `sound` in the `Lion` class is defined as `'roar'` which overrides the class variable `sound` inherited from `Cat`. The class method `make_sound` is inherited from `Cat` however when called from a `Lion` object it uses the `sound` class variable defined in the `Lion` class.

