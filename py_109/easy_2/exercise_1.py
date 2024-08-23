def greetings(name_list, occupation_dict):
    return(f'Hello {' '.join(name_list)}! Nice to have a {occupation_dict['title']} {occupation_dict['occupation']} around.')

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.