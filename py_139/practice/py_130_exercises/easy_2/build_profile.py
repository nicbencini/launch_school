

def build_profile(first_name, last_name, **kwargs):

    dictionary = {}

    dictionary['first_name'] = first_name
    dictionary['last_name'] = last_name

    for key, value in kwargs.items():
        dictionary[key] = value
    
    return dictionary



print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}