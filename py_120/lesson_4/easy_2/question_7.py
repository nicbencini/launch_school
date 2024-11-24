# Question 7

What would happen if you ran the following code? Don't run it until you've checked your answer:

```python
class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer()) #prints 'Amazon'
print(tv.model()) #prints 'Omni Fire'

print(Television.manufacturer()) #print 'Amazon'
print(Television.model()) #raises a TypeError because it can only be called from a class instance
```

### Answer

