# class Dog:
#   # Initialize name, age, breed
#   def __init__ (self, name, age, breed):
#     self.name = name
#     self.age = age
#     self.breed = breed

#   def getName(self):
#     return self.name

#   def setName(self, name):
#     self.name = name
  
#   def bark(self):
#     print("woof")
  
#   def walk(self):
#     print("the dog is going for a walk")
#   # description method
#   # print doggo's name is a self.age years old and the breed is self.breed
#   def description(self):
#     print("The doggo's name is", self.name, "it is", self.age, "years old, and the breed is", self.breed)



# doggo = Dog('cute doggo', 1, 'idk')
# print(doggo.getName())

# doggo.setName("bob")
# print(doggo.getName())

# doggo.bark()
# doggo.walk()
# doggo.description()

# Your first class

class Rat:
  def __init__(self, age, tail_length, color = "gray"):
    self.age = age
    self.color = color
    self.tail_length = tail_length

  def setAge(self, age):
    self.age = age

  def setTail_length(self, tail_length):
    self.tail_length = tail_length

  def setColor(self, color):
    self.color = color

  def getName(self):
    return self.name

  def getTail_length(self):
    return self.tail_length

  def getColor(self):
    return self.color

  def pet(self):
    print("petting rat")

  def feed(self):
    print("om nom nom")


class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def compute(self):
    return self.length*self.width


rectang = Rectangle(3,5)

print (rectang.compute())