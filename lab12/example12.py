import math

class Cylinder:
  def __init__(self, height, radius):
    self.set_height(height)
    self.set_radius(radius)

  def get_height(self):
    return self.height
  
  def get_radius(self):
    return self.radius

  def set_height(self, height):
    self.height = height

  def set_radius(self, radius):
    self.radius = radius
  
  def calc_base_area(self):
    return math.pi * (self.radius**2)
  
  def calc_surface_area(self):
	  return 2 * (math.pi * self.radius) * self.height

  



