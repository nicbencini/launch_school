#Exercise 6

age = int(input())
var_1 = 10
var_2 = 20
var_3 = 30
var_4 = 40

age_1 = age + var_1
age_2 = age + var_2
age_3 = age + var_3
age_4 = age + var_4


print('You are ' + str(age) + ' years old.')
print('In ' + str(var_1) +' years, you will be ' + str(age_1) + 'years old.')
print('In ' + str(var_2) +' years, you will be ' + str(age_2) + 'years old.')
print('In ' + str(var_3) +' years, you will be ' + str(age_3) + 'years old.')
print('In ' + str(var_4) +' years, you will be ' + str(age_4) + 'years old.')

#Exercise 8

initial_ammount = 1000
interest = 0.05

balance = initial_ammount*((1+interest)**5)

print(balance)