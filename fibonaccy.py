# def fibonaccy(numbers):
#   a = 0
#   b = 1
#   for n in range(numbers):
#     yield a
#     a, b = b, b + a

# for x in fibonaccy(1001):
#   print(x)

# Using memoization
from functools import lru_cache
fibonacci_cache = {}
@lru_cache(maxsize = 1000)
def fibo_func(n):
  if n in fibonacci_cache:
    return fibonacci_cache[n]

  if n == 1:
    value = 1
  elif n == 2:
    value = 1
  elif n > 2:
    value = fibo_func(n - 1) + fibo_func(n - 2)
  fibonacci_cache[n] = value
  return value

for n in range(1, 500):
  print(fibo_func(n))