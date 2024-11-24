# Question 5

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

None of these classes would create an instance variable. The `Fruit` class declares the variable `my_name` however this is a local variable that does not get assigned as an instance variable because it does not have the prefix `self.` which is required to initialize instance variables. The `Pizza` class declares `my_name` with the correct `self.` prefix therefore this will be initialized as an instance variable.