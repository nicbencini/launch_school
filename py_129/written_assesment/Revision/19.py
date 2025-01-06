
class Pet:
    def __init__(self, animal_type, name):
        self._animal_type = animal_type
        self._name = name
    
    @property
    def animal_type(self):
        return self._animal_type
    
    @property
    def name(self):
        return self._name

class Owner:
    
    def __init__(self, name):
        self._name = name
        self.pet_count = 0

    @property
    def name(self):
        return self._name
    
    def add_pet(self):
        self.pet_count += 1
    
    def number_of_pets(self):
        return self.pet_count

class Shelter:
    def __init__(self):
        self.adpotions = {}

    def adopt(self, owner, pet):

        if owner.name not in self.adpotions:
            self.adpotions[owner.name] = []
        
        self.adpotions[owner.name].append(pet)
        owner.add_pet()
    
    def print_adoptions(self):
        for owner in self.adpotions.items():
            print(f'{owner[0]} has adopted the following pets:')

            for pet in owner[1]:
                print(f'a {pet.animal_type} names {pet.name}')



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