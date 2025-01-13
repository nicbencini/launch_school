def describe_pet(animal_type, /, *, name=''):
    
    if name != '':
        print(f'{name} is an {animal_type}')
    else:
        print(f'This animal is a {animal_type}')

describe_pet('dog')
describe_pet('cat', name='LeTigre')