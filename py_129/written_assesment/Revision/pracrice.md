## Question 1

Alyssa asked Ben to code review the following code:

Copy Code

```python
class BankAccount:
    def __init__(self, starting_balance):
        self._balance = starting_balance

    def balance_is_positive(self):
        return self.balance > 0

    @property
    def balance(self):
        return self._balance
```

Ben glanced over the code quickly and said - "It looks fine, except that you're trying to access `self.balance` instead of `self._balance` in the `balance_is_positive` method."

"Not so fast," Alyssa replied. "What I'm doing here is valid; I can definitely use `self.balance` there!"

Who is correct, Ben or Alyssa? Why?

### Answer

Alyssa is correct. `self.balance` should be used to access the balance instance variable from within the `balance_is_positive` method. This is because `balance` is being defined as a property using the `@property` decorator which returns `self._balance`. When properties are defined in the class it is generally good practice to reference the property from other methods in the class rather than the original instance variable.

## Question 2

Alan created the following code to keep track of items for a shopping cart application he's writing:

Copy Code

```python
class InvoiceEntry:
    def __init__(self, product_name, number_purchased):
        self._product_name = product_name
        self._quantity = number_purchased

entry = InvoiceEntry('Marbles', 5000)
print(entry.quantity)         # 5000

entry.quantity = 10_000
print(entry.quantity)         # 10_000
```

Without changing any of the above lines of code, update the `InvoiceEntry` class so it functions as shown.

## Question 3

What are the benefits of using object-oriented programming in Python? Think of as many as you can.

- Creates organized and more manageable code
- Easier to modify and make changes without the risk of affecting multiple areas of the code
- Complex problems can be broken down in logic of of objects that contain all the relevant methods and variables within their classes
- 

## Question 4

Suppose you have an `AngryCat` class that looks like this:

Copy Code

```python
class AngryCat:
    def hiss(self):
        print('Hisssss!!!')
```

How would you create a new instance of this class?

### Answer

To create a new instance of `AngryCat` you can call the class `constructor` `AngryCat()` which will call the static method `__new__`which allocates memory for the class. The class constructor then calls the `__init__` method which will create an new instance object of the `AngryCat()` class. Since the `AngryCat()` class does not have an `__init__` method defined, Python will used the default `__init__` method defined in the `object` class.

## Question 5

If we have a `Car` class and a `Truck` class and we want to be able to `go_fast`, how can we add the ability for them to `go_fast` using the mix-in `SpeedMixin`? How can you check whether your `Car` or `Truck` can now go fast?

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

For the `Car` and `Truck` class to access `SpeedMixin` we would need to add it to the inheritance list in the class statements `Car(SpeedMixin)`. This will give the `Car` and `Truck` classes access to all of the methods within the `SpeedMixin` through **inheritance**.

## Question 4

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

This is occurs because the `Car` class inherits the `go_fast` method from the `SpeedMixin` by referencing it the **class statement** on line x. When the `go_fast` method is called on an object of the `Car` class, the method will reference the class that is calling it since it is an instance method that uses the `self` object reference as a parameter which will refer to the class from which the method is called. So when printing the name of the class using `self.__class__.name` it will print the name of the `Car` class since it is the class from which the method is called.

## Question 5

Which of the following classes would create objects that have an instance variable. How do you know?

Copy Code

```python
class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name
```

### Answer

The `Pizza` class will create an object that has an instance variable because the `self` object reference is being used to tell Python that the variable belongs to the object that contains the method in which the variable is assigned.

In the `Fruit` class the variable is being created as a local variable in the `__init__` method because it is not using the `self` object reference.