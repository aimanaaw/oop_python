try:
  f = open('testfile', 'r')
  f.write("Write a test line")
except TypeError:
  print("There was a type error!")
except OSError:
  print("Hey you have an OSError!")

finally:
  print("I always run!")