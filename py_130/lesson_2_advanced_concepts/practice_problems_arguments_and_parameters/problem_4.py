def calculate_average(*args):

    if len(args) == 0:
        return None

    return sum(args)/(len(args))

print(calculate_average(2,3,4,5,6,7))

print(calculate_average())