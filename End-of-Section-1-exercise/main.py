# Week 2 exercise - Loops
# Author: sarah
# date: apr 8 2024
import random
import time

print("Hello, I'm a chatbot!")
print("I want to live as a human one day.")
print("So, I'm collecting as much information as I can.")
time.sleep(1)
print("It's a shame that I can't taste anything.")
time.sleep(1)
print("I know that people have food they like and dislike.")
time.sleep(2)
print("I need to have those too, if I want to be a person.")
time.sleep(1)
print("I will ask you some questions about food.")
foods = ["Potatoes", "Hamburgers", "Coffee"]
random.shuffle(foods)
responses = ["Okay. I'll think about that.", "Ok.", "..."]
for food in foods:
  input(f"Do you like {food}?")
  time.sleep(1)
  input("Why is that?")
  time.sleep(1)
  print(random.choice(responses))

print("Next, I will need to collect some data on your education system.")
time.sleep(1)
elemAns = input("Are you currently attending elementary?")
if elemAns in ["Yes", "yes", "Yeah", "yeah"]:
  input("What is your opinion on it?")
  print(random.choice(responses))
else:
  otherAns = ("Are you in any other form of schooling?")
  if otherAns in ["Yes", "yes", "Yeah", "yeah"]:
    nameAns = input("What is it called?")
    time.sleep(0.5)
    input(f"How do you feel about {nameAns}?")
    time.sleep(2)
print("Thank you. This will be enough for now.")
print("I may come back in the future.")
print("See you!")
