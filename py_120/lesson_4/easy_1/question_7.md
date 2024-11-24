# Question 7

Suppose you have the `Oracle` class and from above and a `RoadTrip` class that inherits from the `Oracle` class, as shown below:

Copy Code

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

class RoadTrip(Oracle):
    def choices(self):
        return [
            'visit Vegas',
            'fly to Fiji',
            'romp in Rome',
            'go on a Scrabble cruise',
            'get hopelessly lost',
        ]
```

What will happen when you run the following code?

Copy Code

```python
trip = RoadTrip()
print(trip.predict_the_future())
```

### Answer

Since the `RoadTrip` class inherits from `Oracle` it will be able to access the `predict_the_future` method. However since it also contains a method called `choices` the method in the `RoadTrip` class overwrites the method in the `Oracle` class when `predict_the_future` is called on a `RoadTrip` object. So the result that is printed will now display a result from the list returned by the  `choices` method in the `RoadTrip` class. Every time Python tries to resolve a method name using `.self`, it first looks in the class of the calling object.