import random
import time

# ss10 exercise chatbot
# Author: Sarah 
# Date: March 12th 2024

print("Hello, I'm a chatbot!") 
time.sleep(0.5)
print("I'm here to collect information on humans.")
time.sleep(1.5)
print("Oh, don't worry - it's just to update the galactic encyclopedia.")
time.sleep(1)
ready = input("Are you ready?")
if ready in ["Yes", "yes", "Yeah", "yeah"]:
  print("Okay, let's go!")
else:
  print("Okay, see you then!")
  quit()

print("Hmm, let me think of a question...")
time.sleep(2.0)
print("Okay, I got it!")
user_school = input("Are you still in school?")
subject_responses = ["I love that subject too!", 
                     "I don't know that much about it...", 
                     "Ooh, that's really interesting."]
if user_school in ["Yes", "yes", "Yeah", "yeah"]:
  input("What's your favourite subject?")
  print(random.choice(subject_responses))
else:
  print("Hmm, okay then.")

time.sleep(2.5)
print("Okay, next question!")
user_animal = input("What's your favourite animal?")
if user_animal in ["Cats", "Cat", "cats", "cat"]:
  print("I love cats too! Did you know that there are over 2mil cat videos on Youtube?")
elif user_animal in ["Dogs", "Dog", "dogs", "dog"]:
  print("Dogs are great animals - their noses are 40x more sensitive than a human's!")
else:
  print(f"Sorry, I don't know very much about {user_animal} yet...")

time.sleep(2.5)

print("Last question!")
fave_food = input("What was your favourite meal as a kid?")

if fave_food in ["Broccoli", "broccoli"]:
  print("Wow, that's interesting! I thought everyone hated broccoli as a kid.")
elif fave_food in ["Mcdonalds", "mcdonalds", "McDonalds"]:
  print("Yeah, I get that answer a lot.")
  print("I bet you didn't get to eat it often.")
else:
  print("Hmm...")
  time.sleep(1)
  print("I wish I had taste buds - just to see what all the fuss is about.")

time.sleep(2)
print("Well, that's all the questions I have for now.")
print("See you later!")