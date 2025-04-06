# 1
# a = 34
# while a <= 67:
#     if a % 2 != 0:
#         print(a)
#     a += 1
#
# print('Finish')

# 2
# i = 0
# while True: # Нескінченний цикл, який спрацює сто відсотків
# 	print (i)
# 	i += 1
# 	if i > 0: # Далі йде умова і якщо вона не вірна, то виходимо з циклу
# 		break

# 3
# for i in range(1, 101):
# 	if i == 50:
# 		continue
# 	if i == 99:
# 		continue
# 	print(i)

# i = 1
# while i <= 100:
# 	if i != 50 and i != 99:
# 		print (i)
# 	i += 1

# 4
i = input('Enter words: ')
b = input('Enter number: ')
for c in i:
	print(c * int(b))