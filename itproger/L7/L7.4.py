# lis = [1, 34, 8, -5, 7, 32, 74, 59, 92, 41, 10]
# lis.sort()
# print(lis)
# a = lis.pop(0)
# print(a)
# if a < 0:
#     lis.append(a)
#     print(lis)
# elif a >= 0:
#     lis.insert(0, a)
#     print(lis)

# другий варіант
lis = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]
# у min присвоюємо перший елемент списку
min = lis[0]
for i in lis:  # проходимо по всіх елементах
    # якщо знаходимо елемент менший ніж той, що перебувати в змінній, то присвоюємо нове значення
    if i < min:
        min = i

print("Мінімальна кількість: ", min)
print("Список до видалення:", lis)
lis.remove(min)
print("Список після видалення:", lis)
if min < 0:
    lis.append(min)
else:
    lis.insert(0, min)
print("Список з доданим елементом:", lis)