def century(year):
        
    remainder = year%100
    century = int((year - remainder)/100)

    if remainder > 0:
        century += 1
    
    suffix = 'th'

    century_str = str(century)

    if century_str[-1] == '1':
        suffix = 'st'
    elif century_str[-1] == '2':
        suffix = 'nd'
    elif century_str[-1] == '3':
        suffix = 'rd'
    else:
        pass

    if len(century_str) > 1 and century_str[-2] == '1':
        suffix = 'th'
    
    return (century_str + suffix)


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
