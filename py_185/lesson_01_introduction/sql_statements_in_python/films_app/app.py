import psycopg2
from psycopg2 import extras

connection = psycopg2.connect('dbname = films')

try:
    with connection:
        with connection.cursor(cursor_factory=extras.DictCursor) as cursor:
            cursor.execute("""
                           SELECT films.* 
                            FROM films
                            INNER JOIN directors
                            ON films.director_id = directors.id
                            WHERE directors.name = 'Francis Ford Coppola'
                            ORDER BY duration DESC;
                           """)
            result = cursor.fetchall()
finally:
    connection.close

print(result[1]['duration'])