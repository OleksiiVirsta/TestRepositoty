#Перший спосіб
a = int(input('Enter number: '))
c_1 = a / 10000
c_2 = (a - (int(c_1) * 10000)) / 1000
c_2_1 = a - (int(c_1) * 10000)
c_3 = (c_2_1 - (int(c_2) * 1000)) / 100
c_3_1 = c_2_1 - (int(c_2) * 1000)
c_4 = (c_3_1 - (int(c_3) * 100)) / 10
c_4_1 = c_3_1 - (int(c_3) * 100)
c_5 = (c_4_1 - (int(c_4) * 10)) / 1
print('\nПерший спосіб:')
print(int(c_5))
print(int(c_4))
print(int(c_3))
print(int(c_2))
print(int(c_1))
#Другий спосіб
print('\nДругий спосіб:')
thth, thou1 = divmod(a, 10000)
thou, hund1 = divmod(thou1, 1000)
hund, tens1 = divmod(hund1, 100)
tens, units = divmod(tens1, 10)
print(units)
print(tens)
print(hund)
print(thou)
print(thth)