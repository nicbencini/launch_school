
class Cat:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):

        if not isinstance(other, Cat):
            raise NotImplemented
        
        return self.name.casefold() == other.name.casefold()
    
    def __ne__(self,other):

        if not isinstance(other, Cat):
            raise NotImplemented
        
        return self.name.casefold() != other.name.casefold()
    
    def __iadd__(self, increment):

        if not isinstance(increment, str):
            raise NotImplemented
        
        self.name = self.name  + increment

        return self


kit = Cat('Chow')
kat = Cat('chow')

kit += 'bob'
kit += 'bob'

print(kit.name)

print(kit == kat)