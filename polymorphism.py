class Dog ():

  def __init__(self, name):
    self.name = name
    
  def speak(self):
    return self.name + " says woof!"

class Cat ():
  
  def __init__(self, name):
    self.name = name
    
  def speak(self):
    return self.name + " says meow!"

niko = Dog('niko')
felix = Cat('felix')

# print(niko.speak())
# print(felix.speak())

for pet in [niko, felix]:
  print(type(pet))
  print(pet.speak())

def pet_speak(pet):
  print(pet.speak())

pet_speak(niko)
pet_speak(felix)

class Animals ():
  def __init__(self, name):
    self.name = name
  def speak(self):
    raise NotImplementedError("Subclass not implemented this abstract method")

class Dogs(Animals):
  def speak(self):
    return self.name+ " says woofs!"

class Cats(Animals):
  def speak(self):
    return self.name+ " says meows!"

fido = Dogs("Fido")
simba = Cats("simba")

print(fido.speak())
print(simba.speak())