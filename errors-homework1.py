# for i in ['a', 'b', 'c']:
#   try:
#     print(i**2)
#   except TypeError:
#     print("Something wrong")

# x = 5
# y = 0

# try:
#   z = x / y
# except ZeroDivisionError:
#   print("One of the values is zero")

def ask_function():
  while True:
    try:
      number = int(input("\nEnter a number: "))
    except:
      print("That is not an integer. Please enter another integer")
    else:
      print(number**2)
      print("That is correct")
      break

ask_function()