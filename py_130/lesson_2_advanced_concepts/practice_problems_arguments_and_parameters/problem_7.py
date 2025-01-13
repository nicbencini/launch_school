
def register(username, /, age=None, *, password):
    return {'username': username, 'password': password, 'age': age}