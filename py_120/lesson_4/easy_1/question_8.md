# Question 8

Suppose you have an object named `my_obj` and that you want to call a method named `foo` using `my_obj` as the caller. How can you see where Python will look for the method. You don't need to determine the actual method location; just identifying the search sequence is sufficient.

### Answer

You can check where Python will look for the method by using the `mro()` method that will print the Method Resolution Order. Since we are using `my_obj` as the caller we would need to call the `mro()` method on its class: `my_obj.__class__.mro()`. This will return a list of the classes in which Python will look for the method in sequence. If the method is not found in any of these classes Python will return an `AttributeError`.

