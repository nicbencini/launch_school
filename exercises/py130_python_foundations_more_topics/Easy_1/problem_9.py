def generate_numbers():
    for number in range(1,6):
        yield(number)

print(list(generate_numbers()))