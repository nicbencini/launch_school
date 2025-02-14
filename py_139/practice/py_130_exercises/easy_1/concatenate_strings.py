from functools import reduce

string_list = ['This', 'is', 'a', 'test']

conactenated_string = reduce(lambda x,y: x+y, string_list)

print(conactenated_string)