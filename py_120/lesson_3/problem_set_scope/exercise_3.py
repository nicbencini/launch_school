class Cat:

    def get_name(self):

        if not hasattr(Cat, 'name'):
            print('Name not set!')
        
        else:
            return self.name

cat_1 = Cat()
cat_1.get_name()