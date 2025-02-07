

## Question

How do we create a class and an object in Python?

Write a program that defines a class and creates two objects from that class. The class should have at least one instance variable that gets initialized by the initializer.

What class you create doesn't matter, provided it satisfies the above requirements.

## Answer

The class is first defined in Python and given a name. For example

````python
class Person():
    def __init__(self, name):
        print(name)
````

 To create an object from the class the a new instance of the class should be created within the code after the class has been defined. 

```Python
p1 = Person('Jack')
```

The code above creates a new instance of the `Person` class or a new `Person` object. The example below shows a program that defines a class with two objects crated from that class.

```Python

class Person():
    def __init__(self, name_):

        self.name = name_

P1 = Person('Jack')
P2 = Person('Jill')

print(P1.name)
print(P2.name)
```

