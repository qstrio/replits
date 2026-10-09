"""
Hangman Game Design:

- Print a welcome message
- Give users the option to start a game or quit
- If they choose to start a game:
    - Let users guess a letter
    - If it's correct, add it to the result so far. If it is not correct, add a part to the hangman
    - Continue this until a user either guesses the word or loses the game
- If they choose to quit:
    - print a goodbye message
"""
# Game Setup
import random
words = ["string", "index", "function", "integer", "boolean"]
incorrect_guesses = [1]
correct_guesses = [0]
result = []
person = [" o\n", "\\", "|", "/\n", "/", " \\"]


# Handler Setup
def setup():
  # random.choice(list_name)
  play_word = random.choice(words)
  for i in range(len(play_word)):
    result.append('_')
  return play_word

# Handle Correct Guess Function
def handle_guess(play_word, letter, person_string):
  # Check if the letter is correct_guesses
  # Also check if it is duplicate
  # Do something

  if letter in play_word:
    correct_guesses[0] += 1
    print("That guess is correct!")
    guess_index = play_word.find(letter)
    guess_index2 = play_word.rfind(letter)
    if result[guess_index] == '_':
      result[guess_index] = letter
    elif result[guess_index] == letter and guess_index2:
      result[guess_index2] = letter
    else:
      print("You have already entered that letter. Enter another!")

    print(" ".join(result))
  else:
    person_string += ''.join(person[: incorrect_guesses[0]])
    incorrect_guesses[0] += 1
    print("That guess is incorrect")
    print(person_string)
    
    

# Game Implementation
print("Welcome to Hangman!")
entry = input('Type "start" to start or "quit" to quit ')
# Game startup
if entry == "quit":
  print("Quitting. Come again soon!")
elif entry == "start":
  # Getting random word
  play_word = setup()
  person_string = ''
  # Guessing
  while True:
    letter = input("Enter your guess: ")
    if incorrect_guesses[0] < 7:
      handle_guess(play_word, letter, person_string)

    if correct_guesses[0] == len(play_word):
      print("Congrats! You won the game!!!!!!!!!!!!")
      break
      
    
  


