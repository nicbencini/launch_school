def find_person(**kwargs):

    if 'Antonina' in kwargs.keys():
        print(f'Antonina is a {kwargs['Antonina']}')
    else:
        print('Antonina not found')

find_person(Antonina='Doctor', Joe='Lawyer')
