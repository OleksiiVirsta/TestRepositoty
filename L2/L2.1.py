a = int(input('Enter number: '))
print('Number:', a, sep='')
thousands, nothing = divmod(a, 1000)
hundreds1, nothing_1 = divmod(a, 100)
nothing_2, hundreds = divmod(hundreds1, 10)
tens1, units = divmod(a, 10)
some1, tens = divmod(tens1, 10)
print(thousands)
print(hundreds)
print(tens)
print(units)
print('\n', thousands, '\n', hundreds, '\n', tens, '\n', units )