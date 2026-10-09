# Greetings Chatbot
# Author: sarh
# Date: 5 March 2024

import random # import the RANDOM module

# Interactive chatbot that talks to the user

# 1. Say hi to the user and introduce ourselves

print("I am a chatbot. I am here to talk to you")

# 2. Ask the person for their name and store it somewhere

user_name = input("What's your name?")

# 3. Respond nice to meet you name

print(f"nice to meet you {user_name} !")

# 4. Ask what their favourite book is

print("What's your favourite book?")
input()

# 5. Respond
#    a. Create a collection of responses to store in a list
#    b. Randomly choose a response from the list
#    c. print the chosen response
#

book_responses = ["Ooh, I've never read that one!", "That's a good one!", "I'm going to put that one on my reading list", "I don't really like that one...", "Hmmm..."]

print(random.choice(book_responses))

# 6. Ask what their favourite food is

print("What's your favourite food?")
input()

# 7. Respond with an appropriate response

food_responses = ["Yummy", "Ewwwwww", "I'm allergic...", "Sounds exciting, I've never eaten that before!", "hmm. your taste is questionable."]

print(random.choice(food_responses))

# 8. Ask who their favourite character is

print("Who's your favourite character? It can be from anything!")
fave_char = input()

#9. Respnod with an appropriate response

char_responses = [f"{fave_char}... I can't say I've heard of them, but I'm sure they're a fantastic character!", f"I really love {fave_char} too!", f"I actually don't like {fave_char} very much... but we are all entitled to our own opinion."]

print(random.choice(char_responses))

# 10. Ask who their favourite celebrity is
print("Who's your favourite celebrity?")
fave_celeb = input()

# 11. Respond with an appropriate response

celeb_responses = [f"I find {fave_celeb} incredibly annoying, actually.", 
                   f"I think {fave_celeb} fell off but that's just me", 
                   "I love them so much!!"]

print(random.choice(celeb_responses))

# 12. Ask what their favourite video game is

print("Final question! What's your favourite video game?")
fave_game = input()

# 13. Respond with an appropriate response

game_responses = [f"So true, {fave_game} is peak", f"{fave_game} is overrated in my opinion, but you are free to enjoy anything you want.", "That's a unique response! Not many people have said that."]

print(random.choice(game_responses))

# Ask the user how they are doing
user_mood = input("So, how are you doing today?")

# If they respond with good, reply appropriately
if user_mood == "good" or user_mood == "GOOD" or user_mood == "Good":
  good_response = ["I'm happy to hear that!", "That's good news!", "yippee"]
  print(random.choice(good_response))
elif user_mood == "bad":
  bad_response = ["I'm sorry to hear that", "I hope you feel better soon", "rip"]
  print(random.choice(bad_response))
elif user_mood == "frustrated":
  frustrated_response = ["Oh, I hope whatever is causing you frustration goes away soon.", "It's only natural - we live in a stressful world.", "same"]
  print(random.choice(frustrated_response))
elif user_mood == "depressed":
  depressed_response = ["That's very sad to hear.", "I'm sorry to hear that - there is always someone in the world you can talk to."]
  print(random.choice(depressed_response))
else:
  print(f"sorry, I don't understand {user_mood}.")

# ask another question

user_school = input("What type of school are you in? (elementary/middle/high/etc)")
# respodnd

if user_school == "elementary" or user_school == "Elementary":
  print("Wow, you still have many years to go!")
elif user_school == "middle" or user_school == "Middle":
  print("Halfway there! Good luck!")
elif user_school == "High" or user_school == "high":
  print("You're almost there! I hope you get good grades on all your tests.")

# ask another question

user_season = input("What's your favourite season?")

# repond
if user_season == "spring":
  print("Spring is wonderful! All the life begins to wake.")
elif user_season == "summer":
  print("Oh, Summer's too hot for me... I start to feel like I might melt.")
elif user_season == "fall" or user_season == "autumn":
  print("Fall is beautiful - everything's a fiery red and a warm yellow.")
elif user_season == "winter":
  print("I love making snowmen - if only my batteries didn't freeze.")

print("Well... that's about all the questions I have for you. You're a great person to talk to! ")
print("Goodbye!")