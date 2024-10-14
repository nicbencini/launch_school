import datetime

def friday_the_13ths(year):
    thirteenths = [datetime.date(year, month, 13)
                   for month in range(1, 13)]

    count = 0
    for day in thirteenths:
        if day.weekday() == 4:
            count += 1

    return count


thirteens = [datetime.date(2024,2,day) for day in range(1,10)]

for day in thirteens:
    print(day.strftime('%d of %B in %Y'))