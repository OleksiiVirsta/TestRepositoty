a = int(input('Enter number: '))
print('Number:', a, sep='')
thousands, nothing = divmod(a, 1000)
hundreds, nothing_1 = divmod(nothing, 100)
tens, units = divmod(nothing_1, 10)
print(thousands)
print(hundreds)
print(tens)
print(units)