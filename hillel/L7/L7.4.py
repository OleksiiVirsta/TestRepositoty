def common_elements():
    r = list(range(0, 100, 3))
    d = list(range(0, 100, 5))

    set1 = set(r)
    set2 = set(d)
    inter = set1.intersection(set2)

    return (inter)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('Ok')