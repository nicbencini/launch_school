What does the following program print? Try to answer without running the code:

Copy Code

```python
def make_counter():
    def counter_func():
        counter = 0
        counter += 1
        return counter

    return counter_func

increment_counter = make_counter()
print(increment_counter())
print(increment_counter())

increment_counter = make_counter()
print(increment_counter())
print(increment_counter())
```



### Answer

The code will print:

```python
1
1
1
1
```

This is because on line 9 the `make_counter` function is called and assigned to the varibale `increment counter` this will assign the `counter_func` function to the variable. This function is then run on line 10 when `increment_counter()` is called. This will return the counter value of `1`. On `line 11` the `increment_counter()` function is called again which will re-run the `counter_func()` which will re-assign the counter variable to `0` and increment it by `1` to return the value of `1`.  This process will be repeated on line 12-14.