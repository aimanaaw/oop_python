mylist = [1, 2, 3]
print(len(mylist))

class Book ():
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages

  def __str__(self):
    return f"{self.title} by {self.author}"

  def __len__(self):
    return self.pages

  def __del__(self):
    print("A book object has been deleted")


b = Book('Python rocks', 'Jose', 200)

print(b)
print(len(b))
print (f"Checking {b}")
del b