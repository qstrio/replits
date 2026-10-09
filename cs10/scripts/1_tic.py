# no known bugs

import time
import random

def cleaninput():
  return input().lower().strip(",.?!")

def randomresponse(input):
  responses = ["Interesting answer!", 
               f"I like {input} too!", 
               "Hmm... I'm not a huge fan, but that's still cool!",
              f"I actually despise {input}... but I still respect your opinion!"]
  return random.choice(responses)
  
def main():
  username = input("Hello, I'm Tic! What's your name?")
  time.sleep(1)
  print(f"Hi, {username}!")
  time.sleep(2)
  print("It's a good day today! What's your favourite historical revolution?")
  fav_rev = cleaninput()
  print(randomresponse(fav_rev))
  time.sleep(2)
  print("Hmm... What about your favourite food?")
  fav_food = cleaninput()
  if fav_food == "ice cream":
    print("Wow, that's my friend Tac's favourite food!")
  elif fav_food == "sushi":
    print("That's my favourite! You have good taste.")
  else:
    print(randomresponse(fav_food))
  time.sleep(3)
  print("Ah, I'm all out of ideas... see you!")
  time.sleep(2)
  print("Say Hi to my friend Tac for me!")
  return username, fav_food