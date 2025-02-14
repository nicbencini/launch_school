
def creater_greeting():
    greet = 'hello'

    def display_greeting():
        print(greet)
    
    return display_greeting

greet = creater_greeting()
greet()