# Question 4

In the previous question, we had a mix-in called `SpeedMixin` that contained a `go_fast` method. We add this mix-in to the `Car` class as shown below:

Copy Code

```python
class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}!')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

small_car = Car()
print(small_car.go_fast())
# I am a super fast Car!
```

When we called `small_car.go_fast`, you may have noticed that the output includes the vehicle type. How is this done?

### Answer

This is done because in the `SpeedMixin` the output that is printed uses `self` to references the object class name of whichever class calls it. Once this method is called from a subclass it references the class name of the subclass which in this case is of type `Car` and returns it as a string.