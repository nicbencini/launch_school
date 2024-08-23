def is_odd(num):
    if abs(num) % 2 != 0:
        return False
    else:
        return True

print(is_odd(1))
print(is_odd(2))
print(is_odd(3))
print(is_odd(4))
print(is_odd(-5))