def add(n1, n2):
  print(n1 + n2)

number1 = 10
number2 = input('Enter the second number')
print(type(number2))
number3 = int(number2)
print(type(number3))


try:
  add(number1, number2)
  print("Add function was successful")

except:
  print("something went wrong with the add function")