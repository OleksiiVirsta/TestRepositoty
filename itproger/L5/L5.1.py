#калькулятор
a = int(input('First number: '))
b = input('Second number: ')
c = int(input('Threeth number: '))
# if b == '/' and c == 0:
#     print('Error zerro')

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