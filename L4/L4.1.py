# З циклом for
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 0, 0, 96, 0]
print(lst)

for i in lst:
    if i == 0:
        a = lst.remove(i)
        lst.append(0)
print(lst)
