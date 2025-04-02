import string

text = list(input('Enter words: '))

first = text.pop(0)
second = text.pop()

a = string.ascii_letters.find(first)
b = string.ascii_letters.find(second)
print(string.ascii_letters[a:b+1])