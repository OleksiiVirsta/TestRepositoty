def popular_words (text, words):
    dict_one = {}
    for i in words:
        dict_one.setdefault(i, 0)

    text = text.lower().split()

    for el in words:
        if el in text:
            val = text.count(el)
            dict_one[el] = val

    return dict_one
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
