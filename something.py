class Dog():

  species = 'mammal'
  def __init__(self, mybreed, name):
    self.mybreed = mybreed
    self.name = name

    # Operations/Actions ---> Methods
  def bark(self, number):
    print("woof! My name is {} and the number is {}".format(self.name, number))

my_dog = Dog('lab', 'sammy')

print(type(my_dog))
print('dog name is', my_dog.name)
print('dog has species defined? ', my_dog.species)

my_dog.bark(5)


class Circle():
  # Class object attribute
  pi = 3.14
  def __init__(self, radius = 1):
    self.radius = radius
    self.area = radius*radius*self.pi

    # 
  def get_circumference(self):
    return self.radius * self.pi * 2

my_circle = Circle(30)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)