cont = True

while cont == True:
    a = int(input('First number: '))
    b = input('Operations: ')
    c = int(input('Second number: '))
    if b == '+':
        print(a, b, c, '=', (a+c))
    elif b == '-':
        print(a, b, c, '=', (a-c))
    elif b == '*':
        print(a, b, c, '=', (a*c))
    elif b == '/':
        print(a, b, c, '=', (a / c if c != 0 else 'На нуль ділити не можна'))
    else:
        print ("Ви ввели щось не те!")
    answ = input('Enter "y" if you want continue: ')
    if answ.lower() != 'y':
        cont = False
print('Work finished!')