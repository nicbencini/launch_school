students = {'John': 25, 'Jane': 22, 'Doe': 30}

def get_name(name):

    try:
        age = students[name]
    except KeyError:
        return 'Student not found'
    else:
        return age


print(get_name('John'))
print(get_name('Mark'))