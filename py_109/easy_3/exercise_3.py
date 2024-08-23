def print_in_box(input_string):
    print(f'+-{'-' * len(input_string)}-+')
    print(f'| {' ' * len(input_string)} |')
    print(f'| {input_string} |')
    print(f'| {' ' * len(input_string)} |')
    print(f'+-{'-' * len(input_string)}-+')

print_in_box('To boldly go where no one has gone before.')
print_in_box('')