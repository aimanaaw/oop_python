import random

def rand_num(low, high, n):
  for eachNumber in range(n):
    yield random.randint(low, high)

for eachNumber in rand_num(1, 10, 12):
  print(eachNumber)