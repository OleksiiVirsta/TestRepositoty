import string

text = input('Some text: ')

for b in string.punctuation:
    text = text.replace(b, "")#.replace(' ', '')
text = '#' + text.title().replace(' ', '').ljust(-10)
right_text = text[:140]
print(right_text)


