def ask_for_int():
  while True:
    try:
      result = int(input("\nPlease provide a number: "))
    except:
      print("\nWhoops! That is not a number")
      continue
    else:
      print(f"Yes, the result is {result}")
      break
    finally:
      print("I am going to ask again")

ask_for_int()