N = int (input ("Введіть число n: "))

some = [9, "Hi", 23.5, "A"]
# temp_list = []

while N > 0:
	some.append (input ("Введіть щось: "))
	N -= 1

# some.extend (temp_list)
print (some)