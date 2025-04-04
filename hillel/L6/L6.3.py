import math

a = '999'

lst = []
res = int(a)

while res <= 9:
    for el in a:
        d = el
        lst.append(d)
    res = math.prod(lst)

print(res)




