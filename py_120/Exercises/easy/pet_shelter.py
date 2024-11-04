
class Pet:

    def __init__(self, pet_type, name):
        self._pet_type = pet_type
        self._name = name

    @property
    def pet_type(self):
        return self._pet_type
    
    @property
    def name(self):
        return self._name

class Owner:

    def __init__(self, name):
        self._name = name
        self.pets = 0

    @property
    def name(self):
        return self._name
    
    def number_of_pets(self):
        return self.pets
    

    
class Shelter:

    def __init__(self):
        self._adoptions = {}
    
    @property
    def adoptions(self):
        return self._adoptions

    def adopt(self, owner, pet):
        owner.pets += 1

        if owner.name not in self.adoptions:
            self.adoptions[owner.name] = []
        
        self.adoptions[owner.name].append(pet)
    
    def print_adoptions(self):
        
        for item in self.adoptions.items():
            print(f'{item[0]} has the following pets:')

            for pet in item[1]:
                print(f'a {pet.pet_type} name {pet.name}')
        
            print('\n')


        


cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")


#P Hanson has adopted the following pets:
#a cat named Cocoa
#a cat named Cheddar
#a bearded dragon named Darwin

#B Holmes has adopted the following pets:
#a dog named Molly
#a parakeet named Sweetie Pie
#a dog named Kennedy
#a fish named Chester

#P Hanson has 3 adopted pets.
#B Holmes has 4 adopted pets.