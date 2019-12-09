class Dog():
  def __init__(self, mybreed, name, spots):

    self.mybreed = mybreed
    self.name = name
    # Expect a boolean
    self.spots = spots


my_dog = Dog('lab', 'sammy', False)

print(type(my_dog))
print('dog name is', my_dog.name)

print('dog has spots? ', my_dog.spots)