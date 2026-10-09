import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 800

steve = Actor('steve2.jpg')
steve.pos = 400, 400

potion = Actor('potion2.png')
potion.pos = 600, 600

speed = 4

def draw():
  screen.fill('white')
  steve.draw()
  potion.draw()
  screen.draw.text(f'Speed: {speed}', color='black', fontsize=50, topleft=(0, 10)) 

def update():
  global speed
  
  if keyboard.right:
    steve.x += speed

  if keyboard.left:
    steve.x -= speed

  if keyboard.up:
    steve.y -= speed

  if keyboard.down:
    steve.y += speed

  if steve.colliderect(potion):
    x = randint(0, WIDTH)
    y = randint(0, HEIGHT)
    potion.pos = x, y
    speed += 1
    
def randomize():
  x = randint(0, WIDTH)
  y = randint(0, HEIGHT)
  potion.pos = x, y

clock.schedule_interval(randomize, 3)

pgzrun.go()