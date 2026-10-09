# cs 10 exercise 
# date: apr 18 2024
# author" sarah

def rectangularprism(length, width, height):
  sides1 = length*width
  sides2 = width*height
  sides3 = length*height
  area = (sides1+sides2+sides3)*2
  volume = length*width*height
  perimeter = (length+width)*4 + height*4
  return (f"Area: {area}, Volume: {volume}, Perimeter: {perimeter}")

print(rectangularprism(2, 3, 2))