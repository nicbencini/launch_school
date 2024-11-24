# Question 4

Suppose we have this code:

```python
class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')
```

Without running the above code, what would each snippet do were you to run it?

```python
hello = Hello()
hello.hi()
```

Snippet 1: This will print `Hello`.

```python
hello = Hello()
hello.bye()
```

Snippet 2: This will raise and `attriubute error` because neither `Hello` nor `Greeting` define a method called `bye`

```python
hello = Hello()
hello.greet()
```

Snippet 3 This will raise an TypeError because the `greet` method requires one argument.

```python
hello = Hello()
hello.greet('Goodbye')
```

Snippet 4 This will print `Goodbye`

```python
Hello.hi()
```

Snippet 5 This will raise an TypeError because Hello needs to be initialized before the `hi()` method can be used since high takes self as one of its arguments.