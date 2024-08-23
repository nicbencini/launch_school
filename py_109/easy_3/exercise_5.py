def triangle(n):

    for i in range(n):
        row = ''
        for j in range(n):
            if j >= (n-1-i):
                row += '*'
            else:
                row += ' '
        
        print(row)



triangle(5)
triangle(9)