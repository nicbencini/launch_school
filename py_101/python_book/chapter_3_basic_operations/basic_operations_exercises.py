
# Exercise 1

full_name = 'Nicolo' + ' ' + 'Bencini'

print(full_name) 

# Exercise 2

value = 4936

one_place = value % 10
ten_place = (value % 100 - one_place)
hunderd_place = (value % 1000 - ten_place - one_place)
thousand_place = (value % 10000 - hunderd_place - ten_place - one_place)

one_place = one_place
ten_place = (int)(ten_place/10)
hunderd_place = (int)(hunderd_place/100)
thousand_place = (int)(thousand_place/1000)

print(one_place)
print(ten_place)
print(hunderd_place)
print(thousand_place)

# Exercise 4

print('5' + '10')

print(int('5') + int('10'))


