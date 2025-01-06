
def get_age(name):

    students = {'John': 25, 'Jane': 22, 'Doe': 30}

    try:
        age = students[name]
    except KeyError:
        return 'Student not found'
    else:
        return age


print(get_age('John'))
print(get_age('Max'))
