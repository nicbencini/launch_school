"""
Create a function create_user that takes a username and requires keyword-only arguments for email and age.
"""
def create_user(username,*,email,age):
    output = {}

    output['username'] = username
    output['email'] = email
    output['age'] = age

    print(output)

print(create_user("Srdjan", email="srdjan@example.com", age=39))
# {"username": "Srdjan", "email": "srdjan@example.com", "age": 39}
print(create_user("Srdjan", "srdjan@example.com", age=39))
# Raises an exception