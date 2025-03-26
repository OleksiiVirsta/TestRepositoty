# З циклом for
# lst = [0, 5, 8, 15, 45, 145, 0, 78, 0, 122]
# print(lst)
#
# for i in lst:
#     if i == 0:
#         a = lst.remove(i)
#         lst.append(0)
# print(lst)

# З циклом while
lst = [0, 5, 8, 15, 45, 145, 0, 78, 0, 122]
print(lst)
i = 0
while i < len(lst):
    l = lst[i]
    if l == 0:
        a = lst.pop(i)
        lst.append(a)
    i += 1
print(lst)