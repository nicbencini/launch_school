#Practice Problem 1

lst = [10, 9, -6, 11, 7, -16, 50, 8]

print(sorted(lst))
print(sorted(lst, reverse=True))
print(lst)

#Practice Problem 2

lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

#Practice Probelm 3

lst = [10, 9, -6, 11, 7, -16, 50, 8]

print(sorted(lst,key=str))
print(sorted(lst,key=str,reverse=True))

# Practice Problem 4

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def published_year(x):
    return int(x['published'])

print(sorted(books, key=published_year))
