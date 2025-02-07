## Question

Given an instance of a `Foo` object, show two ways to print `I am a Foo object` without hardcoding the word `Foo`.

## Answer

The phrase can be printed by either getting the class type name:

```python
print(f'I am a {type(Foo).__name__} object')
```

or by getting the class name:

```python
print(f'I am a {Foo.__class__.__name__} object')
```



