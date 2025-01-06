## Question 1

```python
class Dog:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

    def bark(self):
        print('Woof! Woof!')
```

The code added above is a `class` which provides a blueprint for the behaviors of the `object instances` created from it. 

The code on *line 3 and 4* are the `class constructors` which initialize new object instances of the class with the values provided as arguments. For example on *line 3* an instance of the `Dog()` class is initialized with the arguments `'Fido'` and `'5'` which will define the `state` of the object assigned to the variable `fido`.



## Question 3

When run, this code will output `"i'm whispering...."`.

What is the underlying mechanism that determines which `speak` method Python invokes? Describe, in detail, how this mechanism works in Python, including what happens when a method can't be found. Explain why, in the context of this specific example, invoking `speak` outputs `"i'm whispering...."` rather than `"I'M SHOUTING!!!"` or `"I'm speaking."`.





### Answer

The mechanism that defines which `speak` method Python invokes is the `Method Resolution Order` (`MRO`).

The `Method Resolution Order` is the order of classes in which Python searches to find the method that is being invoked. Python will look through the classes added to the inheritance list in the `Child` class statement on *line 13* using a 'depth first' search from left to right. Python will keep searching through the inheritance list until the method is found. If the method is not found in any of the classes in the inheritance list then Python will search in the `Object` class since it is the class from which all other objects inherit. If the method cannot be found in the `object` class then Python will return an `AttributeError`.

In the context of this specific example invoking `speak` Python will first search in the first class in the inheritance list which in this case is `WhisperMixin` and since it contains a method called `speak` it will call that method which will print `"i'm whispering..."`. 



## Question 4

What OO programming concept is described by the following text?

> The ability of objects with different types to respond to the same method invocation, often, but not always, in different ways.

Why is it useful? Provide a code example to illustrate how this concept is implemented in Python.



The concept described by the text is `polymorphism`. It is useful because it can lead to more maintainable code since different objects can respond to the same interfaces. It can also reduce the amount of code that needs to be written.

This concept is implemented in Python in 2 ways:

- Through `inheritance` where multiple classes can inherit the same method from another class or mixin. In this case unless the methods from the inherited class are overwritten then the same method will be called for all of the subclasses.

```python
class Person:
    def walk(self):
        print("I'm walking.")

class Child(Person):
    pass

class Adult(Person):
    pass

Child().walk()
Adult().walk()
```



- Through `duck typing` where objects of different types respond to the same method name  even though the result may be very different.

```python

class Child():
    
    def walk(self):
        print('I am running')

class Adult():

    def walk(self):
        print('I am walking')

Child().walk()
Adult().walk()
```

## Question 15

You're designing a course tracking application, and have identified three classes that you need: `Course`, `Teacher`, and `Student`. 

Each Course has one or more Teachers and one or more Students. In our application, the Teachers and Students don't interact directly, and neither needs to know anything about the Course to which they belong.

Given the above details, what kind of object-oriented relationship (inheritance, mix-in, collaboration, or none) should exist between objects of each pair of classes, and why?

- `Course` and `Teacher`
- `Course` and Student
- `Teacher` and Student

Use the description of the design as written; don't read additional details into it that are not explicitly stated.

### Answer

- A `course` has a `teacher` so in this case the object oriented relationship would be `collaboration` since one or more `Teacher` classes can be created within the `Course` class to access its functionality but the `Teacher` class does not need to inherit any methods from the `Course` class or vice-versa.
- Similar to the `Teacher` class, the `Student` class is also a collaborator object of the `Course` class since it doesn't need to inherit any of its methods.
- The `Teacher` and `Student` classes do not have any object oriented relationship since they don't interact directly.



## Question 2

In Python, **inheritance** can be provided by either class inheritance or using mix-ins. Identify the differences between class inheritance and using mix-ins, then describe when you should use one over the other. Provide code examples that demonstrate each approach.

## Answer

Class inheritance is when an object inherits from another class and is said to be a subclass of the class it inherits from. This is useful when objects have a `is a` relationship where one object  or multiple objects are variations of a base class an there is an apparent hierarchy. For example in the code below both `Car` and `Plane` are subclasses of `Vehicle`:

```python
class Vehicle:

    def __init__(self):
        pass
        
    def start(self):
        pass

class Car(Vehicle):
    pass

class Plane(Vehicle):
    pass
```

Mixins on the other hand are designed to provide common functionality to multiple classes however they cannot be initialized as an object themselves. They provide common behaviors to classes that have no apparent hierarchy:

```python
class ColorMixin:
    def set_color(self):
        pass

class Car(ColorMixin):
    pass

class Plane(ColorMixin):
    pass
```

# Question 5

What is the scope of an instance variable? Provide some code that supports your answer, along with an explanation of *why* your code example supports your answer.

## Answer

An instance variable is a variable created for storing data of the instance object. They keep track of the state of the object and every new instance of an object  It is created by using the `self` reference which represents the object that is creating them.  They continue to exist as long as the object exists unless explicitly deleted.  For example in the code below `self._wheels` is an instance variable of the `Vehicle` class that gets initialized when an new class object is created. However the variable `windows` is a local variable created within the `__init__` method since it does not contain a `self` reference.

```python

class Vehicle:

    def __init__(self, wheels):
        self._wheels = wheels
        windows = 2
        

```

## Question6

In Python, `self` and `cls` are commonly used in class definitions. Explain the differences and similarities between these two terms, and provide examples to illustrate how each is used within a Python class.

`cls` and `self` are both references to the context in which the methods or variables within a class are used. In the case of `self` this references the instance of an object created by the class and any variable or method created with the `self` reference are instance methods or instance variables. In the example below the variable `self.wheels` is an instance variable which will get initialized once an instance of the `Vehicle` class is created.

`cls` is used to reference the class rather than the instance. It is used to reference methods or variables that belong to the class and are not specific to any instance objects. In the example below `seat` is a class variable that can be accessed from with the `class method` `driver`. 

```python
class Vehicle:

    seat = 4

    def __init__(self, wheels):
        self._wheels = wheels
        windows = 2
    
    @classmethod
    def driver(cls):
        print(cls.seat)
```

## Question 12

The program outputs `False` even though `bob1` and `bob2` are identical objects because when on line 8 they are tested for equality using the `==` operator Python by default will check whether `bob1` and `bob2` are the same object and do not have the same id reference. Even though they are initialized with the same values `bob1` and `bob2` are not the same objects since they are both different instances of the `Student` class. If instead the code is altered to check whether `bob1 == bob1` this will return `True` since in this case both operands are the same object. 

## Question 13

The `__eq__` magic method can be defined for the `Student` class to overwrite the behavior of the default `__eq__` method. In the example below the `__eq__` magic method has been overridden to check for equality between the `name` and `grade` of the `Student` class and returns `True` if they match.

```python
class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self._name == other._name and self._grade == other._grade
        
        return NotImplemented
```

## Question 8

The code outputs `False` since the instance variable `speed` is not being referenced and re-assigned on line 15. This is because the `self` object reference is missing so instead of reference the instance variable and re-assigning it to the new value, a new local variable called `speed` is being created within the `accelerate` method. This can be fixed as shown below:

```python

class Car:
    def __init__(self, speed):
        self.speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    def accelerate(self):
        new_speed = self.speed + 10
        self.speed = new_speed

    def is_faster_than(self, other_car):
        return self.speed > other_car.speed

# Testing the Car class
car1 = Car(40)
car2 = Car(40)
car1.accelerate()
print(car1.is_faster_than(car2))
```

