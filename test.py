test = 'greetings, friends'

if test[-1] != '.':
    test += '.'
if test[0] != test[0].upper():
    test = test.capitalize()

print(test)