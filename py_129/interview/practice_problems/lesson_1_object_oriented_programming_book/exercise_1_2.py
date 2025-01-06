class Foo:
    pass


f1 = Foo()

print(f'I am a {type(f1).__name__} object')
print(f'I am a {f1.__class__.__name__}')