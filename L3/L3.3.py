import  copy

#old_list = [1, 2, 3, 4, 5, 6, 'Parni', 'Chusla']  # => [[1, 2, 3], [4, 5, 6]]
#old_list = [1, 2, 3] # => [[1, 2], [3]]
old_list = [1, 2, 3, 4, 5, 'Hello', ['NE', 'Parni' ,'Chusla']] # => [[1, 2, 3], [4, 5]]
#old_list = [1] # => [[1], []]
#old_list = [] # => [[], []]

if len(old_list) % 2 == 0:
    a = len(old_list) // 2
    b = old_list[:a]
    c = old_list[a:]
    new_list = [b, c]
    print(new_list)
elif len(old_list) % 2 != 0:
    a = (len(old_list) // 2) + 1
    b = old_list[:a]
    c = old_list[a:]
    new_list = [b, c]
    print(new_list)


