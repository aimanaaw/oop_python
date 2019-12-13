import math

class Line:
  def __init__(self, coor1, coor2):
    self.coor1 = coor1
    self.coor2 = coor2
    print(f"class inherited {coor1} and {coor2}")

  def distance(self):
    x2 = (self.coor2[0] - self.coor1[0]) ** 2
    print (f"the x squared distance is {x2}")
    y2 = (self.coor2[1] - self.coor1[1]) ** 2
    print (f"the y squared distance is {y2}")
    squared = y2 + x2
    result = math.sqrt(squared)
    print (f"the distance is {result}")
    return result

  def slope(self):
    gradient = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
    print (f"the slope is {gradient}")
    return gradient


li = Line((3,2), (8,10))
li.distance()
li.slope()