import math
def isprime(arg):
    limit = math.isqrt(arg)
    num = True

    if arg < 2:
        num = False
    elif arg == 2:
        num = True
    else:
        for i in range(2, limit + 1):
            if arg % i == 0:
                num = False
                break
    return num


def prime_generator(end):
    for i in range(2, end + 1):
        if isprime(i):
            yield i

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
