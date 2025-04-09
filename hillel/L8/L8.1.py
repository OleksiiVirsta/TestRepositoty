def add_one(some_list):
    x = "".join([str(y) for y in some_list])
    x1 = str(int(x) + 1)
    lst = [int(el) for el in x1]
    return lst
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
