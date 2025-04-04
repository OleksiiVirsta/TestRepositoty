d_t = int(input('Enter seconds: '))

days, d = divmod(d_t, 86400)
hour, h = divmod(d, 3600)
min, m = divmod(h, 60)

text = ' днів, '
if str(days)[-1] == '1' and days != 11:
    text = ' день, '
elif 5<= days <= 20:
    text = ' днів, '
elif 2<= days%10 <=4:
    text = ' дні, '

print(days, text, str(hour).zfill(2), ':', str(min).zfill(2), ':', str(m).zfill(2), sep='')