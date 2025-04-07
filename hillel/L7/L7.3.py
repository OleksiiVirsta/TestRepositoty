def second_index(text, some_str):
  if text.count(some_str) <= 1:
    ans = None
  elif text.count(some_str) > 1:
    ind = text.find(some_str)
    ind = text.find(some_str, ind + 1)
    ans = ind
  return (ans)
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
