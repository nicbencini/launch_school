class KrispyKreme:
    def __init__(self, filling, glazing):
        self.filling = filling
        self.glazing = glazing
    
    def __str__(self):

        filling_string = self.filling
        glazing_string = self.glazing

        if filling_string == None:
            filling_string = 'plain'
        
        if glazing_string != None:
            glazing_string = f' with {glazing_string}'
        else:
            glazing_string = ''
        
        return f'{filling_string}{glazing_string}'

donut1 = KrispyKreme(None, None)
donut2 = KrispyKreme('Vanilla', None)
donut3 = KrispyKreme(None, 'sugar')
donut4 = KrispyKreme(None, 'chocolate sprinkles')
donut5 = KrispyKreme('Custard', 'icing')

print(donut1)       # Plain
print(donut2)       # Vanilla
print(donut3)       # Plain with sugar
print(donut4)       # Plain with chocolate sprinkles
print(donut5)       # Custard with icing