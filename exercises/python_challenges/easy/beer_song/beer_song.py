"""

problem
Write a program that can generate the lyrics of the 99 Bottles of Beer song. See the test suite for the entire song.

rules:
- can take 0 as an input
- request for a single verse or multiple verses
- whole song up to 99 verses

Data:

BeerSong(class):
    verse(class method) -returns on verse
    verses(class method) -returns multiple verses
    lyrics(class method) -returns entire song
"""

class BeerSong:

    @staticmethod
    def verse(number):
        if number == 0:
            return ("No more bottles of beer on the wall, no more bottles of beer.\n"
                    "Go to the store and buy some more, 99 bottles of beer on the wall.\n")
        
        elif number == 1:
            return (f"1 bottle of beer on the wall, 1 bottle of beer.\n"
                    "Take it down and pass it around, no more bottles of beer on the wall.\n")
        
        elif number == 2:
            return (f"2 bottles of beer on the wall, 2 bottles of beer.\n"
                    f"Take one down and pass it around, 1 bottle of beer on the wall.\n")
        
        elif 2 < number <= 99:
            return (f"{number} bottles of beer on the wall, {number} bottles of beer.\n"
                    f"Take one down and pass it around, {number - 1} bottles of beer on the wall.\n")
    
    @classmethod
    def verses(cls, end, start):

        output_verses = []

        for i in range(end,start -1, -1):

            output_verses.append(cls.verse(i))

        return '\n'.join(output_verses)
    
    @classmethod
    def lyrics(cls):

        return cls.verses(99,0)


