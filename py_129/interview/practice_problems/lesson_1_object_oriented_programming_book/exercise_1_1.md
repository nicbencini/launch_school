## Question 

How do we create a class and an object in Python?

Write a program that defines a class and creates two objects from that class. The class should have at least one instance variable that gets initialized by the initializer.

What class you create doesn't matter, provided it satisfies the above requirements.

### Answer

A class is defined in python by using a class statement which includes the word `class` followed by the name of the class. An object is created in python by calling a the class constructor function which has the same name as the class. This creates a new instance object of the class by calling the initializer which initializes the instance object and any instance variables.

```python
class Dog:
    
    def __init__(self, color):
        self._color = color

dog_1 = Dog('brown')
dog_2 = Dog('grey')
```

