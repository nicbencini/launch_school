from functools import reduce

string_list = ['This', 'is', 'a', 'test']

print(reduce(lambda x,y: x+y, string_list))