lst = [2, 5, 7, 2, 2]
i = 0
suma = 0
while i < len(lst):
    l = lst[i]
    # n = len(lst) - 1
    # h = lst[n]
    if len(lst) == 0:
        suma = lst
    elif i % 2 == 0:
        n = len(lst) - 1
        h = lst[n]
        suma += l * h
    i += 1
print(suma)