class Cat:

    cat_count = 0

    def __init__(self):
        Cat.cat_count += 1
    
    @classmethod
    def total(cls):
        print(cls.cat_count)

Cat.total()         # 0

kitty1 = Cat()
Cat.total()         # 1

kitty2 = Cat()
Cat.total()         # 2

print(Cat())        # <__main__.Cat object at 0x104ed7290>
Cat.total()         # 3