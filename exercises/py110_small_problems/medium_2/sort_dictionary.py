

diction = {'a':1,
           'c':20,
           'b':15,
           'd':102,
           'z': 1000,
           'e': 200

}

def get_value(item):
    return item[1]

print(sorted(diction.items(), key=get_value))