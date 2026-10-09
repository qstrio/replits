# Mind reader game
# Author: Srah
# 4/4/2024

import replit
import time
import random

# Two player game
# Game to test how conneced
# you are to another person

# print("Hello, Welcome to our Mind Reader Game! 🔮")
# time.sleep(1)
# print("This game requires two players.")
# time.sleep(1)
# print("I will see how well you two know each other!")

# repeat game for a sequence of words
# create a list of words

words = [
  "sports",
  "animals",
  "music",
  "video games",
  "superheroes"
]
random.shuffle(words)

print("Player one, it's your turn.")
time.sleep(2)
p1Name = input("So, what's your name?")
print(f"Okay! {p1Name}, get ready!")
time.sleep(1)

for word in words:
  # Give p1 instructions
  # - show them a word
  # - ask them to ehter 3 words
  #   that they associatewith the shown word
  print("The word I want you to focus on is... ")
  time.sleep(2)
  print(f"__{word.upper()}!__")
  time.sleep(3)
  print("Okay, now enter 3 words you associate with that word.")
  word1 = input("First word:")
  word2 = input("Second word")
  word3 = input("Third word:")
  print("Thank you!")
  time.sleep(2)
  print("Now, give control to player 2.")
  time.sleep(5)
  
  # clear the screen
  replit.clear()
  # gives p2 instrcutions    
  # - show them the ssamr word
  # - try to guess what words p1 associated with it
  p2Name = input("So, player 2, what's your name?")
  print(f"Okay! {p2Name}, get ready!")
  time.sleep(1)
  print("The word I want you to focus on is... ")
  time.sleep(2)
  print(f"__{word.upper()}!__")
  time.sleep(3)
  print(f"{p2Name}, what word do you think {p1Name} associates with the word above?")
  p2Word = input()
  print("Calculating...")
  time.sleep(4)
  # if any words match, they win
  # otherwise, they lose
  if p2Word in [word1, word2, word3]:
    print("Congratulations! You won!")
    time.sleep(1)
  else:
    print("Sorry, you lost this time.")
  time.sleep(1.5)
  print(f"{p1Name} entered the words: ")
  print([word1, word2, word3]) 