# Question 1

Alyssa asked Ben to code review the following code:

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

Aliysa is correct because `self.balance` is created as a property however there is no setter method. When the `balance_is_positive` function is called it will reference the property `balance` which returns the value for `self.balance`. However a setter function will be required to be able to set the value of `balance`.