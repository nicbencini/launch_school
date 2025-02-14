
def create_user(username,*, email, age):

    dictionary = {}

    dictionary['username'] = username
    dictionary['email'] = email
    dictionary['age'] = age

    return dictionary


print(create_user("Srdjan", email="srdjan@example.com", age=39))
# {"username": "Srdjan", "email": "srdjan@example.com", "age": 39}
print(create_user("Srdjan", "srdjan@example.com", age=39))
# Raises an exception