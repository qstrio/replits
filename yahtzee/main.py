import random

def roll_die():
#Return an integer between 1 and 6.
  die = random.randint(1,6)
  return die
      
def check_yahtzee(dice):
    '''Check if we have a Yahtzee. (All numbers are the same)'''
    num = dice[0]
    for i in range(1, len(dice)):
      if num != dice[i]:
        return False

    return True

def play_yahtzee(dice):
    '''
    Roll dice until we get a Yahtzee.
    User inputs 5 numbers, 1 if we re-roll that die, 0 if we don't re-roll.
    Example inputs:
    11111 - reroll all dice
    10000 - reroll first die
    00000 - don't reroll any die
    01100 - reroll 2nd and 3rd dice
    '''
    while True:
   	 roll = str(input())
   	 for i in range(5):
   		 if roll[i] == '1':
   			 dice[i] = roll_die()

   	 print(dice)
   	 if check_yahtzee(dice) == True:
   		 break
    print("Yahtzee!")

def start(dice):
    '''Roll all dice.'''
    for i in range(5):
   	 dice[i] = roll_die()
    print(dice)
    return dice

dice = [0, 0, 0, 0, 0]
dice = start(dice)