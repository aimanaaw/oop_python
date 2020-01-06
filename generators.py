def simple_gen():
  for x in range(3):
    yield x

for number in simple_gen():
  print(number)

g = simple_gen()
print(next(g))
print(next(g))
print(next(g))


s = 'hello'
for letter in s:
  print(letter)

s_iter = iter(s)
next(s_iter)
next(s_iter)