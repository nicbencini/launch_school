"""
Write a function build_profile that takes a first name and a last name, and any number of keyword arguments to add to a user's profile.
"""

def build_profile(name, surname, **kwargs):

    output = {'name': name,
              'surname': surname,
              }

    for key,value in kwargs.items():
        output[key] = value
    
    print(output)


print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}