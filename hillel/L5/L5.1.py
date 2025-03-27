import keyword
import string

user_name = input("Enter user name: ")

if user_name[0].isdigit():
    print(False)
elif any(c.isupper() for c in user_name):
    print(False)
elif any(c in string.punctuation.replace("_", "") or c.isspace() for c in user_name):
    print(False)
elif user_name.count('_') >= 2:
    print(False)
elif user_name in keyword.kwlist:
    print(False)
else:
    print(True)
