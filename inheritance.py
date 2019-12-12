class Animal ():

  def __init__(self):
    print ("ANIMAL CREATED")

  def who_am_i(self):
    print("IAM AN ANIMAL")


  def eat(self):
    print("I am eating")


myAnimal = Animal()

myAnimal.eat()

class Dog(Animal):
  def __init__(self):
    Animal.__init__(self)
    print("Dog created!")
  def who_am_i(self):
    print('I am a dog')

  def bark(self):
    print("WOOF!!!")

myDog = Dog()
myDog.who_am_i()
myDog.eat()
myDog.bark()