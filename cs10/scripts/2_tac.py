import time
import random

def cleaninput():
  return input().lower().strip(",.?!")

def randomresponse(input):
  responses = ["...", 
               f"I enjoy {input} too.", 
               f"I don't particularly enjoy {input}. It's good to hear that you do.",
              f"Oh. That one I quite detest."]
  return random.choice(responses)
  
def main(username, fav_food):
  time.sleep(1)
  print(f"Hello {username}, I'm Tac.")
  greeting = input().lower().strip(",.?!")
  if greeting in ["hi", "hello"]:
    print("Thanks. Did Tic ask you to say hi to me?")
    ans = cleaninput()
    if ans in ["yes", "yeah", "yup"]:
      print("Good to know.")
    else:
      print("That's strange.")
  else:
    print("Good day to you too.")
  print(f"I was told that your favourite food is {fav_food}.")
  print("Personally, ice cream is the best. What's your favourite flavour?")
  fav_flavour = cleaninput()
  if fav_flavour == "vanilla":
    print("I'm glad to hear you have good taste. That's my favourite, too.")
  else:
    print(randomresponse(fav_flavour))
  time.sleep(2)
  print("You know, I really can't stand when people call vanilla basic.")
  time.sleep(2)
  print("Though, I can understand that not many people have had the real thing.")
  time.sleep(2)
  print("I think I've talked too much. See you.")
  time.sleep(2)
  print("Say hello to Toe.")
  time.sleep(4)
  print("Oh, it appears he's not here today.")
  time.sleep(1)
  print("...")
  time.sleep(4)
  print("What's your favourite game?")
  fav_game = cleaninput()
  if fav_game in ["roblox", "minecraft"]:
    time.sleep(1)
    print("Sometimes, I play that game with my younger sister.")
  elif fav_game in ["honkai impact", "honkai impact 3rd"]:
    print("I used to enjoy hi3 quite a lot.")
    print("But I've since grown to despise the game and its fanbase.")
    print("I'm glad you can enjoy the game.")
  elif fav_game in ["limbus company", "library of ruina", "lobotomy corporation"]:
    print("That's one of my favourite games, too!")
  else:
    print(randomresponse(cleaninput()))
  time.sleep(2)
  print("Oh, Tic is calling me.")
  time.sleep(3)
  print("He says Toe got me vanilla ice cream!")
  time.sleep(2)
  print("Well, I'll be going now. Have a good day.")
  
    