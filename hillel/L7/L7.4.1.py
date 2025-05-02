import random

def common_elements():
    r = [random.randrange(0, 100, 3) for i in range(random.randint(0, 100))]
    d = [random.randrange(0, 100, 5) for i in range(random.randint(0, 100))]
    set1 = set(r)
    set2 = set(d)
    inter = set1.intersection(set2)

    return inter

print(common_elements())