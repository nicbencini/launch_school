# Question 6

Without running the following code, can you determine what the following code will do? Explain why you will get those results.

```python
import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

oracle = Oracle()
print(oracle.predict_the_future())
```

### Answer

The code above will return a string with a phrase selected at random from the list returned by the method `choices` within the `Oracle` class. This happens because the `Oracle` class is initialized using the `Oracle` constructor. Then the on the next line the `predict_the_future` method is called and the result is printed. This method returns a formatted string that references the `choices` method that returns a list of choices. The `random` class is used to select a random string from this list.