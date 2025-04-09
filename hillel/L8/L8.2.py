import string
def is_palindrome(text):
    for i in string.punctuation.replace('', ' '):
        text = text.replace(i, '')
    a = list(text.lower())
    b = list(reversed(text.lower()))
    ans = True if a == b else False
    return ans
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
