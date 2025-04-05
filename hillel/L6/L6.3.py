import math

a = int(input('Enter number: '))

while a > 9:
    digits = [int(el) for el in str(a)]
    a = math.prod(digits)

print(a)




