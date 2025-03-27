import random
my_list = [random.randint(1, 100) for i in range(random.randint(3, 10))]
print(my_list)

a = my_list[0]
b = my_list[2]
c = my_list[-2]
new_lst = [a, b, c]
print(new_lst)