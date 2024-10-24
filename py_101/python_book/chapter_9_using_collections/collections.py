######### Exercise 1 #########

my_range = range(0,25,3)
print(my_range[6])

######### Exercise 2 #########

test_string = 'Launch School'

print(test_string[4:10])

tuple1 = (1,2,3,4,5)

list1 = list(tuple1)
list1.pop(0)
list1.pop(-1)
list1.reverse()

tuple2 = tuple(list1)
print(tuple2)

######### Exercise 3 #########

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog'])
print(pets.get('Lizard'))
print(pets.get('Lizard','Silence'))

######### Exercise 7 #########

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

print(info.replace(':','+'))

######### Exercise 9 #########

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606

print(stuff)

######### Exercise 10 #########

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])

######### Exercise 12 #########

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print (3 in numbers1)

######### Exercise 14 #########

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

print(list(zip(my_str,my_list,my_tuple,my_range)))