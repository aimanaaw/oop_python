import math

class Cylinder:
  def __init__(self, height=1, radius=1):
    self.height = height
    self.radius = radius
    print (f"class inherited {self.height} and {self.radius}")

  def volume(self):
    result = round((math.pi * (self.radius ** 2) * self.height), 2)
    print(f"The volume of the cylinder is {result}")
    return result

  def surface_area(self):
    result = round(((math.pi * (self.radius ** 2) * 2) + (2 * math.pi * self.radius * self.height)), 2)
    print (f"The surface area is {result}")
    return result

c = Cylinder(2, 3)
c.volume()
c.surface_area()