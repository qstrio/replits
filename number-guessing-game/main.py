from random import randint

print('Welcome to the number guessing game! please select your options.')

max_guess = int(input('Max guesses: '))
min = int(input('Lower bound: '))
max = int(input('Upper bound: '))
while max < min:
  print('please make the max larger than the min')
  min = int(input('Lower bound: '))
  max = int(input('Upper bound: '))
print("Let's begin!")

num = randint(min, max)

def guess_number():
  global max_guess
  while max_guess > 0:
    print("----------------------------------------")
    print('You have', max_guess, 'guesses remaining.')
    guess = int(input('guess a number: '))
    
    if guess < num:
      print(guess, "is too low!")
    elif guess > num: 
      print(guess, 'is too high!')
    elif guess == num: 
      print(guess, 'is correct!')
      print('Correct! \nYay, you won!')
      break
    max_guess -= 1


guess_number()