d_t = int(input('Enter seconds: '))

days, d = divmod(d_t, 86400)
hour, h = divmod(d, 3600)
min, m = divmod(h, 60)
sec = d_t - ((days * 86400) + (hour * 3600) + (min * 60))

text = ' днів, '
if str(days)[-1] == '1' and days != 11:
    text = ' день, '
if str(days)[-1] == '2':
    text = ' дні, '

print(days, text, str(hour).zfill(2), ':', str(min).zfill(2), ':', str(sec).zfill(2), sep='')