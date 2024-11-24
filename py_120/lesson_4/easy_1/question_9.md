# Question 9

There are several variables listed below. What are the different variable types and how do you know which is which?

Copy Code

```python
excited_dog = 'excited dog'
self.excited_dog = 'excited dog'
self.__class__.excited_dog = 'excited dog'
BigDog.excited_dog = 'excited dog'
```

### Answer

- `excited_dog` is a local variable. If this is defined in the main class body it will be a class variable

- `self.excited_dog` is an instance variable because it is assigned to `self`. These are usually defined within the `__init__` method for a class 

- `self.__class__.excited_dog` is a class variable being accessed from within an object instance. This is because it is getting the objects class using `__class__` and then accessing the variable `excited_dog`

- `BigDog.excited_dog` is a class variable because it is being accessed directly from the class `BigDog` 

  

  

