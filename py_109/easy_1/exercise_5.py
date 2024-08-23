bill = float(input('What is the bill? '))
tip_percent = float(input ('What is the tip percentage? '))

tip = bill * (tip_percent / 100)
total = bill + tip

print(f'\nThe tip is ${tip:.2f}')
print(f'The total is ${total:.2f}')