import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.tracer(0)
t.speed(0)
# t.ht()

# for i in range(2000):
#   t.clear()

#   for i in range(4):
#     t.forward(100)
#     t.right(90)
  
#   s.update()

#   t.forward(0.2)

# while True:
#   t.clear()
#   t.forward(100)
#   t.goto(0, 0)
#   t.left(0.1)
#   s.update()

# t.pencolor('blue')
# t.fillcolor('blue')
# while True:
#   t.clear()
#   t.begin_fill()
#   for i in range(4):
#     t.forward(100)
#     t.right(90)
#   t.end_fill()
#   t.right(0.1)
#   s.update()

# t.pencolor('orange')
# t.fillcolor('orange')
# x = 100
# while True:
#   t.clear()
#   t.begin_fill()
#   for i in range(4):
#     t.forward(x)
#     t.right(90)
#   t.end_fill()
#   x -= 0.1
#   if x <= 0:
#     x = 100
#   s.update()

def draw_car():
  t.pencolor('blue')
  t.fillcolor('blue')
  t.begin_fill()
  t.forward(50)
  t.left(90)
  t.forward(50)
  t.right(90)
  t.forward(150)
  t.right(90)
  t.forward(100)
  t.right(90)
  t.forward(200)
  t.right(90)
  t.forward(50)
  t.end_fill()
  t.pencolor('#83ccd4')
  t.fillcolor('#83ccd4')
  t.penup()
  t.forward(45)
  t.right(90)
  t.forward(55)
  t.pendown()
  t.begin_fill()
  # t.left(45)
  for i in range(2):
    t.forward(80)
    t.right(90)
    t.forward(40)
    t.right(90)
  t.end_fill()
  t.penup()
  t.right(90)
  t.forward(100)
  t.pendown()
  t.dot(50, 'black')
  t.dot(40, '#c5dbde')
  t.penup()
  t.left(90)
  t.forward(100)
  t.pendown()
  t.dot(50, 'black')
  t.dot(40, '#c5dbde')
  t.left(180)
  t.penup()
  t.forward(155)
  t.right(90)
  t.forward(55)
  t.right(90)
  t.pendown()
  
  
draw_car()

for i in range(500):
  t.clear()
  draw_car()
  s.update()
  t.forward(-0.5)