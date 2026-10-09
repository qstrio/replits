"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.tracer(0)
t.speed(0)

t.pencolor('blue')
t.fillcolor('blue')
def drawshark():
  t.begin_fill()
  t.left(45)
  t.forward(50)
  t.left(45)
  t.forward(50)
  t.right(140)
  t.forward(60)
  t.left(45)
  t.forward(100)
  t.left(45)
  t.forward(50)
  t.right(140)
  t.forward(90)
  t.right(140)
  t.forward(40)
  t.left(90)
  t.forward(100)
  t.right(40)
  t.forward(80)
  t.right(55)
  t.forward(30)
  t.end_fill()
  t.left(75)
drawshark()

for i in range(500):
  t.clear()
  drawshark()
  s.update()
  t.forward(0.2)
  
