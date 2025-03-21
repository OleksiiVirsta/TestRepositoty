
#chang = [15, 8, 4, 10, 22, 18] # => [18, 15, 8, 4, 10, 22]
#chang = [2] # => [2]
#chang = [] # => []
chang = [48, 3, 5, 10, 89, 33, 4, [7, 'son']] # => [[7, 'son'], 48, 3, 5, 10, 89, 33, 4]

#інша перевірка
# if len(chang) == 0:

if chang == []:
    print(chang)
else:
    a = chang.pop(-1)
    chang.insert(0, a)
    print(chang)

