# Question 3

If we have a `Car` class and a `Truck` class and we want to be able to `go_fast`, how can we add the ability for them to `go_fast` using the mix-in `SpeedMixin`? How can you check whether your `Car` or `Truck` can now go fast?

Copy Code

```python
class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}')

class Car:
    def go_slow(self):
        print('I am safe and driving slow.')

class Truck:
    def go_very_slow(self):
        print('I am a heavy truck and like going very slow.')
```

### Answer

For the `Car` and `Truck` classes to access the method in the mixin, the mixin would need to be added to the inheritance list for the classes: `class Truck(SpeedMixin):`. To check that the `Car` or `Truck` can now go fast you can test whether the `go_fast` method can be called on an instance of the class.