class Rectangle:

  def __init__(self, width, height):

    self.width = width
    self.height = height 

  def set_width (self, set_width):
     self.width = set_width

  def set_height(self, set_height):
    self.height = set_height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    picture = ""
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
   
    else:
      for i in range(self.height):
        picture += "*" * self.width + "\n"
      return picture

  def get_amount_inside(self, shape = None):
    counted = 0
    self.shape = shape

    if isinstance(shape, Rectangle) == True:
      if self.height >= (self.width*2):
        counted = int(self.height/self.width) -1
        return counted
      elif self.height >= (self.width):
        counted = int(self.height/self.width) -1
        return counted
      elif self.width >= (self.height*2) :
        counted = int(self.width/self.height) 
        return counted
      else:
        counted = int((self.width*self.height)/ int(self.width+self.height))
        return counted
    
  def __str__(self):
    this = ""
    this += 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'
    return this
class Square(Rectangle):
  def __init__(self, side ):
    self.side = side
    self.width = side
    self.height = side
  def set_width(self, width):
     self.side = width


  def set_height(self, height):
    self.side = height
    
  def set_side(self, side):
    self.side = side
    self.width = side
    self.height = side
    
  def __str__(self):
    this = ""
    this = 'Square(side=' + str(self.side) + ')'
    return this

